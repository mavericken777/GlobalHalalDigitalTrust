# Global Halal Digital Trust

**GLOBAL HALAL SUPPLY CHAIN LIMITED** · Hong Kong CR **79801544** · incorporation recorded from the supplied scan dated 11 February 2026; original verification remains open

[Current target architecture](00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md) · [Implementation completeness rule](00_EXECUTIVE_COMMAND/IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md) · [Codex rebuild prompt](docs/CODEX_PLATFORM_REBUILD_MASTER_PROMPT_2026-09-30.md) · [Website spec v2.1+](docs/WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md) · [Trip pack](CHINA_TRIP_2026/00_READ_THIS_FIRST.md) · [Execution board](CHINA_TRIP_2026/EXECUTION_BOARD.md) · [A–Z index](REPO_INDEX.md) · [STATUS](STATUS.md)

## Current project architecture — 30 September 2026

The project is a **Global Halal Digital Trust & Trade / Halal Tayyib infrastructure**

Default physical corridor:

**China → GCC direct**

Malaysia is the governance/assurance and authority-connectivity plane unless a Malaysia physical movement is explicitly scoped.

[PILOT: Shipment 001 — China → GCC direct]

Target operating chain:

```text
VERIFIED RAW-MATERIAL ORIGIN
→ SUPPLIER / PRODUCER
→ SAMPLE / SEAL / CHAIN OF CUSTODY
→ CHINA LABORATORY SYSTEM
→ SIGNED SCIENTIFIC EVIDENCE
→ MANUFACTURER / FACTORY SYSTEMS
→ STANDARDS / APPLICABILITY
→ HCP / SCCP / CONTROLS
→ SMART-GLASS AI-ASSISTED SITE AUDIT
→ FINDING / CAPA / RE-VERIFICATION
→ DIRECT JAKIM API / HUMAN AUTHORITY WORKFLOW
→ AHTE TRUST-STATE PROPAGATION
→ PACKAGING / BATCH / LOT / PALLET
→ SINOTRANS WAREHOUSE
→ SINOTRANS END-TO-END LOGISTICS
→ CONTAINER / SEAL / TELEMETRY / CUSTODY
→ ORIGIN PORT / CUSTOMS API
→ INTERNATIONAL TRANSIT
→ GCC PORT / CUSTOMS API
→ IMPORTER / DESTINATION WAREHOUSE
→ DISTRIBUTION / RETAIL
→ BUYER / CONSUMER AUTHORISED VERIFICATION
```

Across the chain:

```text
AHTE
+ 24/7 GHSCL + JAKIM-connected Command Center
+ AI/ML predictive analytics
+ Preemptive Strategy Engine
+ cryptographic/tamper-evident evidence integrity
+ role-based authorised transparency
```

Target transaction-support plane:

`Authorised AHTE trust/trade data → Shariah Financing API → Islamic financing / Takaful / tokenomics`

## No artificial implementation blocks

**FULL ARCHITECTURE NOW → REAL CONNECTORS WHEN AVAILABLE → NO REDESIGN REQUIRED.**

Missing production APIs, credentials, partner feeds, lab interfaces, port systems, financial counterparties or transaction data do **not** justify deleting, hiding, disabling or downgrading the target capability. Implement the complete production interface/workflow with replaceable development/sandbox providers until the real connector is available.

Development state must be clearly labelled and must not be represented as real authority, partner or transaction evidence.

## Commercial foundation

- **Perak Halal Corporation** — Perak State Government GLC for the Halal industry, local and global.
- **GHSCL Hong Kong** — international operating and digital-infrastructure vehicle.
- **AHTE** — continuous standards, evidence, compliance, traceability and trust intelligence.
- **Direct JAKIM API** — target authority-system connectivity according to authorised production scope.
- **Sinotrans** — target warehouse + end-to-end logistics real-time evidence integration.
- **China laboratory / traceability plane** — scientific evidence and physical/digital identity integration.
- **Port/customs interfaces** — authorised minimum-necessary trust/API access; sovereign decisions remain with competent authorities.
- **GCC destination layer** — importer, customs, authority, warehouse, distributor, retailer and verification.
- **Shariah Finance/Takaful/tokenomics** — target transaction-support plane; independent financial/Shariah/regulatory decisions remain external.

Start papers recorded in the repository include PHC–JGC, JGC–Sinotrans and GHSC HK–Sinotrans instruments/summaries. Execution status remains controlled by the trip/signing registers; a prepared or reported instrument is not automatically a production integration.

## Readiness

Commercial foundation is recorded; current repository status remains controlled by [`STATUS.md`](STATUS.md).

The [readiness register](00_EXECUTIVE_COMMAND/october-2026-readiness.json) records travel as `NOT_TRAVEL_READY` and signing as `NOT_SIGNING_READY`. Operator-reported `TRAVEL_READY` wording in the status and trip pack is not yet reconciled with the register's open travel gates and missing closure references. This describes repository evidence completeness; it does not determine whether the delegation can travel. Reconciliation requires confirmed gate updates and evidence references, followed by execution-board regeneration.

Target architecture completeness and production readiness are separate:

- target architecture may be fully built with development providers;
- production activation requires real external permissions, security controls, credentials, counterparties and transaction-native evidence;
- Shipment 001 remains uninstantiated until transaction evidence exists.

## What this repository is

This repository contains:

- governance and doctrine;
- standards/applicability architecture;
- evidence/trust schemas;
- China execution pack;
- laboratory integration architecture;
- smart-glass audit specification;
- Sinotrans warehouse/logistics integration;
- port/customs workflows;
- Platinum real-time monitoring;
- Command Center architecture;
- Shariah Financing API/Takaful/tokenomics architecture;
- website/Codex build specifications;
- partner/trip materials;
- reference software.

The code under `platform/` is a **reference implementation**, its the real model for the production multi-region network and the live authority/partner integration.

## Core principles

> **Data stays where it belongs. Trust travels.**

> **Certificate ≠ Trust.**

> **NOT DETECTED ≠ HALAL.**

> **AI assists; competent humans/authorities decide where the decision class requires them.**

A hash proves integrity of the hashed content after creation; it does not by itself prove truth, authority or Halal status.

## 17-standard operating catalogue

1. MS 1500:2019 — Halal food
2. MS 2400-1:2019 — Transport
3. MS 2400-2:2019 — Warehousing
4. MS 2400-3:2019 — Retailing
5. MS 2424:2019 — Pharmaceuticals
6. MS 2634:2019 — Cosmetics
7. MS 2636:2019 — Medical device
8. MS 2738:2023 — Consumable goods
9. MS 2803:2025 — Animal bone, skin and hair
10. MS 2393:2023 — Islamic terminology
11. MS 2627:2017 — Porcine DNA (food)
12. MS 2627-2:2025 — Porcine DNA (cosmetics)
13. MS 1900:2025 — Shariah-based QMS
14. MS 2691:2021 — Halal profession — General requirements
15. MS 2610:2015 — Muslim-friendly hospitality
16. MS 2809:2025 — Chemometric authentication
17. MS 2810:2025 — Pig skin and hair identification

AHTE is not limited to MS2400. It resolves the complete applicable Malaysian/JAKIM operating framework plus destination requirements and applicable contractual requirements.

Normative MS wording is source-governed and not redistributed. Current standards registry: `master-standards-stack/iq300-all-jakim-ms/01_MASTER_STANDARDS_REGISTER.md`; current authority/source status must be rechecked against JSM/JAKIM before operational reliance.

## Canonical path

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

Trust State is a machine-readable evidence/operational state, not the certificate.

## Current engineering controls

- The superseded 17 September 2026 standards package has been removed from the current repository tree.
- Three corrupt legacy archives remain retired/quarantined; do not reconstruct normative content from corrupted assets.
- The replacement MS2400 source index is an index/locator asset, not licensed normative text or a complete control set.
- The reviewed derived Sinotrans MS2400 playbook bundle must not override verified source/control mappings where conflicts exist.
- `platform/` reference runtime and `platform/web/` prototype are not the complete production platform.
- Current website/Codex implementation is governed by the v2.1+ website specification and v2.1+ Codex master prompt.
- Current machine architecture registry v1.1.0+ carries the no-artificial-block implementation rule.
