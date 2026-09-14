# 05 — Smart-Glass Audit Specification

## 1. Objective

Provide auditors and authorised field personnel with a wearable, hands-free inspection interface that binds real-world observations to AHTE requirements, HCPs, evidence and authority workflows.

## 2. Device profile

### Required capabilities

- Camera capable of still image and video capture.
- Barcode/QR/DataMatrix/OCR scanning.
- NFC support where approved.
- GNSS/location capability where permitted.
- Secure clock/time synchronisation.
- Device identity and certificate.
- Hardware-backed key store where available.
- Local encrypted storage.
- Offline-first event queue.
- Noise-tolerant microphone for dictated observations.
- Optional connection to approved environmental sensors.

## 3. User identity

Authentication:

`Device identity + Auditor identity + MFA + role/scope policy`

The device alone cannot authorise an audit action.

## 4. Audit session lifecycle

```text
LOGIN
 ↓
LOAD ASSIGNED AUDIT
 ↓
VERIFY FACILITY + SCOPE
 ↓
LOAD APPLICABLE REQUIREMENTS / HCPs
 ↓
WALK FACILITY / PROCESS
 ↓
IDENTIFY OBJECT
 ↓
CAPTURE OBSERVATION
 ↓
ATTACH EVIDENCE
 ↓
OPTIONAL AI ASSIST
 ↓
AUDITOR ASSESSMENT
 ↓
FINDING / ACCEPT
 ↓
CAR / RE-VERIFICATION
 ↓
SIGN SESSION
 ↓
SYNC / RECONCILE
```

## 5. Requirement-guided navigation

The smart-glass interface should present an ordered inspection path:

`Requirement → control objective → control question → expected evidence → physical verification → observation → result`.

The auditor can jump to another area while preserving the session graph.

## 6. Object identification

Scan targets include:

- facility QR/NFC identity;
- production-line/area identity;
- equipment identity;
- material/ingredient identity;
- container/seal identity;
- pallet/logistic-unit identity;
- sample identity;
- document QR/identifier;
- certificate/decision reference where applicable.

## 7. Evidence capture

Every evidence item receives:

`EvidenceID, ObjectID, AuditID, RequirementID, HCPID, ActorID, Timestamp, DeviceID, LocationID (where appropriate), MediaHash, SourceType, Description, IntegrityProof`.

## 8. Image/video protocol

For controlled evidence:

1. Capture object context.
2. Capture identifier.
3. Capture relevant condition/observation.
4. Record date/time automatically.
5. Generate local hash.
6. Sign evidence manifest where required.
7. Queue upload if offline.

Original media remain immutable in the evidence store; annotations are separate objects.

## 9. Offline mode

A field session must continue when the network fails.

Offline package contains:

- audit assignment;
- signed requirement snapshot;
- HCP/control list;
- local object registry required for the site;
- evidence capture functions;
- encrypted event queue;
- revocation/expiry cache for authorised credentials.

When connectivity returns:

`LOCAL EVENT HASH → SERVER VALIDATION → SEQUENCE RECONCILIATION → SIGNATURE CHECK → COMMIT → ACKNOWLEDGEMENT`.

Conflicts are surfaced rather than overwritten.

## 10. AI assist

AI may:

- find potentially missing evidence;
- compare observation against prior patterns;
- detect visual anomalies;
- identify contradictory document fields;
- propose likely HCP relevance;
- prioritise high-risk inspection areas.

AI must expose evidence references and model/version metadata. The auditor remains the decision actor for the audit finding.

## 11. Voice workflow

Example command grammar:

```text
"Open HCP 14"
"Scan material"
"Capture evidence"
"Record observation: ..."
"Mark exception"
"Open finding"
"Attach previous certificate"
"Save and continue"
```

Voice input is interpreted as an operational command only after role/permission validation.

## 12. Safety and human factors

- High-risk device functions require confirmation.
- No distracting visual overlays while the wearer is operating machinery or moving through hazardous zones.
- Device use must comply with factory PPE and safety restrictions.
- The audit application must support immediate pause/lock.
- Sensitive screens auto-lock after inactivity.

## 13. Smart-glass evidence graph

```text
AUDIT SESSION
   ↓
REQUIREMENT
   ↓
HCP / CONTROL
   ↓
OBJECT IDENTIFIED
   ↓
OBSERVATION
   ├── IMAGE / VIDEO
   ├── DOCUMENT
   ├── SENSOR
   ├── SAMPLE
   └── INTERVIEW / NOTE
   ↓
AUDITOR ASSESSMENT
   ↓
FINDING / PASS
```

## 14. Data minimisation

Only audit-relevant records are loaded onto the device. Personal information and commercially sensitive information that are not necessary for the inspection should not be cached.

China's network-data rules require appropriate security controls, including access control, encryption and backup, and require data processors to govern third-party processing and important-data handling. citeturn748828search0

## 15. Device trust

Each device has:

- `DeviceID`;
- device certificate;
- public/private key pair;
- attestation state;
- software release ID;
- security policy version;
- time-synchronisation state.

A compromised or revoked device is denied access to new audit packages; previously captured evidence is preserved for investigation.

## 16. Audit package versioning

An audit package is immutable after sign-off. Any revised audit scope creates a new package version with a parent reference.

## 17. Acceptance tests

- Authenticate auditor and device.
- Load correct site/scope.
- Scan object.
- Capture signed evidence.
- Operate offline.
- Reconnect and reconcile.
- Detect replayed events.
- Enforce expired role credentials.
- Prevent unauthorised evidence access.
- Generate traceable finding/CAR records.
