"""Reference consignment engine: 12-state FSM, spatial buffer, HTI breaker, Ed25519 receipts.

Does not issue statutory Halal certificates. Madhab floats are caller assertions.
"""

from __future__ import annotations

import base64
import hashlib
import json
import math
from datetime import datetime, timezone
from enum import Enum
from typing import Any

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


class State(str, Enum):
    ST01 = "INGREDIENT_REGISTERED"
    ST02 = "ANTE_MORTEM_CLEARED"
    ST03 = "RITUAL_SLAUGHTER_RECORDED"
    ST04 = "POST_MORTEM_VERIFIED"
    ST05 = "PROCESSING_SEGREGATED"
    ST06 = "PACKAGED_SMART_SEALED"
    ST07 = "COLD_CHAIN_IN_TRANSIT"
    ST08 = "BORDER_PORT_INSPECTED"
    ST09 = "CUSTOMS_RELEASED"
    ST10 = "RETAIL_DISPENSING_ACTIVE"
    ST11 = "QUARANTINED"
    ST12 = "REJECTED"


FORWARD = {
    State.ST01: State.ST02,
    State.ST02: State.ST03,
    State.ST03: State.ST04,
    State.ST04: State.ST05,
    State.ST05: State.ST06,
    State.ST06: State.ST07,
    State.ST07: State.ST08,
    State.ST08: State.ST09,
    State.ST09: State.ST10,
}

HARD_REJECT_FROM = {State.ST01, State.ST02, State.ST03, State.ST04}
QUARANTINE_FROM = {State.ST05, State.ST06, State.ST07, State.ST08, State.ST09, State.ST10}


class CanonicalCryptoEngine:
    @staticmethod
    def canonicalize(data: dict[str, Any]) -> bytes:
        return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")

    @classmethod
    def generate_ed25519_keypair(cls) -> tuple[str, str]:
        private_key = ed25519.Ed25519PrivateKey.generate()
        public_key = private_key.public_key()
        priv_raw = private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption(),
        )
        pub_raw = public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        return base64.b64encode(priv_raw).decode("utf-8"), base64.b64encode(pub_raw).decode("utf-8")

    @classmethod
    def sign_document(cls, document: dict[str, Any], private_key_b64: str) -> str:
        key = ed25519.Ed25519PrivateKey.from_private_bytes(base64.b64decode(private_key_b64))
        return base64.b64encode(key.sign(cls.canonicalize(document))).decode("utf-8")

    @classmethod
    def verify_document(cls, document: dict[str, Any], signature_b64: str, public_key_b64: str) -> bool:
        key = ed25519.Ed25519PublicKey.from_public_bytes(base64.b64decode(public_key_b64))
        try:
            key.verify(base64.b64decode(signature_b64), cls.canonicalize(document))
            return True
        except Exception:
            return False

    @classmethod
    def compute_sha256(cls, data: dict[str, Any]) -> str:
        return hashlib.sha256(cls.canonicalize(data)).hexdigest()


class CutValidation(BaseModel):
    trachea_cut: bool
    esophagus_cut: bool
    carotid_jugular_cut: bool


class SlaughterhouseEvent(BaseModel):
    facility_id: str
    slaughterer_credential_active: bool
    cut_validation: CutValidation
    mechanical_blade: bool


class Coordinate3D(BaseModel):
    x: float
    y: float
    z: float


class WMSLocationEvent(BaseModel):
    bin_id: str
    coordinates: Coordinate3D
    adjacent_non_halal_coordinates: Coordinate3D | None = None
    cross_contamination_detected: bool = False


class TelemetryRecord(BaseModel):
    temp_celsius: float = Field(..., ge=-50.0, le=50.0)
    seal_tamper_detected: bool
    timestamp: str


class MadhabScores(BaseModel):
    shafii: float = Field(..., ge=0.0, le=1.0)
    hanafi: float = Field(default=1.0, ge=0.0, le=1.0)
    maliki: float = Field(default=1.0, ge=0.0, le=1.0)
    hanbali: float = Field(default=1.0, ge=0.0, le=1.0)


class IngestionPayload(BaseModel):
    consignment_id: str
    state: State
    destination_country: str
    slaughterhouse: SlaughterhouseEvent
    telemetry: TelemetryRecord
    wms: WMSLocationEvent
    madhab_scores: MadhabScores


class EvaluationResult(BaseModel):
    consignment_id: str
    state: str
    allowed: bool
    hti_score: float
    reasons: list[str]
    notarized_hash: str
    signature: str
    certificate_issued: bool = False
    madhab_scores_are_assertions: bool = True


class HalalTrustEngine:
    MIN_SEPARATION_METERS = 3.0

    def __init__(self, authority_privkey: str, authority_pubkey: str):
        self.privkey = authority_privkey
        self.pubkey = authority_pubkey

    @staticmethod
    def compute_euclidean_distance(p1: Coordinate3D, p2: Coordinate3D) -> float:
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)

    def evaluate_transaction(self, payload: IngestionPayload) -> EvaluationResult:
        reasons: list[str] = []
        current = payload.state
        if current in {State.ST11, State.ST12}:
            return self._sign(payload, current, False, 0.0, ["terminal state; no transition"])

        quarantine = False
        reject = False

        if payload.telemetry.seal_tamper_detected:
            quarantine = True
            reasons.append("CRITICAL_SECURITY: seal tamper asserted")
        if payload.telemetry.temp_celsius > -18.0 or payload.telemetry.temp_celsius < -25.0:
            quarantine = True
            reasons.append(f"TEMPERATURE_BREACH: {payload.telemetry.temp_celsius}C outside [-25,-18]")
        if payload.wms.cross_contamination_detected:
            quarantine = True
            reasons.append("CONTAMINATION_EVENT")
        if payload.wms.adjacent_non_halal_coordinates:
            dist = self.compute_euclidean_distance(
                payload.wms.coordinates, payload.wms.adjacent_non_halal_coordinates
            )
            if dist < self.MIN_SEPARATION_METERS:
                quarantine = True
                reasons.append(f"SPATIAL_VIOLATION: {dist:.2f}m < 3.0m")

        cuts = payload.slaughterhouse.cut_validation
        if not (cuts.trachea_cut and cuts.esophagus_cut and cuts.carotid_jugular_cut):
            reject = True
            reasons.append("RITUAL_FIELDS_INCOMPLETE")
        if payload.slaughterhouse.mechanical_blade:
            reject = True
            reasons.append("MECHANICAL_BLADE_ASSERTED")
        if payload.madhab_scores.shafii < 1.0:
            reject = True
            reasons.append("SHAFI_ASSERTION_BELOW_1")
        if not payload.slaughterhouse.facility_id.startswith("FIXTURE-"):
            reject = True
            reasons.append("FACILITY_NOT_IN_FIXTURE_NAMESPACE")

        if reject and current in HARD_REJECT_FROM:
            nxt, allowed, hti = State.ST12, False, 0.0
        elif quarantine and current in QUARANTINE_FROM | HARD_REJECT_FROM:
            nxt, allowed, hti = State.ST11, False, 0.0
        elif reject:
            nxt, allowed, hti = State.ST12, False, 0.0
        else:
            nxt = FORWARD.get(current, current)
            allowed = nxt in {State.ST09, State.ST10}
            hti = 100.0 if allowed else 0.0

        return self._sign(payload, nxt, allowed, hti, reasons)

    def _sign(
        self, payload: IngestionPayload, nxt: State, allowed: bool, hti: float, reasons: list[str]
    ) -> EvaluationResult:
        body = {
            "consignment_id": payload.consignment_id,
            "resulting_state": nxt.value,
            "allowed": allowed,
            "hti_score": hti,
            "evaluation_timestamp": datetime.now(timezone.utc).isoformat(),
            "reasons": reasons,
        }
        return EvaluationResult(
            consignment_id=payload.consignment_id,
            state=nxt.value,
            allowed=allowed,
            hti_score=hti,
            reasons=reasons,
            notarized_hash=CanonicalCryptoEngine.compute_sha256(body),
            signature=CanonicalCryptoEngine.sign_document(body, self.privkey),
        )


app = FastAPI(
    title="AHTE consignment engine (reference)",
    version="2.0.0-reference",
    description="FSM + receipts. Not a statutory certification service.",
)

AUTH_PRIVKEY, AUTH_PUBKEY = CanonicalCryptoEngine.generate_ed25519_keypair()
engine = HalalTrustEngine(AUTH_PRIVKEY, AUTH_PUBKEY)


@app.get("/api/v1/health")
async def health():
    return {
        "status": "healthy",
        "runtime": "REFERENCE",
        "issues_statutory_certificates": False,
        "jakim_anchored": False,
        "authority_public_key": AUTH_PUBKEY,
        "model_baseline": "MS themes modelled; licensed clauses not reproduced",
    }


@app.post("/api/v1/evaluate", response_model=EvaluationResult)
async def evaluate_consignment(payload: IngestionPayload):
    try:
        return engine.evaluate_transaction(payload)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
