# 16 — Auditability / Explainability

[PROPOSAL]

## Required records

1. OPA decision log: input class/action, allow/deny, deny_reason, policy bundle version.
2. assessment_object: model_id, prompt_hash12, evidence_refs, confidence, `creates_authority_decision=false`.
3. hitm_case_object: class, jurisdiction, mandate_ref, opa_decision_log_ref.
4. authority_decision_object: owner, outcome, `issued_by_ahte=false`.
5. ai_provenance_object + C2PA ref for generated assets.

## Explainability rule

The system must be able to answer: *which rule, which class, which actor, which evidence hashes, which human mandate* produced a state change.

Model token-probability is not an audit trail.
