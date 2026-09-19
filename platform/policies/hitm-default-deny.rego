package ahte.hitm

default allow := false

# Advisory AI confidence never authorises D5/D6.
allow if {
  input.decision_class == "D0"
  input.action == "record_evidence"
}

allow if {
  input.decision_class == "D1"
  input.action == "record_assessment"
}

# D5/D6 require a human authority actor. This engine still does not emit certificates.
allow if {
  input.decision_class == "D5"
  input.action == "record_authority_decision"
  input.actor_type == "human_authority"
  input.emits_certificate == false
}
