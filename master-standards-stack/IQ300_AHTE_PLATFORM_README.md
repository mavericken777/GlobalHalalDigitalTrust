# IQ300 - Amanah Halal Trust Ecosystem (AHTE)

## Mission

Map the Amanah Halal Trust Ecosystem end-to-end against the JAKIM/JSM Malaysian Halal standards architecture and operationalise the resulting controls, evidence, audit, authority and trade workflows across the China ↔ Malaysia ↔ GCC corridor.

## Sovereign doctrine

AHTE treats the complete Malaysian Halal standards and governance architecture represented in the IQ300 library as the sovereign operating baseline for the ecosystem. The platform operationalises standards as authoritative system objects, controls, HCPs, evidence requirements, audit tests, authority gates, trust states and execution workflows.

## Core architecture

`Authority -> Standard/Instrument -> Requirement -> Applicability -> Control -> HCP -> Evidence -> Audit Test -> Finding -> Corrective Action -> Re-verification -> Authority Gate -> Trust State -> Operational Release`

## Current standards universe

The Master Standard Stack currently contains **17 standards/standard contexts**:

1. MS 1500:2019 — Halal food — General requirements
2. MS 2400-1:2019 — Halal supply chain management system — Transportation
3. MS 2400-2:2019 — Halal supply chain management system — Warehousing
4. MS 2400-3:2019 — Halal supply chain management system — Retailing
5. MS 2424:2019 — Halal pharmaceuticals — General requirements
6. MS 2634:2019 — Halal cosmetics — General requirements
7. MS 2738:2023 — Halal consumable goods — General requirements
8. MS 2803:2025 — Usage of animal bone, skin and hair — General requirements for halal products
9. MS 2809:2025 — Authentication of products using chemometric techniques
10. MS 2810:2025 — Consumable goods — Test method — Identification of pig skin and hair
11. MS 2393:2023 — Islamic and halal terminologies — Definitions and interpretations
12. MS 2627:2017 — Detection of porcine DNA — Test method — Food and food products
13. MS 2627-2:2025 — Detection of porcine DNA — Test method — Part 2: Cosmetics
14. MS 1900:2025 — Shariah-based quality management system — Requirements
15. MS 2691:2021 — Halal profession — General requirements
16. MS 2610:2015 — Muslim-friendly hospitality services — supporting hospitality context
17. MS 2636:2019 — Halal medical device — General requirements

Current catalogue verification is maintained against the JSM MySOL NSC 09 Halal catalogue. Historical and withdrawn editions are retained as lineage data.

## Deliverables

- `AMANAH_PLATFORM_AZ_MAPPING.md` — A-Z platform decomposition and standard-to-platform matrix.
- `iq300-all-jakim-ms/` — Master standards register, full standards matrix, requirement/control/HCP/evidence architecture and standards lineage.
- `iq300-full-matrix/` — 613 numbered MS 2400 requirement objects from the three supplied MS 2400 source PDFs.
- `process-flow-infographics/` — complete 17-standard infographic atlas and automated generator.
- `CHINA_EXECUTION_PACK/` — complete China implementation pack.
- `china-deployment/CHINA_SOVEREIGN_HOD_DEBRIEF.md` — HOD decision and deployment package.

## China Execution Pack

The China execution architecture is organised as a synchronized physical + digital corridor:

`China Manufacturer -> Factory Systems -> AHTE Trust/Evidence -> Production/Batch -> Pallet/Container/Seal -> China Export/Port -> Transit -> GCC Border -> Destination Warehouse -> Retail -> Trust Verification`

The pack contains:

1. Department-by-department China/Malaysia/GCC RACI.
2. China ↔ Malaysia ↔ GCC rule-precedence engine.
3. Complete Shipment 001 event catalogue.
4. Factory ERP/MES/QMS/WMS/LIMS/API integration contracts.
5. Smart-glass audit specification.
6. Port officer UI/workflow specification.
7. Cryptographic trust-anchor architecture.
8. China Pilot → Shipment 001 → GCC Release operating playbook.
9. Machine-readable execution manifest.

## Full Master Standards Matrix

The canonical full matrix is:

`CHINA_EXECUTION_PACK/09_MASTER_STANDARDS_FULL_MATRIX.md`

Every standard row maps to AHTE domains, HCP families, evidence profiles, audit tests, authority gates and process-flow infographics.

## Machine-readable baseline

The unified standards library contains **684 requirement/control objects**, including **613 individually numbered MS 2400 objects**. The China Execution Pack adds canonical event, rule, API, identity, trust-anchor and operating-gate specifications.

## Physical + digital binding

The system binds:

`material -> production -> batch/lot -> package -> pallet -> container -> seal -> custody -> border -> warehouse -> retail`

to its corresponding digital evidence, event and authority state. Each critical physical transition creates or consumes a signed digital event.

## A-Z platform layer

`AMANAH_PLATFORM_AZ_MAPPING.md` maps A–Z platform domains from Authority & Accountability through Zero-Knowledge / selective disclosure and Evidence Sovereignty.

## Source references

JSM MySOL Halal catalogue:
`https://mysol.jsm.gov.my/search-catalogue?keyword=halal`

JSM MySOL NSC 09 sector catalogue:
`https://mysol.jsm.gov.my/search-catalogue?is-advance=1&page=1&sector=204`

MS 2636:2019 catalogue result:
`https://mysol.jsm.gov.my/search-catalogue?keyword=halal&page=4`
