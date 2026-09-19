# Repository status — honest operating picture

Control date: 2026-09-20

## What this repository is

Adopted project specification **plus** a **local reference runtime** under `platform/`.

The reference runtime can record evidence, assessments, HITM evaluations, asserted authority decisions, trust states and corridor events on a single process or Compose stack.

## What this repository is not

| Claim | Actual state |
|---|---|
| Production multi-region platform | **No.** Reference process / Compose only. |
| Smart contracts | **None.** |
| Hosted OPA / SPIRE / SCITT / live EPCIS | **Not deployed.** Rego draft + in-process PEP. |
| Official Halal certification service | **Forbidden by the API.** |
| JAKIM / JSM / GCC / lab / customs endorsement | **None on file.** |
| Executed partner contracts | **None on file.** |
| Instantiated Shipment 001 | **No.** Events are pilot-tagged and not transaction-native. |
| External independent audit | **None.** |
| Zero air gap to the real world | **False.** External authorities, labs, carriers and buyers are still outside this git repo. |

## Runtime that does exist

`platform/` — FastAPI reference app, default-deny HITM, tests, Dockerfile, Compose, CI workflow `platform-reference.yml`.

## External air gaps that still exist

- competent-authority systems
- licensed standards text
- laboratory LIMS and accreditation
- carrier / port / customs APIs
- executed commercial instruments
- production IAM, HA, observability, key management
