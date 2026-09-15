# 04 — FACTORY-SYSTEM API CONTRACTS

## 1. Integration target

The AHTE factory connector sits between AHTE and the manufacturer’s ERP/MES/WMS/QMS/LIMS/serialization and access-control systems. The connector should minimise modification of the factory core systems while guaranteeing identity, evidence and event integrity.

## 2. Canonical interfaces

### Factory → AHTE
- `POST /v1/facilities`
- `POST /v1/products`
- `POST /v1/materials`
- `POST /v1/suppliers`
- `POST /v1/formulas`
- `POST /v1/process-versions`
- `POST /v1/batches`
- `POST /v1/production-events`
- `POST /v1/samples`
- `POST /v1/lab-results`
- `POST /v1/evidence`
- `POST /v1/nonconformities`

### AHTE → Factory
- `GET /v1/requirements/{scope}`
- `GET /v1/hcp-plans/{product}`
- `GET /v1/release-state/{batch}`
- `GET /v1/authority-gates/{object}`
- `POST /v1/holds`
- `POST /v1/release-instructions`
- `POST /v1/change-notices`

## 3. Event-first pattern

Transactions that change trust or release state should emit a business event as the system of record. REST is the transport; event identity and ordering are the trust primitive.

Example envelope:

```json
{
  "event_id":"EVT-BATCH-000001",
  "event_type":"E-BATCH-CREATED",
  "schema_version":"1.0",
  "occurred_at":"2026-09-15T00:00:00Z",
  "issuer_org":"FACTORY-001",
  "issuer_role":"QA_LEAD",
  "subject_id":"BATCH-001",
  "correlation_id":"SHIPMENT-001",
  "payload":{},
  "evidence_refs":[],
  "previous_event_hash":"sha256:..."
}
```

## 4. Idempotency

Every write request must provide `Idempotency-Key`. A retry of an accepted key returns the original result and never creates a duplicate business event.

## 5. Batch release contract

Required input: batch ID, product ID, formula version, production start/end, source material IDs, applicable HCP statuses, test/sample references, deviations, packaging lot, responsible QA actor.

AHTE returns: release state, blocking controls, unresolved exceptions, required authority action, trust graph references.

## 6. Change control

Formula, supplier, source material, manufacturing site, critical process parameter, packaging material, outsourced process, storage conditions or product claims can trigger re-evaluation. The factory connector must notify AHTE before production use where the change-control rule requires prior review.

## 7. LIMS integration

Sample ID is immutable. Result payload binds matrix, method ID/version, lab ID, analyst, controls, result, interpretation, instrument and chain-of-custody references. A result without sample identity is not accepted into the evidentiary graph.

## 8. WMS integration

Warehouse status transitions must support `QUARANTINED`, `RELEASED`, `HOLD`, `REJECTED`, `RETURNED`, `RECALLED`. Inventory movement references batch/lot, pallet and container where applicable.

## 9. Security

TLS for transport; mutual TLS for system-to-system trust where supported; short-lived access tokens; role-based scopes; signed event envelopes; network allowlists; replay protection; clock-drift monitoring; audit logging.

## 10. Versioning

APIs are versioned by major version in the path. Additive fields are backward-compatible; changes to event meaning require a schema version increment and migration test.

## 11. Availability model

Factories can operate in disconnected mode. Local gateway persists signed events, evidence references and device identity; synchronisation uses ordered replay with conflict detection.

## 12. Minimum audit trail

`request -> authentication -> authorisation -> input hash -> business decision -> event ID -> evidence refs -> response -> operator identity -> timestamp`.
