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
    STORE.put_trust(
        {"object_id": body.object_id, "state": TrustState.pending.value, "reason": "evidence_recorded"},
    )
    return rec


def assess(body: AssessmentIn):
    # D2 is machine assessment under the current canonical registry. It may create
    # an assessment object but never an authority decision.
    evaluate("record_assessment", DecisionClass.D2, body.actor_type)
    if not body.evidence_ids:
        raise ValueError("assessment requires evidence")
    missing = [eid for eid in body.evidence_ids if STORE.get("evidence", eid) is None]
    if missing:
        raise ValueError(f"unknown evidence ids: {missing}")
    if any(STORE.get("evidence", eid).body["object_id"] != body.object_id for eid in body.evidence_ids):
        raise ValueError("evidence belongs to another object")
    rec = STORE.put(
        "assessments",
        {**body.model_dump(), "path_node": "Audit Test", "ai_may_not_decide": True, "decision_class": "D2"},
        "as",
    )
    fracture = "ncr" in body.finding.lower() or "hold" in body.finding.lower()
    if fracture:
        # D4 may auto-HOLD a trust fracture; release still requires human
        # determination and re-verification.
        evaluate("hold", DecisionClass.D4, ActorType.system)
        STORE.put_trust({"object_id": body.object_id, "state": TrustState.hold.value, "assessment_id": rec.id})
        STORE.put(
            "hitm",
            {
                "object_id": body.object_id,
                "assessment_id": rec.id,
                "class": "D3",
                "reason": "finding_requires_human_accountability",
            },
            "hitm",
        )
    else:
        STORE.put_trust({"object_id": body.object_id, "state": TrustState.assessed.value, "assessment_id": rec.id})
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
    states = {
        "record": TrustState.pending,
        "approve": TrustState.pending,
        "release": TrustState.pending,
        "reject": TrustState.hold,
        "hold": TrustState.hold,
        "revoke": TrustState.revoked,
        "recall": TrustState.recalled,
        "expire": TrustState.expired,
    }
    decision = body.decision.strip().lower()
    if decision not in states:
        raise ValueError("unsupported decision")
    state = states[decision]
    rec = STORE.put(
        "decisions",
        {
            **body.model_dump(),
            "certificate_issued": False,
            "path_node": "Authority Gate",
            "decision_class": "D5",
            "note": "Record of an asserted authority act; AHTE is not the issuing body",
        },
        "dec",
    )
    STORE.put_trust(
        {
            "object_id": body.object_id,
            "state": state.value,
            "authority_authenticated": False,
            "reason": "asserted_decision_only_requires_external_verification",
            "decision_id": rec.id,
            "not_a_certificate": True,
        },
    )
    return rec


def corridor_event(body: CorridorEventIn):
    evaluate("record_event", DecisionClass.D0, ActorType.human)
    if body.segment not in SEGMENTS:
        raise ValueError(f"segment must be one of {SEGMENTS}")
    return STORE.put(
        "events",
        {**body.model_dump(), "pilot": True, "instantiated_shipment_workflow": False},
        "evt",
    )
