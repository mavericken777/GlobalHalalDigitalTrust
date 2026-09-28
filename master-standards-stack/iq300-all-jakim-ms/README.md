# IQ300 — COMPLETE JAKIM / JSM MALAYSIAN HALAL STANDARDS LIBRARY

## Purpose

This directory is the consolidated IQ300 standards library for the Malaysian Halal standards architecture represented in the project source corpus and cross-checked against the current JSM MySOL NSC 09 Halal-sector catalogue.

## Canonical full matrix

`../CHINA_EXECUTION_PACK/09_MASTER_STANDARDS_FULL_MATRIX.md`

## Current IQ300 standards universe

1. MS 1500:2019 — Halal food — General requirements
2. MS 2400-1:2019 — Halal supply chain management system — Part 1: Transportation
3. MS 2400-2:2019 — Halal supply chain management system — Part 2: Warehousing
4. MS 2400-3:2019 — Halal supply chain management system — Part 3: Retailing
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

## Matrix architecture

Every standard is represented through the IQ300 chain:

`Standard -> Edition/Status -> Applicability -> Requirement -> Control Objective -> Control -> HCP -> Risk -> Evidence -> Audit Test -> Finding -> Corrective Action -> Re-verification -> Authority Gate -> Trust State`

## Machine-readable backbone

The [current source index](../iq300-full-matrix/source-index-2026-09-27/SOURCE_INDEX_MANIFEST.json) has **628 distinct numbered heading locators** across supplied MS 2400-1/-2/-3:2019 editions (192/206/230). It contains clause IDs and 1-based PDF page locations, not licensed normative wording or a validated requirement/control mapping.

The former 187/201/225 = 613 proposed control objects are **historical and incomplete**: five deeper numbered headings were omitted in each part. The transport and retail compressed assets and the old master archive failed integrity and were retired; only the 201-object warehouse gzip remains as a historical partial mapping. See the [source review](../18_SUPPLIED_PDF_SOURCE_REVIEW_2026-09-27.md).

The wider standards library extends the same operating model across food, transport, warehousing, retailing, pharmaceuticals, cosmetics, consumables, animal-derived materials, analytical methods, terminology, Shariah-based QMS, halal profession, hospitality and medical devices.

## Process-flow visual layer

`../process-flow-infographics/` contains the complete **17-standard** process-flow infographic set, including the master atlas.

## Standards lineage

Historical/withdrawn standards remain available as lineage references where they establish replacement relationships or explain the evolution of the current Malaysian Halal standards stack. They are not silently treated as current production editions.

## Current source reference

JSM MySOL Halal catalogue:
`https://mysol.jsm.gov.my/search-catalogue?keyword=halal`

NSC 09 Halal sector catalogue:
`https://mysol.jsm.gov.my/search-catalogue?is-advance=1&page=1&sector=204`

MS 2636:2019 catalogue result:
`https://mysol.jsm.gov.my/search-catalogue?keyword=halal&page=4`

## Operating note

Licensed normative standards are not reproduced verbatim. IQ300 uses source-derived paraphrase, structured requirement/control objects, operational mappings, provenance and version metadata.
