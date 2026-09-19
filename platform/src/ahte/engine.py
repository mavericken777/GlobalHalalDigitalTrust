from __future__ import annotations

from .hitm import evaluate
from .models import (
    ActorType,
    AssessmentIn,
    AuthorityDecisionIn,
    CorridorEventIn,
    DecisionClass,
    EvidenceIn,
    TrustState,
)
from .store import STORE

CANONICAL = [
    "Authority",
    "Standard/Instrument",
    "Clause/Requirement",
    "Applicability",
    "Control",
    "HCP/SCCP",
    "Evidence",
    "Audit Test",
    "Finding",
    "Corrective Action",
    "Re-verification",
    "Authority Gate",
    "Trust State",
    "Operational Release",
]

SEGMENTS = [
    "origin_factory",
    "inland_logistics",
    "export_port",
    "maritime_transit",
    "gcc_port_warehouse",
]


def ingest_evidence(body: EvidenceIn):
    evaluate("record_evidence", DecisionClass.D0, body.actor_type)
    interpretation = None
    if body.lab_result and body.lab_result.lower() in {"not_detected", "not detected"}:
        interpretation = "NOT_DETECTED_IS_NOT_HALAL"
    rec = STORE.put(
        "evidence",
        {
            **body.model_dump(),
            "interpretation": interpretation,
            "path_node": "Evidence",
        },
        "ev",
    )
    STORE.put(
        "trust",
        {"object_id": body.object_id, "state": TrustState.pending.value, "reason": "evidence_recorded"},
        "ts",
    )
    return rec


def assess(body: AssessmentIn):
    evaluate("record_assessment", DecisionClass.D1, body.actor_type)
    missing = [eid for eid in body.evidence_ids if STORE.get("evidence", eid) is None]
    if missing:
        raise ValueError(f"unknown evidence ids: {missing}")
    rec = STORE.put(
        "assessments",
        {**body.model_dump(), "path_node": "Finding", "ai_may_not_decide": True},
        "as",
    )
    state = TrustState.hold if "ncr" in body.finding.lower() or "hold" in body.finding.lower() else TrustState.assessed
    STORE.put("trust", {"object_id": body.object_id, "state": state.value, "assessment_id": rec.id}, "ts")
    STORE.put("hitm", {"object_id": body.object_id, "assessment_id": rec.id, "class": "D2"}, "hitm")
    return rec


def authority_decision(body: AuthorityDecisionIn):
    evaluate(
        "record_authority_decision",
        DecisionClass.D5,
        body.actor_type,
        emits_certificate=body.emits_certificate,
    )
    if STORE.get("assessments", body.assessment_id) is None:
        raise ValueError("assessment not found")
    rec = STORE.put(
        "decisions",
        {
            **body.model_dump(),
            "certificate_issued": False,
            "path_node": "Authority Gate",
            "note": "Record of an asserted authority act; AHTE is not the issuing body",
        },
        "dec",
    )
    STORE.put(
        "trust",
        {
            "object_id": body.object_id,
            "state": TrustState.verified.value,
            "decision_id": rec.id,
            "not_a_certificate": True,
        },
        "ts",
    )
    return rec


def corridor_event(body: CorridorEventIn):
    evaluate("record_event", DecisionClass.D0, ActorType.human)
    if body.segment not in SEGMENTS:
        raise ValueError(f"segment must be one of {SEGMENTS}")
    return STORE.put(
        "events",
        {**body.model_dump(), "pilot": True, "instantiated_shipment_001": False},
        "evt",
    )
