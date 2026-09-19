---
name: ahte-platinum-asset-generation
description: Generate a source-governed AHTE corporate, visual, website, video or documentary asset with authority-boundary, provenance, versioning and repository controls.
agent: halal-trust-editor
argument-hint: "Provide asset type, objective, audience, output formats and repository target path."
---

# AHTE Platinum Asset Generation Workflow

## Control Metadata

- Artifact: `.github/prompts/ahte-platinum-asset-generation.prompt.md`
- Revision: `v1.0.0`
- Control date: `2026-09-19`
- Classification: reusable post-freeze asset-production prompt
- Authority effect: none
- Suggested commit: `docs(prompt): add source-governed AHTE asset workflow [MINOR]`

[PROPOSAL: closes controlled asset-generation gap — path point: Control / Evidence / Stakeholder View]

## Required Inputs

- Asset type: `${input:assetType:corporate profile, website, dashboard, logo/brand system, business card, video, infographic, chart, process flow or other}`
- Objective: `${input:objective:state the exact business and communication objective}`
- Primary audience: `${input:audience:identify the intended viewers or users}`
- Required deliverables: `${input:deliverables:list exact files, dimensions, formats and variants}`
- Repository target path: `${input:targetPath:provide the exact existing path or request a path proposal}`
- Required source scope: `${input:sourceScope:list standards, doctrine, pilot, partner or corridor content to use}`
- Visual direction: `${input:visualDirection:institutional, technical, restrained, executive or other}`
- Language and locale: `${input:language:English unless otherwise specified}`
- Deployment authorization: `${input:deploymentAuthorization:no by default}`
- External-tool authorization: `${input:externalToolAuthorization:no by default}`
- Paid-generation authorization: `${input:paidGenerationAuthorization:no by default}`
- Controlled-data upload authorization: `${input:controlledDataUploadAuthorization:no by default}`

## 1. Source Preflight

Before generating anything, read:

- `README.md`
- `AGENTS.md`
- `00_EXECUTIVE_COMMAND/ABSOLUTE_MODE_SYSTEM_INSTRUCTION_v14.1.md`
- `00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md`
- `master-standards-stack/verified-2026-09-17/00_README.md`
- `master-standards-stack/verified-2026-09-17/MANIFEST.json`

Record source path, source status, revision or control date, applicable freeze,
claim or content supported, and unresolved source limitation.

## 2. Missing-Input Classification

### Source or Evidence Missing

If a required normative, authority, partner, certificate, laboratory,
commercial or transaction source is absent, begin with:

`DATA NOT AVAILABLE — SOURCE-LOCKED.`

Then list missing item, source owner, blocked canonical-path point, exact
retrieval action, and which parts of the asset must stop.

### Creative Preference Missing

If only a creative preference is missing, ask one concise clarification
question or use an existing repository brand rule where one is verified.

Do not misuse `SOURCE-LOCKED` for creative preferences.

## 3. Authority Boundary

AHTE supports evidence, controls, traceability, audit and accountable decisions.

AHTE and AI do not issue official Halal certificates.

Do not use wording, icons, seals, badges, colours, marks or layouts that could
reasonably imply government endorsement, JAKIM/MAIN/JAIN certification, GCC
authority approval, laboratory accreditation, customs clearance, or instantiated
Shipment 001.

## 4. Canonical Path

Where the asset explains compliance, show the complete chain or accurately
scoped subset:

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

Do not render an internal trust state as official certification.

## 5. Pilot Separation

Mark Shipment 001 content:

`[PILOT: Shipment 001 — <component>]`

Keep permanent architecture visually and textually separate from proposed
manufacturers, SKUs, importer/buyer, logistics route, and simulated events.

Do not represent Shipment 001 as instantiated unless transaction-native
evidence exists.

## 6. Repository Placement

- doctrine, commands and registries → `00_EXECUTIVE_COMMAND/`
- numbered reports and corporate documents → `deliverables/`
- ecosystem documentation → `docs/`
- standards process flows → `master-standards-stack/process-flow-infographics/`
- Shipment 001 execution assets → `master-standards-stack/CHINA_EXECUTION_PACK/`
- partner-specific content → `partners/<partner-slug>/`
- generators and validators → `tools/`
- GitHub agents, instructions and prompts → `.github/`

Do not create an unapproved top-level directory.

## 7. Public Authority Disclaimer

Include the following or an approved equivalent on claim-bearing public assets:

> AHTE is an evidence and decision-support platform. Official Halal
> certification and destination regulatory decisions remain with the competent
> authorities.

## 8. Required Output Order

Return:

1. `SOURCE PREFLIGHT`
2. `APPLICABLE FLAGS`
3. `ASSET SPECIFICATION`
4. `COMPLETE ASSET OR FILE CONTENT`
5. `PROVENANCE PACKAGE`
6. `VALIDATION REPORT`
7. `REMAINING GATES`
8. `TARGET PATHS AND FILENAMES`
9. `SUGGESTED COMMIT MESSAGE`
10. `REPOSITORY COMMIT-CONTROL TAG`

The generated asset must contain no unresolved placeholder tokens.
