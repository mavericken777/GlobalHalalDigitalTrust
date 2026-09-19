# IQ300 Autonomous Assurance Control Plane — Specification v0.1

| Field | Value |
|---|---|
| Artifact | `IQ300_ASSURANCE_CONTROL_PLANE_SPEC_v0.1.md` |
| Revision | v0.1.0 |
| Control date | 2026-09-20 |
| Classification | post-freeze proposal — not controlled doctrine |
| Authority effect | none |
| Freeze | `master-standards-stack/verified-2026-09-17/` (16 modules 00–15 + MANIFEST.json) |
| Suggested commit | `docs(control-plane): add IQ300 assurance control-plane spec v0.1 [DOCTRINE-CRITICAL]` |

[PROPOSAL: IQ300 Autonomous Assurance Control Plane — path point: Control → Authority Gate]
[PILOT: Shipment 001 — target execution architecture]
[ENGINEERING-GATE: runtime implementation, signed statements, policy bundles]

## 1. Proposition

IQ300 does not automate away authority. IQ300 automates the assurance system around authority.

The machine may execute encoded controls autonomously. A HITM policy enforcement point identifies the exact reserved-decision class. High AI confidence never removes a mandatory authority gate.

## 2. Invariants (non-negotiable)

```
EVIDENCE              ≠ CERTIFICATION
AI ASSESSMENT         ≠ CERTIFICATION
AI RECOMMENDATION     ≠ CERTIFICATION
LAB RESULT            ≠ CERTIFICATION
BLOCKCHAIN / SCITT    ≠ CERTIFICATION
QR / C2PA MANIFEST    ≠ CERTIFICATION
TRUST VECTOR          ≠ CERTIFICATION
TRUST SCORE           ≠ CERTIFICATION
OPERATIONAL RELEASE   ≠ CERTIFICATION
NOT DETECTED          ≠ HALAL
```

AHTE is an evidence, control, orchestration and decision-support layer.
Malaysia Halal certification remains with JAKIM / MAIN / JAIN.
Destination acceptance remains with competent GCC authorities and importer processes.
Malaysian Standards are technical instruments only.

## 3. Two paths — do not silently replace the freeze path

### 3.1 Controlling doctrine path (v3.1 / v14.1) — UNCHANGED

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

### 3.2 Proposed machine refinement (maps onto 3.1; see `canonical-path-machine-map.json`)

Machine objects refine Evidence through Operational Release. They do not delete Authority, Standard, Applicability or Authority Gate.

HITM sits **before** Authority Gate as a policy decision point. Signed authoritative decision **is** the Authority Gate output (E5), not a parallel certificate issuer.

## 4. Five sovereign objects

| Object | Meaning | Must not do |
|---|---|---|
| Evidence Object | What was measured / observed / recorded | Establish Halal status |
| Assessment Object | What the machine concluded | Bypass HITM or Authority Gate |
| HITM Case Object | Why a reserved human determination is required | Be decided by model confidence |
| Authority Decision Object | What the authorised human / competent authority decided | Be issued by AHTE as SPHM |
| Trust State Object | Machine-computed state from evidence + controls + decisions | Substitute for certification |

A trust state may change without a new certificate.
An evidence event may fracture trust without changing certification.
A laboratory result may open an authority case without determining Halal status.

## 5. HITM as policy PEP

Input: applicable rule + jurisdiction + decision type + authority mandate + decision scope + state transition.

Evaluator: Open Policy Agent / Rego (`policies/hitm-default-deny.rego`). Default deny. Decision logs required.

```
Low AI confidence  → may escalate
High AI confidence → MUST NOT remove a mandatory D5/D6 gate
```

Classes D0–D6: `hitm-decision-class-registry.json`.

## 6. Universal Trust Vector (primary) and score (secondary)

Vector dimensions are descriptive. Hard-gates are non-compensable. Score is computed only after hard-gate evaluation yields an eligible state space. Score never decides what the competent authority decided.

## 7. Trust fracture loop

`Authorise → continuous evidence → reconcile → fracture? → NO continue / YES hold + blast-radius + re-verification → resolved-release OR authority-matter-HITM`

[PILOT: Shipment 001 — continuous trust-fracture monitoring]
Do not instantiate fracture events without transaction-native evidence.

## 8. Interop stack (characterised, not project authority)

See `IQ300_2026_INTEROP_STACK.md`.

| Layer | Standard / tool | Role |
|---|---|---|
| Authority decision wrap | W3C VC Data Model 2.0 (Rec 15 May 2025) | Hold/verify E5; AHTE does not issue Halal VCs |
| Signed evidence statements | IETF RFC 9943 SCITT (Jun 2026) | Transparency receipts for statement hashes |
| Custody events | GS1 EPCIS 2.0 / ISO/IEC 19987:2024 | What/when/where/why physical events |
| HITM PDP | OPA / Rego (CNCF graduated) | Policy decision; runtime enforces |
| Workload identity | SPIFFE / SPIRE | Short-lived SVIDs; node compromise remains a residual risk |
| Generated assets | C2PA Content Credentials 2.4 (Apr 2026) | Provenance of AI media; not a seal of authority |

Until a runtime is provisioned: `[TOOL-SPEC UNVERIFIED]` at execution time.

## 9. Specification inventory (01–18) — delivery status

| ID | Item | v0.1 status |
|---|---|---|
| 01 | Agent Authority Model | Specified in this document §5–§8 |
| 02 | AI Action Authority Matrix | Encoded as D0–D6 registry |
| 03 | HITM Decision-Class Registry | `hitm-decision-class-registry.json` |
| 04 | Human Authority / Mandate Registry | Stub classes only; live mandates EXTERNAL-GATE |
| 05 | HITM Case Schema | Added to `trust-packet-schemas.json` |
| 06 | Authority Decision Schema | Extension of authority_gate_object |
| 07 | AI Provenance Envelope | Added schema |
| 08 | Trust Vector Schema | Added schema |
| 09 | Hard-Gate / Non-Compensation Engine | Encoded in vector schema + Rego |
| 10 | Release Decision Schema | Operational release remains non-certifying |
| 11 | Trust Fracture Event Taxonomy | Specified in interop + vector schema |
| 12 | Autonomous State Machine | Specified; not implemented |
| 13 | Cryptographic Event Binding | SCITT/VC profile — ENGINEERING-GATE |
| 14 | Authority-Aware API | Not implemented |
| 15 | Agent Runtime Permissions | SPIFFE recommended; not deployed |
| 16 | Auditability / Explainability | OPA decision logs + assessment object |
| 17 | Failure-Closed Controls | Default deny in Rego |
| 18 | Shipment 001 Acceptance Tests | Checklist only; TRANSACTION-GATE |

## 10. Promotion rule

This specification does not rewrite `IQ300_DOCTRINE.md` v3.1 or the 14-node path in README / AGENTS / v14.1.
Promotion requires `[PROMOTION]` + canonical-path review + `[DOCTRINE-CRITICAL]` maintainer acceptance.

## 11. Open gates

- `[SOURCE-LOCKED: exact MS / MPPHM Pindaan 2026 wording]`
- `[OPEN GATE: live authority VC issuer — owner: JAKIM/GCC — blocking: E5 issuance]`
- `[OPEN GATE: SCITT transparency service — owner: engineering — blocking: signed receipts]`
- `[TRANSACTION-GATE: Shipment 001 events]`
- `[ENGINEERING-GATE: OPA/SPIRE/EPCIS runtime]`
