from __future__ import annotations

from .models import ActorType, DecisionClass


class HitmDenied(Exception):
    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)


def evaluate(action: str, decision_class: DecisionClass, actor_type: ActorType, emits_certificate: bool = False) -> None:
    """In-process default-deny PEP. AI cannot skip D5/D6. Nothing may emit a certificate."""
    if emits_certificate:
        raise HitmDenied("AHTE does not issue Halal certificates")
    if actor_type == ActorType.ai_advisory and decision_class in {DecisionClass.D5, DecisionClass.D6}:
        raise HitmDenied("AI advisory cannot execute D5/D6")
    allowed = {
        ("record_evidence", DecisionClass.D0),
        ("record_assessment", DecisionClass.D1),
        ("open_hitm", DecisionClass.D2),
        ("hold", DecisionClass.D3),
        ("reverify", DecisionClass.D4),
        ("record_authority_decision", DecisionClass.D5),
        ("recommend_release", DecisionClass.D6),
        ("record_event", DecisionClass.D0),
    }
    if (action, decision_class) not in allowed:
        raise HitmDenied(f"deny {action}/{decision_class.value}")
    if action == "record_authority_decision" and actor_type != ActorType.human_authority:
        raise HitmDenied("D5 requires human_authority actor")
