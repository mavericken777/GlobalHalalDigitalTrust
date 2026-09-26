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


def preserve_restriction(object_id, proposed):
    current = STORE.trust_for(object_id)
    restricted = {"HOLD", "REVOKED", "RECALLED", "EXPIRED", "DISPUTED"}
    if current and current.body["state"] in restricted:
        return current.body["state"]
    return proposed


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
        {"object_id": body.object_id, "state": preserve_restriction(body.object_id, TrustState.pending.value), "reason": "evidence_recorded"},
        "ts",
    )
    return rec


def assess(body: AssessmentIn):
    evaluate("record_assessment", DecisionClass.D1, body.actor_type)
    if not body.evidence_ids:
        raise ValueError("assessment requires evidence")
    missing = [eid for eid in body.evidence_ids if STORE.get("evidence", eid) is None]
    if missing:
        raise ValueError(f"unknown evidence ids: {missing}")
    if any(STORE.get("evidence", eid).body["object_id"] != body.object_id for eid in body.evidence_ids):
        raise ValueError("evidence belongs to another object")
    rec = STORE.put(
        "assessments",
        {**body.model_dump(), "path_node": "Finding", "ai_may_not_decide": True},
        "as",
    )
    state = TrustState.hold if "ncr" in body.finding.lower() or "hold" in body.finding.lower() else TrustState.assessed
    STORE.put("trust", {"object_id": body.object_id, "state": preserve_restriction(body.object_id, state.value), "assessment_id": rec.id}, "ts")
    STORE.put("hitm", {"object_id": body.object_id, "assessment_id": rec.id, "class": "D2"}, "hitm")
    return rec


def authority_decision(body: AuthorityDecisionIn):
    evaluate(
        "record_authority_decision",
        DecisionClass.D5,
        body.actor_type,
        emits_certificate=body.emits_certificate,
    )
    assessment = STORE.get("assessments", body.assessment_id)
    if assessment is None:
        raise ValueError("assessment not found")
    if assessment.body["object_id"] != body.object_id:
        raise ValueError("assessment belongs to another object")
    states = {"record": TrustState.pending, "approve": TrustState.pending,
              "release": TrustState.pending, "reject": TrustState.hold,
              "hold": TrustState.hold, "revoke": TrustState.revoked,
              "recall": TrustState.recalled, "expire": TrustState.expired}
    decision = body.decision.strip().lower()
    if decision not in states:
        raise ValueError("unsupported decision")
    state = states[decision]
    current = STORE.trust_for(body.object_id)
    if state == TrustState.pending and current and current.body["state"] in {
        TrustState.hold.value, TrustState.revoked.value, TrustState.recalled.value, TrustState.expired.value
    }:
        state = TrustState(current.body["state"])
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
            "state": state.value,
            "authority_authenticated": False,
            "reason": "asserted_decision_only_requires_external_verification",
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
