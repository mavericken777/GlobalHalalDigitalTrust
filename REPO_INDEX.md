# Repository index — A–Z operating map

**30 September architecture synchronization:** current target architecture consolidated for implementation, website rebuilding and Codex execution. The verified freeze remains unchanged. Historical China→Malaysia pilot wording does not control Shipment 001; default physical corridor is China→GCC direct.

**28 September reconciliation:** commercial foundation is recorded; travel `NOT_TRAVEL_READY`; signing `NOT_SIGNING_READY`. Current controls: [signing matrix](CHINA_TRIP_2026/SIGNING_MATRIX.md), [execution board](CHINA_TRIP_2026/EXECUTION_BOARD.md).

Control date: 2026-09-30
Vehicle: **GLOBAL HALAL SUPPLY CHAIN LIMITED** · Hong Kong CR **79801544** on the project-supplied incorporation scan dated 11 Feb 2026; original verification remains open.

## Start here

| Need | Open |
|---|---|
| **Current target architecture — 30 Sep** | [`00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md`](00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md) |
| **Machine-readable current architecture** | [`00_EXECUTIVE_COMMAND/current-target-architecture-2026-09-30.json`](00_EXECUTIVE_COMMAND/current-target-architecture-2026-09-30.json) |
| **Website rebuild specification v2** | [`docs/WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md`](docs/WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md) |
| Trip room line + foundation | [`CHINA_TRIP_2026/00_READ_THIS_FIRST.md`](CHINA_TRIP_2026/00_READ_THIS_FIRST.md) |
| What to fill in China | [`CHINA_TRIP_2026/EXECUTION_BOARD.md`](CHINA_TRIP_2026/EXECUTION_BOARD.md) |
| Papers already in hand | [`CHINA_TRIP_2026/01_INSTRUMENT_REGISTER.md`](CHINA_TRIP_2026/01_INSTRUMENT_REGISTER.md) |
| Malaysia Halal system | [`CHINA_TRIP_2026/MALAYSIA_HALAL_AUTHORITY_MAP.md`](CHINA_TRIP_2026/MALAYSIA_HALAL_AUTHORITY_MAP.md) |
| MoA templates (CODA, Sinotrans x2, NICFS x2) | [`CHINA_TRIP_2026/MOA_TEMPLATES/`](CHINA_TRIP_2026/MOA_TEMPLATES/) |
| Lulu / MAF-Carrefour / Tamimi / noon | [`CHINA_TRIP_2026/RETAILERS/`](CHINA_TRIP_2026/RETAILERS/) |
| Runtime honesty (what the code actually is) | [`STATUS.md`](STATUS.md) |
| Doctrine | [`00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md`](00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md) |

## 30 September current implementation topology

```text
CHINA ORIGIN
  ↓
RAW MATERIAL / SUPPLIER / SAMPLE / LAB
  ↓
MANUFACTURER + FACTORY SYSTEMS
  ↓
AHTE STANDARDS / EVIDENCE / AI
  ↓
SMART-GLASS AUDIT / CAR / RE-VERIFICATION
  ↓
DIRECT JAKIM API / HUMAN AUTHORITY WORKFLOW
  ↓
AHTE TRUST STATE
  ↓
SINOTRANS WAREHOUSE + END-TO-END LOGISTICS
  ↓
ORIGIN PORT / CUSTOMS API
  ↓
INTERNATIONAL TRANSIT
  ↓
GCC PORT / CUSTOMS API
  ↓
IMPORTER / WAREHOUSE / RETAIL / VERIFICATION

Across all stages:
24/7 GHSCL + JAKIM Command Center
+ AI/ML predictive analytics
+ preemptive strategies
+ integrity-protected evidence
+ role-based authorised transparency

Target transaction-support plane:
Shariah Financing API → Islamic financing / Takaful / tokenomics
```

[PILOT: Shipment 001 — China → GCC direct]

## A–Z map

| Letter | Subject | Path |
|---|---|---|
| A | Authority map, Malaysia | `CHINA_TRIP_2026/MALAYSIA_HALAL_AUTHORITY_MAP.md` |
| B | Business / economics (assumptions) | `deliverables/13_BUSINESS_MODEL_AND_ECONOMICS.md` |
| C | CODA | `partners/coda/` + `CHINA_TRIP_2026/MOA_TEMPLATES/MOA_CODA.md` |
| D | Doctrine IQ300 | `00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md` |
| E | Evidence / schemas | `schemas/` + `00_EXECUTIVE_COMMAND/schema-registry.json` |
| F | Finance / Shariah Finance target plane | `deliverables/13_BUSINESS_MODEL_AND_ECONOMICS.md` + current target architecture |
| G | GHSC HK | `partners/ghsc-hk/` |
| H | HITM / default-deny | `platform/` + `00_EXECUTIVE_COMMAND/policies/hitm-default-deny.rego` |
| I | Instruments | `CHINA_TRIP_2026/01_INSTRUMENT_REGISTER.md` |
| J | JAKIM / direct API target connectivity | doctrine + current target architecture |
| K | Known mandate / contracting entity | authority map |
| L | Lulu + logistics MoA | `CHINA_TRIP_2026/RETAILERS/LULU/` + Sinotrans logistics MoA |
| M | MS catalogue (17) | this README + `master-standards-stack/verified-2026-09-17/` |
| N | NICFS / China lab + traceability | `partners/nicfs/` + `partners/china-food-security-lab/` |
| O | October mission | `00_EXECUTIVE_COMMAND/OCTOBER_2026_STRATEGIC_IMPLEMENTATION_MISSION.md` — operate from `CHINA_TRIP_2026/` |
| P | PHC | `partners/phc/` |
| Q | Quarantine (corrupt legacy archives) | `00_EXECUTIVE_COMMAND/artifact-quarantine-2026-09-26.json` |
| R | Retailers | `CHINA_TRIP_2026/RETAILERS/` |
| S | Sinotrans + STATUS + standards freeze snapshot | `partners/sinotrans/` + `deliverables/07_SINOTRANS_PLAYBOOK.md` + `STATUS.md` + `verified-2026-09-17/` |
| T | Tamimi + traceability MoA | retailer pack + NICFS trace MoA |
| U | UAE receiving (Lulu / MAF / noon) | retailer pack |
| V | Verified standards snapshot | `master-standards-stack/verified-2026-09-17/` |
| W | Website v2 / Warehouse MoA | `docs/WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md` + `MOA_SINOTRANS_WAREHOUSE.md` |
| X | Execution board | `CHINA_TRIP_2026/EXECUTION_BOARD.md` |
| Y | Year-control / Pekeliling 1/2026 | live JAKIM primary when used operationally |
| Z | Zone / site annex — fill on trip | execution board commercial outputs |

## Folder tree (working)

```text
CHINA_TRIP_2026/          trip file — use this
partners/                 corridor parties
00_EXECUTIVE_COMMAND/     doctrine, registries, mission, current target architecture
master-standards-stack/   MS catalogue + process maps
deliverables/             long-form playbooks
platform/                 reference FastAPI + HITM + public-web prototype
runtime/                  legacy demo stack
schemas/ contracts/ circuits/
docs/                     website/codex/implementation specifications
```

## Current control changes — 30 September

- Current target project topology is consolidated in `CURRENT_TARGET_ARCHITECTURE_2026-09-30.md` without changing the verified freeze.
- Default physical corridor is China→GCC direct; Malaysia remains governance/assurance unless separately scoped as physical transit.
- Direct JAKIM API is the target authority connectivity path.
- 24/7 GHSCL + JAKIM Command Center is a first-class operating layer.
- AI/ML includes predictive analytics plus explicit preemptive strategy generation subject to HITM/authority gates.
- Sinotrans is modeled as warehouse + end-to-end logistics real-time evidence integration.
- Port/customs users receive authorised API/trust interfaces while retaining sovereign decision authority.
- Shariah Financing API / Takaful / tokenomics is a target transaction-support plane; no unverified counterparty/product/regulatory approval is implied.
- Website v2 supersedes older public architecture where inconsistent.

## Current control changes — 28 September

- Commercial foundation, travel, signing, demonstration and production are separate statuses.
- The [signing matrix](CHINA_TRIP_2026/SIGNING_MATRIX.md) maps the original six instruments and four optional drafts.
- Partner v2.1 restores structured authority/evidence fields and retains unresolved laboratory identities separately.
- The [closure report](00_EXECUTIVE_COMMAND/RECONCILIATION_2026-09-27.md) records completed fixes and external dependencies.
- Three corrupt legacy archives were retired on 27 September. The valid replacement holds 628 MS 2400 clause/page locators without licensed text or completed control rules; the historical 613-object assertion is incomplete. See [source status](STATUS.md) and [retirement ledger](00_EXECUTIVE_COMMAND/artifact-quarantine-2026-09-26.json).
