# IQ300 — CHINA EXECUTION PACK
## China Pilot → Shipment 001 → GCC Release

This directory is the execution-grade implementation layer for the China deployment of the Amanah Halal Trust Ecosystem (AHTE). It converts the programme into accountable departments, executable cross-border rules, machine-readable events, system interfaces, field audit tooling, border operations and release gates.

## Operating architecture

`Sovereign Governance -> China Activation -> Factory Qualification -> Material/Process Assurance -> Batch/Lot Identity -> Evidence -> Audit -> Authority Decision -> Container/Seal -> Export -> Transit -> GCC Border -> Destination Warehouse -> Retail -> Consumer/Stakeholder Trust`

## Pack contents

1. `01_DEPARTMENT_RACI.md` — department-by-department RACI across China, Malaysia and GCC interfaces.
2. `02_RULE_PRECEDENCE_ENGINE.md` — China ↔ Malaysia ↔ GCC jurisdiction and rule-resolution engine.
3. `03_SHIPMENT_001_EVENT_CATALOGUE.md` — canonical event catalogue from manufacturer onboarding through GCC release and recall.
4. `04_FACTORY_SYSTEM_API_CONTRACTS.md` — factory/MES/ERP/WMS/LIMS/API integration contracts and canonical payload rules.
5. `05_SMART_GLASS_AUDIT_SPECIFICATION.md` — field audit operating model, device workflow, evidence binding and offline/online synchronisation.
6. `06_PORT_OFFICER_UI_WORKFLOW.md` — port/customs/inspection tablet workflow and exception/release states.
7. `07_CRYPTOGRAPHIC_TRUST_ANCHOR_ARCHITECTURE.md` — trust root, signing, key rotation, evidence hashing, custody binding and selective disclosure.
8. `08_CHINA_PILOT_SHIPMENT001_GCC_RELEASE_PLAYBOOK.md` — integrated operating playbook and stage gates.
9. `09_MASTER_STANDARDS_FULL_MATRIX.md` — consolidated current JSM/MySOL NSC 09 Halal standards matrix used by IQ300.
10. `10_MACHINE_READABLE_EXECUTION_PACK.json` — canonical identifiers, states, event domains and interface envelope definitions.

## Execution doctrine

The platform is operated as a federated trust infrastructure. Physical events and digital events are paired wherever practical: `asset -> action -> actor -> place -> time -> evidence -> signature -> resulting state`.

Every material object receives a stable identifier. Identity must survive transformations: organisation → facility → production line → formula/material → batch/lot → package/case → pallet → container → seal → shipment → destination inventory → retail unit.

Cross-border policy is resolved before operational release. A control may be stricter than the minimum legal requirement, but the engine never silently substitutes a private project rule for a competent authority requirement.

## Primary pilot scope

Shipment 001 is designed as a China-origin direct-to-GCC corridor. The reference flow is:

`Chinese manufacturer -> source/material verification -> factory qualification -> production/batch evidence -> audit/lab -> Malaysian/JAKIM evidence and applicable authority workflows -> palletisation -> containerisation/seal -> China logistics -> export/port -> transit -> GCC import/inspection -> destination warehouse -> retail -> verification`

## Engineering principles

- Authority, standards, evidence, audit and commercial release are separate object classes.
- One event has one authoritative emitter and one immutable event identifier.
- Corrections create a new event; historical evidence is never silently rewritten.
- Offline field operations are first-class, with signed local records and later synchronisation.
- Sensitive China source records remain in the applicable China-controlled data zone; cross-border exchange uses minimised assertions and policy-approved evidence.
- Analytical results are linked to sample identity, method identity, laboratory identity and chain of custody.
- Container release is conditional on shipment, batch, custody and seal state.
- Recall logic is graph-based: identify affected lots, custody paths, destinations and retail exposure.

## Master release gates

`G0 Programme authority -> G1 manufacturer onboarded -> G2 factory qualified -> G3 materials/processes verified -> G4 batch released -> G5 shipment assembled -> G6 container sealed -> G7 export release -> G8 GCC border clearance -> G9 destination release -> G10 retail release`

Any failed mandatory gate produces a deterministic exception state and a named owner.

## Repository integration points

The pack binds to the existing AHTE standards layer, A-Z platform mapping, MS 2400 requirement objects, process-flow infographics, Evidence Fabric, Digital Audit Twin, Trust Graph and current JSM standards register.
