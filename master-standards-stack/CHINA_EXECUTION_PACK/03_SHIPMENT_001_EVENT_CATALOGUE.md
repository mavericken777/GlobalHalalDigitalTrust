# 03 — Shipment 001 Complete Event Catalogue

## 1. Event envelope

Every Shipment 001 event uses the common envelope:

```json
{
  "EventID": "EVT-...",
  "EventType": "E-...",
  "EventVersion": "1.0",
  "OccurredAt": "2026-...Z",
  "RecordedAt": "2026-...Z",
  "TimeSource": "device|server|authority",
  "ActorID": "ACT-...",
  "ActorRole": "...",
  "OrganisationID": "ORG-...",
  "Jurisdiction": "CN|MY|SA|AE|GCC",
  "LocationID": "LOC-...",
  "DeviceID": "DEV-...",
  "ObjectRefs": [],
  "PreviousEventID": "EVT-...",
  "EvidenceRefs": [],
  "Payload": {},
  "ResultingState": "...",
  "Integrity": {"PayloadHash":"sha256:..."},
  "Signature": {"Algorithm":"...","KeyID":"...","Value":"..."}
}
```

## 2. Lifecycle catalogue

### A. Programme and organisation

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-PROGRAMME-OPEN` | Pilot formally opened | programme, sponsor, scope | ACTIVE |
| `E-ORG-ONBOARD` | Participant admitted | legal identity, scope, owner | ONBOARDED |
| `E-FACILITY-REGISTERED` | Factory/site registered | site, address, facility class | REGISTERED |
| `E-ROLE-ASSIGNED` | Operational role assigned | actor, role, authority/scope | ACTIVE |
| `E-COMPETENCE-VERIFIED` | Competence checked | qualification, validity, scope | VERIFIED |

### B. Product and standards

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-SCOPE-CLASSIFIED` | Product/transaction scope classified | commodity, markets, activity | SCOPE-SET |
| `E-STANDARD-APPLIED` | Requirement pack activated | standard IDs, versions, jurisdiction | APPLIED |
| `E-REQUIREMENT-RESOLVED` | Precedence engine resolves rules | ruleset, conflicts, controls | READY |
| `E-HCP-OPEN` | HCP instantiated | HCP, risk, owner, control | OPEN |
| `E-HCP-MONITOR` | Control monitoring recorded | observation, measurement, result | MONITORED |

### C. Supplier/material provenance

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-SUPPLIER-REGISTERED` | Supplier accepted | identity, scope | REGISTERED |
| `E-MATERIAL-CREATED` | Material object created | material ID, source class | CREATED |
| `E-MATERIAL-RECEIVED` | Material arrives | supplier, batch, quantity, docs | RECEIVED |
| `E-MATERIAL-VERIFIED` | Source/specification verified | evidence, verifier, status | VERIFIED |
| `E-MATERIAL-REJECTED` | Material fails control | reason, containment | HOLD |

### D. Manufacturing

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-BATCH-CREATED` | Production batch starts | product, formula, batch ID | ACTIVE |
| `E-PROCESS-START` | Production begins | work order, equipment, operator | IN-PROCESS |
| `E-PROCESS-HCP-CHECK` | HCP check | HCP, observation, evidence | PASS/EXCEPTION |
| `E-BATCH-COMPLETED` | Manufacturing complete | yield, lot IDs, records | COMPLETE |
| `E-PACKAGING-VERIFIED` | Packaging/label controls complete | packaging version, lot | VERIFIED |
| `E-LOT-RELEASE` | Lot authorised internally | lot, criteria, approver | RELEASED |

### E. Evidence and laboratory

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-EVIDENCE-CAPTURED` | Evidence attached | source, hash, object refs | LINKED |
| `E-SAMPLE-COLLECTED` | Sample taken | sample, matrix, method, seal | IN-LAB/TRANSIT |
| `E-SAMPLE-CUSTODY` | Sample transferred | from/to, seal, time | CUSTODIED |
| `E-LAB-RECEIPT` | Lab accepts sample | sample, condition | RECEIVED |
| `E-LAB-RESULT` | Test completed | method, controls, result, report | RESULTED |
| `E-LAB-REVIEW` | Technical review | reviewer, interpretation | REVIEWED |

### F. Audit and authority

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-AUDIT-OPEN` | Audit begins | scope, team, site | OPEN |
| `E-AUDIT-OBSERVATION` | Observation captured | requirement, evidence, location | RECORDED |
| `E-FINDING` | Nonconformity/observation opened | severity, requirement, evidence | FINDING |
| `E-CAR-OPEN` | Corrective action opened | owner, cause, action | CORRECTIVE-ACTION |
| `E-CAR-CLOSE` | Action evidence accepted | evidence, effectiveness | CLOSED |
| `E-REVERIFICATION` | Follow-up verification | scope, evidence, result | VERIFIED/REJECTED |
| `E-AUTHORITY-DECISION` | Competent decision recorded | authority, decision, scope, validity | DECIDED |

### G. Shipment construction

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-SHIPMENT-CREATED` | Shipment 001 opened | shipment, route, importer | OPEN |
| `E-PALLET-CREATED` | Pallet built | pallet, lot list, quantity | BUILT |
| `E-CONTAINER-ASSIGNED` | Container assigned | container, shipment | ASSIGNED |
| `E-SEAL-APPLIED` | Seal applied | seal ID, actor, image | SEALED |
| `E-LOAD-COMPLETED` | Container loading finished | load plan, reconciliation | LOADED |
| `E-ORIGIN-RECONCILIATION` | Origin check passed | docs, objects, discrepancies | PASS/HOLD |
| `E-EXPORT-PACKET-SEALED` | Border packet locked | packet ID, hashes, issuer | SEALED |

### H. China logistics and export

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-CARRIER-ACCEPTANCE` | Carrier takes custody | shipment, condition | IN-CUSTODY |
| `E-CUSTODY-TRANSFER` | Custody changes | from/to, time, location, condition | TRANSFERRED |
| `E-VEHICLE-ARRIVAL` | Vehicle reaches node | vehicle, shipment | ARRIVED |
| `E-GATE-CHECK` | Gate entry/exit | identity, seal, status | CLEARED/HOLD |
| `E-PORT-INSPECTION` | Port/customs inspection | officer, packet, findings | CLEARED/HOLD |
| `E-EXPORT-RELEASE` | Export clearance | declaration ref, release actor | RELEASED |

### I. Transit

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-TRANSIT-DEPARTURE` | Vessel/air/road departure | carrier, departure, seal | IN-TRANSIT |
| `E-CONDITION-CAPTURED` | Condition telemetry recorded | temperature/location/etc. | RECORDED |
| `E-ROUTE-EXCEPTION` | Route/condition event | exception, evidence | HOLD/REVIEW |
| `E-ARRIVAL-PORT` | GCC port arrival | port, container, seal | ARRIVED |

### J. GCC border

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-GCC-PACKET-PRESENTED` | Import presentation | importer, packet | PRESENTED |
| `E-SEAL-VERIFIED` | Physical seal checked | expected/actual, evidence | VERIFIED/MISMATCH |
| `E-DOCUMENT-RECONCILIATION` | Docs checked | declaration, product, certificate refs | PASS/EXCEPTION |
| `E-GCC-INSPECTION` | Destination inspection | authority, observations | PASS/HOLD |
| `E-IMPORT-RELEASE` | Customs/authority release | decision, validity | RELEASED |

### K. Destination warehouse and retail

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-DEST-WAREHOUSE-RECEIPT` | Container received | seal, quantity, condition | RECEIVED |
| `E-DEST-QUARANTINE` | Destination hold | reason, scope | QUARANTINED |
| `E-DEST-RECONCILIATION` | Physical-vs-digital match | variance report | PASS/EXCEPTION |
| `E-DEST-RELEASE` | Warehouse release | approver, scope | RELEASED |
| `E-DISTRIBUTION-DISPATCH` | Retail delivery dispatched | logistic unit, destination | DISPATCHED |
| `E-RETAIL-RECEIPT` | Retail receives | unit, condition | RECEIVED |
| `E-CONSUMER-VERIFICATION` | Verification service used | assertion ID, result | VERIFIED/NOT-VERIFIED |

### L. Exceptions and recall

| Event | Trigger | Minimum payload | Result |
|---|---|---|---|
| `E-SEAL-BROKEN` | Seal mismatch/break | expected/actual, place, evidence | HOLD |
| `E-ID-MISMATCH` | Identity mismatch | expected/actual IDs | HOLD |
| `E-EVIDENCE-CONTRADICTION` | Contradictory records | evidence refs, contradiction | REVIEW |
| `E-CUSTODY-GAP` | Missing custody hop | previous/next event | REVIEW/HOLD |
| `E-TRUST-FRACTURE` | Graph dependency broken | affected nodes | REVIEW/HOLD |
| `E-RECALL-OPEN` | Recall initiated | scope, reason, authority | RECALLED |
| `E-RECALL-TRACEBACK` | Affected origin identified | object graph | SCOPED |
| `E-RECALL-TRACEFORWARD` | Downstream scope identified | lots, pallets, locations | SCOPED |
| `E-RECALL-CLOSE` | Recall completed | disposition evidence | CLOSED |

## 3. Mandatory event invariants

1. Event IDs are unique.
2. Event versions are explicit.
3. Actor identity is mandatory for controlled events.
4. Physical events reference the physical object.
5. Digital events reference the source record when one exists.
6. Critical events form a hash/signature chain.
7. A state transition cannot be generated without the event that caused it.
8. Replays are idempotent.
9. Out-of-order events are quarantined for reconciliation rather than silently merged.
10. Event deletion is prohibited from the operational ledger; correction occurs by a compensating event.

## 4. Shipment 001 critical-path sequence

```text
PRODUCT_SCOPE
 → MATERIAL_VERIFICATION
 → FACILITY/AUDIT
 → BATCH
 → LOT_RELEASE
 → PALLET
 → CONTAINER
 → SEAL
 → ORIGIN_RECONCILIATION
 → CARRIER_CUSTODY
 → EXPORT_RELEASE
 → TRANSIT
 → GCC_ARRIVAL
 → SEAL_VERIFICATION
 → DESTINATION_RECONCILIATION
 → IMPORT_RELEASE
 → WAREHOUSE_RELEASE
 → RETAIL
 → VERIFICATION
```

## 5. Event-sourcing requirements

The event stream must permit reconstruction of:

- current shipment state;
- every custody holder;
- every physical identity relation;
- every applicable rule set at event time;
- every evidence object used;
- every authority decision in force;
- every exception and resolution;
- the exact affected scope for recall.

## 6. Event registry controls

Each event type is versioned independently. Changes require schema compatibility testing, migration rules and consumer impact assessment. Event consumers include factory systems, logistics, AHTE, authority gateways, destination systems and analytics.
