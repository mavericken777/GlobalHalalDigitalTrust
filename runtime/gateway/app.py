import datetime
import math
import os
from typing import Any, Optional

import httpx
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from crypto import CanonicalCryptoEngine, Ed25519Signer
from fsm import ConsignmentFSM, HalalFSMError
from models import (
    EPCISObjectEvent,
    IngestionEvaluationResponse,
    IssueCredentialRequest,
    ProofModel,
    VerifiableCredential,
)

app = FastAPI(
    title="AHTE Trust Gateway (reference)",
    version="1.1.0",
    description="EPCIS ingest, one-hop FSM, Ed25519 receipts. Does not issue statutory Halal certificates.",
)

OPA_URL = os.getenv("OPA_URL", "http://127.0.0.1:8181/v1/data/halal/compliance")
OPA_PLATINUM = os.getenv("OPA_ENDPOINT", "http://127.0.0.1:8181/v1/data/halal/platinum")
GATEWAY_PRIVATE_KEY, GATEWAY_PUBLIC_KEY = Ed25519Signer.generate_keypair()
LEDGER_DB: dict[str, dict[str, Any]] = {}


class Coordinate3D(BaseModel):
    x: float
    y: float
    z: float


class CorridorEvent(BaseModel):
    consignment_id: str
    current_state: str = "COLD_CHAIN_IN_TRANSIT"
    facility_id: str
    destination_country: str
    temp_celsius: float
    seal_tamper_detected: bool
    coordinates: Coordinate3D
    adjacent_non_halal_coordinates: Optional[Coordinate3D] = None
    mechanical_blade: bool = False
    shafii_score: float = 1.0
    slaughterer_credential_active: bool = False
    trachea_cut: bool = False
    esophagus_cut: bool = False
    carotid_jugular_cut: bool = False


@app.get("/api/v1/health")
async def health_check():
    return {
        "status": "healthy",
        "runtime": "REFERENCE",
        "issues_statutory_certificates": False,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "public_key": GATEWAY_PUBLIC_KEY,
        "consignments_tracked": len(LEDGER_DB),
    }


@app.post("/api/v1/credentials/issue", response_model=VerifiableCredential)
async def issue_halal_credential(request: IssueCredentialRequest):
    if "halal.gov" in request.issuer_did.lower() or "jakim" in request.issuer_did.lower():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Refusing to mint credentials under a statutory-authority DID.",
        )
    issuance_timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    cred_id = f"urn:uuid:ahte:assertion:{request.subject.batchId}"
    unsigned_doc = {
        "@context": ["https://www.w3.org/2018/credentials/v1", "https://example.local/ahte/v1"],
        "id": cred_id,
        "type": ["VerifiableCredential", "HalalBatchAssertion"],
        "issuer": request.issuer_did,
        "issuanceDate": issuance_timestamp,
        "credentialSubject": request.subject.model_dump(),
    }
    signature = Ed25519Signer.sign_payload(unsigned_doc, GATEWAY_PRIVATE_KEY)
    proof = ProofModel(
        created=issuance_timestamp,
        verificationMethod=f"{request.issuer_did}#keys-1",
        proofValue=signature,
    )
    return VerifiableCredential(**unsigned_doc, proof=proof)


@app.post("/api/v1/telemetry/evaluate", response_model=IngestionEvaluationResponse)
async def evaluate_epcis_telemetry(event: EPCISObjectEvent):
    event_payload = event.model_dump()
    epcis_hash = Ed25519Signer.compute_sha256(event_payload)
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            opa_response = await client.post(OPA_URL, json={"input": event_payload})
            if opa_response.status_code != 200:
                raise HTTPException(status_code=502, detail=f"OPA HTTP {opa_response.status_code}")
            opa_data = opa_response.json().get("result", {})
    except httpx.RequestError as exc:
        raise HTTPException(status_code=503, detail=f"OPA unreachable: {exc}") from exc
    allowed = bool(opa_data.get("allow", False))
    reason = opa_data.get("violation_reason") or ""
    notarized_payload = {
        "epcis_hash": epcis_hash,
        "allowed": allowed,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "evaluated_by": "urn:did:example:ahte-gateway-reference",
    }
    return IngestionEvaluationResponse(
        status="PASSED" if allowed else "REJECTED",
        allowed=allowed,
        violation_reason=reason,
        epcis_hash=epcis_hash,
        notarized_receipt={
            "payload": notarized_payload,
            "proof": Ed25519Signer.sign_payload(notarized_payload, GATEWAY_PRIVATE_KEY),
            "gateway_public_key": GATEWAY_PUBLIC_KEY,
        },
    )


@app.post("/api/v1/corridor/clearance")
async def evaluate_corridor_clearance(event: CorridorEvent):
    if not event.facility_id.startswith("FIXTURE-"):
        raise HTTPException(400, "facility_id must use FIXTURE- namespace")
    record = LEDGER_DB.get(event.consignment_id, {"current_state": event.current_state, "history": []})
    fsm = ConsignmentFSM(record["current_state"])
    distance = 10.0
    if event.adjacent_non_halal_coordinates:
        p1, p2 = event.coordinates, event.adjacent_non_halal_coordinates
        distance = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)
    opa_input = {
        "slaughterhouse": {
            "facility_id": event.facility_id,
            "slaughterer_credential_active": event.slaughterer_credential_active,
            "cut_validation": {
                "trachea_cut": event.trachea_cut,
                "esophagus_cut": event.esophagus_cut,
                "carotid_jugular_cut": event.carotid_jugular_cut,
            },
            "mechanical_blade": event.mechanical_blade,
        },
        "telemetry": {"temp_celsius": event.temp_celsius, "seal_tamper_detected": event.seal_tamper_detected},
        "wms": {"cross_contamination_detected": False, "segregation_distance_meters": distance},
        "logistics": {"destination_country": event.destination_country},
        "madhab_scores": {"shafii": event.shafii_score, "hanafi": 1.0, "maliki": 1.0, "hanbali": 1.0},
        "hti_metrics": {"science_score": 1.0, "process_score": 1.0, "traceability_score": 1.0, "esg_score": 1.0},
    }
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            res = await client.post(OPA_PLATINUM, json={"input": opa_input})
            if res.status_code != 200:
                raise HTTPException(502, "OPA platinum query failed")
            decision = res.json().get("result", {})
    except httpx.RequestError as exc:
        raise HTTPException(503, f"OPA unreachable: {exc}") from exc
    allowed = bool(decision.get("allow", False))
    quarantine = bool(decision.get("quarantine_required", False))
    try:
        if quarantine:
            new_state = fsm.transition_to("QUARANTINED")
        elif allowed:
            nxt = {"COLD_CHAIN_IN_TRANSIT": "BORDER_PORT_INSPECTED", "BORDER_PORT_INSPECTED": "CUSTOMS_RELEASED"}.get(
                fsm.current_state
            )
            if nxt is None:
                raise HalalFSMError(f"no single success hop from {fsm.current_state}")
            new_state = fsm.transition_to(nxt)
        else:
            target = "REJECTED" if "REJECTED" in ConsignmentFSM.VALID_TRANSITIONS.get(fsm.current_state, []) else "QUARANTINED"
            new_state = fsm.transition_to(target)
    except HalalFSMError as exc:
        raise HTTPException(400, str(exc)) from exc
    receipt = {
        "consignment_id": event.consignment_id,
        "state": new_state,
        "allowed": allowed and new_state == "CUSTOMS_RELEASED",
        "hti_score": decision.get("hti_score", 0.0),
        "reasons": decision.get("reasons", []),
        "notarized_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "one_hop": True,
    }
    record["current_state"] = new_state
    record["history"].append(receipt)
    LEDGER_DB[event.consignment_id] = record
    return {
        "receipt": receipt,
        "receipt_hash": CanonicalCryptoEngine.compute_sha256(receipt),
        "signature": CanonicalCryptoEngine.sign_document(receipt, GATEWAY_PRIVATE_KEY),
        "authority_public_key": GATEWAY_PUBLIC_KEY,
    }
