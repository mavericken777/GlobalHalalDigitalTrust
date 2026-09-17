# IQ300 Audit Closure, Traceability and Halal Governance Operating Model

**Control date:** 17 September 2026  
**Source basis:** user-supplied compliance manual, reconciled against the canonical JAKIM/MS source hierarchy and existing source-backed repository controls.

## 1. Purpose

This module converts the useful cross-cutting material in the uploaded compliance manual into executable project controls without importing unsupported clause claims.

It sits above individual product/sector standards and below authority decision layers:

`Authority source -> applicable standard/procedure -> governance -> risk/HCP -> operational evidence -> internal verification -> NCR/CAR -> re-verification -> authority gate -> trust state`.

---

# 2. Halal governance object model

## 2.1 Governance roles

Every organisation in scope shall model, at minimum, the roles actually required by its current certification profile. AHTE stores:

`RoleID, organisation, site, scheme, role type, person, appointment source, effective date, competence evidence, authority level, delegated authority, conflicts, training state, expiry/review state`.

Typical roles include:

- top-management sponsor;
- Halal Executive / designated halal lead;
- Internal Halal Committee members where required;
- quality/regulatory representative;
- production/operations representative;
- warehouse/logistics representative;
- procurement/supplier-quality representative;
- HR/training representative;
- laboratory/technical representative where applicable;
- Shariah advisor/committee only where required by the applicable system/standard or organisation governance model.

The system does not impose the uploaded PDF's proposed committee composition as a universal legal minimum. Applicability is resolved from MHMS/MPPHM/current scheme requirements.

## 2.2 Governance meeting object

`MeetingID -> meeting type -> participants -> quorum rule/source -> agenda -> evidence reviewed -> decisions -> action owners -> due dates -> closure -> approval/signature -> record retention`.

Meeting types:

- routine internal halal governance;
- management/HAS review;
- incident/emergency halal review;
- supplier escalation;
- change-control review;
- recall/withdrawal command review.

## 2.3 Decision rights

Decision rights are explicit. Recommended project matrix:

| Decision | Operational owner | Required review/evidence | Authority dependency |
|---|---|---|---|
| approve supplier/material for internal use | procurement/QA/halal governance | supplier/material dossier and risk assessment | authority recognition/status where relevant |
| release quarantined material | QA/halal authorised role | closure evidence and test/source status | authority direction if case escalated |
| open NCR/CAR | auditor/QA/halal role | objective evidence | no authority gate to open |
| close major halal NCR | accountable management/halal governance | root cause, correction, effectiveness | authority re-verification if required |
| change formula/supplier/process/site | change-control owner | impact assessment | notify/obtain approval when current certification rules require it |
| use halal mark/claim | regulatory/halal authorised role | exact valid credential and approved scope | competent authority |
| release shipment | operations + regulatory gate | product/batch/label/custody/destination evidence | export/import/halal authority gates as applicable |

---

# 3. Controlled-document architecture

The uploaded manual's document hierarchy is adopted as an information-governance model.

## Level 1 - Policies

Examples: halal policy, quality policy, Shariah policy where applicable.

Required metadata:

`owner, approver, version, effective date, communication state, review date, supersedes`.

## Level 2 - Manuals/system descriptions

Examples: HAS/IHCS system manual, facility halal plan, scheme-specific compliance manual.

Required metadata:

`scope, sites, schemes, standards profile, document owner, approval, change history, linked procedures`.

## Level 3 - SOPs/procedures

Examples:

- supplier approval;
- material receipt;
- segregation;
- cleaning/sanitation;
- sertu;
- traceability;
- withdrawal/recall;
- sampling;
- internal audit;
- change control;
- label/claim approval;
- complaints;
- calibration/monitoring equipment;
- nonconformity/CAPA.

## Level 4 - Work instructions/forms/records

Examples:

`receiving checklist, batch record, cleaning log, training attendance, audit worksheet, sample form, lab report, committee minutes, seal record, custody handoff, NCR/CAR form`.

## Level 5 - External controlled sources

Examples:

`Malaysian Standards, JAKIM circulars/protocols, fatwa, licences, recognised-body lists, supplier certificates, regulator letters, destination rules`.

External sources require:

`publisher, document ID, edition/version, publication/effective date, source URL/location, verification timestamp, supersession state, access class`.

---

# 4. Record-retention engine

Retention is a rule object, not a global hard-coded number:

`RecordType -> source rule -> minimum period -> event that starts the clock -> legal/product shelf-life extension -> litigation/incident hold -> destruction approval`.

The uploaded PDF reports a three-year baseline associated with MHMS/MPPHM Pindaan 2026. Until the official 2026 circular is archived in the project corpus, this remains tagged:

`SECONDARY-VERIFIED / PRIMARY-SOURCE-LOCK`.

AHTE therefore supports a configurable `>=3-year` profile but shall source-freeze the exact current authority requirement before certification deployment.

---

# 5. Supplier and material assurance model

## 5.1 Supplier risk classes

### VERY-HIGH

Typical characteristics:

- animal-derived materials;
- slaughter-sensitive inputs;
- gelatin/collagen/capsules;
- enzymes/process aids from uncertain origin;
- fermentation media with complex origin;
- high-risk cosmetics/pharmaceutical excipients;
- materials previously linked to a halal incident.

Minimum control pattern:

`legal entity -> manufacturing site -> exact material -> manufacturing route -> species/origin -> halal evidence -> certificate issuer/status -> supplier audit/risk assessment -> change notification -> batch/lot linkage -> periodic re-verification`.

### HIGH

- single-source critical ingredient;
- compound ingredient with opaque subcomponents;
- flavour/colour/carrier/emulsifier systems;
- materials with significant certificate/route-change risk.

### MEDIUM

- formulated ingredient with good documentation but meaningful source/change risk.

### LOW

- commodity/low-risk material with clear identity/specification and low halal-origin risk.

## 5.2 Frequency rule

The uploaded PDF proposes fixed frequencies. IQ300 instead uses dynamic frequency:

`base risk + certificate expiry + supplier history + change events + complaint/incident + audit performance + destination/customer requirement = verification cadence`.

No fixed annual/on-site cadence is asserted unless the controlling source or contract requires it.

## 5.3 Supplier-change event

Any of these creates a `SUPPLIER-CHANGE-REVIEW` event:

- legal entity/site change;
- formula/specification change;
- manufacturing-route change;
- source-country change;
- certificate issuer/scope/status/expiry change;
- sub-supplier change;
- packaging/contact-material change where relevant;
- adverse test/audit/complaint/recall.

---

# 6. Traceability architecture

## 6.1 Minimum genealogy

`Supplier -> Material -> SupplierLot -> Receipt -> InternalMaterialLot -> FormulaVersion -> ProcessVersion -> Batch -> PackLot -> Pallet -> Container/Shipment -> Importer/Customer -> Warehouse/Retail destination`.

Each edge stores:

`quantity, unit, timestamp, actor, location, source system, evidence reference, integrity hash/signature where applicable`.

## 6.2 One-step-back / one-step-forward is the minimum, not the design ceiling

AHTE maintains full event genealogy wherever data is available. The minimum operational test is that any finished lot can identify relevant source lots and any source lot can identify affected finished lots/customers.

## 6.3 Lot-code control

Lot code must bind to the internal genealogy. Recommended fields:

- manufacturing date/time window;
- line/work centre;
- batch/lot sequence;
- site;
- shift/team where required;
- packaging/rework linkage.

The project does not mandate a specific human-readable format unless a regulator/customer does.

---

# 7. Recall/withdrawal simulation model

The uploaded PDF usefully emphasises regular mock recall but asserts `24 hours` and `>=95%` as if universally regulatory. These thresholds are not promoted without primary-source proof.

## 7.1 Simulation object

`ExerciseID, date/time, scenario, initiator, affected product/batch, trigger, trace-back target, trace-forward target, jurisdictions, quantity reconciliation, time to identify, time to notify, time to contain, unresolved gaps, corrective actions, management review, follow-up verification`.

## 7.2 Project KPIs

Internal performance targets may include:

- trace completeness percentage;
- quantity reconciliation percentage;
- time to determine blast radius;
- time to generate customer/importer list;
- time to open hold/quarantine;
- time to issue decision package;
- unresolved data gaps.

Targets must be labelled `INTERNAL-KPI` unless directly sourced from law/regulator/contract.

---

# 8. Audit-closure control set

The uploaded compliance manual contains a useful 33-item closure checklist. The project converts it into control families instead of copying disputed clause numbering.

## 8.1 Certification-system backbone

- organisation/site/scheme eligibility;
- applicable standards/source profile;
- HAS/IHCS applicability;
- halal policy;
- responsible halal personnel;
- internal governance;
- operational records sufficient for the current authority requirement;
- document/record control.

## 8.2 Product/process baseline

- material/supplier approval;
- halal-risk/HCP identification;
- premises/facility flow;
- equipment status;
- hygiene/sanitation;
- processing integrity;
- segregation;
- storage/transport/display controls;
- packaging/label/claim controls;
- sertu readiness;
- traceability/withdrawal capability.

## 8.3 Sector overlays

- MS 2400 transport/warehouse/retail controls;
- pharmaceutical material/QMS/outsourcing controls;
- cosmetic material-origin/process controls;
- consumable-goods controls;
- animal bone/skin/hair provenance controls;
- analytical testing method/sample/result controls;
- professional competency controls;
- hospitality controls where applicable;
- Shariah-based QMS controls where the organisation adopts/certifies against MS 1900.

---

# 9. NCR/CAR workflow

`Observation -> Evidence -> Requirement/source -> Finding -> Severity/source rule -> Immediate containment -> Affected-scope determination -> Root cause -> Correction -> Corrective action -> Responsible owner -> Due date -> Effectiveness evidence -> Re-verification -> Closure/authority escalation`.

Trust effects may include:

`NO-EFFECT, WATCH, HOLD, QUARANTINE, RELEASE-BLOCK, CORRECTIVE-ACTION, RE-VERIFICATION, CERTIFICATE-STATUS-DEPENDENT, RECALL/WITHDRAWAL`.

---

# 10. Change-control workflow

Every planned or unplanned change is tested against:

`product/SKU -> material -> supplier -> formula -> process -> equipment -> site/layout -> outsourced provider -> lab method -> packaging/label -> logistics route -> certificate scope -> destination registration -> authority notification/approval`.

No change is treated as administratively closed until its affected evidence objects and certifications are reconciled.

---

# 11. Digital Audit Twin minimum dataset

Each audit case contains:

`AuditCaseID, authority/owner, scheme, standard profile, sites, products, clauses/requirements, control tests, sample plan, observations, evidence IDs, findings, CARs, re-verification, decision, certificate/status dependency, timestamps, actors, signatures/hashes, source versions`.

This structure allows the uploaded manual's audit-readiness approach to be operationalised without reproducing copyrighted normative text or importing incorrect clause numbering.

# 12. Completion state

This module closes the repository's prior gap between individual standard maps and day-to-day governance/traceability/audit closure. Exact mandatory frequencies, retention periods, committee composition and recall thresholds remain source-driven rather than hard-coded from secondary literature.