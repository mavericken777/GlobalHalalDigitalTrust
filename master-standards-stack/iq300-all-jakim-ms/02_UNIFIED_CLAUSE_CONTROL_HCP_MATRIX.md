# IQ300 - UNIFIED CLAUSE -> CONTROL -> HCP -> EVIDENCE -> AUDIT -> AUTHORITY MODEL

## 1. Canonical requirement object

Every standard is represented by an object with these logical fields:

`requirement_id`
`instrument`
`edition/status`
`clause`
`clause_title`
`clause_status`
`source_basis`
`requirement_intent`
`applicability`
`control_objective`
`control_object`
`control_owner`
`hcp`
`risk_class`
`evidence`
`audit_tests`
`authority_gate`
`digital_events`
`failure_states`
`corrective_action`
`reverification`
`trust_state_effect`
`notes`

## 2. Standard-specific mapping

### MS 1500:2019 - Food

| Requirement family | Control | HCP | Evidence | Audit test | Authority gate |
|---|---|---|---|---|---|
| Management responsibility | HALAL-MGMT | HALAL-MGMT | policy, records, interviews | DOC-01/REC-01/INT-01 | AUTH-CERT |
| Premises/facilities | PREM-HYGIENE | PREM-HYGIENE | layout, inspection, cleaning, pest records | SITE-01/WIT-01 | AUTH-AUDIT |
| Materials | MAT-ORIGIN | MAT-ORIGIN | halal cert, specification, supplier file | DOC-01/TRACE-01/AUTH-01 | AUTH-MATERIAL |
| Equipment/utensils | EQP-HALAL | EQP-HALAL | status, cleaning, sertu records | SITE-01/AUTH-01 | AUTH-SERTU |
| Processing | PROC-HALAL | PROC-HALAL | flow, HCP records, batch evidence | WIT-01/TRACE-01 | AUTH-AUDIT |
| Hygiene/sanitation/food safety | HYGIENE | HYGIENE | monitoring records/site state | SITE-01/REC-01 | AUTH-AUDIT |
| Storage/transport/display/sale/serving | CHAIN-INT | CHAIN-INT | custody/handling records | TRACE-01/WIT-01 | AUTH-CHAIN |
| Packaging/labelling/advertising | CLAIM-CONTROL | CLAIM-CONTROL | approved artwork, claim controls | DOC-01/SITE-01 | AUTH-LOGO |
| Sertu annex | SERTU | SERTU | procedure, witness, verification | WIT-01/AUTH-01 | AUTH-SERTU |
| Slaughter/stunning interface | SLAUGHTER | SLAUGHTER | current Protocol, competency, HCP records | WIT-01/COMP-01/AUTH-01 | AUTH-PROTOCOL |

### MS 2400-1:2019 - Transportation

The supplied PDF is fully parsed into **187 individually numbered requirement objects** in `../iq300-full-matrix/MS2400-12019_IQ300_REQUIREMENTS.json.gz`. Each object is mapped through transport HCPs including loading, vehicle/container status, cleaning/sertu, segregation, seal/custody, condition/temperature where required, handover and delivery, outsourced carriers and traceability.

### MS 2400-2:2019 - Warehousing

The supplied PDF is fully parsed into **201 individually numbered requirement objects** in `../iq300-full-matrix/MS2400-22019_IQ300_REQUIREMENTS.json.gz`. Core HCPs include inbound verification, quarantine/release/reject/return state transitions, segregation, storage conditions, pest/hygiene, traceability, dispatch, damaged/returned stock and outsourced warehousing.

### MS 2400-3:2019 - Retailing

The supplied PDF is fully parsed into **225 individually numbered requirement objects** in `../iq300-full-matrix/MS2400-32019_IQ300_REQUIREMENTS.json.gz`. Core HCPs include receipt, retail segregation, display, serving/sale, utensils/equipment, opened products, tasting samples, returns, staff competence and contamination prevention.

### MS 2424:2019 - Pharmaceuticals

| Clause family | Primary control object | HCP focus | Evidence/test | Gate |
|---|---|---|---|---|
| 4.1 | PH-QMS | halal embedded in quality system | DOC-01/REC-01 | AUTH-AUDIT |
| 4.2 | PH-MGMT | policy, IHC, resources, records | DOC-01/INT-01 | AUTH-AUDIT |
| 4.3 | PH-HMS | documented HMS, HCPs, training, audit, control | DOC-01/CHANGE-01 | AUTH-AUDIT |
| 4.4 | PH-HALAL | permitted inputs, no najs, separation | DOC-01/SITE-01/TRACE-01 | AUTH-AUDIT |
| 4.5 | PH-MAT-QC | halal identity + pharmaceutical QC | DOC-01/LAB-01/TRACE-01 | AUTH-MATERIAL |
| 4.6 | PERSON-HALAL | responsibility and approval of origin records | COMP-01/DOC-01 | AUTH-AUDIT |
| 4.7 | COMPETENCE | GMP + halal + sertu + HCP competence | COMP-01/REC-01 | AUTH-COMPETENCE |
| 4.8 | HYGIENE | classified-area hygiene + halal conduct | SITE-01/WIT-01 | AUTH-AUDIT |
| 4.9 | EQP-HALAL | equipment status, contamination/mix-up prevention | SITE-01/AUTH-01 | AUTH-SERTU |
| 4.10 | PH-OPS | manufacturing/storage segregation and status | SITE-01/REC-01 | AUTH-AUDIT |
| 4.11 | PH-TRANS | transport custody/segregation | TRACE-01/SITE-01 | AUTH-CHAIN |
| 4.12 | PH-QC | QC area contamination prevention | SITE-01/DOC-01 | AUTH-AUDIT |
| 4.13 | ANCILLARY | prayer facility and animal-house isolation | SITE-01/DOC-01 | AUTH-AUDIT |
| 4.14 | DOC-CONTROL | complete HMS/material origin documentation | DOC-01/TRACE-01 | AUTH-AUDIT |
| 4.15 | LINE-CLEAR | line clearance includes halal status | WIT-01/SITE-01 | AUTH-AUDIT |
| 4.16 | PH-MATERIAL | synthetic/natural route assessment | DOC-01/TRACE-01/LAB-01 | AUTH-MATERIAL |
| 4.17 | PH-CLAIM | packaging/artwork/mark control | DOC-01/SITE-01 | AUTH-LOGO |
| 4.18 | OUTSOURCE | CMO/lab/packer control | DOC-01/TRACE-01/AUTH-01 | AUTH-OUTSOURCE |
| 4.19 | SELF-INSPECT | internal Halal/GMP inspection and closure | REC-01/SITE-01/CHANGE-01 | AUTH-AUDIT |
| 4.20 | LEGAL | NPRA + Shariah + legal conformity | DOC-01/AUTH-01 | AUTH-LEGAL |
| Annex A | SERTU | mughallazah washing + verification | WIT-01/AUTH-01 | AUTH-SERTU |
| Annex B | VAX-HCP | cell/seed/media/sera/etc. | TRACE-01/SITE-01/AUTH-01 | AUTH-VACCINE |

### MS 2634:2019 - Cosmetics

Controls include management, every INCI/material source or synthesis route, animal-derived ingredients, ethanol source where fatwa-sensitive, glycerin/stearates/emulsifiers, carmine, keratin/collagen/gelatin, human-derived materials, enzymes/fermentation media, animal-hair tools, hygiene, production/handling/distribution, OEM control, packaging/claims, sertu and MS 2627-2 evidence.

### MS 2738:2023 - Consumable goods

Maps scope/applicability, management, source-controlled materials, premises/equipment, process integrity, packaging/claims, legal conformity and competent-authority certification.

### MS 2803:2025 - Animal bone, skin and hair

Maps species/origin, slaughter evidence where applicable, processing integrity, najs prevention, segregation, traceability and certification-file evidence. Links to MS 2810 where pig-origin skin/hair identification is analytically relevant.

### MS 2393:2023 - Terminology

Maps controlled vocabulary objects: halal, haram, najs, sertu, fatwa, competent authority, syubhah, mutlaq water and related definitions. Terminology objects are referenced by every downstream ruleset.

### MS 2627:2017 - Porcine DNA in food

Maps sample/matrix suitability, extraction, controls, positive/negative control validity, inhibition/internal control, difficult-matrix validation, reporting and interpretation. `Not detected` is evidence only and does not itself establish halal.

### MS 2627-2:2025 - Porcine DNA in cosmetics

Maps solid/semi-solid/liquid cosmetic matrices, qPCR, extraction effects from surfactants/pigments/ethanol/waxes, matrix-specific validation and result linkage to material/halal decisions.

### MS 1900:2025 - Shariah-based QMS

Maps organisation-wide Shariah conformity, stakeholder/statutory requirements, system effectiveness and continual improvement. It is not a replacement for Malaysia-specific Halal Management System requirements and does not itself issue a product halal mark.

### MS 2691:2021 - Halal profession

Maps qualifications, training, experience, competence assessment and role authorization for Halal Executives, auditors, consultants and related professionals.

### MS 2610:2015 - Muslim-friendly hospitality

Maps accommodation, tours and guide services to the relevant manual procedure and competent-authority path.

### MS 2809:2025 - Chemometric authentication

Maps dataset provenance, quantitative chemical data, chromatography/spectroscopy/spectrometry, mathematical modelling, statistical analysis, pattern recognition, model versioning and authentication evidence. The method supports evidence; it is not a Halal certificate.

### MS 2810:2025 - Pig skin/hair identification

Maps applicable sample classes, pig-origin identification evidence and explicit scope limitation for highly processed leather/hair. Result must be linked to material provenance and authority decision objects.

## 3. Cross-cutting HCP register

- Material origin / supplier approval
- Animal species and slaughter provenance
- High-risk animal-derived ingredients
- Equipment status and shared-line contamination
- Sertu
- Slaughter/stunning
- Receiving
- Loading/unloading
- Seal and chain of custody
- Warehouse state transition
- Retail handling
- Packaging/labelling/claims
- Outsourced provider
- Personnel competence
- Laboratory sample/method validity
- Traceability / recall
- Change control
- Nonconformity / corrective action
- Authority verification

## 4. Audit test library

`DOC-01` document review; `REC-01` record sampling; `SITE-01` site inspection; `INT-01` interview; `TRACE-01` forward/backward trace; `WIT-01` witness; `COMP-01` competence verification; `AUTH-01` authority evidence check; `LAB-01` laboratory evidence/method validity; `CHANGE-01` change-control review; `RECALL-01` withdrawal/recall simulation.

## 5. Authority gate library

`AUTH-AUDIT`; `AUTH-CERT`; `AUTH-LOGO`; `AUTH-MATERIAL`; `AUTH-SERTU`; `AUTH-PROTOCOL`; `AUTH-CHAIN`; `AUTH-OUTSOURCE`; `AUTH-LEGAL`; `AUTH-LAB`; `AUTH-VACCINE`; `AUTH-COMPETENCE`; `AUTH-GOV`.

## 6. Trust-state rule

No result can skip from `PENDING` directly to `VERIFIED` without the required human assessment and authority gates. Laboratory evidence, AI inference, QR codes, blockchain records, manufacturer declarations and platform events are evidence/identity mechanisms, not substitutes for competent-authority certification.
