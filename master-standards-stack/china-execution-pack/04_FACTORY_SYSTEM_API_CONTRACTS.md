# 04 — Factory-System API Contracts

## 1. Integration objective

Connect AHTE to the factory's existing operational systems without forcing replacement of ERP, MES, QMS, WMS, LIMS, HR/identity, document-management or IoT platforms.

## 2. Source-of-truth rule

| Object | Preferred system of record | AHTE role |
|---|---|---|
| Legal entity / site | ERP / corporate master | Reference + trust identity |
| Product / SKU | ERP / PLM | Identity + standards binding |
| Formula / BOM | ERP / PLM | Versioned assurance object |
| Production order | MES/ERP | Event source |
| Process record | MES | HCP execution evidence |
| Material receipt | WMS/ERP | Provenance evidence |
| Inventory status | WMS | State synchronisation |
| NCR/CAPA | QMS | Finding/CAR linkage |
| Lab sample/result | LIMS | Analytical evidence |
| Training/role | HR/LMS/identity | Competence object |
| SOP/specification | DMS/QMS | Controlled-document evidence |
| Sensor telemetry | IoT/SCADA | Condition evidence |
| Shipment / booking | TMS/ERP | Logistics object |

AHTE becomes the **cross-system trust graph**, not the only operational source.

## 3. Interface patterns

- REST/JSON for synchronous master-data and command interfaces.
- Webhooks/event bus for operational events.
- SFTP/object gateway only where legacy systems cannot support APIs.
- Offline edge gateway for factory/field environments with intermittent connectivity.
- mTLS for service-to-service transport.
- OAuth 2.0/OIDC or equivalent enterprise identity for user-facing APIs.
- Signed event envelopes for critical business events.

## 4. Common headers

```text
Authorization: Bearer <token>
X-Tenant-ID: <tenant>
X-Trace-ID: <trace>
X-Event-ID: <event>
X-Schema-Version: 1.0
X-Request-Timestamp: <iso8601>
Idempotency-Key: <stable-key>
```

## 5. Core API resources

### Organisation / facility

`POST /v1/organisations`

`POST /v1/facilities`

`GET /v1/facilities/{facilityId}`

### Product / material

`POST /v1/products`

`POST /v1/materials`

`POST /v1/suppliers`

`POST /v1/products/{productId}/requirements:resolve`

### Batch / lot

`POST /v1/batches`

`GET /v1/batches/{batchId}`

`POST /v1/batches/{batchId}/hcp-checks`

`POST /v1/lots/{lotId}:release`

### Evidence

`POST /v1/evidence`

`GET /v1/evidence/{evidenceId}`

`POST /v1/evidence/{evidenceId}:verify`

### Laboratory

`POST /v1/samples`

`POST /v1/samples/{sampleId}/custody`

`POST /v1/lab-results`

### Audit

`POST /v1/audits`

`POST /v1/audits/{auditId}/observations`

`POST /v1/findings`

`POST /v1/corrective-actions`

### Shipment

`POST /v1/shipments`

`POST /v1/shipments/{shipmentId}/pallets`

`POST /v1/shipments/{shipmentId}/containers`

`POST /v1/containers/{containerId}/seals`

`POST /v1/custody-transfers`

`POST /v1/shipments/{shipmentId}/export-packet:seal`

### Trust

`GET /v1/objects/{objectId}/trust`

`GET /v1/shipments/{shipmentId}/trust-assertion`

`POST /v1/trust-assertions:verify`

## 6. Factory event subscriptions

AHTE should consume, where available:

```text
material.received
material.released
material.rejected
workorder.started
hcp.checked
process.completed
batch.created
batch.completed
lot.created
lot.released
ncr.opened
capa.closed
sample.collected
lab.resulted
shipment.created
pallet.created
container.assigned
seal.applied
shipment.loaded
shipment.released
```

## 7. Event mapping

| Factory event | AHTE event |
|---|---|
| Work order started | `E-PROCESS-START` |
| Material receipt | `E-MATERIAL-RECEIVED` |
| HCP inspection | `E-HCP-MONITOR` / `E-PROCESS-HCP-CHECK` |
| Batch close | `E-BATCH-COMPLETED` |
| NCR creation | `E-FINDING` + `E-CAR-OPEN` where applicable |
| Sample collection | `E-SAMPLE-COLLECTED` |
| Lab result | `E-LAB-RESULT` |
| Palletisation | `E-PALLET-CREATED` |
| Container loading | `E-LOAD-COMPLETED` |
| Seal application | `E-SEAL-APPLIED` |
| Carrier handover | `E-CUSTODY-TRANSFER` |

## 8. Material API payload

```json
{
  "materialId":"MAT-001",
  "supplierId":"SUP-001",
  "supplierBatch":"S-BATCH-01",
  "description":"...",
  "sourceClass":"animal|plant|synthetic|mineral|microbial|mixed|unknown",
  "countryOfOrigin":"CN",
  "specificationRefs":[],
  "certificateRefs":[],
  "riskClass":"H|M|L",
  "effectiveVersion":"v1",
  "evidenceRefs":[]
}
```

## 9. HCP check payload

```json
{
  "hcpCheckId":"HCPCHK-001",
  "hcpId":"HCP-...",
  "objectId":"BATCH-...",
  "performedBy":"ACT-...",
  "performedAt":"...",
  "result":"PASS|EXCEPTION|FAIL",
  "measurements":[],
  "observation":"...",
  "evidenceRefs":[],
  "deviceId":"DEV-...",
  "signature":{ "keyId":"...","value":"..." }
}
```

## 10. Idempotency

Every POST creating a business event accepts an idempotency key. A repeated request returns the original event/object result. Business events are append-only; corrections use compensating events.

## 11. Error model

```json
{
  "code":"AHTE-RULE-CONFLICT",
  "message":"Applicable requirements conflict",
  "traceId":"...",
  "objectId":"...",
  "details":[],
  "retryable":false,
  "nextAction":"AUTHORITY_REVIEW"
}
```

## 12. Data minimisation

Factory APIs must support field-level projection so the China zone can share a minimal trust packet without exporting detailed personnel, production or commercially sensitive records unnecessarily.

## 13. OT/IT boundary

AHTE must not directly control safety-critical industrial equipment from the trust layer. The preferred pattern is:

`OT/PLC/SCADA → MES/Edge → validated integration gateway → AHTE event API`.

AHTE may record condition states and HCP evidence but should not become an unmanaged control-plane bridge into production equipment.

## 14. API acceptance tests

- Correct object identity binding.
- Duplicate-event rejection/idempotent replay.
- Schema validation.
- Signature validation for critical events.
- Out-of-order event handling.
- Offline event reconciliation.
- Permission enforcement.
- Data projection by jurisdiction.
- Evidence attachment.
- Trust-state update only after valid event processing.

## 15. Versioning

API versions use `/v1`, `/v2`, etc. Event schemas carry independent versions. Backward-compatible additions do not break existing consumers; breaking changes require a new major version and migration period.
