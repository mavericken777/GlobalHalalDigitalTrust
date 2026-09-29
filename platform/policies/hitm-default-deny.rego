package ahte.hitm

import rego.v1

default allow := false

# Advisory AI confidence never authorises D5/D6.
allow if {
  input.decision_class == "D0"
  input.action == "record_evidence"
}

allow if {
  input.decision_class == "D0"
  input.action == "record_event"
}

allow if {
  input.decision_class == "D1"
  input.action == "execute_control"
}

# D2 creates an assessment object only; never an authority decision.
allow if {
  input.decision_class == "D2"
  input.action == "record_assessment"
}

# D3 is human-accountable; AI may recommend only.
allow if {
  input.decision_class == "D3"
  input.action == "recommend_finding"
}

# D4 permits automatic HOLD, never automatic release.
allow if {
  input.decision_class == "D4"
  input.action == "hold"
}

allow if {
  input.decision_class == "D4"
  input.action == "reverify"
  input.actor_type != "ai_advisory"
}

# D5 requires a human authority actor. This engine still does not emit certificates.
allow if {
  input.decision_class == "D5"
  input.action == "record_authority_decision"
  input.actor_type == "human_authority"
  input.emits_certificate == false
}

# D6 sovereign/legal decisions are intentionally not executable here.
