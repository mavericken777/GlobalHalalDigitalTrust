from __future__ import annotations

from . import engine
from .mock_integrations import MOCK_HUB
from .models import ActorType, AssessmentIn, CorridorEventIn, EvidenceIn


def run_demo(shipment_id: str = "SHIPMENT-001", object_id: str = "DEMO-PRODUCT-001") -> dict:
    """Run a presentation-safe synthetic China→GCC journey in one call."""
    lab = MOCK_HUB.laboratory(object_id)
    evidence = engine.ingest_evidence(EvidenceIn(
        object_id=object_id,
        evidence_type="LABORATORY_RESULT",
        source_system="CHINA_LABORATORY_MOCK",
        payload=lab,
        actor="demo-lab",
        actor_type=ActorType.system,
        lab_result="not_detected",
    ))
    assessment = engine.assess(AssessmentIn(
        object_id=object_id,
        evidence_ids=[evidence.id],
        finding="Evidence complete for demonstration assessment",
        actor="demo-ai",
        actor_type=ActorType.ai_advisory,
        ai_confidence=0.97,
    ))
    authority = MOCK_HUB.jakim(object_id, "review")
    logistics = MOCK_HUB.sinotrans(shipment_id)
    origin_port = MOCK_HUB.port_customs(shipment_id, "ORIGIN_PORT")
    transit = engine.corridor_event(CorridorEventIn(
        shipment_id=shipment_id,
        segment="maritime_transit",
        bizstep="in_transit",
        actor="demo-logistics",
    ))
    destination = MOCK_HUB.port_customs(shipment_id, "GCC_PORT")
    gcc = MOCK_HUB.gcc(shipment_id, "receive")
    finance = MOCK_HUB.finance(object_id, "quote")
    return {
        "demo": True,
        "synthetic": True,
        "object_id": object_id,
        "shipment_id": shipment_id,
        "steps": [
            {"name": "laboratory", "result": lab},
            {"name": "evidence", "result": evidence.model_dump()},
            {"name": "ahte_assessment", "result": assessment.model_dump()},
            {"name": "direct_jakim_api", "result": authority},
            {"name": "sinotrans", "result": logistics},
            {"name": "origin_port_customs", "result": origin_port},
            {"name": "international_transit", "result": transit.model_dump()},
            {"name": "gcc_port_customs", "result": destination},
            {"name": "gcc_receiving", "result": gcc},
            {"name": "shariah_finance", "result": finance},
        ],
        "trust_state": "ASSESSED",
        "next_authority_gate": "HUMAN_AUTHORITY",
        "presentation_note": "All external provider responses are synthetic demonstration data.",
    }
