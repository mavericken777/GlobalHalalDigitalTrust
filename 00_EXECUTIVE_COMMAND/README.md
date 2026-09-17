# 00_EXECUTIVE_COMMAND — AHTE / IQ300 COMMAND LAYER

## Control status

- Current operating instruction artifact: `ABSOLUTE_MODE_SYSTEM_INSTRUCTION_v14.1.md`
- Current doctrine artifact: `IQ300_DOCTRINE.md` v3.1
- Controlled standards freeze: `master-standards-stack/verified-2026-09-17/`
- Post-freeze repository completion audit: `REPOSITORY_COMPLETION_AUDIT_2026-09-18.md`
- Default pilot corridor: China → GCC direct
- Shipment 001: architecture/evidence-gate complete; transaction not instantiated

This directory is the command, doctrine, machine-readable governance and source-control layer for AHTE/IQ300. It does not create Halal certification, customs clearance, import approval or partner contractual authority.

## Command artifacts

| Artifact | Purpose | Status |
|---|---|---|
| `ABSOLUTE_MODE_SYSTEM_INSTRUCTION_v14.1.md` | Runtime operating constraints, source hierarchy, flags, crawl discipline, drift/adversarial handling | CURRENT |
| `IQ300_DOCTRINE.md` | Complete operational doctrine, canonical path, standards set, partner/corridor/port governance | CURRENT POST-FREEZE REFERENCE |
| `MASTER_DISCUSSION_DECISION_LOG_2026.md` | Executive decision lineage | CONTROLLED |
| `OCTOBER_2026_STRATEGIC_IMPLEMENTATION_MISSION.md` | Strategic implementation mission | CONTROLLED |
| `REPOSITORY_COMPLETION_AUDIT_2026-09-18.md` | Chat-to-repository completion and integrity audit | CURRENT AUDIT |

## Registry artifacts

| Artifact | Purpose |
|---|---|
| `live-source-registry.json` | Controlled authority/canonical endpoints and retrieval classes |
| `partner-registry.json` | Project-designated partner roles, evidence classes and open contractual gates |
| `port-authority-registry.json` | China/GCC port-customs authority references and transaction-gated port selection |
| `corridor-registry.json` | Five-segment China → GCC direct Shipment 001 corridor model |
| `commit-tag-taxonomy.json` | Repository-to-Project synchronization triggers |
| `project-file-curation.json` | High-frequency Project source curation and PROJECT-REPO fallback |
| `trust-packet-schemas.json` | Draft 2020-12 trust/evidence/custody/audit/authority/trust-state schema definitions |
| `schema-registry.json` | Structured-output schema index |

## Canonical path

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

## Authority boundary

- Malaysian Standards are technical normative instruments; they do not create certification authority.
- Malaysia Halal certification decisions remain with JAKIM/MAIN/JAIN under the applicable framework.
- Destination import and Halal acceptance remain with competent GCC authorities/importer processes.
- Laboratory, AI, QR, blockchain, sensors, partner declarations and AHTE trust states are evidence/assurance mechanisms only.
- `NOT DETECTED != HALAL`.

## Pilot linkage

[PILOT: Shipment 001 — command layer]

Supporting controlled artifacts include:

- `deliverables/26_GCC_IMPORTER_BUYER_ENGAGEMENT_PROTOCOL_2026.md`
- `deliverables/29_GLOBAL_PORT_AUTHORITIES_PROTOCOL_2026.md`
- `partners/coda/README.md`
- `partners/china-food-security-lab/README.md`
- `partners/china-merchant/README.md`
- `partners/sinotrans/README.md`
- `master-standards-stack/CHINA_EXECUTION_PACK/10_MACHINE_READABLE_EXECUTION_PACK.json`

## Completion semantics

`COMPLETE` means the repository workstream is evidence-accounted. External/source/transaction gates remain open until authoritative or transaction-native evidence exists. They must never be downgraded to assumed completion.
