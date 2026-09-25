# Repository status — honest operating picture

Control date: 2026-09-26

## What this repository is

Adopted project specification **plus** a **local reference runtime** under `platform/`.

The reference runtime can record evidence, assessments, HITM evaluations, asserted authority decisions, trust states and corridor events on a single process or Compose stack.

## What this repository is not

| Claim | Actual state |
|---|---|
| Production multi-region platform | **No.** Reference process / Compose only. |
| Smart contracts | **Reference/prototype Solidity exists under `contracts/`; not deployed or authority-endorsed.** |
| Hosted OPA / SPIRE / SCITT / live EPCIS | **Not deployed.** Rego draft/reference policies + in-process PEP. |
| Official Halal certification service | **Forbidden by the authority model/API.** |
| JAKIM / JSM / GCC / lab / customs endorsement | **None on file.** |
| Executed partner contracts | **None on file.** |
| Instantiated Shipment 001 | **No.** Events are pilot-tagged and not transaction-native. |
| External independent audit | **None.** |
| Zero air gap to the real world | **False.** External authorities, labs, carriers and buyers are still outside this git repo. |

## Runtime that does exist

`platform/` — FastAPI reference app, default-deny HITM, tests, Dockerfile, Compose, CI workflow `platform-reference.yml`.

`runtime/` — legacy/reference Trust Gateway + OPA demonstration stack. It contains fixture registries and demonstration thresholds. It must **not** be treated as the normative production control plane without source/version/applicability binding.

## 26 September 2026 source-verification event

A new 43-page user-supplied master reference, `platinum_tier_ms_master.pdf` (SHA12 `4f1240560664`), was nano-audited against the frozen standards package and repository.

The post-freeze reconciliation is recorded under:

`master-standards-stack/verified-2026-09-26/`

Status: **POST-FREEZE PROPOSAL — not promoted into `verified-2026-09-17/` doctrine/freeze.**

Key result:

- the 17-standard catalogue is materially consistent with the frozen repository;
- the PDF is a mixed-source compilation, not a single authority-issued normative instrument;
- exact 2026 MPPHM/MHMS amendment parameters, universal audit durations/cadences, fixed retention/training cycles, laboratory cut-offs, fatwa numeric translations and “universal acceptance criteria” remain source-locked unless independently verified;
- the existing open gate for the primary JAKIM 2026 MPPHM amendment remains blocking.

[OPEN GATE: PRIMARY SOURCE FOR MPPHM 2020 PINDAAN 2026 — owner: JAKIM — blocking: exact amendment text and applicability]

## Runtime source-lock gaps identified in the repository audit

The legacy/reference `runtime/policies/` layer still includes demonstration constants such as fixed cold-chain bounds, a fixed spatial-segregation distance, fixture-based facility status and demonstration madhhab weighting/HTI logic. These values are **not promoted as Malaysian Standard/JAKIM normative rules** by this repository status.

Before any production use they must be replaced by source-bound control profiles carrying at minimum:

`authority/source -> standard/instrument -> clause/requirement -> applicability -> control profile -> effective date/version -> evidence method -> authority gate`.

[SOURCE-LOCKED: legacy runtime fixed thresholds and jurisprudential demo weights — required: explicit source-bound operational profile or removal before production deployment]

## External air gaps that still exist

- competent-authority systems
- licensed standards text
- official primary source for the claimed 2026 MPPHM amendment details
- laboratory LIMS and accreditation
- carrier / port / customs APIs
- executed commercial instruments
- production IAM, HA, observability, key management
