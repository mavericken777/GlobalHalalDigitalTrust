# IQ300 — China Execution Pack
## China Pilot → Shipment 001 → GCC Release

This package is the execution layer for the Amanah Halal Trust Ecosystem (AHTE) across the China → Malaysia-linked governance context → GCC trade corridor.

## Objective

Convert the existing AHTE standards, HCP, evidence, audit, trust-graph and physical/digital identity architecture into deployable operating specifications for:

1. China counterpart departments and technical HOD interfaces.
2. China manufacturer/factory activation.
3. Factory-system integration.
4. Physical custody and shipment control.
5. Smart-glass field audit execution.
6. Port/customs inspection and release workflows.
7. Cryptographic trust anchoring and selective disclosure.
8. Shipment 001 execution from China to the GCC.
9. GCC destination admission, warehouse release, distribution and retail verification.

## Repository map

| File | Function |
|---|---|
| `00_MASTER_CHINA_EXECUTION_MODEL.md` | Common operating model, architecture and implementation doctrine |
| `01_CHINA_HOD_RACI.md` | Department-by-department interface and RACI model |
| `02_RULE_PRECEDENCE_ENGINE.md` | China ↔ Malaysia ↔ GCC rule resolution and conflict handling |
| `03_SHIPMENT_001_EVENT_CATALOGUE.md` | Complete Shipment 001 event model, state machine and payload requirements |
| `04_FACTORY_SYSTEM_API_CONTRACTS.md` | ERP/MES/QMS/WMS/LIMS/IoT/identity/document API contracts |
| `05_SMART_GLASS_AUDIT_SPEC.md` | Smart-glass audit device, field workflow, offline mode and evidence capture |
| `06_PORT_OFFICER_UI_WORKFLOW.md` | Port/customs officer workflow, trust packet, inspection and release UI |
| `07_CRYPTOGRAPHIC_TRUST_ANCHOR_ARCHITECTURE.md` | Key hierarchy, signatures, trust anchors, evidence hashes and selective disclosure |
| `08_CHINA_PILOT_SHIPMENT_001_GCC_RELEASE_PLAYBOOK.md` | Integrated China pilot and Shipment 001 operating playbook |
| `schemas/shipment-001-event.schema.json` | Event envelope schema |
| `schemas/trust-assertion.schema.json` | Cross-border trust assertion schema |
| `schemas/authority-decision.schema.json` | Signed authority-decision object schema |
| `schemas/custody-transfer.schema.json` | Physical custody transition schema |
| `api/ahtE-factory-openapi.yaml` | Canonical factory integration API contract |
| `data/CHINA_HOD_INTERFACE_REGISTER.csv` | Department-interface register |
| `data/SHIPMENT_001_EVENT_REGISTER.csv` | Event register suitable for implementation tracking |

## Common architecture

```text
CHINA SOVEREIGN OPERATING PLANE
  Factory / Supplier / Lab / Auditor / Logistics / Port
                │
                ▼
       Local system-of-records
                │
                ▼
     AHTE local trust + evidence services
                │
     ┌──────────┴───────────┐
     │                      │
 local detailed data    cross-border assertion
     │                      │
     ▼                      ▼
  China retention      TrustAssertion / proof
                           │
                           ▼
                Malaysia governance context
                           │
                           ▼
                    GCC destination plane
                    / importer / authority
                    / warehouse / retail
```

## Five binding layers

### 1. Identity
Every organisation, facility, person, product, batch, lot, pallet, container, seal, sample, shipment, document and authority decision receives a globally unique identifier and stable parent/child genealogy.

### 2. Control
Every applicable requirement is mapped to a control objective, control implementation, halal control point (HCP), owner, evidence requirement and verification method.

### 3. Evidence
Every material control action generates attributable evidence with source, timestamp, location where appropriate, object references, integrity hash and signer/actor identity.

### 4. Trust
Trust is derived from linked evidence, verified custody, laboratory/technical results, audit observations and authority decisions. Trust assertions are scoped and time-bounded.

### 5. Physical release
No shipment state changes without reconciliation between the digital object graph and the physical object at the corresponding control point.

## Source and jurisdiction model

The project source materials establish a federated model in which China-origin operational records remain in their owning environment and cross-border exchange is minimised to the information necessary to support verification, trade and authorised decision workflows.

Current Chinese data-governance architecture materially supports this pattern. The Network Data Security Management Regulation took effect on 1 January 2025 and requires data processors to apply security controls, manage important-data risks and govern provision/entrusted processing. China's 2024 rules on cross-border data flows provide exemptions for certain international trade, cross-border transport and manufacturing data that contain neither personal information nor important data, while regulated exports of personal information and important data remain subject to applicable mechanisms. citeturn748828search0turn164534search0turn164534search1

Chinese standardisation is administered through a multi-level system; the revised Standardization Law distinguishes national, sector, local, association and enterprise standards and places unified administration with the State Council's standardization administration department while recognising sector and local authorities. citeturn356679search1

SAMR's responsibilities include product quality traceability, food-safety supervision, standards administration, inspection/testing and certification/recognition supervision. citeturn748828search1 MOFCOM's mission includes foreign trade, import/export policy, economic and trade cooperation and intergovernmental economic/trade liaison. citeturn356679search2

Saudi destination logic must accommodate SFDA food-import registration and applicable import documentation, including halal documentation where required; UAE destination logic must accommodate MoIAT conformity and Halal National Mark workflows where applicable. citeturn848971search1turn848971search0turn848971search5

## Operating doctrine

- Jurisdictional law and mandatory requirements are evaluated before project-specific controls.
- Destination-market requirements are evaluated for the actual commodity, importer, route and intended claim.
- Malaysian Halal standards and associated JAKIM/JAIN governance instruments are represented as controlled AHTE requirements and assurance objects for applicable scopes.
- Contractual controls can add obligations but cannot cancel mandatory law.
- AHTE must preserve every source, version, applicability decision and effective date used to derive an operational rule.
- Physical identifiers and digital identifiers must remain bound throughout the lifecycle.
- Exception states are engineered as first-class operating paths.
- Human authority remains explicit in the data model through signed decisions and role-authorised actions.

## Programme gates

```text
G0 — Institutional alignment
  ↓
G1 — Governance / HOD ownership confirmed
  ↓
G2 — Pilot manufacturers + products selected
  ↓
G3 — Factory systems connected
  ↓
G4 — Audit / laboratory / evidence dry-run passed
  ↓
G5 — Shipment 001 physical-digital rehearsal passed
  ↓
G6 — Export packet + border workflow ready
  ↓
G7 — GCC destination admission ready
  ↓
G8 — Shipment 001 released into destination operations
  ↓
G9 — Post-shipment assurance + recall drill
  ↓
G10 — Scale-out decision
```

## Core implementation objects

`Authority`, `Organisation`, `Facility`, `Person`, `Role`, `Competence`, `Standard`, `Requirement`, `ApplicabilityDecision`, `ControlObjective`, `Control`, `HCP`, `Material`, `Supplier`, `Product`, `Formula`, `Batch`, `Lot`, `Pallet`, `Container`, `Seal`, `Shipment`, `Sample`, `LabResult`, `Evidence`, `Audit`, `Finding`, `CorrectiveAction`, `AuthorityDecision`, `TrustAssertion`, `TrustState`, `CustodyTransfer`, `Inspection`, `Release`, `Recall`, `DigitalEvent`, `Key`, `TrustAnchor`.

## Canonical identity chain

`Organisation → Facility → Product → Batch → Lot → Pallet → Container → Seal → Shipment → Custody → Port Inspection → Destination Inventory → Retail Unit`

## Canonical event chain

`OBJECT_CREATED → ID_ASSIGNED → QUALIFIED → EVIDENCE_ATTACHED → CONTROL_EXECUTED → AUDITED → VERIFIED → AUTHORITY_DECISION → RELEASED → CUSTODY_TRANSFER → BORDER_INSPECTION → DESTINATION_RECONCILIATION → DISTRIBUTED → VERIFIED_BY_STAKEHOLDER`

Exceptions branch to `HOLD`, `QUARANTINE`, `DISPUTE`, `CORRECTIVE_ACTION`, `RE-VERIFICATION`, `RECALL` and `CLOSE`.

## Success definition

Shipment 001 is considered operationally successful when AHTE can reconstruct, from signed events and linked physical evidence, the complete chain from the selected Chinese manufacturer's source materials and production records through container/seal custody to the GCC destination and provide an authorised party with a deterministic, scope-specific verification view.

## Security baseline

- Zero-trust identity.
- Hardware-backed or equivalent protection for high-value private keys.
- Mutual TLS for machine-to-machine interfaces.
- Signed business events for authority decisions and critical custody transitions.
- Hash-linked evidence records.
- Key rotation and revocation.
- Device attestation for smart-glass and port devices.
- Offline-capable field execution with signed reconciliation queues.
- Role + attribute + purpose-based access control.
- Encryption in transit and at rest.
- Full audit trail for administrative actions.

## Repository integrity

All normative standard content remains paraphrased. The execution pack stores implementation semantics, metadata, mappings, schemas and process logic rather than reproducing licensed standards verbatim.
