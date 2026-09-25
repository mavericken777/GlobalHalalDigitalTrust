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

## 26 September 2026 source-verification events

### Master PDF

A 43-page user-supplied master reference, `platinum_tier_ms_master.pdf` (SHA12 `4f1240560664`), was nano-audited against the frozen standards package and repository.

Recorded under:

`master-standards-stack/verified-2026-09-26/`

### Illustrated v2 PDF

A 30-page illustrated derivative, `platinum_tier_v2_illustrated.pdf` (SHA12 `f3696b038f41`), containing 30 detailed process-flow diagrams, was separately delta-audited against both the master PDF and repository.

Recorded under:

`master-standards-stack/verified-2026-09-26-v2/`

Status of both packages: **POST-FREEZE PROPOSAL — not promoted into `verified-2026-09-17/` doctrine/freeze.**

Key v2 findings:

- the 17-standard architecture remains materially consistent with the controlled repository;
- the illustrated source is a mixed-source visual compilation, not an authority-issued normative instrument;
- diagrams compress applicability and authority gates and therefore cannot compile directly to production policy;
- v2 contains an internal source-quality conflict: cover `MS 2610:2014` vs body `MS 2610:2015`; the controlled catalogue remains unchanged;
- figures 25-26 embed historical MS 1500:2009 stunning values and must not be represented as current MS 1500:2019 requirements;
- figures 03/17/18 contain laboratory/PCR/Ct logic that remains analytical evidence only;
- figures 19-20 contain MS1900 governance composition/cadence/reporting constants not established by the live public catalogue;
- figures 02/21-24/28 operationalise claimed 2026 MPPHM amendment details that remain blocked pending JAKIM primary text.

[OPEN GATE: PRIMARY SOURCE FOR MPPHM 2020 PINDAAN 2026 — owner: JAKIM — blocking: exact amendment text, effective date, scope and applicability]

[OPEN GATE: SOURCE CONFLICT — V2-MS2610-YEAR — owner: Department of Standards Malaysia — blocking: illustrated-source metadata accuracy]

[SOURCE-LOCKED: v2 historical stunning parameters for current operations — required: current JAKIM/DVS authority source + facility applicability]

[SOURCE-LOCKED: v2 analytical thresholds — required: current licensed method text + laboratory validation/matrix scope]

[SOURCE-LOCKED: v2 MS1900 governance constants — required: current licensed MS 1900:2025 clauses or competent-source instrument]

## Runtime source-lock gaps identified in repository audits

The legacy/reference `runtime/policies/` layer still includes demonstration constants such as fixed cold-chain bounds, a fixed spatial-segregation distance, fixture-based facility status and demonstration madhhab weighting/HTI logic. These values are **not promoted as Malaysian Standard/JAKIM normative rules** by this repository status.

Before any production use they must be replaced by source-bound control profiles carrying at minimum:

`authority/source -> standard/instrument -> clause/requirement -> applicability -> control profile -> effective date/version -> evidence method -> authority gate`.

[SOURCE-LOCKED: legacy runtime fixed thresholds and jurisprudential demo weights — required: explicit source-bound operational profile or removal before production deployment]

## External air gaps that still exist

- competent-authority systems
- licensed standards text
- official primary source for the claimed 2026 MPPHM amendment details
- laboratory LIMS and accreditation
- current authority applicability for historical stunning settings
- carrier / port / customs APIs
- executed commercial instruments
- production IAM, HA, observability, key management
