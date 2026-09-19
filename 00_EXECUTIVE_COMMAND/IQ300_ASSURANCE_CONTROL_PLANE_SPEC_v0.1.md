# IQ300 Autonomous Assurance Control Plane — Specification v0.1

| Field | Value |
|---|---|
| Artifact | `IQ300_ASSURANCE_CONTROL_PLANE_SPEC_v0.1.md` |
| Revision | v0.1.1 |
| Control date | 2026-09-20 |
| Classification | post-freeze proposal — not controlled doctrine |
| Authority effect | none |
| Freeze | `master-standards-stack/verified-2026-09-17/` (16 modules 00–15 + MANIFEST.json) |

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

HITM sits **before** Authority Gate as a policy decision point. Signed authoritative decision **is** the Authority Gate output (E5), not a parallel certificate issuer.

## 4. Five sovereign objects

Defined in `trust-packet-schemas.json` v1.2.0: Evidence, Assessment, HITM Case, Authority Decision, Trust State.

## 5. HITM as policy PEP

Evaluator: `policies/hitm-default-deny.rego` + fixtures F01–F12. Default deny.

## 6–8. Vector, fracture, interop

See `machine-spec/09-hard-gate-rules.json`, `machine-spec/11-trust-fracture-taxonomy.json`, `IQ300_2026_INTEROP_STACK.md`.

## 9. Specification inventory (01–18)

| ID | Item | Artifact |
|---|---|---|
| 01 | Agent Authority Model | `machine-spec/01-agent-authority-model.md` |
| 02 | AI Action Authority Matrix | `machine-spec/02-ai-action-authority-matrix.json` |
| 03 | HITM Decision-Class Registry | `hitm-decision-class-registry.json` |
| 04 | Human Authority / Mandate Registry | `machine-spec/04-human-authority-mandate-registry.json` (stub; EXTERNAL-GATE) |
| 05 | HITM Case Schema | `trust-packet-schemas.json#hitm_case_object` |
| 06 | Authority Decision Schema | `trust-packet-schemas.json#authority_decision_object` |
| 07 | AI Provenance Envelope | `trust-packet-schemas.json#ai_provenance_object` |
| 08 | Trust Vector Schema | `trust-packet-schemas.json#trust_vector_object` |
| 09 | Hard-Gate / Non-Compensation | `machine-spec/09-hard-gate-rules.json` |
| 10 | Release Decision Schema | `trust-packet-schemas.json#release_decision_object` |
| 11 | Trust Fracture Taxonomy | `machine-spec/11-trust-fracture-taxonomy.json` |
| 12 | Autonomous State Machine | `machine-spec/12-autonomous-state-machine.json` |
| 13 | Cryptographic Binding | `machine-spec/13-cryptographic-binding-profile.md` |
| 14 | Authority-Aware API | `machine-spec/14-authority-aware-api.md` |
| 15 | Agent Runtime Permissions | `machine-spec/15-agent-runtime-permissions.json` |
| 16 | Auditability / Explainability | `machine-spec/16-auditability-layer.md` |
| 17 | Failure-Closed Controls | `policies/hitm-default-deny.rego` |
| 18 | Shipment 001 Acceptance Tests | `SHIPMENT_001_ACCEPTANCE_TESTS.md` |

Index: `machine-spec/README.md`.

## 10. Promotion rule

This specification does not rewrite `IQ300_DOCTRINE.md` v3.1 or the 14-node path in README / AGENTS / v14.1.
Promotion requires `[PROMOTION]` + canonical-path review + `[DOCTRINE-CRITICAL]` maintainer acceptance.

## 11. Open gates

- `[SOURCE-LOCKED: exact MS / MPPHM Pindaan 2026 wording]`
- `[OPEN GATE: live authority VC issuer — owner: JAKIM/GCC — blocking: E5 issuance]`
- `[OPEN GATE: SCITT transparency service — owner: engineering — blocking: signed receipts]`
- `[TRANSACTION-GATE: Shipment 001 events]`
- `[ENGINEERING-GATE: OPA/SPIRE/EPCIS runtime]`
