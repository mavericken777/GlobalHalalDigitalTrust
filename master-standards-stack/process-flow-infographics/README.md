# AHTE JAKIM/JSM Standards Process-Flow Infographics

This directory is the visual execution layer for the **Amanah Halal Trust Ecosystem (AHTE)** standards library.

> AHTE is an evidence and decision-support platform. Official Halal certification and destination regulatory decisions remain with the competent authorities.

## Deliverables

- `AHTE_HD_VISUAL_ATLAS.md` — complete mermaid graph set (canonical path, 17-standard router, evidence fabric, HITM plane, custody, sertu, lab boundary, audit, port, Shipment 001 corridor, exception states, recall, warehouse).
- `00_AHTE_MASTER_JAKIM_MS_PROCESS_FLOW.svg` — master atlas covering the full standards universe.
- `01_...` through `17_...` — one detailed process-flow SVG per represented standard.
- `STANDARDS_FLOW_SPEC.json` — machine-readable standard/flow definitions.
- `../../tools/generate_ahtem_infographics.py` — reproducible SVG generator.
- `../../.github/workflows/generate-ahtem-infographics.yml` — automatic regeneration on source/spec changes.

## Standards covered

| Flow | Standard | Process emphasis |
|---:|---|---|
| 01 | MS 1500:2019 | Food materials → premises → processing → storage/handling → labelling → audit/release |
| 02 | MS 2400-1:2019 | Transportation scope → carrier/vehicle → loading/seal/custody → transit → handover → release |
| 03 | MS 2400-2:2019 | Warehouse scope → inbound checks → stock status → segregation → inventory → dispatch |
| 04 | MS 2400-3:2019 | Retail receiving → display/handling → sale → returns → recall → release |
| 05 | MS 2424:2019 | Pharmaceutical HMS → materials → manufacturing → QC → outsourced activities → certification |
| 06 | MS 2634:2019 | Cosmetic formula/INCI → source/route → manufacturing → QC → OEM → certification |
| 07 | MS 2738:2023 | Consumable scope → sourcing → manufacture → hygiene/segregation → traceability → release |
| 08 | MS 2803:2025 | Animal material scope → species/source → origin/slaughter → segregation → provenance → release |
| 09 | MS 2809:2025 | Sample/matrix → analytical data → chemometric model → validation → result → evidence |
| 10 | MS 2810:2025 | Sample custody → test method → controls → result → authority linkage |
| 11 | MS 2393:2023 | Term intake → authority definition → semantics → ontology → change control → publication |
| 12 | MS 2627:2017 | Food matrix → sampling → DNA extraction/PCR → controls → result → authority linkage |
| 13 | MS 2627-2:2025 | Cosmetic matrix → sampling → qPCR → controls/validation → result → authority linkage |
| 14 | MS 1900:2025 | Organisation context → leadership → planning → operation → internal audit/review → improvement |
| 15 | MS 2691:2021 | Role → qualification → training → competence → authorisation → renewal/recognition |
| 16 | MS 2610:2015 | Hospitality scope → premises → F&B → service controls → staff/guest journey → assurance |
| 17 | MS 2636:2019 | Medical-device eligibility → QMS/HMS → materials/manufacturing → QC → audit/legal → certification |

## Common AHTE execution chain

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

The graphics are **implementation-oriented paraphrases**. They do not reproduce copyrighted normative standard text. They do not imply JAKIM, MAIN, JAIN, GCC, laboratory or customs endorsement.
