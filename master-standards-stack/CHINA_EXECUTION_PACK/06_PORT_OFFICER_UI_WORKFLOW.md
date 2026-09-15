# 06 — PORT OFFICER UI / WORKFLOW SPECIFICATION

## 1. Mission

Provide a controlled operational view for port, customs, inspection and authorised border personnel to authenticate a shipment and act on exceptions using the minimum necessary trust information.

## 2. Entry point

`Authenticate officer -> select jurisdiction/port -> scan container/seal/shipment -> retrieve authorised trust view`.

## 3. Officer dashboard

**Header:** shipment ID, container ID, vessel/route, origin, destination, ETA/ATA, current trust state.

**Primary panels:** identity match, seal status, document set, custody chain, product/batch summary, applicable destination controls, inspection history, active exceptions, authority instructions.

## 4. Workflow

### A. Pre-arrival
- Verify pre-arrival data exists.
- Verify importer/consignee identity.
- Pre-fetch authorised document and trust assertions.
- Flag missing/expired material.

### B. Arrival
- Scan container and seal.
- Compare physical ID to digital record.
- Confirm custody transfer.
- Confirm arrival event and location.

### C. Inspection
- Record officer identity and inspection start.
- Capture document checks.
- Record physical observations.
- Capture sample event where required.
- Bind inspection evidence to shipment/container/seal.

### D. Decision
Allowed actions: `RELEASE`, `HOLD`, `QUARANTINE`, `REFER`, `SAMPLE`, `ADDITIONAL-DOCUMENTS`.

Decision action creates an authenticated event and named authority actor.

## 5. Colour/visual state logic

Use consistent semantic states: normal/verified, attention, blocked, expired, disputed. The state itself is never the evidence; the UI must allow the officer to drill into the supporting record.

## 6. Selective disclosure

Default view exposes shipment identity, authority status, relevant certificates/attestations, custody/seal facts and decision-support evidence. Sensitive manufacturing records are not displayed unless the officer’s role and rule decision authorise the disclosure.

## 7. Seal discrepancy workflow

`SCAN -> MISMATCH -> AUTO-HOLD -> PHOTO/EVIDENCE -> VERIFY PRIOR CUSTODY -> PHYSICAL INSPECTION -> RECONCILE OR REFER -> AUTHORITY DECISION -> NEW RELEASE STATE`.

## 8. Hold management

A hold object must include: hold ID, reason code, authority, scope, affected objects, start time, location, required action, owner and release conditions.

## 9. Offline mode

Where connectivity is unavailable, the device stores encrypted signed inspection records, preserves sequence, and synchronises when network service returns. The UI clearly marks unsynchronised records.

## 10. Accessibility / field design

Large touch targets, high contrast, minimal typing, barcode-first navigation, multilingual labels where required, clear exception codes, confirmation before irreversible actions.

## 11. Audit trail

Every officer action logs: officer ID, role, device ID, timestamp, location, target object, action, evidence references, resulting state, signature/digest.

## 12. Release condition object

```json
{
  "shipment_id":"SHIPMENT-001",
  "container_id":"CONT-001",
  "seal_id":"SEAL-001",
  "decision":"RELEASE",
  "authority_gate":"GCC-BORDER-RELEASE",
  "required_checks":["identity","seal","documents","inspection"],
  "evidence_refs":[],
  "decision_actor":"OFFICER-001",
  "decision_at":"event-time"
}
```

## 13. Exception analytics

Port control room view aggregates holds by port, carrier, route, exception class, dwell time and affected product/lot. The blast radius is calculated from the trust graph, not guessed from a document list.
