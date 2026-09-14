# AHTE China-to-GCC Port / Customs Gateway Specification

## 1. Objective

Provide a common digital inspection and trust-resolution workflow for authorised port/customs users while preserving each authority's operational mandate.

## 2. Gateway flow

`Officer/device authentication -> Shipment lookup -> Container/seal resolution -> Trust packet -> Physical inspection -> Evidence capture -> Exception assessment -> Release / Hold -> Signed event -> Audit log`

## 3. Screen / workflow requirements

| View | Required information |
|---|---|
| Shipment | Shipment ID, origin, destination, carrier, status |
| Container | Container ID, seal ID(s), loading event, custody chain |
| Product | SKU, batch/lot, pallet aggregation |
| Authority | Issuer, decision reference, scope, validity, status |
| Evidence | Evidence IDs, integrity hash, issuer, timestamps |
| Inspection | Observations, photos/documents, actor, location, time |
| Exceptions | Seal mismatch, identity mismatch, damaged package, status conflict |
| Decision | Release/hold reason, authority role, signature, timestamp |

## 4. Minimum gateway event payload

```json
{
  "eventId": "E-PORT-...",
  "shipmentId": "SHIP-...",
  "containerId": "CONT-...",
  "sealId": "SEAL-...",
  "actorId": "...",
  "location": "...",
  "timestamp": "...",
  "inspectionType": "...",
  "observations": [],
  "evidenceIds": [],
  "exceptionFlags": [],
  "result": "RELEASE|HOLD|QUARANTINE",
  "signature": "..."
}
```

## 5. Reconciliation rules

- Expected container/seal must equal observed container/seal unless a controlled exception exists.
- Batch/lot records must reconcile to pallet and container aggregation.
- Authority decision scope must cover the object presented.
- Expired, suspended, revoked or recalled states must trigger controlled exception handling.
- A corrected or superseded record must retain lineage to the previous record.

## 6. Offline mode

Inspection devices should cache only the minimum required operational data, record actions locally with device/time integrity, and reconcile to the central/federated gateway when connectivity is restored. Conflicts must enter a controlled reconciliation queue rather than silently overwrite records.

## 7. Physical infrastructure

Recommended physical kit for the pilot: secure inspection tablet, identity reader where permitted, seal scanner/reader, package barcode/QR/NFC reader, camera, optional RFID capability, network connectivity, secure local storage for offline events, and a portable printer where operational documents are needed.

## 8. Auditability

Every inspection action should be attributable to an authenticated actor and device, time-stamped, linked to the shipment/container/lot, and preserved as an auditable event. Any subsequent correction creates a new event with lineage rather than destructive overwrite.
