# IQ300 Halal Built-In vs Retrofit Factory Transformation Model

**Control date:** 17 September 2026  
**Source basis:** user-supplied `compliance_manual.pdf`, reconciled with the canonical standards/JAKIM control stack.  
**Use:** manufacturer onboarding, factory transformation planning and [PILOT: Shipment 001] readiness.  
**Boundary:** secondary-source timing/cost claims are not treated as mandatory or universal; actual controls are resolved from the applicable current standards, certification instruments, facility and destination requirements.

## 1. Purpose

The uploaded compliance manual distinguishes two implementation modes:

- `HALAL-BUILT-IN`: controls designed into a new facility/line/product system from inception;
- `HALAL-ASSURED-RETROFIT`: an existing operation is converted or upgraded to meet the applicable halal assurance/certification controls.

AHTE uses the distinction because the evidence, risk, change-control burden and cost profile differ materially.

## 2. Transformation object

`TransformationID -> organisation -> site -> line/process -> product/SKU -> current state -> target certification/scope -> applicable standards -> authority profile -> gap register -> change plan -> owners -> costs -> evidence plan -> audit plan -> target date -> residual risks -> decision gates`.

## 3. Built-In control model

Design-stage requirements are converted into controlled design inputs:

- facility flow and zoning;
- material/people/waste movement;
- dedicated or controlled equipment status;
- storage and quarantine zones;
- receiving/dispatch interfaces;
- cleaning/sertu access and utilities;
- traceability/identity architecture;
- monitoring/calibration points;
- laboratory/sample flow where applicable;
- packaging/label-control workflow;
- staff facilities and religious/operational facility requirements where applicable;
- digital evidence capture/API/device plan;
- logistics loading/seal/custody interfaces.

Design verification occurs before commissioning and is repeated after process/SKU changes.

## 4. Retrofit control model

Retrofit requires a baseline gap assessment against the exact current source profile.

Canonical flow:

`BASELINE -> GAP CLASSIFICATION -> RISK/IMPACT -> CHANGE PLAN -> SUPPLIER/MATERIAL TRANSITION -> FACILITY/EQUIPMENT CONTROL -> DOCUMENT/SOP UPDATE -> TRAINING -> OPERATIONAL RECORD GENERATION -> INTERNAL AUDIT -> NCR/CAR -> RE-VERIFICATION -> AUTHORITY/AUDIT GATE`.

## 5. Gap categories

### Regulatory/source gap

- wrong/outdated standard or procedure;
- missing applicable scheme profile;
- missing certificate/recognition source;
- outdated label/claim rule.

### Material/supplier gap

- supplier lacks acceptable evidence;
- formula/BOM incomplete;
- high-risk animal/fermentation/enzyme/process-aid provenance unresolved;
- current stock remains from the pre-transition source.

### Facility/process gap

- cross-contact/segregation risk;
- shared equipment status unresolved;
- receiving/storage/dispatch flow incompatible;
- contamination/sertu risk;
- monitoring/calibration controls absent.

### Governance/evidence gap

- roles not appointed;
- competence/training incomplete;
- procedures do not match real practice;
- operational records insufficient;
- traceability/recall cannot be demonstrated;
- internal audit/CAR closure incomplete.

## 6. Supplier transition closeout

The uploaded manual correctly highlights residual old-stock risk. IQ300 therefore requires:

`OldSupplier -> LastAcceptedLot -> RemainingQuantity -> StorageLocation -> AffectedFormulas -> LastProductionUse -> FinishedLots -> Depletion/Disposition -> NewSupplierFirstLot -> QualificationEvidence -> ChangeApproval -> Closure`.

A supplier change is not closed merely because a new supplier is approved.

## 7. Equipment and line conversion

Conversion record fields:

`asset ID; previous use; contamination risk; cleaning history; sertu applicability; conversion method; witness/verifier; maintenance/calibration; physical identification; scheduling restriction; product scope; change approval; effective date`.

The uploaded PDF contains a strong claim regarding one-way conversion in a cosmetics context. That claim is **not promoted as a universal production rule** without the controlling licensed clause/authority source. The platform stores any such restriction as a source-linked rule specific to the applicable standard/site/process.

## 8. Documentation-before-audit rule

The project adopts the operational principle that evidence must reflect real implementation, not a last-minute paper system.

Readiness therefore tests:

- dated training records;
- actual material approvals;
- actual batch/receiving/storage records;
- executed internal audit;
- NCR/CAR closure;
- traceability/recall evidence;
- governance meeting/review evidence;
- actual cleaning/sertu records where events occurred;
- source/version control.

Any fixed `three-month` first-application record requirement reported by the uploaded PDF remains `SECONDARY-VERIFIED / PRIMARY-SOURCE-LOCK` until the relevant 2026 JAKIM circular is archived and verified.

## 9. Retrofit change-control object

Every action stores:

`ChangeID; trigger; affected standards/clauses; affected SKUs/materials/assets; risk; owner; planned action; validation; training; evidence required; authority notification/approval requirement; implementation date; old-state disposition; new-state verification; closure approval`.

## 10. Cost model linkage

Transformation costs feed `12_MANUFACTURER_ECONOMIC_AND_MARKET_DECISION_MODEL.md` under:

- equipment/facility modification;
- supplier transition;
- testing;
- training;
- staffing;
- IT/evidence systems;
- certification/regulatory costs;
- inventory write-off/rework;
- downtime;
- logistics requalification.

No generic PDF cost range is used as a budget without quotation/evidence.

## 11. Factory qualification gates

A manufacturer cannot progress to [PILOT: Shipment 001] merely because retrofit work is planned.

Required states:

1. `SOURCE-PROFILE-FROZEN`
2. `GAP-REGISTER-APPROVED`
3. `MATERIALS/SUPPLIERS-QUALIFIED`
4. `FACILITY/EQUIPMENT-CONTROLS-VERIFIED`
5. `GOVERNANCE/COMPETENCE-EVIDENCED`
6. `OPERATIONAL-RECORDS-EVIDENCED`
7. `TRACEABILITY/RECALL-TESTED`
8. `INTERNAL-AUDIT-CLOSED`
9. `AUTHORITY/CERTIFICATION-GATE-SATISFIED` where applicable
10. `SKU/DESTINATION-QUALIFIED`
11. `PILOT-BATCH-RELEASED`

## 12. Digital evidence package

Recommended objects:

- baseline facility survey;
- floor/process flow;
- photo/video evidence;
- equipment/asset register;
- material/supplier transition register;
- change-control register;
- training/competence records;
- SOP/work-instruction versions;
- audit/NCR/CAR records;
- traceability simulation;
- authority/certificate links;
- commissioning/re-verification record.

## 13. Completion state

This module closes the implementation-method gap in the uploaded compliance manual by turning `Halal Built-In` and `retrofit` into controlled factory-transformation pathways tied to standards, evidence, audit closure and Shipment 001 readiness rather than generic time/cost assumptions.
