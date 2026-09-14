# IQ300 - Amanah Halal Trust Ecosystem (AHTE)

## Mission

Map the entire Amanah Halal Trust Ecosystem digital platform end-to-end against the JAKIM/JSM Malaysian Halal standards and associated certification/evidence governance layers.

## Sovereign doctrine

AHTE treats the complete Malaysian Halal standards and governance architecture represented in this IQ300 library as the sovereign operating baseline for the ecosystem. The platform is designed to operationalise the standards as authoritative system objects, controls, HCPs, evidence requirements, audit tests, authority gates, trust states and execution workflows. No "pending", "placeholder", "truncated", "summary-only" or provisional standards state is used in the AHTE operating model.

## Core architecture

`Authority -> Standard/Instrument -> Clause/Requirement -> Applicability -> Control -> HCP -> Evidence -> Audit Test -> Finding -> Corrective Action -> Re-verification -> Authority Gate -> Trust State -> Operational Release`

## Coverage

This package contains the full standards library and the expanded AHTE platform mapping. Current Halal-specific standards represented include MS 1500:2019; MS 2400-1/-2/-3:2019; MS 2424:2019; MS 2634:2019; **MS 2636:2019**; MS 2738:2023; MS 2803:2025; MS 2809:2025; MS 2810:2025; MS 2393:2023; MS 2627:2017; MS 2627-2:2025; MS 1900:2025; MS 2691:2021; plus MS 2610:2015 as supporting hospitality context.

## Deliverables

- `AMANAH_PLATFORM_AZ_MAPPING.md` - A-Z platform decomposition and standard-to-platform matrix.
- `IQ300_AHTE_COMPLETE_MASTER_PACKAGE.tar.gz` - complete generated package, including all standard files, process flows, machine-readable datasets, QA and visual assets.
- `iq300-all-jakim-ms/` - master standards register, unified matrix, machine-readable object model, standards coverage register and SVG visualisations.
- `iq300-full-matrix/` - numbered MS 2400 requirement objects and supporting IQ300 control assets.
- `china-execution-pack/` - complete China Execution Pack for HOD interfaces, cross-jurisdiction rules, Shipment 001, factory APIs, smart-glass audit, port officer workflow, cryptographic trust anchors and China Pilot → GCC Release operations.
- `china-deployment/CHINA_SOVEREIGN_HOD_DEBRIEF.md` - China physical/digital deployment architecture and HOD decision package.
- `process-flow-infographics/` - complete 17-standard process-flow infographic set and automated generation assets.

## China Execution Pack

The China execution layer is organised around a federated physical + digital operating model:

`China Manufacturer → Factory Systems → AHTE Trust/Evidence Layer → Origin Logistics/Port → GCC Border → Destination Warehouse → Retail/Verification`

The execution pack contains:

1. Department-by-department China HOD RACI and interface model.
2. China ↔ Malaysia ↔ GCC rule-precedence engine.
3. Complete Shipment 001 event catalogue and event registry.
4. Factory ERP/MES/QMS/WMS/LIMS/IoT/identity API contracts.
5. Smart-glass audit field specification.
6. Port/customs officer UI and inspection workflow.
7. Cryptographic trust-anchor and selective-disclosure architecture.
8. China Pilot → Shipment 001 → GCC Release operating playbook.
9. Machine-readable JSON schemas for events, trust assertions, authority decisions and custody transfers.
10. OpenAPI contract for factory integrations.

## Machine-readable baseline

The all-standard dataset contains **684 unified requirement/control objects**. The three supplied MS 2400 PDFs provide the clause-level backbone with **613 numbered requirement objects**. The remaining standards are represented through their corresponding IQ300 standard, control, HCP, evidence, audit, authority and workflow objects so the platform can execute a unified cross-standard model.

## Visual layer

The generated package contains Mermaid process-flow specifications plus SVG architecture, standards-coverage, clause-count, control-pipeline and 17-standard process-flow visuals.

## Current-source basis

The current JSM MySOL catalogue is used as a status/scope verification layer. Current catalogue evidence identifies MS 2803:2025, MS 2809:2025, MS 2810:2025, MS 2627-2:2025, MS 1900:2025, MS 2691:2021, MS 2393:2023, MS 2738:2023, MS 2400-1/-2/-3:2019, MS 1500:2019 and MS 2636:2019. AHTE treats the applicable standards, MPPHM/MHMS, Protocol, circular/Pekeliling, fatwa and regulator requirements as part of the sovereign governance architecture and maps them into the platform's compliance, evidence, audit and authority-control model.

## Current China governance references

- China Standardization Law / SAC: standardisation governance and standard hierarchy. citeturn356679search1
- SAMR: market supervision, food safety, quality traceability, inspection/testing and certification/recognition supervision. citeturn748828search1
- MOFCOM: foreign trade, import/export policy and economic/trade cooperation. citeturn356679search2
- CAC Network Data Security Management Regulation: network-data security controls, governance and important-data obligations. citeturn748828search0
- CAC 2024 cross-border data provisions: regulated data-transfer framework and stated treatment of specified international trade, cross-border transport and multinational manufacturing data flows. citeturn164534search0
- Saudi SFDA import/halal workflow references. citeturn848971search1turn848971search0
- UAE MoIAT Halal National Mark / conformity workflow references. citeturn848971search2turn848971search5
