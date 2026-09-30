# Implementation Completeness Rule — 30 September 2026

## Artifact metadata

| Field | Value |
|---|---|
| Artifact | `IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md` |
| Revision | v1.0.0 |
| Control date | 2026-09-30 |
| Classification | Post-freeze implementation control |
| Freeze impact | None — `master-standards-stack/verified-2026-09-17/` remains immutable |
| Authority effect | None |
| Governing architecture | `CURRENT_TARGET_ARCHITECTURE_2026-09-30.md` + `current-target-architecture-2026-09-30.json` v1.1.0+ |

[PROPOSAL: closes implementation-completeness gap — path point: Control → Evidence → Authority Gate → Trust State → Operational Release]

## 1. Controlling rule

**FULL ARCHITECTURE NOW → REAL CONNECTORS WHEN AVAILABLE → NO REDESIGN REQUIRED.**

No project implementation, website build, portal build, API build, local development environment or Codex execution may interpret an unavailable external dependency as permission to remove, disable, hide, downgrade, omit or arbitrarily limit an intended target capability.

## 2. No artificial blocks

Do not introduce artificial blocks, feature caps or permanent limitations on:

- manufacturer onboarding;
- supplier/raw-material provenance;
- standards/applicability;
- HCP/SCCP controls;
- evidence ingestion;
- smart-glass auditing;
- laboratory/LIMS integration;
- digital twins;
- traceability depth;
- cryptographic evidence/integrity;
- direct JAKIM API connectivity;
- authority workflows;
- 24/7 Command Center operations;
- AI/ML analytics;
- predictive compliance;
- Preemptive Strategy Engine;
- Sinotrans warehouse/logistics monitoring;
- telemetry/container/seal/custody;
- port/customs APIs;
- GCC receiving/importer/retail workflows;
- verification;
- Shariah financing;
- Takaful;
- tokenomics/digital-value integration;
- multilingual capability;
- stakeholder portals;
- APIs;
- future scale.

## 3. External dependency pattern

When a real external system is not available in the development/runtime environment:

```text
PRODUCTION DOMAIN MODEL
        ↓
PRODUCTION ADAPTER CONTRACT
        ↓
CONNECTION-STATE LAYER
        ├── development-provider-active
        ├── sandbox-connected
        ├── production-credentials-required
        └── production-connected
        ↓
REPLACEABLE DEVELOPMENT PROVIDER
        ↓
COMPLETE WORKFLOW / UI / TESTS
```

The real connector must be able to replace the development provider without redesigning the domain model, route structure, workflow state machine or user experience.

## 4. Development provider rule

A development provider may substitute:

- external connectivity;
- synthetic test data;
- simulated webhooks/events;
- sandbox credentials;
- mock device input;
- synthetic telemetry;
- simulated external state transitions.

It may **not** substitute away the actual capability.

Do not use:

- blank placeholder pages;
- `coming soon` as a permanent substitute;
- disabled navigation for required target capabilities;
- permanent feature flags hiding required architecture;
- reduced domain models that will require a rewrite later;
- generic dashboard placeholders where a role-specific application is required.

## 5. Truthfulness boundary

Architectural completeness does not authorize fabricated operational facts.

Do not fabricate:

- JAKIM approvals/status/credentials;
- laboratory results/accreditation/endorsement;
- Sinotrans production events;
- port/customs release;
- GCC acceptance;
- financing approvals;
- Takaful underwriting/claims decisions;
- token legal/Shariah/regulatory approval;
- Shipment 001 transaction evidence;
- production telemetry.

Development/sandbox state must be visibly labelled and must never be presented as production evidence.

## 6. Decision authority boundary

This rule does not remove human/authority gates.

- D4 auto-hold may operate where policy permits; release remains human where required.
- D5 competent-authority decisions remain human/authority-controlled.
- D6 sovereign/legal/fatwa decisions remain human/authority-controlled.
- AHTE trust state is not certification.
- Operational release is not certification.
- Lab evidence is not certification.
- Financing/Takaful/tokenization are separate decision domains.

The requirement is **no artificial engineering/product block**, not removal of legitimate authority or human-decision controls.

## 7. Definition of implementation completeness

A target capability is architecturally complete only when it has, as applicable:

1. domain types/schemas;
2. workflow/state machine;
3. public/role UI;
4. production adapter contract;
5. development/sandbox provider if real connector unavailable;
6. explicit connector state;
7. errors/retries/reconciliation;
8. identity/auth/access controls;
9. audit/event history;
10. evidence/integrity linkage;
11. tests;
12. production-replacement path that requires no redesign.

## 8. Required application

This rule applies to:

- `docs/CODEX_PLATFORM_REBUILD_MASTER_PROMPT_2026-09-30.md` v2.1.0+;
- `docs/WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md` v2.1.0+;
- `00_EXECUTIVE_COMMAND/current-target-architecture-2026-09-30.json` v1.1.0+;
- current and future platform/web/portal implementations;
- future integration specifications unless explicitly superseded by a newer controlled architecture version.

It does not alter the verified 17 September freeze or manufacture competent-authority facts.
