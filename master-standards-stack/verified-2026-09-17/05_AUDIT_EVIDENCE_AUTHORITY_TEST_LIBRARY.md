# IQ300 Audit, Evidence, Authority and Re-verification Test Library

**Control date:** 17 September 2026  
**Purpose:** convert the JAKIM certification operating layer and Malaysian Standards controls into executable audit/evidence objects without allowing AI or platform state to replace competent-authority decisions.

## 1. Audit doctrine

The system uses an evidence hierarchy:

`SOURCE RULE -> CONTROL DESIGN -> IMPLEMENTATION EVIDENCE -> AUDITOR TEST -> FINDING -> CONTAINMENT -> ROOT CAUSE -> CORRECTIVE ACTION -> RE-VERIFICATION -> AUTHORITY/ACCOUNTABLE DECISION -> TRUST-STATE TRANSITION`.

No single document, certificate image, laboratory result, sensor value or AI inference proves end-to-end halal integrity by itself.

## 2. Audit lifecycle

1. **Scope freeze** - entity/site/product/service/process/standard/scheme/version.
2. **Source freeze** - MPPHM/MHMS/MS/protocol/circular/fatwa/legal version set.
3. **Risk/evidence plan** - HCP/SCCP, material/process/custody risks, sample plan.
4. **Adequacy review** - application and controlled-document sufficiency.
5. **On-site execution** - observe, interview, trace, witness, inspect, sample.
6. **Evidence integrity check** - origin, timestamp, identity, validity, signature, access, tamper indicators.
7. **Finding classification** - affected requirement/object/scope and severity according to controlling authority/system.
8. **Containment** - hold/isolate/stop claim/stop release as required.
9. **Corrective action** - root cause, action, owner, due date, evidence.
10. **Re-verification** - independent check that action addressed cause and scope.
11. **Decision** - accountable auditor/panel/authority according to mandate.
12. **Post-decision monitoring** - surveillance, changes, complaints, recalls and expiration.

## 3. Canonical audit test library

| Code | Test | Execution | Pass evidence | Typical failure |
|---|---|---|---|---|
| DOC-01 | Controlled document review | verify current approved version, scope, owner, approval, effective date | valid controlled source/document | obsolete/unapproved/missing document |
| REC-01 | Record sampling | sample records across time/batches/shifts | complete attributable contemporaneous records | gaps/retrospective completion/inconsistency |
| SITE-01 | Site inspection | inspect physical layout, zoning, equipment, storage, hygiene, identifiers | physical state matches approved control | cross-contact, wrong zone, uncontrolled asset |
| INT-01 | Interview | test role understanding and actual practice | competent consistent responses | staff cannot explain/perform required control |
| TRACE-01 | Forward/backward trace | source -> batch -> shipment and reverse | complete genealogy within defined time | orphan lot/material/custody event |
| WIT-01 | Witness | observe live critical process/HCP/SCCP | execution matches approved SOP/rule | uncontrolled deviation |
| COMP-01 | Competence/authority check | verify appointment, training, scope, validity | competent authorised person | expired/unqualified/unauthorised role |
| AUTH-01 | Authority credential check | issuer, recognition, scope, validity, status | live competent credential | unrecognised/expired/out-of-scope cert |
| MAT-01 | Material qualification | source, supplier, formula/spec, cert, route, change status | approved material dossier | unknown/high-risk source unresolved |
| HCP-01 | HCP control test | monitor criterion/record/action/re-verification | controlled HCP history | unmonitored/out-of-control HCP |
| SCCP-01 | Shariah critical control test | MS1900 profile where applicable | controlled SCCP evidence | unresolved Shariah critical exception |
| LAB-01 | Laboratory evidence test | sample identity, method/version, controls, instrument, result, limitations | valid traceable report | invalid sample/method/control/result |
| CAL-01 | Calibration/verification test | equipment identity, standard, interval, status | valid calibration/verification | overdue/invalid instrument state |
| DATA-01 | Evidence integrity test | hash/signature/source/access/time/version | attributable, tamper-evident evidence | untrusted origin/altered record |
| CHANGE-01 | Change-impact test | supplier/material/process/site/label/equipment/rule changes | approved impact assessment before release | unassessed change |
| RECALL-01 | Trace/withdrawal simulation | identify affected lots/locations/customers and execute hold | complete timely reconciliation | unlocated stock/customer |
| SERTU-01 | Sertu execution test | trigger, containment, rule, procedure, witness/verification, release | fully linked event/evidence | generic cleaning substituted; incomplete scope |
| OUT-01 | Outsourced-provider control | qualification, contract, scope, monitoring, re-evaluation | approved controlled provider | uncontrolled subcontracting |
| CLAIM-01 | Label/logo/claim test | approved artwork vs actual product and credential scope | exact approved match | misleading/expired/out-of-scope claim |
| SHIP-01 | Shipment release test | batch/container/seal/docs/conditions/custody/destination eligibility | complete shipment trust pack | unresolved identity/doc/custody gap |
| PORT-01 | Border/port verification | resolve shipment object, evidence, seal, exceptions, regulatory status | controlled release decision | hold/escalation required |

## 4. Evidence object minimum schema

Every evidence item contains:

`EvidenceID; EvidenceType; SourceOrganisation; SourceSystem; Creator/Issuer; CreatorRole; SubjectType; SubjectID; Product/SKU; Batch/Lot; Site; Jurisdiction; GoverningInstrument; Edition/Version; Clause/RequirementID; CreatedAt; EffectiveAt; ExpiresAt; ReceivedAt; Signature/Attestation; IntegrityHash; OriginalLocation; AccessPolicy; ValidationStatus; Supersedes/SupersededBy; RevocationStatus; AuditID; FindingID; TrustGraphEdges`.

Evidence is never copied into a new system without preserving source lineage. Where sovereignty requires source data to remain in-country, AHTE may retain a signed reference/hash/status object rather than centralising the source payload.

## 5. Evidence strength classes

| Class | Meaning | Examples | Permitted use |
|---|---|---|---|
| E0 | unsupported assertion | verbal/marketing statement without retained evidence | discovery only |
| E1 | primary commercial declaration | manufacturer website, supplier declaration | screening; not final authority proof |
| E2 | controlled organisation record | SOP, batch record, supplier approval, training | operational assessment |
| E3 | independent technical evidence | accredited/competent lab report, calibration record | technical decision support |
| E4 | recognised credential / regulator record | competent certificate, licence, official registration/status | regulatory/authority gate |
| E5 | transaction-native corroboration | signed custody, seal, sensor, border release, importer receipt linked to batch | shipment/end-to-end trust |

A high-strength evidence item does not answer a different requirement. Example: E4 halal certificate does not prove the sealed container was never substituted; E5 seal telemetry does not prove the product formula was halal.

## 6. HCP/SCCP object

`HCP_ID; Standard/Instrument; RequirementID; RiskStatement; Trigger; ControlObjective; ControlMethod; Criterion/Limit where authorised; MonitoringMethod; Frequency; Device/Person; Evidence; ImmediateAction; ProductDisposition; Escalation; Verification; ChangeControl; AuthorityGate`.

Numeric criteria are only stored when verified against the authorised source applicable to the site/species/product/equipment. The platform must not derive legal/Shariah limits from historical documents or secondary summaries.

## 7. Nonconformity object

Minimum:

`NCR_ID; Audit/Event; RequirementID; SourceVersion; FindingStatement; ObjectiveEvidence; AffectedSite; Product/Batch/Asset; Extent; DetectionTime; ImmediateContainment; ProductDisposition; AuthorityNotification; Severity/Category under governing system; Owner; DueDate; Status`.

Severity terminology must follow the competent-authority/current scheme. The platform shall not invent a universal severity vocabulary and project it onto JAKIM or a destination regulator.

## 8. Corrective-action object

`CAR_ID; NCR_ID; RootCauseMethod; RootCause; Correction; CorrectiveAction; Preventive/SystemAction; ResponsibleOwner; DueDate; ImplementationEvidence; ScopeReview; SimilarProcessReview; TrainingChange; DocumentChange; Control/HCPChange; SupplierChange; VerificationPlan; Verifier; Outcome; ClosureDate; RecurrenceMonitor`.

Closure requires evidence that the causal control has been restored, not only that the immediate defect was removed.

## 9. Re-verification rules

Re-verification method is risk-based:

- documentary closure for low-risk administrative corrections where allowed;
- targeted record/sample trace;
- live process witness;
- follow-up site audit;
- new laboratory sample/test;
- authority/technical review;
- repeated trace/recall drill;
- prolonged monitoring window when recurrence risk persists.

The verifier cannot close a requirement outside their authority or competence scope.

## 10. Material evidence engine

Material decision chain:

`MATERIAL ID -> intended use -> supplier -> manufacturer/site -> country -> composition/specification -> species/origin -> manufacturing route -> processing aids/catalysts/enzymes/media -> halal credential/status -> certificate issuer recognition -> validity/scope -> laboratory evidence where relevant -> approved product/SKUs -> receiving lot -> change status`.

High-risk materials include gelatin/collagen, animal fats/derivatives, glycerin/stearates where origin-sensitive, enzymes, fermentation media, capsules, animal-origin colourants and processing aids, animal bone/skin/hair and complex pharmaceutical/biologic inputs.

## 11. Laboratory evidence controls

A valid lab result records:

- exact sample and matrix;
- sampling authority/person/time/place;
- seal/chain of custody;
- receiving condition;
- method and version;
- extraction/preparation method;
- equipment/instrument identity;
- control/blank/reference performance;
- calibration/qualification where applicable;
- raw/derived result lineage;
- interpretation and limitations;
- reviewer/authorisation;
- link to material/product/batch and requirement.

For MS 2627 / 2627-2 and other authentication methods, analytical absence/detection is evidence only. It cannot independently determine slaughter status, source credibility, process integrity or official certification.

## 12. Digital Audit Twin

The Digital Audit Twin holds a time-versioned representation of:

`site -> zones -> processes -> equipment -> people -> materials -> suppliers -> products -> HCP/SCCP -> evidence -> audit observations -> findings -> CAR -> certificates -> custody -> changes`.

A twin snapshot is immutable after the audit decision. Later corrections are appended as new events rather than rewriting the historical audit state.

## 13. Smart-glass / field audit control

Field tooling can:

- identify assets/materials/areas;
- display applicable controls;
- capture time/location-stamped observations;
- link photos/video/voice notes where lawful;
- flag missing evidence/contradictions;
- support trace exercises;
- create draft findings.

It cannot:

- issue halal certification;
- make an unreviewable religious/legal determination;
- overwrite an auditor's accountable decision;
- silently use an outdated rule profile.

## 14. AI evidence-gap and anomaly model

Permitted AI outputs include:

`missing-document likelihood; expiry risk; supplier-certificate mismatch; material/formula contradiction; batch/custody discontinuity; sensor excursion; unusual change frequency; duplicate credential; scope mismatch; label/certificate mismatch; likely untested HCP; recurrence pattern`.

Every AI output records model/version, input references, timestamp, confidence/uncertainty where appropriate and human disposition. AI alerts are never automatically converted into `HALAL` or `NON-HALAL` rulings.

## 15. Authority gate library

| Gate | Meaning |
|---|---|
| REG-SOURCE | controlling source/version validated |
| APP-ELIGIBILITY | applicant/scheme eligibility established |
| MHMS-HAS / MHMS-IHCS | correct internal halal-management profile implemented |
| AUTH-AUDIT | required human audit/assessment completed |
| AUTH-MATERIAL | required material evidence accepted |
| AUTH-SERTU | prescribed sertu verification/release complete where applicable |
| AUTH-PROTOCOL | slaughter/stunning current protocol gate satisfied |
| AUTH-LAB | laboratory evidence accepted for its intended question |
| AUTH-LEGAL | non-halal regulatory prerequisite satisfied |
| PANEL-DECISION | authorised certification decision completed |
| CERT-VALID | exact competent certificate is current and scope-correct |
| DEST-IMPORT | destination importer/product/import eligibility complete |
| SHIP-RELEASE | batch/container/consignment/doc/custody release complete |
| BORDER-RELEASE | destination border authority release recorded |
| RECEIPT-VERIFY | importer/warehouse receiving checks complete |

## 16. Trust state machine

`PENDING -> EVIDENCE-COMPLETE -> ASSESSED -> VERIFIED`.

Exception paths:

`SOURCE-HOLD; EVIDENCE-INCOMPLETE; DOUBTFUL; HOLD; QUARANTINED; CORRECTIVE-ACTION; RE-VERIFICATION; DISPUTED`.

Credential/terminal states:

`CERTIFIED` only when linked to valid competent credential; `EXPIRED; SUSPENDED; REVOKED; RECALLED; REJECTED`.

## 17. Shipment 001 release rule

Shipment 001 cannot proceed from public manufacturer screening directly to release. Minimum release chain:

`manufacturer legal identity -> exact factory -> exact SKU/formula -> current halal credential + issuer recognition for destination -> destination importer/item/label approvals -> commercial PO -> batch production evidence -> quality/halal release -> logistics provider/corridor qualification -> container/seal -> export documents -> custody/telemetry -> destination border/halal/food documents -> border release -> receiving verification -> reconciliation`.

Any missing mandatory gate produces a machine-visible block rather than an inferred pass.