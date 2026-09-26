# Repository status

Control date: 2026-09-26

## Foundation — on

GHSC HK is incorporated (79801544, 11 Feb 2026). Start MoUs are on file (PHC–JGC, JGC–Sinotrans, GHSC–Sinotrans). Perak Halal Corporation is the Perak State Government GLC for the Halal industry. Malaysia State and Federal Halal audit, certification and compliance run as **one** system.

Operating file for the trip: [`CHINA_TRIP_2026/`](CHINA_TRIP_2026/00_READ_THIS_FIRST.md) · execution list: [`EXECUTION_BOARD.md`](CHINA_TRIP_2026/EXECUTION_BOARD.md) · A–Z: [`REPO_INDEX.md`](REPO_INDEX.md).

## What the git tree contains

| Layer | State |
|---|---|
| Corridor vehicle + start papers | On |
| Trip pack, MoAs, retailer dossiers | On |
| MS catalogue + process maps | On (`verified-2026-09-17/`, infographics) |
| Reference runtime `platform/` | Local FastAPI + HITM + Compose |
| Production multi-region host | Not this repo |
| Smart contracts | Prototype under `contracts/` — not deployed |
| Shipment 001 bill of lading | Not yet in git — first live lot is the execution target |
| Priced SLA / named Sinotrans yard | Fill on this trip (execution board 1–5) |

## Standards notes

- Catalogue year for hospitality is **MS 2610:2015** (illustrated v2 cover that says 2014 is wrong).
- Do not use MS 1500:2009 stunning tables as current.
- Pekeliling / MPPHM amendment text is used from JAKIM primary when an audit file is opened.
- Quarantined corrupt archives stay quarantined. They are not the working set.

## Runtime notes

`runtime/policies/` still has demo constants (cold-chain bounds, fixture sites). Do not treat those numbers as MS/JAKIM rules. Bind a source profile before production use.
