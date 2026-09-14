# 00 — Master China Execution Model

## 1. Operating concept

IQ300/AHTE is implemented as a federated execution fabric across three jurisdictional planes:

- **China origin plane:** manufacturer, supplier, laboratory, logistics, export and port operations.
- **Malaysia governance/assurance plane:** applicable Malaysian Halal standards, JAKIM/JAIN governance instruments, assurance data, authority-linked records and project governance.
- **GCC destination plane:** importer, destination authorities, customs, warehouse, retail and consumer/stakeholder verification.

The planes exchange controlled assertions, not uncontrolled replication of source records.

## 2. Physical + digital binding

```text
PHYSICAL OBJECT                 DIGITAL OBJECT
────────────────────────────────────────────────────────
Facility                        FacilityTwin
Material                       MaterialObject
Production run                 BatchObject
Lot                            LotObject
Pallet                         PalletObject
Container                      ContainerObject
Seal                            SealObject
Sample                          SampleObject
Custody handover                CustodyTransferEvent
Inspection                      InspectionEvent
Release                         Authority/ReleaseEvent
Recall                          RecallCase
```

The binding key is `ObjectID + EventID + EvidenceID + ActorID + Timestamp + IntegrityProof`.

## 3. Control loop

```text
AUTHORITATIVE SOURCE
        ↓
APPLICABILITY / RULE SELECTION
        ↓
CONTROL OBJECTIVE
        ↓
HCP / CONTROL IMPLEMENTATION
        ↓
PHYSICAL EXECUTION
        ↓
EVIDENCE CAPTURE
        ↓
AUDIT / ANALYTICS
        ↓
FINDING / CAR / RE-VERIFICATION
        ↓
AUTHORITY DECISION
        ↓
TRUST STATE
        ↓
RELEASE / HOLD / QUARANTINE / RECALL
        ↓
NEXT PHYSICAL HOP
```

## 4. Object hierarchy

`Programme → Organisation → Facility → Product → Formula/Version → Material → Supplier → Process → HCP → Batch → Lot → Logistic Unit → Shipment → Destination Inventory → Retail Unit`

Cross-cutting objects:

`Requirement`, `Control`, `Evidence`, `Sample`, `LabResult`, `Audit`, `Finding`, `CAR`, `AuthorityDecision`, `TrustAssertion`, `TrustAnchor`, `DigitalEvent`.

## 5. Trust state model

Primary lifecycle:

`INITIAL → EVIDENCE-COMPLETE → ASSESSED → VERIFIED → RELEASED`

Exception branches:

`HOLD`, `QUARANTINED`, `DISPUTED`, `CORRECTIVE-ACTION`, `RE-VERIFICATION`, `EXPIRED`, `SUSPENDED`, `REVOKED`, `RECALLED`.

A trust state is always scoped to one object and one authority/control context. A recalled lot must not automatically change unrelated lots; a destination quarantine must not erase origin evidence.

## 6. Physical gate model

Every physical handoff has a digital gate:

1. Identify object.
2. Read expected state.
3. Verify physical identifier.
4. Verify seal where applicable.
5. Verify relevant condition data.
6. Reconcile documentation.
7. Capture actor + timestamp + location.
8. Sign the event.
9. Produce next-state decision.
10. Transfer custody or place on hold.

## 7. Minimum evidence packet

For a critical control point:

- Object IDs.
- Requirement/control/HCP IDs.
- Actor ID and role.
- Time source.
- Location/device ID.
- Source record reference.
- Images/video where required.
- Measurement or test result where relevant.
- Integrity hash.
- Signature where required.
- Previous-event reference.
- Resulting state.

## 8. Federated data architecture

```text
             GLOBAL TRUST NETWORK
                     │
       ┌─────────────┼─────────────┐
       │             │             │
   CHINA ZONE    MALAYSIA ZONE   GCC ZONE
       │             │             │
 Factory SoR     Assurance SoR   Destination SoR
 MES/QMS/WMS     standards &     Import/customs/
 LIMS/ERP/IoT    authority        warehouse/retail
       │             │             │
       └─────── TRUST ASSERTION ───┘
```

The China zone retains granular records needed by the Chinese operators and applicable law. The cross-border layer exposes minimum-necessary assertions, proofs, statuses and references.

China's 2024 cross-border data provisions explicitly address international trade, cross-border transport and multinational manufacturing data that contain neither personal information nor important data, while continuing to regulate personal-information and important-data exports. The Network Data Security Management Regulation also requires security controls, access control, encryption/backup measures, incident handling and governance over provision/entrusted processing. citeturn164534search0turn748828search0

## 9. Standard and rule execution

AHTE shall never apply a standard merely because a product is labelled halal. The engine executes:

```text
Commodity / Product Scope
        ↓
Jurisdiction / Market
        ↓
Applicable Law
        ↓
Mandatory Technical Requirements
        ↓
Competent-Authority Instruments
        ↓
Applicable Halal Standards / Specifications
        ↓
Contractual Requirements
        ↓
AHTE Control Implementation
```

The output is a `ResolvedRequirementSet` with source precedence, effective dates, applicability reason and control bindings.

## 10. AI placement

AI services are placed after the evidence layer:

- evidence-gap prediction;
- anomaly detection;
- contradiction detection;
- trust-graph fracture detection;
- predictive compliance;
- recall blast-radius traversal.

AI outputs must retain model version, feature/input references, score, explanation metadata and reviewer/decision linkage.

## 11. Human decision points

Human/authority decisions are explicit at:

- applicability determination where rules conflict;
- audit findings;
- laboratory interpretation where required;
- certification/recognition decisions;
- authority release/hold;
- exceptional route approvals;
- recall/withdrawal decisions;
- dispute resolution.

## 12. First-wave deployment sequence

```text
HOD GOVERNANCE
    ↓
PILOT FACILITIES
    ↓
DATA / SYSTEM INVENTORY
    ↓
STANDARDS + RULE PACKS
    ↓
FACTORY DIGITAL TWINS
    ↓
HCP / EVIDENCE TEMPLATES
    ↓
SMART-GLASS AUDIT
    ↓
LAB + SAMPLE CHAIN
    ↓
SHIPMENT 001 DIGITAL TWIN
    ↓
CONTAINER + SEAL BINDING
    ↓
ORIGIN / EXPORT REHEARSAL
    ↓
GCC BORDER REHEARSAL
    ↓
DESTINATION WAREHOUSE
    ↓
RETAIL / VERIFICATION
    ↓
POST-SHIPMENT ASSURANCE
    ↓
SCALE DECISION
```

## 13. Engineering acceptance criteria

### Identity
100% of critical physical objects have a stable identifier and parent genealogy.

### Evidence
100% of critical HCPs create linked evidence objects.

### Custody
100% of critical handovers are represented by signed custody events.

### Reconciliation
Every container/seal combination is reconciled before release at each controlled hop.

### Availability
Field devices support offline capture and secure later reconciliation.

### Security
High-value signing keys are hardware-backed or equivalent; access is least-privilege and auditable.

### Cross-border exchange
Only policy-approved fields leave each sovereign data zone.

### Recovery
The system can reconstruct a shipment state from its event stream without relying on free-text notes.

### Recall
A batch/lot recall can be traversed forward and backward through the trust graph with deterministic object relationships.

## 14. Institutional interface principle

Each Chinese HOD interface receives a concrete package:

`Mandate → Required Decision → Data Interface → Technical Interface → Pilot Deliverable → Acceptance Test → Escalation Route → Scale Decision`.

The programme is therefore operated as a series of accountable institutional interfaces rather than as a single software procurement.
