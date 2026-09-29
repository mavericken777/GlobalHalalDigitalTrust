# GlobalHalalDigitalTrust → Amanah platform parity audit — 2026-09-30

[PROPOSAL: closes platform implementation drift — path point: Control → Evidence → Authority Gate → Trust State → Operational Release]

BOUNDARY CHECK: derived from `mavericken777/GlobalHalalDigitalTrust` current `main` plus the frozen `master-standards-stack/verified-2026-09-17/` boundary; freeze: CROSSING → [PROPOSAL].

## Source snapshot

- canonical project repository: `mavericken777/GlobalHalalDigitalTrust`
- reviewed baseline: `b1c0fc63be72fd6fbd2352a997b210a61c2ca28d`
- SHA12: `b1c0fc63be72`
- review date: 2026-09-30
- recursive Git tree: non-truncated; every tracked path was included in the inventory pass
- prior every-file structural audit: `docs/REPOSITORY_DEEP_AUDIT_2026-09-28.md`

This audit extends the repository-wide file inventory with a semantic platform review. It does not claim that licensed standards text, private travel records, authority decisions, partner acceptances, or Shipment 001 evidence are present when they are not.

## Repository-wide folder classification

| Area | Platform effect | Review result |
|---|---|---|
| `.github/` | CI, integrity controls, agent/instruction automation | CI covered `runtime/` but omitted `platform/`; corrected in this change. |
| `00_EXECUTIVE_COMMAND/` | IQ300 doctrine, machine specs, HITM, hard gates, schemas, readiness | Current machine registries are the implementation-reference layer; post-freeze and non-authoritative. |
| `03_ECOSYSTEM_PARTNERS/`, `partners/` | partner/source records | Evidence/proposal layer only; not platform authority. External identity/acceptance gates remain open. |
| `05_PLATINUM_REAL_TIME_MONITORING/` | monitoring design | Reference/proposal material; does not instantiate live telemetry. |
| `CHINA_TRIP_2026/` | trip/signing/readiness | External evidence gates remain `NOT_TRAVEL_READY` / `NOT_SIGNING_READY`; not software defects. |
| `deliverables/` | generated reports and architecture artefacts | Documentation/evidence presentation; not runtime authority. |
| `docs/` | governance, audit, runbooks | Structural source of current repository status and limits. |
| `master-standards-stack/` | standards metadata, mappings, controlled snapshots | Freeze boundary preserved. Normative text remains SOURCE-LOCKED where absent. |
| `platform/` | FastAPI reference implementation | Found stale D0-D6 semantics and missing CI execution. Corrected as a post-freeze proposal. |
| `runtime/` | gateway/OPA/reference engine | Current CI-tested executable reference layer. No authority effect. |
| `schemas/`, root schema/registry artefacts | structured contracts | Formatting/validation layer; schema conformance does not create certification. |
| `contracts/`, `circuits/` | reference technical experiments | Not production certification logic. |
| `tests/`, `tools/` | validation and integrity | Existing checks retained; platform test coverage added. |

## Material implementation conflict found and corrected

The older FastAPI `platform/` used a stale decision-class mapping:

- D1 = assessment
- D2 = HITM open
- D3 = hold
- D4 = re-verification
- D6 = release recommendation

The current project registry `00_EXECUTIVE_COMMAND/hitm-decision-class-registry.json` defines:

- D0 = encoded operational ingest
- D1 = encoded control execution
- D2 = machine assessment
- D3 = finding / CAPA classification with human accountability
- D4 = trust-fracture hold; no automatic release
- D5 = competent-authority gate reserved
- D6 = sovereign / legal reserved

This branch aligns the FastAPI reference PEP and engine to the current registry. D6 has no executable platform action. D5 remains human-authority-only and cannot emit a certificate. D4 may HOLD but cannot auto-release. D2 creates an assessment object only.

## Trust-state source conflict retained explicitly

[OPEN GATE: SOURCE CONFLICT — trust-state-reference-layer — owner: AHTE/IQ300 source governance — blocking: promotion of one state vocabulary to frozen doctrine]

Two project documents currently describe different state vocabularies:

1. `master-standards-stack/AMANAH_PLATFORM_AZ_MAPPING.md` describes the older conceptual chain `PENDING → EVIDENCE-COMPLETE → ASSESSED → VERIFIED → VERIFIED-WITH-EXCEPTION → RELEASED`, with additional failure states.
2. `00_EXECUTIVE_COMMAND/machine-spec/12-autonomous-state-machine.json` is explicitly a post-freeze proposal using `draft → evidence_incomplete → assessed → hitm_open → authority_pending → authority_decided → eligible → released` plus exception states.

This audit does not silently collapse the two. Production implementations may bind to the machine-spec proposal only as `[PROPOSAL]` until governance promotes a vocabulary.

## Amanah parity rule

Amanah is not required to reproduce the volatile `MemoryStore` architecture of this repository. The production implementation may use stronger persistence, authentication, RLS, audit logs, and deployed APIs. Required parity is semantic:

1. authority boundary is identical;
2. canonical path is preserved;
3. D5/D6 remain reserved and AI cannot bypass them;
4. NOT DETECTED ≠ HALAL;
5. hard gates are non-compensable;
6. trust fractures may auto-HOLD but never auto-release;
7. operational release is not certification;
8. evidence/assessment/decision objects remain provenance-bound;
9. Shipment 001 remains pilot/transaction-gated until real evidence exists;
10. source-locked normative text is never synthesized.

Where Amanah contains a `reference-runtime/` mirror, byte-level parity with the corresponding reference source files is expected and should be regression-tested.

## CI correction

The `Gateway and OPA verification` workflow now:

- runs OPA tests for `runtime/policies/`;
- runs OPA tests for `platform/policies/`;
- runs the runtime engine, gateway guards, and e2e shipment pipeline;
- installs and runs `platform/tests/`.

This prevents the FastAPI reference implementation from drifting outside CI again.

## External/open gates not closed by this change

[SOURCE-LOCKED: licensed normative requirement text — required: controlling licensed/authoritative source artifacts]

[OPEN GATE: competent-authority decisions — owner: JAKIM/MAIN/JAIN or applicable competent authority — blocking: Authority Gate]

[OPEN GATE: GCC destination acceptance/import release — owner: applicable GCC authority/importer — blocking: Authority Gate / Operational Release]

[PILOT: Shipment 001 — China → GCC direct]

[OPEN GATE: real Shipment 001 evidence — owner: transaction participants — blocking: Evidence → Audit Test → Authority Gate → Operational Release]

Travel, signing, partner acceptance, laboratory accreditation/results, production integrations, penetration testing, production keys, and independent assurance remain evidence gates. No repository edit closes them.
