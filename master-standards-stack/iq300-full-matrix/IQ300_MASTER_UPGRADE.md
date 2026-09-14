# IQ300 Master Logical Upgrade - Clause -> Control -> HCP -> Evidence -> Audit Test -> Authority Gate

## Executive specification

IQ300 is upgraded from a narrative standards register into a regulatory control graph. A requirement is a versioned object connected to physical controls, evidence, audit procedures, authority boundaries and trust-state transitions.

## Canonical object path

`INSTRUMENT -> EDITION -> CLAUSE -> REQUIREMENT INTENT -> APPLICABILITY -> CONTROL OBJECT -> HCP -> EVIDENCE -> AUDIT TEST -> FINDING -> CORRECTIVE ACTION -> RE-VERIFICATION -> AUTHORITY GATE -> TRUST STATE`

## Complete clause-object backbone from the supplied MS 2400 PDFs

| Standard | Objects | Section 4 | Section 5 | Section 6 | Section 7 | Section 8 |
|---|---:|---:|---:|---:|---:|---:|
| MS 2400-1:2019 | 187 | 55 | 31 | 39 | 52 | 10 |
| MS 2400-2:2019 | 201 | 56 | 31 | 40 | 65 | 9 |
| MS 2400-3:2019 | 225 | 56 | 28 | 40 | 92 | 9 |
| **Total** | **613** | **167** | **90** | **119** | **209** | **28** |

Every extracted numbered clause, including nested clauses, receives its own immutable `requirement_id`.

## Evidence rule

Evidence must answer three questions:
1. Was the control defined?
2. Was the control executed?
3. Can execution be linked to the correct product/lot/asset/custodian/time?

## Audit rule

IQ300 separates document adequacy, on-site compliance, interview evidence, observation evidence, traceability reconstruction, laboratory evidence, competence verification and authority verification.

## Authority rule

IQ300 may calculate completeness, risk, anomalies and evidence sufficiency. It may not convert those calculations into a Malaysian Halal certificate or equivalent authority decision.

## Sector-standard source boundary

The supplied compendia support detailed family-level mappings for MS 1500, MS 2424, MS 2634, MS 2738, MS 2803, MS 2393, MS 2627, MS 1900, MS 2691 and MS 2610. They do not expose every licensed numbered subclause. The repository records an explicit freeze gap rather than fabricating a false clause inventory.

## Production freeze gate

`Acquire licensed official text -> verify edition/confirmation -> parse clauses -> human legal/Shariah review -> create objects -> map controls -> map evidence -> map tests -> map authority gates -> QA -> publish version -> cryptographically freeze`
