# AHTE China Manufacturer Onboarding Dossier

## 1. Objective

Convert a Chinese manufacturer from an ordinary supplier record into a fully traceable AHTE production node with facility, product, material, process, HCP, evidence, competence and shipment readiness represented digitally.

## 2. Dossier structure

| Domain | Required record |
|---|---|
| Corporate identity | Legal entity, licences, site ownership, responsible persons |
| Facility | Site map, zones, flows, equipment, controlled areas |
| Product | SKU, product family, formulation/process version, market scope |
| Materials | Ingredient/raw material list, source, supplier, origin, certificates/specifications |
| Process | Process flow, critical steps, HCPs, sanitation/segregation controls |
| People | Halal roles, competence, training, authorisation and expiry |
| Evidence | SOPs, records, monitoring logs, certificates, audit records |
| Laboratory | Sampling plan, methods, matrix, results and interpretation |
| Packaging | Packaging materials, labels, lot coding, release controls |
| Supply chain | Carrier, container, seal, warehouse and destination interfaces |
| Change control | Formula/material/process/supplier changes and re-verification triggers |

## 3. Activation workflow

`Candidate -> Scope -> Entity -> Facility -> Product -> Materials -> Process -> HCP -> Evidence -> Competence -> Audit -> Lab -> Corrective Action -> Re-verification -> Authority workflow -> Production readiness -> Shipment readiness`

## 4. Minimum acceptance gates

### Gate A - Identity
All organisation, facility, product and material identifiers reconcile.

### Gate B - Scope
Applicable Malaysian and destination requirements are mapped to the product/process scope.

### Gate C - Provenance
Critical materials have source/supplier/origin evidence and traceability.

### Gate D - HCP
Critical halal control points are identified, monitored and evidenced.

### Gate E - Personnel
Responsible roles are assigned and competence records are current.

### Gate F - Evidence
Required evidence can be retrieved by requirement/HCP/batch.

### Gate G - Audit
Facility and records pass the defined audit workflow and corrective-action cycle.

### Gate H - Shipment
Batch/lot/pallet/container/seal relationships are complete and dispatch-ready.

## 5. ERP/MES/WMS/QMS/LIMS integration fields

At minimum exchange stable IDs, timestamps, actor IDs, process/batch references, status, source-system references, integrity metadata and change/version references.

## 6. First shipment readiness checklist

- Product list frozen for the shipment.
- All critical material suppliers mapped.
- Batch and lot IDs allocated.
- Packaging and labels verified.
- Required laboratory samples identified.
- Audit/evidence dossier complete.
- Authority/certification references attached.
- Pallet and container aggregation recorded.
- Seal ID recorded at loading.
- Carrier custody event created.
- Destination importer and warehouse identified.
- GCC destination rule pack applied.

## 7. Continuous operation

The manufacturer remains a live digital twin. New suppliers, material changes, formula changes, process changes, equipment changes, site changes, subcontracting, incidents and recalls create change-control events that propagate into the affected requirements, HCPs, evidence and shipment objects.
