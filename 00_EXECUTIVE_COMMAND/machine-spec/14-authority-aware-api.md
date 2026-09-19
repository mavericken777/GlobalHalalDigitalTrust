# 14 — Authority-Aware API (proposal)

[PROPOSAL] [ENGINEERING-GATE: not implemented]

Base path: `/v0/assurance` (not a certification API).

| Method | Path | Class | Notes |
|---|---|---|
| POST | `/packets` | D0 | Create draft trust packet |
| POST | `/evidence` | D0 | Append evidence_object |
| POST | `/assess` | D2 | Returns assessment_object; never E5 |
| POST | `/hitm/evaluate` | PEP | Body → OPA; default deny |
| POST | `/hold` | D4 | Auto-hold allowed |
| POST | `/release` | D4/ops | Requires human_determination when from hold; `is_certification=false` |
| POST | `/authority-decisions` | D5 | Accepts **external** E5 / VC; rejects AHTE-as-issuer |
| GET | `/state/{packet_id}` | — | trust_state + vector; score secondary |

Every mutating call records `actor`, `spiffe_id` (when runtime exists), `opa_decision_log_ref`.

Error `403 authority_gate_reserved` on D5/D6 machine execute.
