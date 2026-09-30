# 08 — China Pilot → Shipment 001 → GCC Release Operating Playbook

## 1. Mission

Execute the first controlled China → GCC deployment as a complete physical + digital proof-of-operation and establish the repeatable pattern for scale.

## 2. Pilot scope

### China
- One or more nominated manufacturers.
- Selected pilot products.
- Material/supplier dossier.
- Facility/process digital twin.
- HCP/control map.
- Smart-glass audit.
- Laboratory pathway where applicable.
- ERP/MES/QMS/WMS/LIMS integration.
- Logistics provider integration.

### Corridor
`Factory → consolidation/loading → container/seal → China logistics → export gateway → transit → GCC port/customs → destination warehouse → retail/distribution`.

### Destination
Start with a named GCC market and expand after the first shipment. The pack supports Saudi Arabia and UAE destination rule variants.

## 3. Stage gates

### Gate 0 — Governance
**Inputs:** HOD mandate, programme sponsor, pilot scope.

**Outputs:** signed programme charter, interface owners, technical workstreams.

**Pass:** every interface has an accountable owner.

### Gate 1 — Manufacturer activation
**Inputs:** legal/site/product information.

**Outputs:** facility twin, product objects, material dossiers, system inventory.

**Pass:** factory can produce an auditable digital batch genealogy.

### Gate 2 — Assurance readiness
**Inputs:** standards/control set, HCP model, evidence templates.

**Outputs:** audit package, lab plan, corrective-action workflow.

**Pass:** dry-run audit closes with traceable evidence.

### Gate 3 — Shipment readiness
**Inputs:** released lots, packaging, pallets, logistics booking.

**Outputs:** shipment object, container, seal, trust packet, export document set.

**Pass:** 100% critical objects reconcile.

### Gate 4 — Export
**Inputs:** origin packet, declaration, physical cargo.

**Outputs:** export release + signed custody event.

**Pass:** origin inspection and system state match.

### Gate 5 — GCC arrival
**Inputs:** container, seal, trust packet, importer records.

**Outputs:** destination inspection, import decision, warehouse receipt.

**Pass:** seal/container/document reconciliation succeeds or exceptions are dispositioned.

### Gate 6 — Destination release
**Inputs:** import release, destination reconciliation.

**Outputs:** warehouse release, distribution event.

**Pass:** affected inventory objects are correctly scoped.

### Gate 7 — Post-shipment
**Inputs:** event stream, exceptions, audit results.

**Outputs:** lessons, KPI report, scale decision.

## 4. Workstream structure

| Workstream | Deliverable |
|---|---|
| Governance | HOD RACI, programme charter, decision register |
| Standards | China/Malaysia/GCC resolved requirement sets |
| Manufacturer | Facility/product/material digital twins |
| Audit | Smart-glass audit package + evidence templates |
| Laboratory | Method/sample/custody/result chain |
| Factory IT | ERP/MES/QMS/WMS/LIMS integration |
| Cybersecurity | Identity/key/device/security baseline |
| Logistics | Cargo/custody/seal integration |
| Border | Trust packet + officer workflow |
| GCC | Importer/destination/warehouse workflow |
| Consumer/stakeholder | Verification endpoint |
| Analytics | KPI/exception/recall dashboard |

## 5. Four-week integrated sprint

### Week 1 — Institutional + technical freeze

- Confirm counterpart owners.
- Confirm product roster.
- Confirm facility roster.
- Inventory factory systems.
- Establish object IDs.
- Establish data classification.
- Establish trust anchors.
- Finalise destination rule pack.

### Week 2 — Factory activation

- Load material/supplier records.
- Create product/formula versions.
- Build facility/process twin.
- Instantiate HCPs.
- Connect factory APIs.
- Load audit package.
- Validate laboratory chain.

### Week 3 — Physical rehearsal

- Dry-run smart-glass audit.
- Sample chain rehearsal.
- Batch/lot traceability test.
- Pallet/container/seal binding.
- Carrier custody test.
- Port officer workflow simulation.
- GCC destination release simulation.

### Week 4 — Shipment 001 rehearsal and release

- Freeze shipment object.
- Generate signed trust packet.
- Reconcile all critical objects.
- Execute origin gate.
- Execute physical shipment.
- Execute destination gate.
- Perform recall drill after release.
- Hold executive/HOD post-ship review.

## 6. Manufacturer activation dossier

### Corporate
Legal entity, manufacturing licences, site, owners, designated programme contact.

### Products
SKU, specification, formula/BOM, process version, intended GCC market.

### Materials
Supplier, source, origin, specification, certificates and related halal-risk evidence.

### Facility
Layout, zoning, process flow, equipment, hygiene/sanitation, segregation.

### People
Responsible roles, competency, training, authorisation, audit participation.

### Systems
ERP, MES, QMS, WMS, LIMS, DMS, IoT and identity systems.

### Assurance
Audit, evidence, laboratory, corrective-action and change-control records.

## 7. Shipment 001 digital twin

```text
SHIPMENT-001
 ├── Orders
 ├── Products
 │    └── Lots
 │         └── Pallets
 │              └── Container
 │                   └── Seal
 ├── Documents
 ├── Certificates / Decisions
 ├── Evidence
 ├── Custody Events
 ├── Inspections
 ├── Trust Assertion
 ├── Exceptions
 └── Destination Inventory
```

## 8. Origin release checklist

- Product scope resolved.
- Requirements resolved.
- Material provenance complete.
- Applicable HCPs executed.
- Audit status acceptable.
- Laboratory results linked where required.
- Lots released.
- Pallet genealogy complete.
- Container assigned.
- Seal applied and photographed.
- Export documents reconciled.
- Trust assertion signed.
- Carrier custody event signed.

## 9. GCC release checklist

- Importer identified.
- Destination rule pack resolved.
- Trust assertion verified.
- Container identity matched.
- Seal identity matched.
- Documents reconciled.
- Authority/inspection result recorded.
- Destination inventory created.
- Quarantine/release state recorded.
- Distribution permission/status recorded.

## 10. Incident playbook

### Identity mismatch
`STOP → HOLD → CAPTURE → RECONCILE → AUTHORITY REVIEW → RESOLVE`

### Seal mismatch
`HOLD → PHYSICAL INSPECTION → EVIDENCE → CUSTODY INVESTIGATION → AUTHORITY DECISION`

### Evidence contradiction
`FREEZE AFFECTED OBJECTS → COMPARE SOURCES → IDENTIFY AUTHORITATIVE RECORD → CORRECT/ESCALATE`

### Route anomaly
`ALERT → CHECK TELEMETRY → CHECK CUSTODY → VERIFY CONDITION → DECISION`

### Recall
`RECALL OPEN → TRACEBACK → TRACEFORWARD → QUARANTINE → DISPOSITION → CLOSE`

## 11. KPI pack

| KPI | Target |
|---|---|
| Critical traceability completeness | 100% |
| Critical custody capture | 100% |
| Unexplained identity mismatch | 0 |
| Unlinked critical evidence | 0 |
| Seal reconciliation | 100% |
| Recall blast-radius determinism | 100% of tested scenarios |
| Cross-border minimum-data compliance | 100% of approved packets |
| Audit evidence retrieval | Minutes, not days |
| Unauthorized data access | 0 |

## 12. Scale-out

After Shipment 001:

`POST-SHIPMENT REVIEW → CONTROL TUNING → TEMPLATE FREEZE → SECOND MANUFACTURER → SECOND ROUTE/PRODUCT → MULTI-SITE → REGIONAL SCALE`.

The critical scale principle is template standardisation without forcing identical local implementation. The common objects/events remain stable while jurisdiction-specific rule packs and operating procedures can vary.

## 13. Exit report

The post-ship executive report must contain:

- event-completeness report;
- traceability graph;
- evidence completeness;
- audit outcomes;
- laboratory outcomes;
- custody graph;
- border events;
- destination release;
- exceptions;
- corrective actions;
- security events;
- recall drill result;
- KPI dashboard;
- scale recommendation.

## 14. Destination references

Saudi SFDA guidance requires imported food to meet KSA requirements and identifies halal and origin/slaughter documentation where applicable; Saudi Halal Center has a distinct eligibility/audit/decision workflow. citeturn848971search1turn848971search0

UAE MoIAT operates national conformity-mark licensing, including the Halal National Mark, through a digital application and field-assessment workflow and provides a route for registration of halal certification bodies. citeturn848971search2turn848971search12

## 15. Definition of done

Shipment 001 is complete when the complete physical journey and digital trust journey can be reconstructed from the repository's event stream and linked evidence, the destination operating team can verify the scoped shipment state, exceptions can be deterministically isolated, and a repeatable implementation template exists for the next manufacturer and route.
