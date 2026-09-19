# Repository status — honest operating picture

Control date: 2026-09-20  
This file overrides marketing language elsewhere if they conflict.

## What this repository is

A **specification, documentation and evidence-model library** for a proposed Halal/Tayyib trust architecture (AHTE / IQ300).

## What this repository is not

| Claim sometimes implied by folder names | Actual state |
|---|---|
| Live backend / platform | **None.** No production service, API, database or UI is deployed from this repo. |
| Smart contracts | **None.** |
| Running OPA / HITM policy engine | **Draft Rego only.** No OPA server is deployed. |
| Live EPCIS feed | **Event map only.** `epcis-corridor-event-map.json` events are empty. |
| SPIRE / SPIFFE runtime | **Characterisation only.** |
| SCITT / VC 2.0 / C2PA production binding | **Interop note only.** |
| Trust graph / Digital Audit Twin / Evidence Fabric | **Specified, not instantiated.** |
| Official Halal certification | **Never.** Decisions remain with competent authorities. |
| JAKIM / JSM / GCC / lab / customs endorsement | **None recorded.** |
| Executed partner contracts | **None recorded.** Folders are proposed roles. |
| Shipment 001 | **Pilot architecture only.** No transaction-native events. |
| External independent audit | **None.** Files named `*_AUDIT_*.md` are **internal self-assessments** by the same maintainer. |
| Multi-party sovereign federation | **Aspiration.** Current control is a single GitHub account. |

## Runtime gates still open

- deployed application backend
- OPA/HITM policy runtime
- SCITT transparency service
- EPCIS 2.0 event store with live events
- SPIRE workload identities
- laboratory results bound to real samples
- manufacturer certificates and scope files
- importer / buyer / PO / commercial terms
- logistics custody telemetry
- border / customs release events

## Completeness language — corrected

Do **not** read `100% complete` as operational, certified, or commercially live.

In this repository it means only: *documentation workstreams are listed and missing external evidence is named as a gate.*

Preferred status codes going forward:

| Code | Meaning |
|---|---|
| `SPEC` | Written specification or model |
| `DRAFT-STUB` | File exists but is too thin to treat as an implementable spec |
| `SELF-ASSESS` | Maintainer-written ledger, not third-party audit |
| `SOURCE-LOCKED` | Waiting on an authoritative external text |
| `UNEXECUTED-ROLE` | Named organisation; no contract on file |
| `TRANSACTION-GATE` | Waiting on a real commercial or shipment event |
| `ENGINEERING-GATE` | Waiting on a running system |

## Economics

NPV, payback, revenue-uplift, grant-capture and similar figures in this repository are **internal model assumptions** unless a named primary source is attached. They are not forecasts and not investor representations.
