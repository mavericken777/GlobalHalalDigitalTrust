# AHTE / IQ300 Repository Agent Instructions

## Artifact Metadata

- Artifact: `AGENTS.md`
- Revision: `v1.1.0`
- Control date: `2026-09-20`
- Target: repository root
- Classification: post-freeze agent-governance artifact
- Authority effect: none
- Suggested commit: `docs(agent): expand AGENTS.md controlling sources and placement [DOCTRINE-CRITICAL]`

[PROPOSAL: closes cross-agent instruction gap — path point: Control / Evidence / Governance]

## 1. Repository Identity

This repository (`mavericken777/GlobalHalalDigitalTrust`) is the canonical
project repository for the Amanah Halal Trust Ecosystem (AHTE) operated by
Global Halal Supply Chain Ltd HK (GHSCL), under IQ300 doctrine.

Repository content is project doctrine, architecture, evidence mapping and
implementation guidance. It is not itself an external regulatory authority,
certification decision or destination-market approval.

Core principle:

> Data stays where it belongs. Trust travels.

## 2. Controlling Sources

Before substantive work, resolve and read the current controlling artifacts
identified by the root `README.md`.

As of this control date, the primary controls are:

1. `00_EXECUTIVE_COMMAND/ABSOLUTE_MODE_SYSTEM_INSTRUCTION_v14.1.md`
2. `00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md`
3. `master-standards-stack/verified-2026-09-17/00_README.md`
4. `master-standards-stack/verified-2026-09-17/MANIFEST.json`
5. `00_EXECUTIVE_COMMAND/live-source-registry.json`
6. `00_EXECUTIVE_COMMAND/partner-registry.json`
7. `00_EXECUTIVE_COMMAND/port-authority-registry.json`
8. `00_EXECUTIVE_COMMAND/corridor-registry.json`
9. `00_EXECUTIVE_COMMAND/trust-packet-schemas.json`
10. `00_EXECUTIVE_COMMAND/schema-registry.json`
11. `00_EXECUTIVE_COMMAND/commit-tag-taxonomy.json`
12. `00_EXECUTIVE_COMMAND/project-file-curation.json`
13. `00_EXECUTIVE_COMMAND/AGENT_CONTROL_LAYER_AUDIT_2026-09-19.md`
14. `docs/TOOLING.md`

Do not assume a hard-coded version remains current. Check the root `README.md`
and repository state before relying on a command version.

## 3. Freeze Boundary

The current controlled standards freeze is:

`master-standards-stack/verified-2026-09-17/`

**16 content modules (`00`–`15`) + `MANIFEST.json`.**

Treat that directory as an immutable verified snapshot.

Do not edit, replace, rename or delete a frozen artifact in place.

Corrections or expansions must use a versioned post-freeze artifact, explicit
supersession, a new verified-date snapshot under `[FREEZE-UPDATE]`, or an
identified `[SOURCE-LOCKED]` / `[OPEN GATE]` / `[PROPOSAL]` state.

## 4. Non-Negotiable Rules

- Never invent normative text, certificates, laboratory results, approvals, contracts, or shipment events.
- Never treat AI, laboratory results, QR codes, blockchain records, or platform events as official Halal certification.
- Enforce: `NOT DETECTED != HALAL`.
- Never present Shipment 001 as instantiated unless transaction-native evidence exists.
- Never blur pilot material into permanent architecture without `[PILOT]`.
- When required source is absent: respond exactly `DATA NOT AVAILABLE — SOURCE-LOCKED.`

## 5. Authority Boundary

AHTE is an evidence, control, orchestration and decision-support layer.
Malaysian Standards are technical instruments only.
Certification decisions remain with JAKIM / MAIN / JAIN.
Destination decisions remain with GCC authorities and importers.
AI and the platform never issue official Halal certificates.

## 6. Canonical Path

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

## 7. Repository Placement

- `00_EXECUTIVE_COMMAND/` — doctrine, command, registries, audits
- `03_ECOSYSTEM_PARTNERS/` — partner RACI / ecosystem matrices
- `05_PLATINUM_REAL_TIME_MONITORING/` — monitoring architecture
- `deliverables/` — numbered documentary deliverables (`00`–`29` present)
- `docs/` — ecosystem documentation and `TOOLING.md`
- `master-standards-stack/verified-2026-09-17/` — controlled freeze (immutable)
- `master-standards-stack/process-flow-infographics/` — process-flow visuals
- `partners/` — coda, sinotrans, china-merchant, china-food-security-lab
- `tools/` — generation tooling
- `.github/` — agents, instructions, prompts, skills, hooks, workflows

Do not create a new top-level directory without explicit repository-governance
approval.

## 8. See Also

- `.github/copilot-instructions.md`
- `.github/agents/halal-trust-editor.agent.md`
- `.github/prompts/ahte-platinum-asset-generation.prompt.md`
- `.github/skills/ahte-source-governance/SKILL.md`
- `docs/TOOLING.md`
- `00_EXECUTIVE_COMMAND/AGENT_CONTROL_LAYER_AUDIT_2026-09-19.md`
- `00_EXECUTIVE_COMMAND/REPOSITORY_COMPLETION_AUDIT_2026-09-18.md`
