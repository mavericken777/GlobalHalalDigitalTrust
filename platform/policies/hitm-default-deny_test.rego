package ahte.hitm_test

import rego.v1
import data.ahte.hitm

test_d2_assessment_allowed if {
  hitm.allow with input as {"decision_class": "D2", "action": "record_assessment", "actor_type": "ai_advisory", "emits_certificate": false}
}

test_d1_cannot_masquerade_as_assessment if {
  not hitm.allow with input as {"decision_class": "D1", "action": "record_assessment", "actor_type": "system", "emits_certificate": false}
}

test_ai_cannot_execute_d5 if {
  not hitm.allow with input as {"decision_class": "D5", "action": "record_authority_decision", "actor_type": "ai_advisory", "emits_certificate": false}
}

test_human_authority_may_record_d5_without_certificate if {
  hitm.allow with input as {"decision_class": "D5", "action": "record_authority_decision", "actor_type": "human_authority", "emits_certificate": false}
}

test_d6_has_no_executable_action if {
  not hitm.allow with input as {"decision_class": "D6", "action": "recommend_release", "actor_type": "human_authority", "emits_certificate": false}
}
