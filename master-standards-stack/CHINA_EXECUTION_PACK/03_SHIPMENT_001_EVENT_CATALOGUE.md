# 03 — SHIPMENT 001 COMPLETE EVENT CATALOGUE

## Event envelope

Every event uses:

`event_id`, `event_type`, `schema_version`, `occurred_at`, `recorded_at`, `issuer_org`, `issuer_role`, `jurisdiction`, `subject_id`, `parent_event_id`, `correlation_id`, `location_id`, `device_id`, `payload`, `evidence_refs`, `signature`, `previous_event_hash`, `event_hash`.

## Lifecycle catalogue

### Programme / factory
- `E-ORG-ONBOARD` — organisation created/approved for pilot participation.
- `E-FACILITY-REGISTERED` — facility identity and site boundary established.
- `E-SCOPE-CLASSIFIED` — product/process/jurisdiction scope classified.
- `E-STANDARD-APPLIED` — applicable standard set bound to scope.
- `E-ROLE-ASSIGNED` — accountable role assigned.
- `E-TRAINING-COMPLETE` — required training completed.

### Materials and suppliers
- `E-SUPPLIER-REGISTERED`
- `E-MATERIAL-REGISTERED`
- `E-MATERIAL-DOSSIER-COMPLETE`
- `E-MATERIAL-APPROVED`
- `E-MATERIAL-REJECTED`
- `E-MATERIAL-LOT-RECEIVED`
- `E-MATERIAL-QUARANTINED`
- `E-MATERIAL-RELEASED`

### Production
- `E-FORMULA-VERSIONED`
- `E-PROCESS-VERSIONED`
- `E-HCP-OPEN`
- `E-HCP-MONITOR`
- `E-HCP-EXCEPTION`
- `E-LINE-READY`
- `E-PRODUCTION-START`
- `E-SAMPLE-COLLECTED`
- `E-LAB-SUBMITTED`
- `E-LAB-RESULT`
- `E-BATCH-CREATED`
- `E-BATCH-RELEASED`
- `E-BATCH-HOLD`
- `E-BATCH-REJECTED`

### Audit / authority
- `E-AUDIT-OPEN`
- `E-AUDIT-OBSERVATION`
- `E-FINDING`
- `E-CAR-OPEN`
- `E-CAR-CLOSE`
- `E-REVERIFICATION`
- `E-AUTHORITY-SUBMISSION`
- `E-AUTHORITY-DECISION`
- `E-CERTIFICATE-ISSUED`
- `E-CERTIFICATE-SUSPENDED`

### Packaging / identity
- `E-PACKAGING-LOT-CREATED`
- `E-UNIT-ID-BOUND`
- `E-PALLET-CREATED`
- `E-PALLET-LOADED`
- `E-PALLET-UNLOADED`
- `E-CONTAINER-ASSIGNED`
- `E-SEAL-APPLIED`
- `E-SEAL-INSPECTED`
- `E-SEAL-BROKEN`

### China export and logistics
- `E-BOOKING-CREATED`
- `E-CARRIER-ASSIGNED`
- `E-VEHICLE-VERIFIED`
- `E-CUSTODY-TRANSFER`
- `E-EXPORT-DOCUMENT-SET`
- `E-EXPORT-DECLARATION`
- `E-EXPORT-RELEASE`
- `E-PORT-IN`
- `E-PORT-INSPECTION`
- `E-PORT-OUT`
- `E-DEPARTURE`
- `E-TRANSIT-MILESTONE`
- `E-ETA-UPDATED`

### GCC border / destination
- `E-GCC-PREARRIVAL`
- `E-GCC-CUSTOMS-FILING`
- `E-GCC-DOCUMENT-VERIFICATION`
- `E-GCC-PHYSICAL-INSPECTION`
- `E-GCC-SAMPLE-COLLECTED`
- `E-GCC-HOLD`
- `E-GCC-RELEASE`
- `E-DESTINATION-CUSTODY-TRANSFER`
- `E-WAREHOUSE-RECEIPT`
- `E-WAREHOUSE-RELEASE`
- `E-RETAIL-RECEIPT`
- `E-RETAIL-RELEASE`

### Trust / incident / recall
- `E-TRUST-STATE-CHANGED`
- `E-EXCEPTION-OPEN`
- `E-EXCEPTION-CLOSED`
- `E-INCIDENT-OPEN`
- `E-INCIDENT-CONTAINED`
- `E-RECALL-OPEN`
- `E-RECALL-BLAST-RADIUS`
- `E-RECALL-WITHDRAWAL`
- `E-RECALL-CLOSE`

## Trust states

`INITIAL -> EVIDENCE-COMPLETE -> ASSESSED -> VERIFIED -> VERIFIED-WITH-EXCEPTION -> RELEASED`

Failure/control states: `HOLD`, `QUARANTINED`, `DISPUTED`, `CORRECTIVE-ACTION`, `RE-VERIFICATION`, `EXPIRED`, `SUSPENDED`, `REVOKED`, `RECALLED`.

## Event sequencing requirements

1. A batch cannot be released without its required material/process evidence and applicable audit/authority conditions.
2. A pallet must point to one or more released batch/lot objects.
3. Container loading must point to the pallet set and loading event.
4. Seal application creates a unique seal object and links container + custody owner + timestamp + location.
5. Every custody transfer records outgoing and receiving actors.
6. A seal-break event automatically opens an exception and requires inspection/reconciliation before onward release.
7. GCC border release references the shipment dossier and all destination-required checks.
8. Warehouse release inherits the released shipment state but may add destination-specific controls.
9. Recall can propagate backwards and forwards through the graph.

## Correlation identifiers

Use stable correlation IDs for:
- `PROGRAMME-001`
- `FACTORY-<id>`
- `PRODUCT-<sku>`
- `BATCH-<id>`
- `PALLET-<id>`
- `CONTAINER-<id>`
- `SHIPMENT-001`
- `CASE-<authority-case>`
- `RECALL-<id>`

## Exception triggers

Seal discrepancy, temperature excursion where applicable, identity mismatch, unexpected location, unapproved subcontractor, expired evidence, document mismatch, analytical contradiction, unauthorised material substitution, facility/process change, broken custody, border hold, consumer complaint and recall notice.

## Immutability rule

An event is append-only. Correction occurs by a superseding event referencing the original. The trust graph records both.
