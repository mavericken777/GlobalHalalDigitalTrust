# IQ300 MASTER STANDARDS STACK

This folder is the consolidated JAKIM / Department of Standards Malaysia Halal standards intelligence and execution layer for the Amanah Halal Trust Ecosystem (AHTE).

## Canonical verified baseline

The controlled current package is:

`verified-2026-09-17/`

It consolidates the current standards catalogue, revision/supersession register, JAKIM MPPHM 2020/MHMS 2020 operating layer, all-standard clause/control/evidence mapping, sertu and stunning/protocol linkage, audit/evidence test library, China -> GCC manufacturer validation, A-Z gap accounting and source register.

Use `verified-2026-09-17/MANIFEST.json` as the machine-readable package declaration.

## Standards universe

The current IQ300 operating universe contains 17 standards/standard contexts:

1. MS 1500:2019 — Halal food — General requirements
2. MS 2400-1:2019 — Halal supply chain management system — Transportation
3. MS 2400-2:2019 — Halal supply chain management system — Warehousing
4. MS 2400-3:2019 — Halal supply chain management system — Retailing
5. MS 2424:2019 — Halal pharmaceuticals — General requirements
6. MS 2634:2019 — Halal cosmetics — General requirements
7. MS 2636:2019 — Halal medical device — General requirements
8. MS 2738:2023 — Halal consumable goods — General requirements
9. MS 2803:2025 — Usage of animal bone, skin and hair — General requirements for halal products
10. MS 2393:2023 — Islamic terminology
11. MS 2627:2017 — Detection of porcine DNA — Test method — Food and food products
12. MS 2627-2:2025 — Detection of porcine DNA — Test method — Part 2: Cosmetics
13. MS 1900:2025 — Shariah-based quality management system — Requirements
14. MS 2691:2021 — Halal profession competency standard
15. MS 2610:2015 — Muslim-friendly hospitality services — Requirements
16. MS 2809:2025 — Authentication of products using chemometric techniques
17. MS 2810:2025 — Consumable goods — Test method — Identification of pig skin and hair

Historical/withdrawn/replaced standards are retained as version lineage only and must not silently override current editions.

## Source-depth model

### Source-verified numbered requirement objects

`iq300-full-matrix/` contains 613 numbered MS 2400 requirement objects derived from the three controlled user-supplied licensed PDFs:

- MS 2400-1:2019 Transportation — 187
- MS 2400-2:2019 Warehousing — 201
- MS 2400-3:2019 Retailing — 225

### Public structure verified

The current package maps publicly verifiable clause structures, controls, HCPs, evidence, audit tests and authority gates for:

- MS 1500:2019
- MS 2424:2019
- MS 2634:2019
- MS 2636:2019
- MS 2738:2023
- MS 2393:2023
- MS 2627:2017
- MS 2691:2021
- MS 2610:2015

### Current status/control domains verified; detailed normative subclauses source-locked

- MS 2803:2025
- MS 2627-2:2025
- MS 1900:2025
- MS 2809:2025
- MS 2810:2025

This is deliberate. The repository does not fabricate unavailable copyrighted normative wording to create false clause-level completeness.

## Core machine architecture

`Authority -> Standard/Instrument -> Requirement -> Applicability -> Control -> HCP/SCCP -> Evidence -> Audit Test -> Finding -> Corrective Action -> Re-verification -> Authority Gate -> Trust State -> Physical/Digital Release`

Every requirement object is source/version aware. Historical events remain bound to the rule version applicable at the event time.

## JAKIM operating layer

The verified package maps:

- all 71 MPPHM (Domestic) 2020 procedure headings into operational controls/evidence/authority gates;
- all 13 MHMS 2020 HAS elements;
- IHCS as a distinct authority-defined smaller-industry profile;
- adequacy/site/follow-up audit, monitoring/surveillance, panel, certificate, logo, sampling/lab, complaints/objections/appeals and certificate-holder controls;
- MyHALALINGREDIENTS effective 15 August 2025;
- Malaysia Halal e-Certificate implementation from 5 May 2025 for approved applications under the JAKIM announcement.

## Sertu and slaughter/stunning

Sertu is modelled as a governed contamination-control lifecycle, not generic sanitation. Cross-standard sertu links cover MPPHM/MHMS and applicable MS 1500, MS 2400, MS 2424, MS 2634 and MS 2636 controls.

Slaughter/stunning uses rule precedence:

`current law/fatwa -> current JAKIM/DVS Malaysian Protocol for Halal Meat and Poultry Production -> current MPPHM annex/guidance -> MS 1500:2019 -> facility validated SOP/settings`.

Old MS 1500:2009 parameters are not hard-coded as current MS 1500:2019 requirements.

## Analytical evidence

MS 2627, MS 2627-2, MS 2809 and MS 2810 are evidence-producing methods/standards. Their outputs do not independently create halal certification.

`NOT DETECTED != HALAL` is a non-negotiable engine rule.

## Supporting libraries

- `iq300-all-jakim-ms/` — earlier full catalogue/unified control library retained as supporting lineage
- `process-flow-infographics/` — 17-standard process-flow atlas and generation assets
- `AMANAH_PLATFORM_AZ_MAPPING.md` — A-Z platform decomposition
- `AHTE_PLATINUM_REAL_TIME_MONITORING_STACK.md` — continuous/assisted/evidence/authority monitoring architecture
- `CHINA_EXECUTION_PACK/` and `china-execution-pack/` — China deployment and Shipment 001 execution assets
- `china-deployment/` — China sovereign/data/counterpart implementation materials

## China -> GCC direct execution

The canonical pilot corridor is **China -> GCC direct**.

The verified package includes a ten-manufacturer primary-source screen and a qualification workflow. No manufacturer public website claim is treated as a valid shipment certificate, GCC import approval or commercial commitment.

Shipment 001 release requires:

`factory/SKU evidence -> exact halal certificate and issuer/scope/validity -> destination recognition/importer/product/label controls -> buyer/PO -> pilot batch -> logistics qualification -> container/seal/custody -> border release -> receiving verification`.

## Current official source entry points

- Department of Standards Malaysia: `https://www.msonline.gov.my/`
- Standards Malaysia Halal sector catalogue: `https://www.msonline.gov.my/ms/standard/standards-sector/halal`
- JAKIM official portal: `https://www.islam.gov.my/`
- JAKIM Halal status directory / MYeHALAL entry: `https://myehalal.halal.gov.my/portal-halal/v1/`

Individual current standards/procedure versions must be rechecked in the official source immediately before operational reliance.

## Governance boundary

Malaysian Standards are technical normative instruments. Certification remains within the competent Halal authority and applicable legal/certification framework. AHTE supports evidence, controls, traceability, auditability and decision workflows; it does not independently issue or override Malaysia Halal certification.

Licensed normative text is not reproduced in this repository. `SOURCE-LOCKED` status is a controlled truth condition, not a documentation omission.
