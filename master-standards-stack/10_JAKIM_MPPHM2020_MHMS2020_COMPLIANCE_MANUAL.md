# IQ300 JAKIM / MPPHM 2020 + MHMS 2020 Compliance Manual

**Repository:** mavericken777/GlobalHalalDigitalTrust  
**Control date:** 17 September 2026  
**Purpose:** operational compliance-control manual for the Global Halal Digital Trust & Trade Ecosystem.

## 0. Compliance position and use rule

This manual converts the current working JAKIM operating instruments into an auditable control architecture. It does **not** reproduce the copyrighted text of MPPHM 2020, MHMS 2020 or Malaysian Standards. Requirement statements below are paraphrased control intents, linked to evidence and system implementation.

JAKIM's official portal currently lists **Malaysian Halal Management System (MHMS) 2020** and **Malaysia Halal Certification Manual Procedure 2020 (MPPHM)** as certification references. JAKIM's 2020 annual report records that MPPHM (Domestic) 2020 was issued under the Trade Descriptions Act 2011 framework and that MHMS 2020 differentiates **IHCS** for micro/small industry from **HAS** for medium/large industry. [JAKIM portal; JAKIM Annual Report 2020]

**Authority boundary:** IQ300 is a trust, evidence, control and decision-support layer. It does not issue Malaysian Halal certification, change a fatwa, replace a competent authority, or convert a laboratory result into certification.

## 1. Master regulatory hierarchy

`Shariah/fatwa -> law/regulation -> competent authority -> MPPHM/MHMS/protocol/circular -> Malaysian Standards -> company controls/HCPs -> evidence -> audit/assessment -> authority decision -> credential/trust state -> supply-chain release -> surveillance/change control`

### Mandatory system rules

| ID | Rule | System consequence |
|---|---|---|
| REG-01 | Authority source must be versioned | No unversioned production rule |
| REG-02 | Standard != certification | Standard conformance cannot be displayed as a JAKIM certificate |
| REG-03 | Lab result != halal decision | Analytical evidence remains one evidence class |
| REG-04 | Current rule controls | Historical/replaced rules remain historical only |
| REG-05 | AI is advisory | AI cannot issue/override authority decisions |
| REG-06 | Physical/digital identity must bind | Product/batch/lot/consignment IDs must be linked to evidence |
| REG-07 | External claims require evidence | Partnership, recognition and certification claims require source records |
| REG-08 | Cross-border sovereignty is explicit | Sovereign source data remains under the relevant custodian |

## 2. MPPHM 2020 procedure-by-procedure control map

### Part I - Permulaan

| Procedure | Control intent | IQ300 evidence / test |
|---|---|---|
| 1 | Identify short title, applicability and legal operating basis | Controlled source record, version, effective date |
| 2 | Maintain abbreviations consistently | Controlled terminology object |
| 3 | Use controlled definitions | Definition record with source and version |

### Part II - Permohonan

| Procedure | Control intent | IQ300 implementation |
|---|---|---|
| 4 | Route applicant into the correct certification scheme | Scheme routing record |
| 5 | Confirm application eligibility and criteria | Eligibility checklist + source evidence |
| 6 | Prevent applications that fall outside permitted criteria | Hard-stop eligibility gate |

**Application dossier minimum model:** company profile/registration; product or service scope; premises/factory information; ingredient/raw-material data; supplier/manufacturer information; halal status of critical inputs; packaging information; process information; relevant certificates; site/layout information; declarations and other documents required by the competent authority.

### Part III - Fees

| Procedure | Control intent | IQ300 implementation |
|---|---|---|
| 7 | Process application-related charges | Fee transaction record |
| 8 | Product/service certification fee | Fee schedule version + payment evidence |
| 9 | Food-premise certification fee | Scheme-specific charge record |
| 10 | Menu/addition fee | Product/menu change transaction |
| 11 | Halal-logo poster printing charge | Controlled artwork/order record |
| 12 | Slaughterhouse certification charges | Slaughter scheme fee record |
| 13 | Reprint certificate | Credential replacement event |
| 14 | Consignment-note charge | Consignment document event |
| 15 | Payment control | Reconciliation + payment status |
| 16 | Fee exemption | Authority-approved exemption record |

### Part IV - Certification requirements

| Procedure | Control intent | Mandatory evidence |
|---|---|---|
| 17 | General certification requirements | Scheme applicability + base dossier |
| 18 | Specific scheme requirements | Scheme control profile + scheme evidence |
| 19 | IHCS | Current IHCS implementation record for eligible small/micro applicants |
| 20 | HAS | HAS manual, policy, Halal Executive, committee, HCP/risk, training, traceability, audit, management review and records for applicable medium/large applicants |

### Part V - Application procedures

| Procedure | Control intent | IQ300 gate |
|---|---|---|
| 21 | New application | Intake -> eligibility -> document sufficiency -> audit readiness |
| 22 | Renewal | Credential continuity -> changes -> surveillance/assessment -> renewal decision |
| 23 | Addition | Scope/product addition linked to current credential and evidence |
| 24 | Combination | Consolidate permitted scopes without losing source lineage |

### Part VI - Auditing

| Procedure | Control intent | IQ300 audit event |
|---|---|---|
| 25 | Audit notification | E-AUDIT-OPEN + notice |
| 26 | Audit scope | ScopeRecord frozen before fieldwork |
| 27 | Adequacy audit | Document/system readiness assessment |
| 28 | On-site audit | Site observations + sample + evidence linkage |
| 29 | Follow-up audit | CAR closure / re-verification evidence |
| 30 | Nonconformity | NCR, classification, containment, CAR, due date, verification |

### Part VII - Monitoring

| Procedure | Control intent | IQ300 control |
|---|---|---|
| 31 | Monitoring types | Monitoring plan by risk and scheme |
| 32 | Monitoring categories | Product/process/premises/credential/risk surveillance categories |
| 33 | Monitoring actions | Maintain, warn, investigate, isolate, corrective action, suspend/cancel/other authority action as applicable |

### Part VIII - Certificate

| Procedure | Control intent | IQ300 implementation |
|---|---|---|
| 34 | Certificate issuance | Only authority-issued credential becomes official certification object |
| 35 | Certificate validity | Start/end date and scope tracked |
| 36 | Certificate/halal mark usage | Usage constrained to approved scope/status |
| 37 | Information amendment | Change-control workflow with authority impact assessment |
| 38 | Lost/damaged certificate | Credential replacement event |
| 39 | Cancellation | Official revocation/cancellation event; downstream release rules triggered |

### Part IX - Halal logo

| Procedure | Control intent | IQ300 implementation |
|---|---|---|
| 40 | Logo form/features | Artwork master and authenticity verification |
| 41 | Logo usage | Scope/claim/channel controls and evidence of authorization |

### Part X - Inspectors

| Procedure | Control intent | IQ300 implementation |
|---|---|---|
| 42 | Appointment | Authorized personnel identity |
| 43 | Authority | Role permissions and mandate |
| 44 | Values/ethics | Impartiality, confidentiality, conduct and conflict controls |

### Part XI - Panel

| Procedure | Control intent | IQ300 implementation |
|---|---|---|
| 45 | Appointment | Panel member identity / appointment |
| 46 | Membership | Composition control |
| 47 | Quorum | Decision-validity test |
| 48 | Authority | Decision boundary |
| 49 | Termination | Membership status / revocation |
| 50 | Subcommittee | Delegated scope |
| 51 | Appeal panel | Appeal decision independence / traceability |

### Part XII - Sampling

| Procedure | Control intent | IQ300 implementation |
|---|---|---|
| 52 | Sample types | Sampling plan and reason |
| 53 | Procedure | Chain of custody from sampling through laboratory result |
| 54 | Cost | Cost responsibility and transaction record |
| 55 | Analysis laboratory | Approved/recognized laboratory status and result provenance |

### Part XIII - Certificate holder obligations

| Procedure | Control intent | IQ300 implementation |
|---|---|---|
| 56 | Law/regulation compliance | Legal register and continuing compliance declaration |

### Part XIV - Miscellaneous controls

| Procedure | Control intent | IQ300 |
|---|---|---|
| 57 | ISPHM / related information | Controlled scheme/reference object |
| 58 | Sertu | Sertu event, method, supervision/verification where required, records |
| 59 | Slaughterer authorization | Competence/authorization object |
| 60 | MyEHALAL information | Application/status-system record |
| 61 | Consignment note | Consignment credential/document object |
| 62 | Procedure-making authority | Source governance record |
| 63 | Islamic finance | Distinct finance-control object; no automatic halal inference |
| 64 | Confidentiality | Data-classification and access policy |
| 65 | Impartiality | Conflict-of-interest controls |
| 66 | Complaints | Complaint intake -> investigation -> resolution |
| 67 | Objection | Formal objection workflow |
| 68 | Appeal | Appeal workflow and decision record |
| 69 | Exemption | Authority-controlled exception record |
| 70 | Authoritative copy | Source hierarchy / canonical copy control |
| 71 | Cancellation | Final credential/status cancellation event |

## 3. MHMS 2020 control manual

### 3.1 Sections 1-4: foundation

**1 Introduction.** MHMS 2020 replaces the earlier halal assurance management-system guidance and defines two implementation modes: IHCS for small/micro industry and HAS for medium/large industry.

**2 Objective.** The system must enable an applicant/holder to establish, implement and maintain halal assurance sufficient to meet Malaysian Halal certification requirements.

**3 Scope.** MHMS applies to authorities and organizations/applicants for the Malaysian Halal Certification System and is read with MS, MPPHM, fatwa, laws, regulations and circulars.

**4 Definitions.** Every production rule must reference a controlled definition source rather than relying on informal platform terminology.

### 3.2 HAS control architecture

| HAS element | Mandatory control artifact | Digital evidence |
|---|---|---|
| HAS Manual | Controlled manual, owner, version, approval | ManualRecord |
| Halal Policy | Signed policy and communication | PolicyRecord |
| Halal Executive | Appointment, role, competency, authority | PersonCredential |
| Internal Halal Committee | Appointment, terms/reference, meetings | CommitteeRecord |
| Internal Halal Audit | SOP, schedule, checklist, reports | AuditRecord |
| Halal Risk Control | Risk analysis, HCPs, monitoring, corrective action | RiskRecord / HCPRecord |
| Raw Material Control | approved supplier/material list, status | MaterialRecord |
| Halal Training | training plan, attendance, competency/effectiveness | TrainingRecord |
| Traceability | forward/backward traceability and recall | TraceabilityRecord |
| HAS Review | periodic management review | ManagementReview |
| Lab Analysis | risk-based lab plan and results | LabResult |
| Sertu | controlled method, execution, authority involvement as required | SertuRecord |
| Documentation / Records | retention, access, integrity, revision | DocumentRecord |

### 3.3 IHCS control architecture

For eligible micro/small organizations, the internal halal control system must still cover at minimum:

1. halal policy;
2. raw material control and halal risk control;
3. traceability.

IQ300 should treat IHCS as a smaller control footprint, not a lower standard of honesty, traceability or evidence integrity.

### 3.4 Specific scheme routing

The MHMS scheme layer is routed against the applicable MPPHM scheme, including food/beverage, cosmetics, pharmaceuticals, consumer goods, medical devices, food premises, slaughterhouse, logistics and contract/OEM contexts as applicable to the current certification framework.

### 3.5 Required HAS evidence package

**Governance:** appointment letters, policy, committee terms, meeting minutes, Halal Executive authority.  
**Material:** master list, supplier list, certificates/status, specifications, change notifications, risk classification.  
**Process:** process flow, layout, HCP plan, risk ranking, controls, monitoring logs.  
**People:** training plan, attendance, competence assessment.  
**Traceability:** lot/batch identity, input-to-output linkage, recall/withdrawal test.  
**Verification:** internal audits, management review, laboratory analysis where required.  
**Sertu:** event and execution evidence where applicable.  
**Records:** controlled versions, retention, retrieval and integrity.

## 4. JAKIM audit-ready evidence architecture

### 4.1 Evidence quality gates

An evidence object is only accepted as audit-ready when it has:

`EvidenceID + source + issuer + object/batch relationship + timestamp + governing rule/version + scope + integrity mechanism + validity/status + access classification.`

### 4.2 Audit sequence

`Application -> adequacy -> on-site -> observations -> findings/NCR -> CAR -> follow-up/re-verification -> panel/authority decision -> certificate/status -> surveillance.`

### 4.3 Finding logic

| Finding state | Action |
|---|---|
| Observation | Record; no release decision based on observation alone |
| Minor/control gap | Corrective action, owner and due date |
| Major/critical or doubtful halal condition | Immediate containment / hold and authority escalation as applicable |
| Confirmed contamination | Isolate affected scope, investigate, apply required cleansing/disposition rules |
| Expired/revoked evidence | Block reliance and revalidate source |

## 5. Sertu boundary

Sertu is a prescribed cleansing control where the applicable contamination condition triggers it. Laboratory-negative evidence cannot substitute for the prescribed cleansing process. The system therefore uses:

`contamination event -> affected asset/lot -> hold/quarantine -> sertu -> execution evidence -> supervision/verification where required -> release decision`

## 6. International factory operating rule

For a Chinese manufacturer seeking a Malaysia-linked or GCC export trust pathway:

- do not imply Malaysian Halal certification before the competent authority decision;
- maintain a separate JAKIM certification status object and factory digital-trust onboarding status;
- freeze the exact manufacturing site, formula/SKU and certification scope;
- map destination-market requirements separately from Malaysian certification requirements;
- preserve sovereign evidence references rather than copying sensitive source files unnecessarily.

## 7. Minimum A-Z audit pack

A. Legal identity  
B. Site identity  
C. Product/SKU list  
D. Ingredients/materials  
E. Supplier controls  
F. Halal credentials  
G. Process flow  
H. HCP/risk plan  
I. Internal audit  
J. Corrective actions  
K. Laboratory evidence  
L. Label/packaging  
M. Management review  
N. Nonconformity/hold  
O. Outsourcing controls  
P. Personnel competence  
Q. Quality/food safety systems  
R. Recall/withdrawal  
S. Sertu  
T. Traceability  
U. Uncontrolled-change detection  
V. Verification  
W. Warehouse/transport interface  
X. Export/import documents  
Y. Year/version control  
Z. Zero-unresolved-critical-gaps gate.

## 8. Source basis

1. JAKIM, Halal Malaysia Portal - current certification page listing MHMS 2020 and MPPHM 2020.
2. JAKIM Annual Report 2020 - launch, legal basis and IHCS/HAS distinction.
3. MPPHM Domestic 2020 working copy / jurisdictional mirror for procedure structure.
4. MHMS 2020 working copy for system-control structure.
5. Supplied MS 2400-1:2019, MS 2400-2:2019 and MS 2400-3:2019 PDFs.
6. Supplied JAKIM halal audit and awareness training PDFs.

## 9. Verification statement

**Verified to the extent supported by the named source set and current web references as of 17 September 2026.** Any future JAKIM circular, protocol, fatwa, portal rule, scheme condition or authoritative standard revision supersedes this operational snapshot for future events and must create a new versioned rule object.
