# Global Halal Digital Trust

**GLOBAL HALAL SUPPLY CHAIN LIMITED** · Hong Kong CR **79801544** · formed 11 February 2026

[Trip pack](CHINA_TRIP_2026/00_READ_THIS_FIRST.md) · [Execution board](CHINA_TRIP_2026/EXECUTION_BOARD.md) · [A–Z index](REPO_INDEX.md) · [STATUS](STATUS.md) · [Governance](GOVERNANCE.md) · [License](LICENSE)

## Foundation (locked 2026-09-26)

- **Perak Halal Corporation** — Perak State Government GLC for the Halal industry, local and global.
- **Malaysia Halal system** — State and Federal work as **ONE** on audit, certification and compliance. One MS set. One MYeHALAL path. Sultan is Head of Islam in Perak. The King is Head of the nation.
- Start papers: PHC–JGC MoU (27 Aug 2025) · JGC–Sinotrans framework (Sep 2025) · **GHSC HK–Sinotrans MoU (3 Mar 2026)**.
- Vehicle formed. MoU is the start. Trip executes the annexes (named yard, named lane, first SKU, retailer packs).

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
14. MS 2691:2021 — Halal profession competency  
15. MS 2610:2015 — Muslim-friendly hospitality  
16. MS 2809:2025 — Chemometric authentication  
17. MS 2810:2025 — Pig skin and hair identification  

Normative MS wording is not redistributed. Snapshot: `master-standards-stack/verified-2026-09-17/`.

## Parties

See [`partners/README.md`](partners/README.md). Retailer packs: [`CHINA_TRIP_2026/RETAILERS/`](CHINA_TRIP_2026/RETAILERS/).

## Canonical path

`Authority → Standard/Instrument → Clause → Applicability → Control → Evidence → Audit → Finding → CAPA → Re-verification → Decision → Trust State → Release`

Trust State is an internal model state, not the certificate.

## Engineering notes (do not confuse with the commercial foundation)

- Two legacy MS 2400 compressed assets and an old master tarball are corrupt and [quarantined](00_EXECUTIVE_COMMAND/artifact-quarantine-2026-09-26.json). Use the verified snapshot and playbooks, not those files.
- Illustrated PDF v2 has a cover-year typo on MS 2610 (2014 vs 2015). Catalogue stays **MS 2610:2015**.
- Shipment 001 is the first live lot to evidence — not yet a bill of lading in this git tree.
