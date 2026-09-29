import pytest

from ahte.hitm import HitmDenied, evaluate
from ahte.models import ActorType, DecisionClass


def test_d2_is_machine_assessment():
    evaluate("record_assessment", DecisionClass.D2, ActorType.ai_advisory)


def test_d1_is_not_assessment():
    with pytest.raises(HitmDenied):
        evaluate("record_assessment", DecisionClass.D1, ActorType.system)


def test_d4_may_hold_but_does_not_define_release():
    evaluate("hold", DecisionClass.D4, ActorType.system)
    with pytest.raises(HitmDenied):
        evaluate("recommend_release", DecisionClass.D4, ActorType.system)


def test_d5_requires_human_authority():
    with pytest.raises(HitmDenied):
        evaluate("record_authority_decision", DecisionClass.D5, ActorType.ai_advisory)
    evaluate("record_authority_decision", DecisionClass.D5, ActorType.human_authority)


def test_d6_is_sovereign_legal_reserved():
    with pytest.raises(HitmDenied):
        evaluate("recommend_release", DecisionClass.D6, ActorType.human_authority)
