# Global Halal Digital Trust

**GLOBAL HALAL SUPPLY CHAIN LIMITED** · Hong Kong CR **79801544** · formed 11 February 2026

[Trip pack](CHINA_TRIP_2026/00_READ_THIS_FIRST.md) · [Execution board](CHINA_TRIP_2026/EXECUTION_BOARD.md) · [A–Z index](REPO_INDEX.md) · [STATUS](STATUS.md) · [Governance](GOVERNANCE.md) · [License](LICENSE)

## Commercial foundation (recorded 2026-09-26)

- **Perak Halal Corporation** — Perak State Government GLC for the Halal industry, local and global.
- **Malaysia Halal system** — A coordinated national framework with distinct JAKIM/MAIN/JAIN mandates; PHC is the commercial industry participant. See the [authority map](CHINA_TRIP_2026/MALAYSIA_HALAL_AUTHORITY_MAP.md).
- Start papers: PHC–JGC MoU (27 Aug 2025) · JGC–Sinotrans framework (Sep 2025) · **GHSC HK–Sinotrans MoU (3 Mar 2026)**.
- Vehicle formed. MoU is the start. Trip executes the annexes (named yard, named lane, first SKU, retailer packs).

**Readiness:** commercial foundation recorded; travel `NOT_TRAVEL_READY`; signing `NOT_SIGNING_READY`; reference software only. The [readiness register](00_EXECUTIVE_COMMAND/october-2026-readiness.json) and [execution board](CHINA_TRIP_2026/EXECUTION_BOARD.md) control closure. Reported source summaries are indexed separately from reviewed originals.

## What this repository is

The operating file for that corridor: standards catalogue, evidence model, reference runtime (`platform/`), partner files, and the China trip pack.

The code under `platform/` is a **local reference** (FastAPI + default-deny HITM + Compose). It records evidence. It does not print a Malaysian Halal certificate and it is not a multi-region production network.

## Core principle

> Data stays where it belongs. Trust travels.

`NOT DETECTED ≠ HALAL`.

## 17-standard operating set (catalogue)

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

Normative MS wording is not redistributed. Snapshot: `master-standards-stack/verified-2026-09-17/`.

## Parties

See [`partners/README.md`](partners/README.md). Retailer packs: [`CHINA_TRIP_2026/RETAILERS/`](CHINA_TRIP_2026/RETAILERS/).

## Canonical path

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

Trust State is an internal model state, not the certificate.

## Engineering notes (do not confuse with the commercial foundation)

- Three corrupt legacy archives were [retired](00_EXECUTIVE_COMMAND/artifact-quarantine-2026-09-26.json). The [replacement MS 2400 source index](master-standards-stack/iq300-full-matrix/source-index-2026-09-27/SOURCE_INDEX_MANIFEST.json) has 628 numbered clause locators and no licensed standard text. The historical 613 proposed control objects were incomplete.
- The [28 September source review](master-standards-stack/19_SUPPLIED_PDF_RECONCILIATION_2026-09-28.md) checks ten additional attachments. MS 2441-2:2014 concerns sewage treatment and is outside the halal catalogue; the illustrated PDF mislabels MS 2610 as 2014, while its supplied primary edition is 2015.
- The [Platinum compilation review](master-standards-stack/20_PLATINUM_COMPILATION_REVIEW_2026-09-28.md) records duplicate PDF hashes, invalid contents page references and a misidentified MS 2565:2014. Use primary editions for exact controls.
- The [Platinum ZIP triage](master-standards-stack/21_PLATINUM_BUNDLE_TRIAGE_2026-09-28.md) finds an intact 69-file bundle whose index claims 80 files and 12 absent HTML sources. Its standards/assay/business claims require primary-source review.
- Shipment 001 is the first live lot to evidence — not yet a bill of lading in this git tree.
