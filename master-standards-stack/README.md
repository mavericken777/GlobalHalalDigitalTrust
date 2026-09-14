# IQ300 MASTER STANDARDS STACK

This folder is the consolidated JAKIM / JSM Malaysian Halal Standards intelligence layer derived from the supplied standards compendia, supplied MS 2400 PDFs and supplied training material, with a current JSM MySOL catalogue check.

## Core library

The IQ300 all-standard library is in `iq300-all-jakim-ms/` and includes:

- master standards register covering MS 1500:2019, MS 2400-1/-2/-3:2019, MS 2424:2019, MS 2634:2019, MS 2738:2023, MS 2803:2025, MS 2393:2023, MS 2627:2017, MS 2627-2:2025, MS 1900:2025, MS 2691:2021, MS 2610:2015, MS 2809:2025 and MS 2810:2025;
- unified Clause -> Control -> HCP -> Evidence -> Audit Test -> Authority Gate -> Trust State model;
- full Mermaid process-flow library;
- standards coverage matrix;
- master architecture and standards-coverage SVG infographics;
- source coverage, gap and production-freeze register;
- authority gate and audit-test catalog;
- machine-readable object schema.

## Fully numbered clause backbone

`iq300-full-matrix/` contains the individually numbered requirement objects extracted from the three supplied MS 2400 PDFs: **613 unique objects**.

- MS 2400-1:2019 Transportation: 187
- MS 2400-2:2019 Warehousing: 201
- MS 2400-3:2019 Retailing: 225

## Source integrity rule

The supplied compendia contain detailed summaries and clause-family mappings for several sector standards but do not reproduce every licensed normative subclause. IQ300 therefore does not fabricate missing clause text or numbers. Those standards are explicitly represented as source-supported family maps until the licensed current JSM edition is available for final clause-level objectization.

## Current catalogue update

The JSM MySOL Halal-sector catalogue currently surfaces MS 2809:2025 (chemometric product authentication) and MS 2810:2025 (pig skin/hair identification) in addition to the standards already present in the earlier compendium.

Source: https://mysol.jsm.gov.my/search-catalogue?is-advance=1&page=1&sector=204

## Authority boundary

Malaysian Standards are technical documents. Halal certification, Malaysia Halal logo permission, Panel decisions, live protocol values, Shariah/fatwa determinations and regulator approvals remain separate authority-controlled objects.

## Core doctrine

`Source provenance first -> Authority boundaries explicit -> Requirements versioned -> Controls operationalized -> Evidence linked -> Human assessment -> Authority decision -> Trust state -> Physical/digital release`
