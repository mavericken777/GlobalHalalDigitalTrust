# 06 — Port Officer UI / Workflow Specification

## 1. Purpose

Give authorised port/customs/inspection personnel a fast operational view of a shipment's identity, trust packet, physical seal, documentary state, exceptions and release status.

## 2. Design principles

- Decision-first interface.
- Minimal data exposure.
- Physical/digital reconciliation before release.
- Offline-capable inspection.
- Every officer action becomes a signed event.
- Clear separation between informational evidence and authority decision.

## 3. Officer journey

```text
AUTHENTICATE
 ↓
SELECT PORT / ROLE / CASE
 ↓
SCAN CONTAINER / SHIPMENT / SEAL
 ↓
LOAD TRUST ASSERTION
 ↓
CHECK IDENTITY
 ↓
CHECK SEAL
 ↓
CHECK DECLARATION / DOCUMENTS
 ↓
CHECK REQUIRED CERTIFICATE / DECISION REFERENCES
 ↓
OPTIONAL PHYSICAL INSPECTION
 ↓
COMPARE EXPECTED VS ACTUAL
 ↓
CLEAR / HOLD / REFER
 ↓
SIGN EVENT
 ↓
ISSUE RELEASE OR EXCEPTION RESULT
```

## 4. Main screens

### 4.1 Login

- officer identity;
- device identity;
- MFA;
- jurisdiction/port assignment;
- certificate validity;
- last synchronisation.

### 4.2 Scan

Support container number, seal number, shipment QR/DataMatrix and approved NFC/RFID identity.

### 4.3 Shipment summary

Display only necessary fields:

- ShipmentID;
- origin/destination;
- container ID;
- seal ID;
- cargo summary;
- declared quantity;
- current trust state;
- authority decision references;
- exceptions;
- verification endpoint.

### 4.4 Trust packet

```text
TrustAssertionID
Issuer
Scope
Validity
Product/Lot refs
Certificate/decision refs
Evidence hashes
Exception flags
Current state
Verification status
```

### 4.5 Physical reconciliation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Container ID | Stored ID | Scanned ID | PASS/FAIL |
| Seal ID | Stored seal | Physical seal | PASS/FAIL |
| Quantity | Manifest | Count/measurement | PASS/VARIANCE |
| Packaging | Expected | Observed | PASS/EXCEPTION |
| Condition | Expected range | Inspection | PASS/EXCEPTION |

## 5. Authority action buttons

### CLEAR
Creates a signed inspection/release event according to the officer's mandate.

### HOLD
Places the relevant object scope on hold and opens an exception case.

### REFER
Routes the case to a named authority/technical team with evidence bundle.

### QUARANTINE
Applies a defined inventory/lot/container quarantine status where authorised.

No action is allowed without a matching officer role and scope.

## 6. Exception workflow

```text
MISMATCH / ALERT
      ↓
CAPTURE ACTUAL CONDITION
      ↓
CREATE EXCEPTION EVENT
      ↓
FREEZE AFFECTED OBJECT SCOPE
      ↓
COLLECT EVIDENCE
      ↓
ROUTE TO RESPONSIBLE AUTHORITY
      ↓
DECISION
 ┌────┼────────┐
 ↓    ↓        ↓
CLEAR HOLD   REFER
 ↓      ↓        ↓
RELEASE  CORRECTIVE / INVESTIGATION
```

## 7. Offline inspection

The device stores:

- signed inspection assignment;
- trust assertion cache;
- revocation cache;
- expected shipment identity;
- evidence capture capability;
- encrypted event queue.

When back online, the device performs a secure reconciliation and submits events in causal order.

## 8. Device security

- Device certificate.
- Hardware-backed key storage where supported.
- Remote revocation.
- Screen lock.
- Encrypted local data.
- Tamper detection.
- No bulk export from the officer interface.

## 9. Data sovereignty

The border interface exposes the minimum information needed to execute the inspection. Detailed factory production records, personnel information and commercially sensitive source records remain behind their respective controlled interfaces unless lawfully required and authorised.

China's current network-data regime requires security controls for network data processing and provides specific governance for data provision, important data and cross-border transfer. citeturn748828search0turn164534search0

## 10. Port trust packet acceptance

A packet is technically admissible to the AHTE verification layer when:

- issuer is trusted;
- signature validates;
- packet is within validity window;
- object identities reconcile;
- referenced authority decision is active;
- exception flags are processed;
- proof hashes match;
- destination rule pack accepts the packet type.

A technically valid packet does not erase a physical inspection finding or local authority requirement.

## 11. Saudi destination adaptation

SFDA's food-import guidance requires importers to register food items and comply with Saudi requirements; it identifies halal certificates and, where relevant, slaughter certificates among possible import documentation. The Saudi Halal Center separately provides a workflow involving eligibility review, audit and decision-committee issuance. citeturn848971search1turn848971search0

The Saudi officer view should therefore be able to surface both the AHTE trust assertion and the relevant SFDA/halal documentation references.

## 12. UAE destination adaptation

MoIAT provides a digital process for national conformity marks, including the Halal National Mark, with document submission and field assessment; it also provides registration of halal certification bodies. citeturn848971search2turn848971search12

The UAE officer view should expose the conformity/halal credential references and status required by the applicable destination workflow.

## 13. Auditability

Every officer action creates:

`OfficerID + DeviceID + CaseID + ObjectIDs + Decision + EvidenceRefs + Timestamp + Signature + PreviousEventID`.

## 14. Acceptance tests

- Valid officer can authenticate.
- Invalid/expired role cannot act.
- Valid container and seal produce matching result.
- Mismatch automatically creates exception.
- Offline capture works.
- Reconnected events reconcile.
- Officer cannot alter historical events.
- Release action requires correct authority scope.
