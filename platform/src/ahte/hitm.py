from __future__ import annotations

from .models import ActorType, DecisionClass


class HitmDenied(Exception):
    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)


def evaluate(action: str, decision_class: DecisionClass, actor_type: ActorType, emits_certificate: bool = False) -> None:
    """In-process default-deny PEP aligned to the current D0-D6 registry.

    D5/D6 can never be executed by AI. This reference runtime records an asserted
    D5 authority act only when the caller identifies as a human authority and it
    still never emits a certificate. D6 sovereign/legal determinations have no
    executable action in this runtime.
    """
    if emits_certificate:
        raise HitmDenied("AHTE does not issue Halal certificates")
    if actor_type == ActorType.ai_advisory and decision_class in {DecisionClass.D5, DecisionClass.D6}:
        raise HitmDenied("AI advisory cannot execute D5/D6")

    allowed = {
        ("record_evidence", DecisionClass.D0),
        ("record_event", DecisionClass.D0),
        ("execute_control", DecisionClass.D1),
        ("record_assessment", DecisionClass.D2),
        ("recommend_finding", DecisionClass.D3),
        ("hold", DecisionClass.D4),
        ("reverify", DecisionClass.D4),
        ("record_authority_decision", DecisionClass.D5),
    }
    if (action, decision_class) not in allowed:
        raise HitmDenied(f"deny {action}/{decision_class.value}")

    if decision_class == DecisionClass.D3 and actor_type == ActorType.ai_advisory and action != "recommend_finding":
        raise HitmDenied("AI may recommend D3 only")
    if action == "record_authority_decision" and actor_type != ActorType.human_authority:
        raise HitmDenied("D5 requires human_authority actor")
    if decision_class == DecisionClass.D6:
        raise HitmDenied("D6 is sovereign/legal reserved and has no executable platform action")
