import datetime
import os

import httpx
from fastapi import FastAPI, HTTPException, status

from crypto import Ed25519Signer
from models import (
    EPCISObjectEvent,
    IngestionEvaluationResponse,
    IssueCredentialRequest,
    ProofModel,
    VerifiableCredential,
)

app = FastAPI(
    title="AHTE Trust Gateway (reference)",
    version="1.0.0",
    description="EPCIS ingest, Ed25519 assertions, OPA evaluation. Does not issue statutory Halal certificates.",
)

OPA_URL = os.getenv("OPA_URL", "http://127.0.0.1:8181/v1/data/halal/compliance")
GATEWAY_PRIVATE_KEY, GATEWAY_PUBLIC_KEY = Ed25519Signer.generate_keypair()


@app.get("/api/v1/health")
async def health_check():
    return {
        "status": "healthy",
        "runtime": "REFERENCE",
        "issues_statutory_certificates": False,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "public_key": GATEWAY_PUBLIC_KEY,
    }


@app.post("/api/v1/credentials/issue", response_model=VerifiableCredential)
async def issue_halal_credential(request: IssueCredentialRequest):
    if "halal.gov" in request.issuer_did.lower() or "jakim" in request.issuer_did.lower():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Refusing to mint credentials under a statutory-authority DID. Use a project DID.",
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
                raise HTTPException(
                    status_code=status.HTTP_502_BAD_GATEWAY,
                    detail=f"OPA engine returned HTTP {opa_response.status_code}",
                )
            opa_data = opa_response.json().get("result", {})
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to communicate with OPA engine: {exc}",
        )

    allowed = bool(opa_data.get("allow", False))
    reason = opa_data.get("violation_reason") or ""
    notarized_payload = {
        "epcis_hash": epcis_hash,
        "allowed": allowed,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "evaluated_by": "urn:did:example:ahte-gateway-reference",
    }
    receipt_signature = Ed25519Signer.sign_payload(notarized_payload, GATEWAY_PRIVATE_KEY)
    return IngestionEvaluationResponse(
        status="PASSED" if allowed else "REJECTED",
        allowed=allowed,
        violation_reason=reason,
        epcis_hash=epcis_hash,
        notarized_receipt={
            "payload": notarized_payload,
            "proof": receipt_signature,
            "gateway_public_key": GATEWAY_PUBLIC_KEY,
        },
    )
