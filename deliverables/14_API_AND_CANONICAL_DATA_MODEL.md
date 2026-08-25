# API & Canonical Data Model

## API principles

- API-first.
- Backward compatible adapters for legacy systems.
- Explicit versioning.
- Strong authentication.
- Fine-grained authorization.
- Idempotency for state-changing calls.
- Schema validation.
- Event signatures for critical events.
- Audit logging.
- Rate limiting and abuse protection.

## Canonical entities

### Organisation
`organisation_id, legal_name, jurisdiction, organisation_type, status, credentials[]`

### Product
`product_id, manufacturer_id, name, category, market_status, evidence_refs[]`

### Ingredient/Material
`material_id, source, supplier_id, lot, specification_ref, Halal_evidence_ref`

### Batch
`batch_id, product_id, production_site, production_time, status`

### Laboratory Evidence
`lab_event_id, specimen_id, method, lab_id, result, report_ref, signature, hash`

### Shipment
`shipment_id, carrier, mode, origin, destination, container_refs[], status`

### Logistics Event
`event_id, shipment_id, event_type, location, timestamp, actor, telemetry_ref, hash`

### Retail Event
`event_id, location, batch_id, receiving/storage/dispatch action, actor, evidence_ref`

### Consumer Scan
`scan_id, product_id, timestamp, coarse location if consented, public_verification_result`

## Example endpoint set

`POST /v1/organisations`

`POST /v1/products`

`POST /v1/evidence`

`POST /v1/lab-results`

`POST /v1/shipments`

`POST /v1/logistics-events`

`POST /v1/retail-events`

`GET /v1/products/{id}/verification`

`GET /v1/evidence/{id}/integrity`

`POST /v1/cases/{id}/corrective-actions`

`POST /v1/recalls`

## Sovereignty controls

Every API request must resolve:
- data owner/controller;
- jurisdiction;
- purpose;
- legal basis/policy;
- requester role;
- data classification;
- allowed fields;
- retention.

## Interoperability

Adapters can connect existing ERP, WMS, TMS, laboratory information systems, customs systems and retail systems. The trust platform should not require replacement of these systems for initial participation.

## Event integrity

Critical events produce a canonical event hash. Where appropriate, events are digitally signed by the source system or authorized actor.
