package ahte.hitm

# IQ300 HITM default-deny policy (proposal).
# High model confidence MUST NOT appear as a bypass for D5/D6.
# Undefined is deny.

default allow := false
default requires_human := true
default decision_class := "D5"

reserved_classes := {"D5", "D6"}
hold_classes := {"D4"}

allow if {
  input.class == "D0"
  input.action == "ingest"
}

allow if {
  input.class == "D1"
  input.action == "apply_encoded_control"
}

allow if {
  input.class == "D2"
  input.action == "assess"
  not input.creates_authority_decision
}

requires_human if {
  input.class == "D3"
}

# Auto-hold permitted; auto-release forbidden.
allow if {
  input.class == "D4"
  input.action == "hold"
}

allow if {
  input.class == "D4"
  input.action == "release"
  input.human_determination == true
}

# D5/D6 never allowed to the machine, regardless of confidence.
deny_reason["authority_gate_reserved"] if {
  reserved_classes[input.class]
}

deny_reason["confidence_bypass_forbidden"] if {
  reserved_classes[input.class]
  input.ai_confidence == "high"
}

deny_reason["not_detected_is_not_halal"] if {
  input.claim == "halal_from_not_detected"
}

deny_reason["assessment_is_not_e5"] if {
  input.object_type == "assessment_object"
  input.evidence_class == "E5"
}
