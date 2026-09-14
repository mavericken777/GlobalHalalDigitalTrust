# IQ300 - COMPLETE JAKIM / JSM MALAYSIAN HALAL STANDARDS LIBRARY

## Purpose
This folder is the consolidated IQ300 standards library for the Malaysian Halal standards architecture represented by the supplied source corpus and the current JSM MySOL Halal-sector catalogue check.

It is designed as the regulatory intelligence layer between Shariah/authority decisions and operational controls:

`Shariah / Fatwa -> Authority -> Applicable MS -> Requirement -> Applicability -> Control -> HCP -> Risk -> Evidence -> Audit Test -> Finding -> Corrective Action -> Re-verification -> Authority Gate -> Trust State`

## Current core standards represented

1. MS 1500:2019 - Halal food - General requirements
2. MS 2400-1:2019 - Halal supply chain management system - Part 1: Transportation
3. MS 2400-2:2019 - Halal supply chain management system - Part 2: Warehousing
4. MS 2400-3:2019 - Halal supply chain management system - Part 3: Retailing
5. MS 2424:2019 - Halal pharmaceuticals - General requirements
6. MS 2634:2019 - Halal cosmetics - General requirements
7. MS 2738:2023 - Halal consumable goods - General requirements
8. MS 2803:2025 - Usage of animal bone, skin and hair - General requirements for halal products
9. MS 2393:2023 - Islamic and halal terminologies - Definitions and interpretations
10. MS 2627:2017 - Detection of porcine DNA - Test method - Food and food products
11. MS 2627-2:2025 - Detection of porcine DNA - Test method - Part 2: Cosmetics
12. MS 1900:2025 - Shariah-based quality management system - Requirements
13. MS 2691:2021 - Halal profession - General requirements
14. MS 2610:2015 - Muslim-friendly hospitality services
15. MS 2809:2025 - Authentication of products using chemometric techniques
16. MS 2810:2025 - Consumable goods - Test method - Identification of pig skin and hair

Supporting / historical references are separately identified and must not be confused with the current core Halal-specific library.

## Machine-readable backbone

The existing `master-standards-stack/iq300-full-matrix/` contains the individually numbered MS 2400 requirement objects. That source set contains 613 unique numbered objects:

- MS 2400-1:2019: 187
- MS 2400-2:2019: 201
- MS 2400-3:2019: 225

This folder extends that backbone across the full current core library with standard-register objects, sector control families, authority gates, process flows and source-gap governance.

## Non-fabrication / non-truncation rule
The supplied compendia provide full-depth summaries and clause-family maps for several standards but do not reproduce every licensed normative subclause. IQ300 therefore does **not** invent missing numbered clauses. Such standards are explicitly labelled as `source_summary_family_map` or `current_catalogue_scope_only` until the licensed official JSM text is available for final clause-level objectization.

## Current source note
The present JSM MySOL Halal-sector catalogue check surfaced MS 2809:2025 and MS 2810:2025 in addition to the standards already represented in the supplied compendium.

Source: https://mysol.jsm.gov.my/search-catalogue?is-advance=1&page=1&sector=204

## Authority boundary
Malaysian Standards are technical documents. Certification, Malaysia Halal logo permission, panel decisions, Shariah determinations, live slaughter/stunning protocol values, regulator approvals and other authority decisions remain distinct controlled objects in IQ300.
