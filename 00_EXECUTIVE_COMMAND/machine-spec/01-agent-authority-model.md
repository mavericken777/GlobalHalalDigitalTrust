# 01 — Agent Authority Model

[PROPOSAL] [ENGINEERING-GATE: runtime]

## Roles

| Agent / workload | May | Must not |
|---|---|---|
| Ingest / hash worker | D0 ingest, schema validate | Change trust state to certified |
| Control executor | D1 encoded SOP steps | Invent controls not in the mapping |
| Assessment engine | D2 conclusions + assessment_object | Emit E5 or authority_decision |
| HITM PEP (OPA) | Classify D0–D6; deny undefined | Treat model confidence as allow |
| Fracture monitor | D4 auto-hold | Auto-release |
| Authority wrapper | Hold/verify external VC / E5 | Issue Malaysia Halal / SPHM VC |
| Release engine | Operational release after gates | Equate release with certification |

## Safety property

Low confidence → may escalate. High confidence → never removes D5/D6.

Principal of record is the competent authority or appointed officer, not the model.
