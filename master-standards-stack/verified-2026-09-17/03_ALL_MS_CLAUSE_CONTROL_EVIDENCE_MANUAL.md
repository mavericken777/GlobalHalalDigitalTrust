# IQ300 All Malaysian Halal Standards - Clause -> Control -> Evidence -> Audit Manual

**Control date:** 17 September 2026  
**Copyright rule:** clause headings and public metadata are used for navigation. Normative text is paraphrased and is not reproduced.  
**Status vocabulary:** `SOURCE-VERIFIED` = controlled source held/verified; `PUBLIC-STRUCTURE-VERIFIED` = official public clause structure verified but full normative wording source-locked; `SOURCE-LOCKED` = exact licensed normative subclauses unavailable to this project snapshot and therefore not fabricated.

## 0. Canonical requirement object

Every row maps to:

`Instrument -> Edition/status -> Clause -> Applicability -> Requirement intent -> Control -> HCP/SCCP -> Evidence -> Audit test -> Failure state -> Corrective action -> Re-verification -> Authority gate -> Trust-state effect`.

Common audit test codes:

- `DOC-01` controlled document review
- `REC-01` transaction/operational record sampling
- `SITE-01` physical site inspection
- `INT-01` personnel interview
- `TRACE-01` forward/backward trace
- `WIT-01` witness activity/process
- `COMP-01` competence/authorization check
- `AUTH-01` authority/certificate verification
- `LAB-01` analytical method/sample/result validity
- `CHANGE-01` change-impact review
- `RECALL-01` trace/withdrawal simulation
- `DATA-01` digital provenance/integrity/access test

---

# 1. MS 1500:2019 - Halal food - General requirements

**Source depth:** `PUBLIC-STRUCTURE-VERIFIED`; current 2019 edition; project baseline records confirmation in 2024.  
**Critical linkage:** slaughter/stunning is maintained through the current JAKIM/DVS Malaysian Protocol and related authority/fatwa/manual controls; do not reintroduce superseded MS 1500:2009 parameters as current 2019 clauses.

| Clause | Public clause heading | Operational control | Evidence | Audit tests | Failure / trust effect |
|---|---|---|---|---|---|
| 1 | Scope | Determine whether product/process/site falls within food standard profile | product/SKU/site/process classification | DOC-01 | wrong profile -> HOLD |
| 2 | Normative references | Resolve current referenced instruments before audit/release | source/version register | DOC-01/AUTH-01 | stale source -> SOURCE-HOLD |
| 3 | Terms and definitions | Apply controlled terminology and authority meanings | ontology/version | DOC-01 | semantic conflict -> RULE-HOLD |
| 4.1 | Management responsibility | Management policy, resources, halal governance, responsibility and documented implementation | policy; organisation; appointment; review records | DOC-01/INT-01/REC-01 | governance failure -> NCR |
| 4.2 | Premises and facilities | Design/location/flow/facilities prevent contamination and support hygiene/halal integrity | layout; zoning; cleaning/pest/waste records | SITE-01/WIT-01 | contamination exposure -> HOLD/QUARANTINE |
| 4.3 | Devices, utensils, machines, processing aids and equipment | Approved halal-compatible status, dedicated/controlled use, cleaning and sertu where triggered | asset register; use history; cleaning/sertu evidence | SITE-01/TRACE-01/AUTH-01 | doubtful/contaminated asset -> HOLD |
| 4.4 | Hygiene, sanitation and food safety | Maintain personnel/process hygiene, sanitation, food-safety and contamination-prevention controls | sanitation plan; hygiene records; water/pest/food-safety records | SITE-01/REC-01 | unsafe/contaminated condition -> HOLD |
| 4.5 | Processing of halal food | Verify material origin/status, process flow, separation, halal HCPs and batch integrity | formula/BOM; supplier/material files; batch record; process flow; HCP monitoring | TRACE-01/WIT-01/DOC-01 | material/process breach -> QUARANTINE |
| 4.6 | Storage, transportation, display, sale and servings | Preserve halal identity and segregation after processing through custody and consumer-facing handling | location/status; transport; storage; display/serving evidence | TRACE-01/SITE-01 | custody/segregation break -> HOLD |
| 4.7 | Packaging and labelling | Packaging material, label, product name, claims and halal-mark usage match approved scope | approved artwork; packaging specification; label inspection | DOC-01/SITE-01/AUTH-01 | misleading/unauthorised claim -> CLAIM-HOLD |
| 4.8 | Legal requirements | Meet applicable law/regulatory prerequisites in addition to halal standard | licences/food approvals/compliance register | AUTH-01/DOC-01 | legal prerequisite failure -> RELEASE-BLOCK |
| 5 | Compliance | Aggregate applicable requirements and evidence into assessment outcome | completed control matrix | AUDIT bundle | unresolved major failure -> NOT-VERIFIED |
| 6 | Halal certificates | Certification state only from competent authority | certificate ID/issuer/scope/validity/status | AUTH-01 | missing/invalid credential -> NO-CERT-CLAIM |
| 7 | Halal certification mark | Logo/mark only when authorised and within exact scope | mark master; label/SKU binding; validity | AUTH-01/SITE-01 | logo misuse -> ESCALATE |
| Annex A | Sertu | Prescribed cleansing lifecycle for applicable najs mughallazah contamination | incident; affected assets; method/source; witness; verification; release | WIT-01/AUTH-01 | incomplete sertu -> QUARANTINE |

### MS 1500 HCP library

`material approval; animal-derived ingredient provenance; slaughter evidence where applicable; shared-line/equipment status; receiving; storage segregation; preparation/processing; rework; packaging/label; finished-batch release; cold-chain where applicable; transport; display/serving; returns/recall; sertu trigger`.

---

# 2. MS 2400-1:2019 - Transportation

**Source depth:** `SOURCE-VERIFIED` from user-supplied licensed PDF.  
**Existing machine-readable coverage:** 187 individually numbered requirement objects in `master-standards-stack/iq300-full-matrix/MS2400-12019_IQ300_REQUIREMENTS.json.gz`.

## 2.1 Clause architecture

| Clause | Control architecture | Minimum evidence / audit |
|---|---|---|
| 1 Scope | transport service applicability and boundary | service profile; modes/routes; scope approval |
| 2 Normative references | live reference set | source/version register |
| 3 Terms/definitions | controlled logistics/halal terminology | ontology |
| 4.1 Shariah requirements | halal/Shariah baseline | requirement profile; authority sources |
| 4.2 Management responsibility | policy, organisation, responsibility/authority, internal halal committee | policy; org; committee minutes; competence |
| 4.3 HMS requirements | documented system, procedures, validation, halal risk plan | HMS; risk register; HCPs; validation; records |
| 4.3.4.1 | identify potential contaminants/precursors and risk | hazard/risk register |
| 4.3.4.2 | define control measures | control plan |
| 4.3.4.3 | determine HCPs | HCP register |
| 4.3.4.4 | monitor HCPs | monitoring record/sensor/inspection evidence |
| 4.3.4.5 | corrective actions | NCR/CAR |
| 4.3.4.6 | verification | verification result |
| 4.3.4.7 | documentation/records | controlled records/retention |
| 4.4 | Halal Risk Management Plan Summary | approved consolidated risk-control summary |
| 4.5 | information/communication system | escalation/contact/data flow evidence |
| 5.1 | process characteristics | inbound/outbound transport description |
| 5.2 | process flow diagram | current verified flow |
| 5.3 | layout plan | transport/depot/loading/storage/personnel layout as applicable |
| 5.4 | chain of custody | consignment identity, next custodian, users/stakeholders, in-transit status, preparation/dispatch, loss/damage, documents, agents/outsourcing |
| 6.1 | transportation services/related activities | trip/service operational records |
| 6.2 | records | record completeness/retrieval |
| 6.3 | nonconformity | contaminated/affected/doubtful goods; corrective action |
| 6.4 | isolation and notification | timely secured isolation, cause/extent/result and effectiveness verification |
| 6.5 | communication | incident/exception notification |
| 6.6 | traceability | shipment/batch/container/custody trace |
| 6.7 | monitoring/measuring equipment | identification, calibration/verification and method suitability |
| 6.8 | emergency preparedness | emergency plan/exercise/incident handling |
| 6.9 | outsourced providers/subcontractors | qualification, control and re-evaluation |
| 7 | premises/infrastructure/facilities/personnel | transport location, design/layout, facilities/equipment/materials, hygiene/health, environment, maintenance, cleaning, sertu, drainage/waste, training, contamination/pest control |
| 8 | maintenance of halal supply chain | internal halal audit, management review, complaints/feedback, responsiveness/change control |
| Annex A-D | HCP worksheet, risk ranking, risk summary, sertu | controlled risk/HCP evidence and sertu lifecycle |

### Transportation HCPs

`vehicle/container previous-use risk; cleaning; sertu; cargo identity; mixed-load segregation; loading; seal; departure; geofence/route; condition/temperature when applicable; door/tamper/opening; custody handoff; damage/loss; proof of delivery; return/backhaul; outsourced carrier status`.

---

# 3. MS 2400-2:2019 - Warehousing

**Source depth:** `SOURCE-VERIFIED`.  
**Existing machine-readable coverage:** 201 requirement objects.

Clauses 1-5 and the management/risk architecture parallel Part 1 but are applied to stationary custody/inventory. Clause 6 is warehouse operations; Clause 7 addresses warehouse premises/infrastructure/facilities/personnel; Clause 8 maintains the system.

### Warehouse control state machine

`EXPECTED -> RECEIVED -> QUARANTINED -> RELEASED -> PICKED -> DISPATCHED`  
Exception branches: `HOLD`, `REJECTED`, `RETURNED`, `DAMAGED`, `SERTU-REQUIRED`, `RECALLED`.

### Warehouse HCPs

`receiving/seal; document identity; packaging integrity; lot/batch; approved supplier/status; quarantine/release; halal/non-halal zoning; pallet/MHE status; spill/breakage; returns; pest/hygiene; environmental/temperature condition; cleaning; sertu; stock rotation; picking; dispatch; third-party warehouse status`.

### Evidence minimum

`ASN/receiving record; batch/lot; seal; zone/bin; status; movement history; environmental record; cleaning/sertu; inventory reconciliation; dispatch record; exception/NCR/CAR; provider qualification`.

---

# 4. MS 2400-3:2019 - Retailing

**Source depth:** `SOURCE-VERIFIED`.  
**Existing machine-readable coverage:** 225 requirement objects.

Clause families apply the common management/risk/HCP architecture to retail receiving, storage, preparation, hot/cold processing where applicable, packaging/assembly, display/merchandising, consumer information, sale/serving, returns and withdrawal/recall.

### Retail HCPs

`approved supplier; receiving/label/status; storage segregation; preparation; hot/cold holding; food-contact surface/utensils; opened packs/samples; display; self-service; staff hygiene; customer-facing claims; return; withdrawal/recall; traceability; cleaning/sertu; outsourced service`.

---

# 5. MS 2424:2019 - Halal pharmaceuticals - General requirements

**Source depth:** `PUBLIC-STRUCTURE-VERIFIED`; current; confirmed 2025.

| Clause | Public heading | Control | Evidence / tests | Gate |
|---|---|---|---|---|
| 0 | Introduction | freeze pharmaceutical/halal regulatory context | source profile | REG-SOURCE |
| 1 | Scope | identify products/sites/processes in scope | product registration/category/site | DOC-01 |
| 2 | Normative references | current refs | version register | DOC-01 |
| 3 | Terms/definitions | pharmaceutical/halal ontology | ontology | DOC-01 |
| 4.1 | Halal pharmaceutical quality system / quality management | embed halal controls in pharmaceutical QMS | QMS/HMS mapping | DOC-01/REC-01 |
| 4.2 | Management responsibility | policy, authority, resources, governance | org/policy/IHC/management review | INT-01/DOC-01 |
| 4.3 | Halal Management System | documented HMS and controlled HCPs | HMS manual/risk/HCP/audits | DOC-01 |
| 4.4 | Fundamentals for halal pharmaceuticals | permitted sources/processes and contamination prevention | material/process provenance | TRACE-01/SITE-01 |
| 4.5 | Halal quality control | halal identity plus pharmaceutical QC | specs/COA/lab/release | LAB-01/DOC-01 |
| 4.6 | Personnel/responsibility | authorised roles and accountability | JD/approval matrix | COMP-01 |
| 4.7 | Training | GMP/halal/HCP/sertu competence | training/assessment | COMP-01 |
| 4.8 | Personal hygiene | hygiene/behaviour controls | hygiene monitoring | SITE-01 |
| 4.9 | Manufacturing premises/equipment | contamination/mix-up prevention and asset status | layout/equipment/cleaning | SITE-01 |
| 4.10 | Manufacturing/storage areas | controlled segregation/status/environment | zone/status/condition | SITE-01/REC-01 |
| 4.11 | Transportation | product/custody/condition integrity | lane/vehicle/shipment evidence | TRACE-01 |
| 4.12 | Quality-control areas | QC area/sample/material integrity | QC layout/access/sample flow | SITE-01 |
| 4.13 | Ancillary areas | ancillary/animal/prayer/personnel area controls | layout/inspection | SITE-01 |
| 4.14 | Documentation | GMP/HMS/material/process evidence control | document register | DOC-01 |
| 4.15 | Manufacturing | batch/process/line-clearance halal integrity | batch records/process witness | WIT-01/TRACE-01 |
| 4.16 | Materials | APIs, excipients, solvents, media, enzymes/process aids, packaging and route provenance | BOM/material dossier/supplier/cert/source | MAT-01/TRACE-01 |
| 4.17 | Packaging/labelling | approved claim/packaging identity | artwork/pack record | DOC-01 |
| 4.18 | Outsourced activities | CMO/lab/packer qualification and control | agreement/audit/quality records | AUTH-01/DOC-01 |
| 4.19 | Self-inspection | internal verification and CAPA | inspection/NCR/CAR | AUD-01 |
| 4.20 | Legal requirements | NPRA/other legal prerequisites remain distinct gates | registration/licence | AUTH-01 |
| 5 | Compliance | aggregate assessment | matrix/outcome | AUTH-AUDIT |
| 6 | Halal certificates | authority credential only | certificate status/scope | AUTH-01 |
| 7 | Halal certification mark | controlled authorised use | artwork/scope | AUTH-01 |
| Annex A | Sertu | asset/process cleansing lifecycle | incident/procedure/verification | SERTU-01 |
| Annex B | Typical vaccine HCPs | biologics dependency/HCP map | seed/cell/media/sera/trypsin/peptone/adjuvant/carrier/culture/harvest/purification/filling/waste evidence | TRACE-01/LAB-01 |

---

# 6. MS 2634:2019 - Halal cosmetics - General requirements

**Source depth:** `PUBLIC-STRUCTURE-VERIFIED`; confirmed 2025; replaces MS 2200-1:2008.

| Clause | Public heading | Control | Evidence / test |
|---|---|---|---|
| 1-3 | Scope / references / terms | determine cosmetic scope; freeze terminology/references | product notification/category/source profile |
| 4.1 | Management responsibility | policy/governance, halal integrity, records, personnel participation | policy/org/review/training |
| 4.2 | Materials | origin/manufacturing route for every INCI/material and process aid | supplier dossier/spec/certificate/source/route |
| 4.3 | Hygiene, sanitation and safety | controlled facility/people/process hygiene and contamination prevention | sanitation/pest/hygiene/site evidence |
| 4.4 | Other aspects in preparation of materials | control pre-processing/preparation and contamination-sensitive operations | process/handling/cleaning records |
| 4.5 | Product manufacturing, handling and distribution | controlled batch/process/storage/distribution and outsourcing | batch genealogy/warehouse/transport/OEM evidence |
| 4.6 | Packaging, labelling and advertising | packaging identity and lawful/approved halal claims | artwork/claim/packaging dossier |
| 4.7 | Other requirements | scheme-specific supporting requirements | applicable evidence profile |
| 4.8 | Legal requirements | cosmetic regulator/legal prerequisites | notification/licence/compliance register |
| 5 | Compliance | aggregate conformity | audit matrix |
| 6 | Halal certificates | competent-authority credential | certificate scope/status |
| 7 | Halal certification mark | authorised mark use | SKU/artwork binding |
| Annex A | Sertu | applicable contamination lifecycle | incident/sertu/verification |

### High-risk cosmetic material graph

`glycerin; stearates; emulsifiers; collagen; gelatin; keratin; placenta/human-derived materials where relevant; lanolin; tallow derivatives; carmine/cochineal; ethanol/alcohol source; enzymes; fermentation media; animal-hair brushes/applicators` -> `source -> supplier -> manufacturing route -> processing aids -> batch -> evidence -> authority status`.

MS 2627-2:2025 may supply analytical evidence where applicable, but analytical result never substitutes for provenance or authority certification.

---

# 7. MS 2636:2019 - Halal medical device - General requirements

**Source depth:** `PUBLIC-STRUCTURE-VERIFIED`; confirmed 2025.

Public clause architecture tracks a regulated-device quality-system model:

`1 Scope; 2 Normative references; 3 Terms/definitions; 4.1 Quality management; 4.2 Management responsibility; 4.3 HMS; 4.4 Fundamentals for halal medical devices; 4.5 Halal quality control; 4.6 Personnel/responsibility; 4.7 Training; 4.8 Personal hygiene; 4.9 Manufacturing premises/equipment; 4.10 Manufacturing/storage areas; 4.11 Transportation; 4.12 QC areas; 4.13 Ancillary areas; 4.14 Documentation; 4.15 Manufacturing; 4.16 Materials; 4.17 Packaging/labelling; 4.18 Outsourced activities; 4.19 Internal audit; 4.20 Legal requirements; 5 Compliance; 6 Halal certificates; 7 Halal mark; Annex A sertu`.

Each clause maps to the same canonical evidence chain used for MS 2424, adapted to device/component/serial or batch identity. Device regulatory registration/conformity remains a separate legal gate.

Key HCPs: `animal-derived component; biological material; lubricant/process aid; cleaning agent; shared equipment; controlled manufacturing; sterilisation/process evidence where applicable; packaging barrier; serial/batch identity; outsourced manufacturing; storage/transport; change control`.

---

# 8. MS 2738:2023 - Halal consumable goods - General requirements

**Source depth:** `PUBLIC-STRUCTURE-VERIFIED`; original/current 2023.

| Clause | Public heading | Control | Evidence / audit |
|---|---|---|---|
| 1-3 | Scope / references / definitions | route product to consumable-goods profile and source versions | product classification/source profile |
| 4.1 | Management responsibility | governance/policy/responsibility | policy/org/review |
| 4.2 | Materials | source/species/origin/manufacturing route and supplier control | material dossiers/trace |
| 4.3 | Hygiene, sanitation and safety in manufacturing/handling | contamination and process hygiene control | site/sanitation/pest/personnel records |
| 4.4 | Product manufacturing, handling and distribution | batch/process/storage/distribution integrity | process/batch/custody records |
| 4.5 | Packaging, labelling and advertising | package/claim/identity control | artwork/label/claim records |
| 4.6 | Other requirements | apply additional product/scheme controls | applicability profile |
| 4.7 | Legal requirements | legal/product prerequisites | licences/approvals |
| 5 | Compliance | evidence aggregation | audit matrix |
| 6 | Halal certificates | competent-authority credential | scope/status |
| 7 | Halal certification mark | controlled mark use | artwork/SKU binding |
| Annex | Annex content is version-controlled against licensed source before operational reliance | source lock | SOURCE-LOCKED |

MS 2738 is the product-level consumer-goods anchor. Animal bone/skin/hair provenance overlays MS 2803; analytical pig skin/hair evidence may overlay MS 2810.

---

# 9. MS 2803:2025 - Usage of animal bone, skin and hair

**Source depth:** official 2025 foreword/revision verified; exact normative numbered clauses `SOURCE-LOCKED` in this snapshot.

Verified revision facts: replaces MS 2200-2:2013; title changed; product requirements removed because MS 2738 covers them.

Until the licensed text is held, IQ300 maps the following mandatory control domains without inventing clause numbers:

| Control domain | Control | Evidence | Audit test |
|---|---|---|---|
| Material identity | classify bone/skin/hair and intended use | specification/BOM/SKU | DOC-01 |
| Species | verified species/source | supplier declaration/certificate/test where relevant | TRACE-01/LAB-01 |
| Origin | country/facility/processor provenance | trace docs | TRACE-01 |
| Slaughter status where applicable | link valid slaughter/halal evidence | recognised credential/process record | AUTH-01 |
| Processing route | map transformations, chemicals and aids | process flow/process-aid list | DOC-01/WIT-01 |
| Segregation | prevent doubtful/prohibited cross-contact | site/warehouse/process evidence | SITE-01 |
| Traceability | source-to-finished-product linkage | lot genealogy | TRACE-01 |
| Analytical support | use MS 2810 or other valid method where question fits method scope | sample/method/result | LAB-01 |
| Product-level requirements | invoke MS 2738/current product standard | applicability record | DOC-01 |

Production status remains `SOURCE-LOCKED` for exact numbered requirement assertions until licensed MS 2803 text is introduced and verified.

---

# 10. MS 2393:2023 - Islamic terminology

**Source depth:** `PUBLIC-STRUCTURE-VERIFIED`; first revision replacing 2013 edition.

Public structure: `1 Scope; 2 Normative references; 3 Terms and definitions; Annex A Transliteration; Annex B Islamic legal rules`.

IQ300 uses MS 2393 as an ontology authority layer, not a certification standard. Every controlled term records canonical term, language, definition source/version, jurisdiction, effective dates, related concepts and interpretation note. Rule engines reference concept IDs rather than hard-coded prose.

Revision-sensitive terminology is never silently overwritten. Historical records retain the edition applicable when the decision/event was made.

---

# 11. MS 2627:2017 - Detection of porcine DNA - Food and food products

**Source depth:** `PUBLIC-STRUCTURE-VERIFIED`.

| Clause | Public heading | Control / evidence logic |
|---|---|---|
| 1 | Scope | confirm food/matrix applicability |
| 2 | Terms/definitions | method ontology |
| 3 | Abbreviations | controlled lab abbreviations |
| 4 | Principle of methods | method principle/version identity |
| 5 | Chemicals, reagents, materials | reagent/material identification, lot/expiry/quality |
| 6 | Preparation of reagents | controlled preparation record |
| 7 | Sampling and preparation | representative sample; chain of custody; contamination prevention |
| 8 | Operating procedure | instrument/method run, controls, extraction/amplification evidence |
| 9 | Expression of results | apply method decision logic; do not translate to halal status automatically |
| 10 | Reporting | report sample/method/result/limitations/authorisation |
| 11 | In-house method validation | demonstrate laboratory implementation performance before reliance |
| 12 | Safety and health precautions | lab safety controls |

Decision rule: `NOT DETECTED != HALAL`. Analytical evidence cannot establish animal slaughter status, supplier provenance, process integrity, sertu completion or competent-authority certification.

---

# 12. MS 2627-2:2025 - Detection of porcine DNA - Part 2: Cosmetics

**Source depth:** current 2025 publication verified; detailed normative numbering `SOURCE-LOCKED` in this snapshot.

Control domains:

`cosmetic matrix identity -> sample chain -> extraction suitability -> inhibition/internal controls -> qPCR method/version -> positive/negative controls -> instrument/run validity -> result -> uncertainty/limitations -> report -> material/batch linkage -> human/authority assessment`.

Cosmetic matrices can create extraction/amplification effects; the engine therefore stores matrix, extraction method and control validity rather than only a binary result.

---

# 13. MS 1900:2025 - Shariah-based quality management system - Requirements

**Source depth:** official preview foreword verified; full normative numbered clause text `SOURCE-LOCKED` unless licensed source is added.

Verified 2025 architecture facts:

- second revision replacing MS 1900:2014;
- modified adoption of OIC/SMIIC 18:2021;
- intended for broader Shariah-based organisational QMS use and explicitly differentiated from the Halal Management System used for Malaysia Halal Certification;
- Malaysian modifications include Maqasid Shariah, stakeholder terminology, `Shariah Executive`, `shariah law and fatwa`, and `Shariah Critical Control Point (SCCP)` terminology.

IQ300 control domains:

`organisation/context -> Shariah governance -> leadership/accountability -> stakeholder/statutory requirements -> planning/risk/opportunity -> Shariah Executive -> SCCP identification/control -> support/competence/awareness -> operational control -> performance evaluation/internal audit/management review -> nonconformity/corrective action -> continual improvement -> Maqasid Shariah governance evidence`.

**Boundary:** MS 1900 compliance must never be rendered as JAKIM product/service halal certification unless the separate Malaysia Halal certification pathway is satisfied.

---

# 14. MS 2691:2021 - Halal profession competency

**Source depth:** `PUBLIC-STRUCTURE-VERIFIED`.

Public structure:

`1 Scope; 2 Normative references; 3 Terms/definitions; 4 Basic requirements for halal profession; 5 Pre-requisite requirements for each level; 6 Personal attributes; 7 Code of conduct; 8 Certificate award and professional development; 9 Upgrade certificate from Halal Expert to Halal Professional`.

IQ300 person object:

`PersonID -> identity -> organisation -> role -> professional level -> prerequisites -> education/training -> experience -> competence assessment -> personal attributes -> code-of-conduct attestation -> certificate/issuer/scope/validity -> CPD -> upgrade history -> suspension/revocation`.

No auditor, Halal Executive, consultant or smart-glass user receives authority solely because an application role is assigned in software.

---

# 15. MS 2610:2015 - Muslim-friendly hospitality services - Requirements

**Source depth:** `PUBLIC-STRUCTURE-VERIFIED`; supporting hospitality context.

Public structure: `1 Scope; 2 Normative references; 3 Terms/definitions; 4 General requirements; 5 Specific requirements; 6 Legal requirements; 7 Compliance`.

The standard applies to Muslim-friendly hospitality service contexts including accommodation/tour-package/tour-guide services within its stated scope. IQ300 routes food production/service halal certification separately to the applicable food/certification instruments where required.

Control families: `service scope; accommodation/service environment; prayer/religious facilitation; food/service interface; staff competence; guest communication; tour/package/guide controls; legal licensing; complaint/feedback; evidence and compliance assessment`.

---

# 16. MS 2809:2025 - Authentication using chemometric techniques

**Source depth:** current 2025 publication/foreword verified; exact numbered normative structure `SOURCE-LOCKED`.

Control domains:

`authentication question -> representative sample -> instrument/quantitative chemical data -> dataset provenance -> preprocessing -> training/validation set -> statistical/chemometric model -> performance/validation -> version/freeze -> prediction/classification -> result/uncertainty -> report -> evidence linkage`.

Model governance is mandatory: training data, feature processing, model version, validation and decision threshold must be preserved. A chemometric classification is evidence, not halal certification.

---

# 17. MS 2810:2025 - Identification of pig skin and hair

**Source depth:** current 2025 publication/foreword verified; exact numbered normative structure `SOURCE-LOCKED`.

Control domains:

`sample/material identity -> applicability -> chain of custody -> preparation -> approved analytical method/version -> controls -> result -> limitations -> report -> link to supplier/material/batch -> authority assessment`.

MS 2810 evidence can support MS 2803/MS 2738 material decisions where method scope is applicable; it cannot independently replace provenance or certification evidence.

---

# 18. Cross-standard applicability engine

For each product/service/site, the platform calculates a layered profile rather than selecting one standard only.

Examples:

### Food manufacturer
`MPPHM 2020 + MHMS 2020 + MS 1500:2019 + applicable legal/food regulation + MS 2400 overlay for controlled logistics + MS 2627 if analytical question arises`.

### Pharmaceutical manufacturer
`MPPHM/MHMS scheme profile + MS 2424:2019 + NPRA/legal gates + MS 2400 logistics + analytical evidence as applicable`.

### Cosmetics
`MPPHM/MHMS + MS 2634:2019 + cosmetic legal prerequisites + MS 2627-2 where applicable + MS 2400 logistics`.

### Consumable goods containing animal skin/hair/bone
`MPPHM/MHMS + MS 2738:2023 + MS 2803:2025 + MS 2810:2025 where analytically relevant + logistics overlay`.

### Organisation-level Shariah QMS
`MS 1900:2025` is a separate organisation-level assurance profile; add halal certification instruments only when the organisation/product/service seeks Malaysia Halal certification.

## 19. Failure-state rules

- `SOURCE-HOLD` - source/version not verified
- `APPLICABILITY-HOLD` - standard/scheme routing unresolved
- `EVIDENCE-INCOMPLETE` - required evidence missing
- `DOUBTFUL` - halal status cannot be established from available evidence
- `HOLD` - operational release stopped pending resolution
- `QUARANTINED` - physical/digital object isolated
- `CORRECTIVE-ACTION` - remediation open
- `RE-VERIFICATION` - corrective evidence under review
- `VERIFIED` - platform control/evidence profile satisfied; not automatically an authority certificate
- `CERTIFIED` - only used when linked to a valid competent-authority credential for exact scope
- `EXPIRED`, `SUSPENDED`, `REVOKED`, `RECALLED`, `DISPUTED` - credential/transaction exception states

## 20. Completion rule

The standards library is complete at the **evidence-accounting level** when every current standard has: edition/status; revision lineage; source depth; applicability; control families; evidence; audit tests; authority boundary; and explicit source locks. Exact copyrighted normative clauses not held under licence are not fabricated to create artificial completeness.