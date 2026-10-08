# JAKIM MPPHM 2020 + MHMS 2020 Operational Compliance Control Manual

**Control date:** 17 September 2026  
**Use:** operational control architecture; not a reproduction of the copyrighted source instruments.

## 1. Authority architecture

Malaysia Halal certification is implemented through the competent Islamic authorities, with JAKIM and State Islamic Religious Departments/authorities operating within the Malaysian framework. The digital platform shall model the competent authority actually responsible for the application, audit, decision, certificate and surveillance event rather than flattening all actors into one generic issuer.

JAKIM's current operating baseline continues to use:

- Manual Prosedur Pensijilan Halal Malaysia (Domestik) 2020 (`MPPHM 2020`);
- Malaysian Halal Management System 2020 (`MHMS 2020`);
- applicable Malaysian Standards;
- protocols, circulars, fatwa and applicable legislation;
- MYeHALAL and current digital certification services.

JAKIM's 2020 annual report records the launch of MPPHM 2020 and MHMS 2020 on 29 October 2020. It also records MHMS differentiation between **IHCS** for micro/small industry and **HAS** for medium/large industry.

## 2. MPPHM 2020 - full procedure/control map

The procedure headings below are used as a navigational/control index. Requirement wording is paraphrased. Exact operative wording remains controlled by the authoritative current source.

### Part I - preliminary

| No. | Procedure family | IQ300 control intent | Minimum evidence / audit test | Authority gate |
|---:|---|---|---|---|
| 1 | Short title / applicability | Freeze manual identity, scope and applicable applicant category | source/version register; applicability decision | REG-SOURCE |
| 2 | Abbreviations | Canonical abbreviation dictionary | ontology/version record | REG-ONTOLOGY |
| 3 | Definitions | Bind certification terms to controlled definitions | terminology objects; conflict check against MS 2393/current authority use | REG-ONTOLOGY |

### Part II - Malaysia Halal certification application

| No. | Procedure family | Control intent | Evidence / test | Gate |
|---:|---|---|---|---|
| 4 | Certification schemes | Select correct scheme before requirements are calculated | legal entity, activity, product/service category, site/scope | APP-SCHEME |
| 5 | Application criteria | Verify applicant meets threshold/eligibility conditions | business registration, licences, operational site, product/service readiness | APP-ELIGIBILITY |
| 6 | Ineligible applications | Prevent non-qualifying application from entering certification workflow | rejection reason; rule/version; decision record | APP-REJECT |

### Part III - fees and charges

| No. | Procedure family | Control intent | Evidence | Gate |
|---:|---|---|---|---|
| 7 | Processing fee | Calculate and evidence applicable processing fee | fee assessment/invoice/payment | FEE-PAID |
| 8 | Products/services fee | Apply scheme/scope fee logic | scope count, invoice, payment | FEE-PAID |
| 9 | Food-premise fee | Apply premise category fee logic | premise profile, invoice | FEE-PAID |
| 10 | Menu addition fee | Control post-approval menu/scope additions | change request; fee; approval | CHANGE-APPROVED |
| 11 | Halal-poster printing | Control approved poster issuance | approved request/issuance record | CERT-DOC |
| 12 | Slaughterhouse fee | Apply slaughterhouse-specific assessment | facility/site/slaughter line scope | FEE-PAID |
| 13 | Certificate reprint | Control replacement/reprint; preserve prior credential lineage | reason, cancelled/replaced credential, reissue record | CERT-REISSUE |
| 14 | Consignment note | Control consignment-document fees/issuance where applicable | shipment identity; application; document | SHIPMENT-DOC |
| 15 | Payment | Verify payment before relevant processing gates | payment evidence/reconciliation | FEE-PAID |
| 16 | Fee exemption | Permit exemption only under authorised rule | authority approval and basis | FEE-EXEMPT |

### Part IV - Malaysia Halal certification requirements

| No. | Procedure family | Control intent | Evidence / test | Gate |
|---:|---|---|---|---|
| 17 | General requirements | Build universal applicant control set: legal status, halal integrity, operational control, traceability, claims and current regulatory compliance | master compliance file; site and document audit | REQ-GENERAL |
| 18 | Specific requirements | Overlay scheme-specific requirements and applicable MS/protocols | standards profile; product/service scope; HCPs | REQ-SPECIFIC |
| 19 | IHCS | Require the appropriate internal halal control structure for micro/small industry | policy, material control, risk control, traceability and required IHCS records | MHMS-IHCS |
| 20 | HAS | Require full Halal Assurance System where applicable | HAS manual; Halal Executive; IHC; audit/risk/material/training/traceability/review/lab/sertu/records | MHMS-HAS |

### Part V - application types

| No. | Application | Control intent | Evidence / test | Gate |
|---:|---|---|---|---|
| 21 | New application | Create new certification object and complete full eligibility/evidence workflow | complete application dataset | APP-NEW |
| 22 | Renewal | Prevent certificate lapse; reassess changes and continued conformity | current certificate; change log; updated evidence | APP-RENEW |
| 23 | Addition | Apply impact assessment to added product/menu/site/scope item | change request; formula/material/process/label evidence | APP-ADD |
| 24 | Consolidation | Merge eligible certification scope without losing provenance/history | relationship map; certificate lineage; authority approval | APP-CONSOLIDATE |

### Part VI - audit

| No. | Audit stage | Control intent | Evidence / test | Gate |
|---:|---|---|---|---|
| 25 | Audit notification | Define audit scope, team, timing and applicant readiness | notification; audit plan; scope | AUDIT-PLANNED |
| 26 | Audit scope | Freeze schemes/sites/products/processes/records to be tested | audit scope object | AUDIT-SCOPE |
| 27 | Adequacy audit | Test application/document sufficiency before site stage | company profile; site; product; ingredients; supplier/manufacturer; halal cert/specification review | AUDIT-ADEQUACY |
| 28 | Site audit | Gather objective evidence of actual implementation | observation, interview, document/record sample, trace, HCP witness | AUDIT-SITE |
| 29 | Follow-up audit | Verify closure of required findings or residual risk | CAR evidence; targeted site/doc verification | AUDIT-FOLLOWUP |
| 30 | Nonconformity | Classify, contain, correct, verify and escalate findings | NCR; root cause; CAR; due date; re-verification | NCR-CLOSED |

Project-supplied JAKIM halal-audit training reinforces the audit sequence: adequacy review -> on-site inspection -> follow-up -> management/panel review, and identifies ingredient/source, production process, contamination control, supply-chain, hygiene/personnel and internal halal controls as core audit evidence domains.

### Part VII - monitoring / surveillance

| No. | Procedure family | Control intent | Evidence | Gate |
|---:|---|---|---|---|
| 31 | Monitoring types | Schedule risk-appropriate surveillance after certification | surveillance plan/events | SURVEILLANCE |
| 32 | Nonconformity categories | Use authority-defined severity/category to drive response | finding classification and evidence | NCR-SEVERITY |
| 33 | Action on monitoring findings | Apply hold/suspension/cancellation/correction pathway as authorised | action record, affected scope, authority decision | CERT-STATUS |

### Part VIII - Malaysia Halal Certificate (SPHM)

| No. | Procedure family | Control intent | Evidence | Gate |
|---:|---|---|---|---|
| 34 | Issuance | Issue credential only after authority approval | panel/authority decision; credential data | CERT-ISSUE |
| 35 | Validity | Maintain effective/expiry status and renewal window | effective/expiry dates | CERT-VALID |
| 36 | Conditions of use | Constrain certificate use to approved holder/site/scope | scope-binding; use monitoring | CERT-USE |
| 37 | Amendment | Version controlled changes only after authority approval | amendment reason, old/new scope | CERT-AMEND |
| 38 | Lost/damaged certificate | Replace while preventing duplicate active credentials | incident/reissue/cancellation lineage | CERT-REISSUE |
| 39 | Cancellation | Terminate credential and propagate status to all dependent trust objects | authority cancellation; effective time; reason | CERT-CANCEL |

**Digital overlay:** JAKIM announced e-Certificate implementation from 5 May 2025 for approved applications within the announced scope. AHTE stores the authority credential reference/status; it does not generate a substitute certificate.

### Part IX - Malaysia Halal logo

| No. | Procedure family | Control intent | Evidence | Gate |
|---:|---|---|---|---|
| 40 | Logo form/features | Validate approved logo representation only | artwork master; issuer/status | LOGO-MASTER |
| 41 | Logo usage | Ensure use only on approved scope and while credential valid | SKU/menu/site mapping; label inspection | LOGO-USE |

### Part X - inspectors / auditors

| No. | Procedure family | Control intent | Evidence | Gate |
|---:|---|---|---|---|
| 42 | Appointment | Verify auditor/inspector appointment and scope | appointment/role/validity | PERSON-AUTH |
| 43 | Authority/powers | Restrict actions to authorised mandate | role-based permission matrix | PERSON-AUTH |
| 44 | Values/ethics | Record impartiality, confidentiality and conduct obligations | declarations; conflict-of-interest record | PERSON-ETHICS |

### Part XI - verification / certification panel

| No. | Procedure family | Control intent | Evidence | Gate |
|---:|---|---|---|---|
| 45 | Panel appointment | Verify authorised decision body | appointment/term | PANEL-AUTH |
| 46 | Membership | Enforce composition requirements | member profile/role | PANEL-COMPOSED |
| 47 | Quorum | Prevent decision without required quorum | attendance/quorum evidence | PANEL-QUORUM |
| 48 | Authority | Bind decision scope and action to formal mandate | decision/authority reference | PANEL-DECISION |
| 49 | Termination | Revoke panel role cleanly | termination record | PANEL-ROLE-END |
| 50 | Subcommittee | Control delegated review activity | delegation/scope/output | PANEL-DELEGATE |
| 51 | Appeal panel | Keep appeal decision path independent and auditable | appeal record/panel decision | APPEAL-DECISION |

### Part XII - sampling and laboratory analysis

| No. | Procedure family | Control intent | Evidence | Gate |
|---:|---|---|---|---|
| 52 | Sample types | Select sample based on identified evidence question/risk | sample plan | SAMPLE-PLAN |
| 53 | Sampling procedure | Preserve identity, integrity and chain of custody | sample ID, collector, seal, time/location, custody | SAMPLE-CUSTODY |
| 54 | Cost | Attribute authorised laboratory/sampling costs | invoice/payment record | LAB-FEE |
| 55 | Analysis laboratory | Use competent/authorised laboratory and appropriate method | laboratory status; method/version; controls; result | LAB-VALID |

Laboratory evidence is supporting evidence. A negative porcine-DNA result does not by itself establish halal status or substitute for source/process/certification evidence.

### Part XIII - certificate-holder responsibilities

| No. | Procedure family | Control intent | Evidence | Gate |
|---:|---|---|---|---|
| 56 | Legal/procedural compliance | Maintain continuing conformity with current halal, safety and regulatory requirements | compliance register; surveillance; change control | HOLDER-COMPLIANT |

### Part XIV - miscellaneous controls

| No. | Procedure family | Control intent | Evidence | Gate |
|---:|---|---|---|---|
| 57 | ISPHM / certification information system | Maintain authoritative digital application/certification record linkage | system reference, access log | SYSTEM-AUTH |
| 58 | Sertu | Trigger prescribed cleansing lifecycle for applicable najs mughallazah contamination | contamination event; hold; procedure; witness/verification; release | SERTU-CLOSED |
| 59 | Slaughterer accreditation | Verify slaughterer competence/authorisation where applicable | credential/competence/status | SLAUGHTER-PERSON |
| 60 | MYeHALAL data update | Maintain current applicant/scope/data state | change log/system confirmation | SYSTEM-CURRENT |
| 61 | Consignment note | Bind consignment credential/document to exact shipment | shipment/container/batch/document | SHIPMENT-DOC |
| 62 | Power to make procedures | Track authorised procedural changes as regulatory source events | new instruction/version/effective date | REG-CHANGE |
| 63 | Islamic finance | Apply Islamic-finance requirement where instrument invokes it | financing product/approval evidence | FINANCE-GATE |
| 64 | Confidentiality | Enforce access, disclosure and retention controls | access policy/logs | DATA-CONF |
| 65 | Impartiality | Identify and manage conflict/bias | COI declarations, segregation of duties | GOV-IMPARTIAL |
| 66 | Complaints | Log, investigate, decide and close complaints | complaint/case/evidence/outcome | COMPLAINT-CLOSED |
| 67 | Objection | Preserve formal objection route | objection, review, decision | OBJECTION-DECISION |
| 68 | Appeal | Preserve appeal route and independent decision | appeal, panel, decision | APPEAL-DECISION |
| 69 | Exemption | Permit only explicit authorised exemption | approval, basis, scope, validity | EXEMPTION |
| 70 | Authentic copy | Control official-copy authenticity and lineage | source/signature/reference | DOC-AUTHENTIC |
| 71 | Cancellation / supersession of procedure | Close superseded procedure versions without erasing history | source-version status | REG-SUPERSEDED |

### Part XV - annex control set

The controlled annex families include application/name restrictions, scheme-specific determination aids, stunning guidance, certification flow, authority contacts, raw-material summaries, certificate/consignment formats and other operating templates. Annex content must be versioned with the manual because operational parameters may change without changing a product standard.

## 3. MHMS 2020 - HAS control architecture

The full HAS control model is implemented as thirteen linked management objects:

| # | HAS element | Operational control | Required evidence | Audit test |
|---:|---|---|---|---|
| 1 | HAS manual | Controlled manual describes system, scope, roles and procedures | approved manual/version | DOC-01 |
| 2 | Halal policy | Management-approved halal commitment communicated and implemented | signed policy; communication | DOC-01/INT-01 |
| 3 | Halal Executive | Competent designated executive with authority/resources | appointment, competence, training | COMP-01/INT-01 |
| 4 | Internal Halal Committee | Cross-functional governance, decisions and escalation | TOR, membership, minutes, actions | DOC-01/REC-01 |
| 5 | Internal halal audit | Planned independent checks and closure | audit plan/report/NCR/CAR | AUD-01/CAR-01 |
| 6 | Halal risk control | Identify risk, controls and HCPs; monitor and correct | risk register/HCP monitoring | RISK-01/HCP-01 |
| 7 | Raw-material control | Supplier/material approval, certificate/spec/source and change control | approved-material register, supplier files | MAT-01/TRACE-01 |
| 8 | Halal training | Role-based awareness and competence | matrix, attendance, assessment | COMP-01 |
| 9 | Traceability | Forward/backward linkage and recall capability | batch genealogy, trace test | TRACE-01/RECALL-01 |
| 10 | HAS review | Management/system review and improvement | review minutes/actions/KPIs | GOV-REVIEW |
| 11 | Laboratory analysis | Risk-based testing with valid sample/method/result handling | sample chain, report, method/version | LAB-01 |
| 12 | Sertu | Controlled procedure for applicable contamination | incident, procedure, verification, release | SERTU-01 |
| 13 | Documentation and records | Controlled creation, approval, revision, retention and retrieval | document register/version/access | DOC-CTRL |

## 4. MHMS 2020 - IHCS control architecture

IHCS is not `HAS-lite` by arbitrary platform choice; it is the authority-defined internal control route for the relevant smaller industry category. The engine maintains a separate profile and calculates only the controls actually required by the current authority instrument.

Core IHCS control domains include:

- halal policy/commitment;
- raw-material approval and halal-risk control;
- process/contamination control;
- traceability and product identification;
- record retention;
- change/escalation to the competent authority where required.

## 5. Current digital overlays

### 5.1 MyHALALINGREDIENTS

JAKIM announced MyHALALINGREDIENTS effective **15 August 2025**. The system records and evaluates raw materials used by industry and is integrated with MYeHALAL. IQ300/AHTE therefore treats raw-material master data as a first-class integration object:

`MATERIAL -> SUPPLIER -> MANUFACTURER -> COUNTRY -> SPECIFICATION -> HALAL EVIDENCE -> CERTIFICATE ISSUER -> VALIDITY -> PRODUCT/SKU USE -> CHANGE EVENT -> AUTHORITY/DIGITAL REFERENCE`.

### 5.2 e-Certificate

JAKIM announced Malaysia Halal e-Certificate implementation from **5 May 2025** for approved applications under the announced scope. AHTE stores e-Certificate identifiers/status and cryptographic/integrity references where available; it does not mint or simulate the authority credential.

## 6. End-to-end certification state machine

`CANDIDATE -> ELIGIBILITY -> APPLICATION -> FEE/ADMIN COMPLETE -> ADEQUACY AUDIT -> SITE AUDIT -> FINDINGS/CAR -> FOLLOW-UP -> PANEL/AUTHORITY DECISION -> CERTIFICATE ISSUED -> ACTIVE/SURVEILLANCE -> RENEWAL/CHANGE -> SUSPENDED/CANCELLED/EXPIRED`.

Every transition records actor, authority, time, source/version, evidence, affected scope and reason.

## 7. AHTE object mapping

| Operating object | Required fields |
|---|---|
| CertificationApplication | applicant, scheme, site, scope, status, dates, source version |
| RequirementProfile | MPPHM/MHMS/MS/protocol/circular/fatwa/legal references |
| Material | identity, supplier, source/origin, specification, certificate, validity, approved uses |
| HCP/SCCP | risk, control, limit/criterion where applicable, monitor, owner, evidence, action |
| Audit | type, scope, team, evidence plan, observations, findings, outcome |
| NCR | class, affected object, evidence, containment, root cause, CAR, due date |
| CAR | owner, action, evidence, completion, verifier, outcome |
| Certificate | issuer, identifier, scope, issue/expiry, status, replaced-by/revoked state |
| SurveillanceEvent | trigger, scope, evidence, decision, next action |
| RegulatorySource | issuer, instrument, version, effective date, supersession, source URI/hash |

## 8. Certification truth rule

A platform state such as `VERIFIED` means the platform's defined evidence/control gates are satisfied. It must never be rendered to a user as `Malaysia Halal Certified` unless a valid competent-authority credential for the exact holder/site/product/service scope is linked and current.