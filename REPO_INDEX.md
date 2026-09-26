# Repository index — A–Z operating map

Control date: 2026-09-26  
Vehicle: **GLOBAL HALAL SUPPLY CHAIN LIMITED** · Hong Kong CR **79801544** · formed 11 Feb 2026

## Start here

| Need | Open |
|---|---|
| Trip room line + foundation | [`CHINA_TRIP_2026/00_READ_THIS_FIRST.md`](CHINA_TRIP_2026/00_READ_THIS_FIRST.md) |
| What to fill in China | [`CHINA_TRIP_2026/EXECUTION_BOARD.md`](CHINA_TRIP_2026/EXECUTION_BOARD.md) |
| Papers already in hand | [`CHINA_TRIP_2026/01_INSTRUMENT_REGISTER.md`](CHINA_TRIP_2026/01_INSTRUMENT_REGISTER.md) |
| Malaysia Halal system (State + Federal as ONE) | [`CHINA_TRIP_2026/MALAYSIA_HALAL_AUTHORITY_MAP.md`](CHINA_TRIP_2026/MALAYSIA_HALAL_AUTHORITY_MAP.md) |
| MoA templates (CODA, Sinotrans x2, NICFS x2) | [`CHINA_TRIP_2026/MOA_TEMPLATES/`](CHINA_TRIP_2026/MOA_TEMPLATES/) |
| Lulu / MAF-Carrefour / Tamimi / noon | [`CHINA_TRIP_2026/RETAILERS/`](CHINA_TRIP_2026/RETAILERS/) |
| Runtime honesty (what the code actually is) | [`STATUS.md`](STATUS.md) |
| Doctrine | [`00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md`](00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md) |

## A–Z map

| Letter | Subject | Path |
|---|---|---|
| A | Authority map, Malaysia | `CHINA_TRIP_2026/MALAYSIA_HALAL_AUTHORITY_MAP.md` |
| B | Business / economics (assumptions) | `deliverables/13_BUSINESS_MODEL_AND_ECONOMICS.md` |
| C | CODA | `partners/coda/` + `CHINA_TRIP_2026/MOA_TEMPLATES/MOA_CODA.md` |
| D | Doctrine IQ300 | `00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md` |
| E | Evidence / schemas | `schemas/` + `00_EXECUTIVE_COMMAND/schema-registry.json` |
| F | Field log | `CHINA_TRIP_2026/FIELD_LOG.md` |
| G | GHSC HK | `partners/ghsc-hk/` |
| H | HITM / default-deny | `platform/` + `00_EXECUTIVE_COMMAND/policies/hitm-default-deny.rego` |
| I | Instruments | `CHINA_TRIP_2026/01_INSTRUMENT_REGISTER.md` |
| J | JAKIM / JAIPK / JSM — one system | authority map |
| K | King / Sultan — Heads of Islam | authority map |
| L | Lulu + logistics MoA | `CHINA_TRIP_2026/RETAILERS/LULU/` + Sinotrans logistics MoA |
| M | MS catalogue (17) | this README + `master-standards-stack/verified-2026-09-17/` |
| N | NICFS lab + traceability | `partners/nicfs/` + two MoAs |
| O | October mission | `00_EXECUTIVE_COMMAND/OCTOBER_2026_STRATEGIC_IMPLEMENTATION_MISSION.md` — operate from `CHINA_TRIP_2026/` |
| P | PHC | `partners/phc/` |
| Q | Quarantine (corrupt legacy archives) | `00_EXECUTIVE_COMMAND/artifact-quarantine-2026-09-26.json` |
| R | Retailers | `CHINA_TRIP_2026/RETAILERS/` |
| S | Sinotrans + STATUS + standards freeze snapshot | `partners/sinotrans/` + `STATUS.md` + `verified-2026-09-17/` |
| T | Tamimi + traceability MoA | retailer pack + NICFS trace MoA |
| U | UAE receiving (Lulu / MAF / noon) | retailer pack |
| V | Verified standards snapshot | `master-standards-stack/verified-2026-09-17/` |
| W | Warehouse MoA | `MOA_SINOTRANS_WAREHOUSE.md` |
| X | Execution board | `CHINA_TRIP_2026/EXECUTION_BOARD.md` |
| Y | Year-control / Pekeliling 1/2026 | live JAKIM primary when used operationally |
| Z | Zone / site annex — fill on trip | execution board lines 1–3 |

## Folder tree (working)

```
CHINA_TRIP_2026/          trip file — use this
partners/                 corridor parties
00_EXECUTIVE_COMMAND/     doctrine, registries, mission
master-standards-stack/   MS catalogue + process maps
deliverables/             long-form playbooks
platform/                 reference FastAPI + HITM
runtime/                  legacy demo stack
schemas/ contracts/ circuits/
docs/
```

## Fixed this pass

- Root README no longer says “not travel-ready” or “UNEXECUTED-ROLE” for parties that have start papers + a formed HK company.
- STATUS no longer treats the trip pack as a footnote that cancels the MoUs.
- Partner registry includes PHC, GHSC HK, JGC, NICFS and the four retailers.
- Malaysia text is State + Federal as ONE.
- Corrupt MS 2400 gzips stay quarantined (engineering fact, not a commercial veto).
