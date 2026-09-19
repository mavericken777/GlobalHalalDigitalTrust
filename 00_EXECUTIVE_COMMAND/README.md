# 00_EXECUTIVE_COMMAND — AHTE / IQ300 COMMAND LAYER

## Control status

- Current operating instruction artifact: `ABSOLUTE_MODE_SYSTEM_INSTRUCTION_v14.1.md`
- Current doctrine artifact: `IQ300_DOCTRINE.md` v3.1
- Controlled standards freeze: `master-standards-stack/verified-2026-09-17/` (**16 content modules `00`–`15` + `MANIFEST.json`**)
- Post-freeze repository completion audit: `REPOSITORY_COMPLETION_AUDIT_2026-09-18.md`
- Agent control-layer audit: `AGENT_CONTROL_LAYER_AUDIT_2026-09-19.md`
- Assurance control-plane proposal: `IQ300_ASSURANCE_CONTROL_PLANE_SPEC_v0.1.md` (2026-09-20)
- Default pilot corridor: China → GCC direct
- Shipment 001: architecture/evidence-gate complete; transaction not instantiated

This directory is the command, doctrine, machine-readable governance and source-control layer for AHTE/IQ300. It does not create Halal certification, customs clearance, import approval or partner contractual authority.

## Command artifacts

| Artifact | Purpose | Status |
|---|---|---|
| `ABSOLUTE_MODE_SYSTEM_INSTRUCTION_v14.1.md` | Runtime operating constraints, source hierarchy, flags, crawl discipline, drift/adversarial handling | CURRENT |
| `IQ300_DOCTRINE.md` | Complete operational doctrine, canonical path, standards set, partner/corridor/port governance | CURRENT POST-FREEZE REFERENCE |
| `IQ300_ASSURANCE_CONTROL_PLANE_SPEC_v0.1.md` | Target machine assurance plane; HITM PEP; five sovereign objects | POST-FREEZE PROPOSAL |
| `IQ300_2026_INTEROP_STACK.md` | VC 2.0 / RFC 9943 / EPCIS 2.0 / OPA / SPIFFE / C2PA 2.4 bindings | POST-FREEZE CHARACTERISATION |
| `MASTER_DISCUSSION_DECISION_LOG_2026.md` | Executive decision lineage | CONTROLLED |
| `OCTOBER_2026_STRATEGIC_IMPLEMENTATION_MISSION.md` | Strategic implementation mission | CONTROLLED |
| `REPOSITORY_COMPLETION_AUDIT_2026-09-18.md` | Chat-to-repository completion and integrity audit | CURRENT AUDIT |
| `AGENT_CONTROL_LAYER_AUDIT_2026-09-19.md` | GitHub Copilot / agent control-layer addition audit | CURRENT POST-FREEZE PROPOSAL |
| `IQ300_ASSURANCE_CONTROL_PLANE_AUDIT_2026-09-20.md` | Control-plane addition ledger | CURRENT POST-FREEZE PROPOSAL |

## Registry artifacts

| Artifact | Purpose |
|---|---|
| `live-source-registry.json` | Controlled authority/canonical endpoints and retrieval classes |
| `partner-registry.json` | Project-designated partner roles, evidence classes and open contractual gates |
| `port-authority-registry.json` | China/GCC port-customs authority references and transaction-gated port selection |
| `corridor-registry.json` | Five-segment China → GCC direct Shipment 001 corridor model |
| `commit-tag-taxonomy.json` | Repository-to-Project synchronization triggers |
| `project-file-curation.json` | High-frequency Project source curation and PROJECT-REPO fallback |
| `trust-packet-schemas.json` | Trust/evidence/custody/audit/authority/HITM/vector schema definitions (v1.2.0) |
| `schema-registry.json` | Structured-output schema index (v1.2.0) |
| `hitm-decision-class-registry.json` | D0–D6 reserved-decision classes |
| `canonical-path-machine-map.json` | Machine-node to 14-node controlling path map |
| `policies/hitm-default-deny.rego` | OPA default-deny HITM policy draft |

## Related repository agent control (root / `.github`)

| Artifact | Purpose |
|---|---|
| `AGENTS.md` (repository root) | Cross-agent repository instructions |
| `.github/copilot-instructions.md` | Copilot repository-wide instructions |
| `.github/instructions/verified-freeze.instructions.md` | Path-scoped freeze immutability |
| `.github/agents/halal-trust-editor.agent.md` | Specialist editor agent |
| `.github/prompts/ahte-platinum-asset-generation.prompt.md` | Reusable asset workflow (IDE) |
| `.github/skills/ahte-source-governance/SKILL.md` | Auto-loaded source governance skill |
| `.github/hooks/validate-freeze-integrity.json` | Defense-in-depth freeze check |
| `docs/TOOLING.md` | Runtime-verified external tool registry (not project authority) |

## Canonical path

Controlling (doctrine v3.1 / v14.1) — unchanged:

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

Machine refinements in the v0.1 spec map onto this path. They are not a silent replacement.

## Authority boundary

- Malaysian Standards are technical normative instruments; they do not create certification authority.
- Malaysia Halal certification decisions remain with JAKIM/MAIN/JAIN under the applicable framework.
- Destination import and Halal acceptance remain with competent GCC authorities/importer processes.
- Laboratory, AI, QR, blockchain, sensors, partner declarations, trust vectors, trust scores and AHTE trust states are evidence/assurance mechanisms only.
- `NOT DETECTED != HALAL`.
- High AI confidence must never remove a D5/D6 authority gate.

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
