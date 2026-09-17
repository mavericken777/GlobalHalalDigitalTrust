# Malaysian Halal Standards - Master Control Manual and 2026 Status Register

**Control date:** 17 September 2026  
**Repository:** mavericken777/GlobalHalalDigitalTrust

## 1. Purpose

This register covers the 17-standard Malaysian Halal standards set already established in the repository. It is a control/mapping layer, not a reproduction of copyrighted standards. Exact normative text remains with Department of Standards Malaysia / MySOL and authorized copies.

## 2. Master 17-standard register

| # | Standard | Domain | IQ300 role | Status / handling |
|---|---|---|---|---|
| 01 | MS 1500:2019 | Halal food - general requirements | Food/product/process baseline | Current confirmed edition; do not use withdrawn 2009 slaughter clauses |
| 02 | MS 2400-1:2019 | Halal transportation | Transport integrity and custody | Confirmed 2024; supplied PDF clause source |
| 03 | MS 2400-2:2019 | Halal warehousing | Storage/segregation/handling | Confirmed 2024; supplied PDF clause source |
| 04 | MS 2400-3:2019 | Halal retailing | Receiving/storage/retail handling | Confirmed 2024; supplied PDF clause source |
| 05 | MS 2424:2019 | Halal pharmaceuticals | Pharmaceutical material/process assurance | Current 2019 edition; 2012 replaced |
| 06 | MS 2634:2019 | Halal cosmetics | Cosmetic material/process assurance | Current 2019 edition; replaces MS 2200-1:2008 |
| 07 | MS 2636:2019 | Halal medical devices | Medical-device Halal control layer | 1st confirmation; current repository scope |
| 08 | MS 2738:2023 | Halal consumable goods | Consumable-goods assurance | Current published standard |
| 09 | MS 2803:2025 | Animal bone, skin and hair | Animal-derived material provenance | Current published; replaces MS 2200-2:2013 |
| 10 | MS 2809:2025 | Product authentication using chemometric techniques | Advanced analytical authentication | Current original standard in repository |
| 11 | MS 2810:2025 | Identification of pig skin and hair in consumable goods | Analytical test method | Current original standard in repository |
| 12 | MS 2393:2023 | Islamic/Halal terminology | Ontology and controlled vocabulary | Current published revision |
| 13 | MS 2627:2017 | Porcine DNA - food/food products | Analytical evidence method | Method/evidence layer; not certification |
| 14 | MS 2627-2:2025 | Porcine DNA - cosmetics qPCR | Analytical evidence method | Current published method |
| 15 | MS 1900:2025 | Shariah-based quality management system | Organization-level QMS | 2nd revision, effective 24/07/2025 |
| 16 | MS 2691:2021 | Halal profession | Professional competency | Current published standard |
| 17 | MS 2610:2015 | Muslim-friendly hospitality services | Supporting hospitality context | Supporting standard; apply by scope |

## 3. Control doctrine by family

### MS 1500:2019 - Food
Core controls: halal raw materials; source/provenance; facilities; utensils/equipment; hygiene; sanitation; food safety; processing; storage; transport; display; sale/service; packaging; labelling; advertising; legal compliance.

### MS 2400-1/-2/-3 - Supply chain
Transport, warehousing and retail each apply common Halal risk-management architecture plus node-specific controls for custody, segregation, condition, traceability, release, withdrawal/recall, outsourced services, cleaning, sertu, training, internal audit, management review and change control.

### MS 2424:2019 - Pharmaceuticals
Trace API, excipients, solvents, enzymes, buffers, process aids, capsules, packaging, contract manufacturers and critical processing routes. High-risk inputs need source, supplier, route and recognized evidence.

### MS 2634:2019 - Cosmetics
Control ingredient origin and animal-derived materials including glycerin/stearates, collagen/gelatin/keratin, placenta, lanolin/tallow derivatives, carmine/cochineal, alcohol/ethanol source where relevant, enzymes, fermentation inputs and applicators.

### MS 2636:2019 - Medical devices
Map device scope, materials, manufacturing, Halal controls, quality management, cleaning/contamination, packaging, sterilization/material provenance where applicable, evidence and certification status.

### MS 2738:2023 - Consumable goods
Route non-food-specific consumables into a product-specific control profile covering materials, manufacturing, contamination, packaging, status, traceability, evidence and authority requirements.

### MS 2803:2025 - Animal materials
Capture species, source, origin, slaughter/provenance where applicable, processor, supplier, batch, segregation, evidence and downstream use.

### MS 2809:2025 - Chemometric authentication
Treat chemical/chromatographic datasets, models, validation, statistics and result provenance as evidence objects. Authentication supports trust; it does not itself create Halal certification.

### MS 2810:2025 - Pig skin/hair identification
Treat the method result as scoped analytical evidence tied to sample identity, matrix, method version, controls and report provenance.

### MS 2393:2023 - Terminology
Use as controlled vocabulary: term, definition, language, jurisdiction, source version, interpretation note and status.

### MS 2627 / 2627-2 - DNA methods
Analytical results are evidence only. Never implement `PCR/qPCR negative => Halal`.

### MS 1900:2025 - Shariah-based QMS
Organization-level management system. It is distinct from MHMS and is not a JAKIM Halal certificate.

### MS 2691:2021 - Halal profession
Person as trust object: role, competency, training, credential, issuer, scope, validity, revocation.

### MS 2610:2015 - Hospitality
Use only where hospitality operations are within scope; map premises, F&B/service, people, guest-facing controls and assurance.

## 4. Cross-standard traceability object

`Product/SKU -> material/formula -> supplier -> site -> batch/lot -> Halal credential/reference -> lab evidence -> HCP -> process -> pallet -> container/seal -> transport -> warehouse -> GCC import -> retail -> consumer`

Every link records actor, timestamp, scope, evidence and status.

## 5. Version-control rules

Each production rule stores: `StandardID + edition + status + effective date + supersedes + source + retrieval date + rule owner + verification state`.

A new edition/confirmation/withdrawal triggers impact analysis across controls, products, audit packs and release rules. Historical events retain the rule version that governed them.

## 6. Analytical evidence boundary

MS 2627, MS 2627-2, MS 2809 and MS 2810 are analytical/evidence instruments. A test result cannot independently establish Malaysian Halal certification. Certification remains an authority decision under the applicable framework.

## 7. Audit test library

| Test | Pass condition |
|---|---|
| STD-01 Version | Current standard edition identified |
| STD-02 Scope | Standard applies to the object/process |
| STD-03 Source | Authoritative source recorded |
| STD-04 Status | Confirmation/current/withdrawn state known |
| STD-05 Evidence | Evidence linked to requirement and object |
| STD-06 HCP | Risk/HCP control implemented and monitored |
| STD-07 Change | Material/process change is assessed and approved |
| STD-08 Trace | Forward and backward trace succeeds |
| STD-09 Authority | Authority decision is distinct from platform state |
| STD-10 Retention | Required evidence remains retrievable |

## 8. Verification statement

Current status checks are based on JSM/MySOL and the established repository standards register, with specific 2025 standards including MS 2803:2025, MS 2809:2025, MS 2810:2025 and MS 1900:2025 incorporated. Any future standard revision, confirmation, withdrawal or authority circular must create a new version before future transactions rely on it.
