# IQ300 MASTER STANDARDS STACK

This folder is the detailed JAKIM / Malaysian Halal Standards intelligence layer built from the supplied PDF corpus.

## Source corpus

- `ms2400 1.pdf` - MS 2400-1:2019 Transportation
- `Ms2400 2.pdf` - MS 2400-2:2019 Warehousing
- `ms2400 3.pdf` - MS 2400-3:2019 Retailing
- `halal audit.pdf` - supplied Halal audit training material
- `halal.pdf` - supplied Halal awareness training material
- `JAKIM_MS_Halal_Standards_Compendium_Exhaustive_Reference.pdf` - supplied standards compendium
- `JAKIM_MS_Halal_Standards_MAXIMUM_DEPTH_Compendium.pdf` - supplied maximum-depth compendium

## Contents

1. `01_MASTER_STANDARDS_STACK.md` - hierarchy, catalogue, authority boundaries and complete IQ300 model
2. `02_MS2400_FULL_CLAUSE_CONTROL_MAP.md` - transportation, warehousing and retailing clause/control architecture
3. `03_SECTOR_STANDARDS_CONTROL_MAP.md` - MS 1500, 2424, 2634, 2738, 2803, 2393, 2627, 1900, 2691 and 2610
4. `04_CERTIFICATION_AUDIT_SERTU_STUNNING.md` - audit lifecycle, MPPHM/MHMS linkage, sertu and stunning boundaries
5. `05_IQ300_EVIDENCE_TRUST_PROCESS_FLOWS.md` - Evidence Fabric, Digital Audit Twin, Trust Graph, event schema and process flows
6. `06_SOURCE_PROVENANCE_AND_VERIFICATION.md` - source register, verification classes and version-freeze rules
7. `07_REQUIREMENT_OBJECT_SCHEMA.json` - machine-readable requirement/evidence/authority decision schema

## IQ300 full matrix

`iq300-full-matrix/` is the logical upgrade layer. It contains the complete numbered-clause object set extracted from the three supplied MS 2400 PDFs: **613 unique requirement objects**.

The clause-level machine path is:

`Clause -> Requirement Intent -> Applicability -> Control -> HCP -> Evidence -> Audit Test -> Finding -> Corrective Action -> Re-verification -> Authority Gate -> Trust State`

It also contains per-standard machine-readable shards, a JSON schema, control catalog, authority-gate catalog, audit-test library, annex map, process-flow library, QA report, and sector-standard source-gap register.

## Core doctrine

`Shariah/fatwa -> competent authority -> certification operating layer -> technical standards -> controls/HCPs -> evidence -> human assessment -> authority decision -> trust state -> physical/digital release`

## Critical boundary

This folder is an implementation intelligence layer derived from the supplied materials. It is not a replacement for the licensed official Malaysian Standards, MPPHM, MHMS, Protocols, Pekeliling, fatwa, laws or current authority portal. Exact current status must be verified before production rule hard-freeze.
