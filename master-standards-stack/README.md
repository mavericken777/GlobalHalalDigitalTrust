# IQ300 MASTER STANDARDS STACK

This folder is the consolidated JAKIM / JSM Malaysian Halal Standards intelligence and execution layer for AHTE, incorporating the current JSM MySOL NSC 09 Halal-sector catalogue and the project source corpus.

## Full current standards matrix

The canonical full matrix is:

`CHINA_EXECUTION_PACK/09_MASTER_STANDARDS_FULL_MATRIX.md`

The current IQ300 operating universe contains **17 standards/standard contexts**:

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

Historical and withdrawn editions remain in the repository as lineage references and are not silently mixed with current production editions.

## Core machine architecture

`Authority -> Standard/Instrument -> Requirement -> Applicability -> Control -> HCP -> Evidence -> Audit Test -> Finding -> Corrective Action -> Re-verification -> Authority Gate -> Trust State -> Physical/Digital Release`

## Core library

`iq300-all-jakim-ms/` contains the standards register, unified control/HCP/evidence model, process-flow material, authority gates and standards metadata.

`iq300-full-matrix/` contains **613 numbered MS 2400 objects** from the three supplied MS 2400 source PDFs:

- MS 2400-1:2019 Transportation — 187
- MS 2400-2:2019 Warehousing — 201
- MS 2400-3:2019 Retailing — 225

The wider library represents the remaining standards through their corresponding standard profiles, control families, HCP families, evidence models, audit tests, authority gates and operational workflows.

## Visual layer

`process-flow-infographics/` contains the complete **17-standard process-flow infographic atlas** plus reproducible generation assets.

## China Execution Pack

`CHINA_EXECUTION_PACK/` is the integrated China deployment layer:

- department-by-department RACI;
- China ↔ Malaysia ↔ GCC rule-precedence engine;
- complete Shipment 001 event catalogue;
- factory ERP/MES/QMS/WMS/LIMS integration contracts;
- smart-glass audit specification;
- port officer UI/workflow specification;
- cryptographic trust-anchor architecture;
- China Pilot → Shipment 001 → GCC Release operating playbook;
- full standards matrix and machine-readable execution manifest.

## AHTE platform mapping

`AMANAH_PLATFORM_AZ_MAPPING.md` maps the platform across A–Z domains from Authority through Zero-Knowledge / selective disclosure, including the standards-to-domain/HCP/evidence/audit/authority relationships.

## Source and version control

Current catalogue verification source:

`https://mysol.jsm.gov.my/search-catalogue?keyword=halal`

NSC 09 Halal sector catalogue:

`https://mysol.jsm.gov.my/search-catalogue?is-advance=1&page=1&sector=204`

MS 2636:2019 catalogue result:

`https://mysol.jsm.gov.my/search-catalogue?keyword=halal&page=4`

Current status, revision, confirmation, effective date and replacement lineage are maintained as structured metadata. Licensed normative text is not reproduced verbatim.
