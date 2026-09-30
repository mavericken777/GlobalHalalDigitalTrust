# IQ300 — China Execution Pack
## China Pilot → Shipment 001 → GCC Release

**Current architecture alignment — 30 September 2026:** this package executes AHTE across a **China-origin → GCC-destination direct physical corridor** with Malaysia as the governance/assurance and authority-connectivity plane unless a Malaysia physical movement is separately scoped. Older wording that could be read as a mandatory China→Malaysia→GCC physical route is superseded for Shipment 001.

[PILOT: Shipment 001 — China → GCC direct]

[PROPOSAL: aligns China execution pack to current target architecture — path point: Control → Evidence → Authority Gate → Trust State → Operational Release]

## Implementation completeness rule

**FULL ARCHITECTURE NOW → REAL CONNECTORS WHEN AVAILABLE → NO REDESIGN REQUIRED.**

External/API/credential/partner availability must not be converted into an omitted target capability. Where a live connector is unavailable, implement the complete production contract and workflow with a replaceable development/sandbox provider. Do not fabricate live authority, laboratory, logistics, customs, GCC or transaction evidence.

Controlling companion: `../../00_EXECUTIVE_COMMAND/IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md`.

## Objective

Convert the existing AHTE standards, HCP, evidence, audit, trust-graph and physical/digital identity architecture into deployable operating specifications for:

1. China counterpart departments and technical HOD interfaces.
2. China manufacturer/factory activation.
3. Factory-system integration.
4. Raw-material/sample/laboratory evidence integration.
5. Physical custody and shipment control.
6. Smart-glass field audit execution.
7. Direct JAKIM API / human authority workflow integration.
8. Sinotrans warehouse and end-to-end logistics integration.
9. Port/customs inspection, API and release workflows.
10. Cryptographic trust anchoring and selective disclosure.
11. Shipment 001 execution from China directly to the GCC.
12. GCC destination admission, warehouse release, distribution and retail verification.
13. 24/7 GHSCL + JAKIM-connected Command Center monitoring.
14. AI/ML predictive analytics and Preemptive Strategy Engine workflows.
15. Shariah-financing/Takaful/tokenomics transaction-support integration where applicable.

## Repository map

| File | Function |
|---|---|
| `00_MASTER_CHINA_EXECUTION_MODEL.md` | Common operating model, architecture and implementation doctrine |
| `01_CHINA_HOD_RACI.md` | Department-by-department interface and RACI model |
| `02_RULE_PRECEDENCE_ENGINE.md` | China operating requirements + Malaysia governance/assurance + GCC destination rule resolution and conflict handling; not a physical-route definition |
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
  Supplier / Factory / Lab / Auditor / Sinotrans / Origin Port
                │
                ▼
       Local systems of record
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
          MALAYSIA GOVERNANCE / ASSURANCE PLANE
          PHC + Direct JAKIM API / authority workflow
                           │
                           ▼
                 TRUST / AUTHORITY STATE
                           │
                           ▼
                CHINA → GCC DIRECT MOVEMENT
                           │
                           ▼
                    GCC destination plane
                 importer / authority / customs
                    warehouse / retail
```

The Malaysia plane above is a governance/assurance/authority-connectivity function. It is not a required physical transshipment leg.

## Five binding layers

### 1. Identity
Every organisation, facility, person, product, batch, lot, pallet, container, seal, sample, shipment, document and authority decision receives a globally unique identifier and stable parent/child genealogy.

### 2. Control
Every applicable requirement is mapped to a control objective, control implementation, halal control point (HCP), Shariah critical control point where applicable, owner, evidence requirement and verification method.

### 3. Evidence
Every material control action generates attributable evidence with source, timestamp, location where appropriate, object references, integrity hash and signer/actor identity.

### 4. Trust
Trust is derived from linked evidence, verified custody, laboratory/technical results, audit observations and authority decisions. Trust assertions are scoped and time-bounded.

### 5. Physical release
No controlled shipment state changes without reconciliation between the digital object graph and the physical object at the corresponding control point.

## Source and jurisdiction model

The project source materials establish a federated model in which China-origin operational records remain in their owning environment and cross-border exchange is minimised to the information necessary to support verification, trade and authorised decision workflows.

Jurisdictional implementation must preserve current Chinese data-governance, cybersecurity, privacy and cross-border-transfer controls and the applicable GCC destination controls. This execution pack is architecture, not a substitute for current legal/authority source verification.

## Operating doctrine

- Jurisdictional law and mandatory requirements are evaluated before project-specific controls.
- Destination-market requirements are evaluated for the actual commodity, importer, route and intended claim.
- Malaysian Halal standards and associated JAKIM/JAIN/MAIN governance instruments are represented as controlled AHTE requirements and assurance objects for applicable scopes.
- Direct JAKIM API is the target authority-connectivity path; exact production endpoint/authentication/schema remain controlled implementation inputs.
- Contractual controls can add obligations but cannot cancel mandatory law.
- AHTE must preserve every source, version, applicability decision and effective date used to derive an operational rule.
- Physical identifiers and digital identifiers must remain bound throughout the lifecycle.
- Exception states are engineered as first-class operating paths.
- Human authority remains explicit in the data model through signed decisions and role-authorised actions.
- AI/ML may analyse, predict and recommend; D5/D6 authority decisions remain human/authority-controlled.
- External gates are not product feature blocks; complete adapters/workflows must still be built.

## Programme gates

```text
G0 — Institutional alignment
  ↓
G1 — Governance / HOD ownership confirmed
  ↓
G2 — Pilot manufacturers + products selected
  ↓
G3 — Factory/lab/logistics integration contracts implemented
  ↓
G4 — Audit / laboratory / evidence dry-run passed
  ↓
G5 — Shipment 001 physical-digital rehearsal passed
  ↓
G6 — Export packet + origin border workflow ready
  ↓
G7 — GCC destination admission ready
  ↓
G8 — Shipment 001 released into destination operations
  ↓
G9 — Post-shipment assurance + recall drill
  ↓
G10 — Scale-out decision
```

These programme gates govern live operational readiness. They must not be implemented as disabled architecture: development providers should allow the target workflow to be exercised before real external gates close.

## Core implementation objects

`Authority`, `Organisation`, `Facility`, `Person`, `Role`, `Competence`, `Standard`, `Requirement`, `ApplicabilityDecision`, `ControlObjective`, `Control`, `HCP`, `SCCP`, `Material`, `Supplier`, `Product`, `Formula`, `Batch`, `Lot`, `Pallet`, `Container`, `Seal`, `Shipment`, `Sample`, `LabResult`, `Evidence`, `Audit`, `Finding`, `CorrectiveAction`, `AuthorityDecision`, `TrustAssertion`, `TrustState`, `CustodyTransfer`, `Inspection`, `Release`, `Recall`, `DigitalEvent`, `Key`, `TrustAnchor`, `Prediction`, `PreemptiveStrategy`, `CommandCenterIncident`, `FinanceEvidencePacket`, `TakafulCase`, `TokenizedAssetReference`.

## Canonical identity chain

`Organisation → Facility → Product → Batch → Lot → Pallet → Container → Seal → Shipment → Custody → Port Inspection → Destination Inventory → Retail Unit`

## Canonical event chain

`OBJECT_CREATED → ID_ASSIGNED → QUALIFIED → EVIDENCE_ATTACHED → CONTROL_EXECUTED → AUDITED → VERIFIED → AUTHORITY_DECISION → RELEASED → CUSTODY_TRANSFER → BORDER_INSPECTION → DESTINATION_RECONCILIATION → DISTRIBUTED → VERIFIED_BY_STAKEHOLDER`

Exceptions branch to `HOLD`, `QUARANTINE`, `DISPUTE`, `CORRECTIVE_ACTION`, `RE-VERIFICATION`, `RECALL` and `CLOSE`.

## 24/7 Command Center

Across the execution pack, relevant events must be routable to the GHSCL + JAKIM-connected Command Center for:

- live monitoring;
- anomaly detection;
- predictive risk;
- preemptive-strategy recommendation;
- ownership assignment;
- alert/escalation;
- configured D4 hold where policy permits;
- CAPA/re-verification;
- recall/blast-radius analysis;
- outcome analytics.

## Success definition

Shipment 001 is considered operationally successful when AHTE can reconstruct, from signed events and linked physical evidence, the complete chain from the selected Chinese manufacturer's source materials and production records through laboratory evidence, authority-linked status, Sinotrans warehouse/logistics, container/seal custody and origin port events to the GCC destination and provide an authorised party with a deterministic, scope-specific verification view.

## Security baseline

- Zero-trust identity.
- Hardware-backed or equivalent protection for high-value private keys.
- Mutual TLS for machine-to-machine interfaces where applicable.
- Signed business events for authority decisions and critical custody transitions.
- Hash-linked evidence records.
- Key rotation and revocation.
- Device attestation for smart-glass and port devices.
- Offline-capable field execution with signed reconciliation queues.
- Role + attribute + purpose-based access control.
- Encryption in transit and at rest.
- Full audit trail for administrative actions.
- Explicit connector-state reporting.
- Development providers isolated from production credentials/data.

## Repository integrity

All normative standard content remains source-governed. The execution pack stores implementation semantics, metadata, mappings, schemas and process logic rather than reproducing licensed standards verbatim.

This file does not modify `master-standards-stack/verified-2026-09-17/`.
