# AHTE 24/7 GHSCL + JAKIM Command Center Specification

## Metadata

- Revision: v1.0.0
- Control date: 2026-09-30
- Classification: post-freeze operating architecture
- Governing topology: `../00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md`
- Companion: `PLATINUM_COMMAND_CENTER_INTEGRATION_ADDENDUM_2026-09-30.md`
- Authority effect: none

[PROPOSAL: establishes command-center operating specification — path point: Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release]

## 1. Mission

Provide a continuously operating command-center layer for the China-origin → GCC-destination trust corridor that can observe, correlate, detect, predict, generate preemptive strategies, assign ownership, escalate, support controlled holds, follow CAPA/re-verification and maintain an auditable operational picture across the complete trust graph.

The Command Center is not a substitute for competent-authority certification, customs release, laboratory competence, manufacturer responsibility, bank credit approval or Takaful underwriting.

## 2. Operator model

### GHSCL

GHSCL is the international operating/digital-infrastructure vehicle responsible for the continuous monitoring/orchestration function.

### JAKIM-connected authority roles

JAKIM is connected through the direct authorised API path according to actual production scope. Authority users receive the visibility/actions granted by their real mandate and interface permissions.

### Other roles

- PHC institutional/industry role;
- appointed auditors;
- laboratory users;
- manufacturer/facility users;
- Sinotrans warehouse/logistics users;
- port/customs users;
- GCC importer/buyer users;
- finance/Takaful users where separately authorised.

## 3. Core operating loop

```text
OBSERVE
↓
INGEST + VALIDATE
↓
CORRELATE OBJECT / EVENT / EVIDENCE
↓
DETECT ANOMALY / CONTRADICTION / FRACTURE
↓
PREDICT RISK / FAILURE
↓
MODEL IMPACT / BLAST RADIUS
↓
GENERATE PREEMPTIVE STRATEGY
↓
POLICY / DECISION-CLASS CHECK
↓
ASSIGN OWNER
↓
ALERT / ESCALATE / APPLY D4 HOLD WHERE AUTHORISED
↓
HUMAN / AUTHORITY ACTION
↓
CAPA / REMEDIATION
↓
RE-VERIFICATION
↓
TRUST-STATE UPDATE
↓
CLOSE / ESCALATE / RECALL
↓
OUTCOME + MODEL/RULE FEEDBACK
```

## 4. Command Center domains

### 4.1 Manufacturer / facility

Monitor:

- onboarding stage;
- facility qualification;
- product/SKU/formula version;
- supplier/material changes;
- evidence freshness;
- HCP/SCCP status;
- production batch state;
- open findings/CAPA;
- audit schedule/status;
- authority/certification status references.

### 4.2 Laboratory

Monitor:

- planned samples;
- collection/seal;
- custody;
- lab receipt/accession;
- testing/QC;
- technical review;
- report/signature/hash;
- evidence acceptance;
- corrected/withdrawn reports;
- re-test requirement.

### 4.3 Smart-glass audit

Monitor:

- assigned audits;
- device/auditor trust;
- site/scope package;
- evidence capture completeness;
- offline queue/reconciliation;
- findings;
- CAR/CAPA;
- re-verification;
- signed audit session.

### 4.4 Sinotrans warehouse

Monitor:

- inbound receipt;
- lot/pallet identity;
- storage zone;
- segregation;
- quarantine/release/reject;
- environment;
- inventory/batch genealogy;
- dispatch;
- warehouse exceptions.

### 4.5 Sinotrans logistics

Monitor:

- booking;
- pickup;
- vehicle/container;
- seal;
- loading;
- route/geofence;
- telemetry;
- custody handovers;
- delays;
- port handoff;
- destination delivery.

### 4.6 Port / customs

Monitor authorised status/events only:

- shipment arrival/receipt;
- container/seal reconciliation;
- inspection/sampling;
- document discrepancy;
- hold;
- release;
- custody transfer.

Sovereign decisions remain with the competent authority.

### 4.7 GCC receiving

Monitor:

- arrival;
- import/inspection status;
- destination authority/importer requirements;
- receiving condition;
- seal check;
- warehouse receipt;
- acceptance/hold;
- retail/distribution progression.

### 4.8 Finance/Takaful

Where separately authorised, display only operational support status such as:

- finance evidence packet ready/requested;
- Takaful underwriting evidence packet ready/requested;
- claim evidence packet opened;
- operational hold affecting finance/insurance prerequisites.

Do not display internal credit/underwriting decisions unless provided by the competent counterparty and authorised for that user.

## 5. Global command views

### 5.1 Corridor map

Map overlays:

- China factory/origin;
- laboratory;
- Sinotrans warehouse;
- current shipment position;
- origin port;
- transit;
- GCC destination port;
- receiving warehouse;
- retail/distribution.

### 5.2 Trust-state matrix

Rows: facilities/products/batches/shipments.

Columns:

- identity;
- authority/certification state;
- AHTE trust state;
- supply-chain state;
- evidence completeness;
- open exceptions;
- CAPA;
- prediction risk;
- last verified;
- owner.

### 5.3 Evidence freshness board

Track:

- expiring authority evidence;
- expiring supplier evidence;
- expiring device/credential/calibration state;
- stale lab evidence;
- stale audit evidence;
- overdue re-verification.

### 5.4 Risk queue

Each row:

`RiskID / Object / Trigger / Prediction / Severity / Confidence / Evidence refs / Recommended preemptive strategy / Decision class / Owner / SLA / Status`

### 5.5 Recall blast-radius explorer

Forward/backward graph traversal:

`material ↔ supplier ↔ batch ↔ lot ↔ pallet ↔ container ↔ shipment ↔ warehouse ↔ retailer/importer`

## 6. Alert taxonomy

Suggested machine-operational alerts:

- `EVIDENCE_MISSING`
- `EVIDENCE_EXPIRING`
- `SUPPLIER_CHANGED`
- `MATERIAL_CHANGED`
- `SAMPLE_MISMATCH`
- `CHAIN_OF_CUSTODY_BREAK`
- `LAB_SCOPE_EXCEPTION`
- `LAB_QC_FAILURE`
- `HCP_EXCEPTION`
- `SCCP_EXCEPTION`
- `AUDIT_FINDING_OPEN`
- `CAPA_OVERDUE`
- `AUTHORITY_STATUS_CHANGE`
- `WAREHOUSE_SEGREGATION_EXCEPTION`
- `INVENTORY_MISMATCH`
- `SEAL_MISMATCH`
- `TAMPER_ALERT`
- `ROUTE_DEVIATION`
- `GEOFENCE_EXCEPTION`
- `TEMPERATURE_EXCEPTION`
- `CUSTODY_GAP`
- `PORT_HOLD`
- `DOCUMENT_DISCREPANCY`
- `DESTINATION_HOLD`
- `RECALL_TRIGGER`

## 7. Severity model

Suggested operational severity:

- S0 — information;
- S1 — advisory;
- S2 — review required;
- S3 — high risk / owner action;
- S4 — policy hold / authority action required;
- S5 — critical / recall or major authority escalation.

Severity is not certification status.

## 8. Decision-class binding

- D0 — ingest/validation;
- D1 — encoded control execution;
- D2 — machine assessment;
- D3 — human finding/CAPA accountability;
- D4 — trust-fracture hold; auto-hold may be configured, auto-release forbidden;
- D5 — competent-authority gate;
- D6 — sovereign/legal.

The Command Center must show the class and next authorised actor for every escalated case.

## 9. Preemptive Strategy Engine

### Inputs

- event history;
- evidence graph;
- trust graph;
- telemetry;
- route/dwell patterns;
- supplier/material changes;
- CAPA recurrence;
- audit findings;
- sample/lab patterns;
- evidence expiry horizon;
- authority-status changes;
- destination requirements.

### Output object

Recommended fields:

```text
StrategyID
PredictionID
SubjectObjects[]
RiskType
PredictedFailure
ExpectedImpact
BlastRadiusRefs[]
EvidenceRefs[]
RecommendedAction
AlternativeActions[]
Urgency
ModelID
ModelVersion
Confidence
Explanation
DecisionClass
RequiredHumanRole
ExpiresAt
Status
OutcomeRefs[]
```

### Examples

- perform re-sampling before a material enters production;
- refresh supplier evidence before expiry;
- reroute a shipment before predicted environmental excursion;
- increase destination inspection after route/seal exception;
- schedule calibration before a high-risk measurement period;
- move stock to compliant warehouse zone;
- pre-stage recall notification/evidence where blast radius is growing;
- add targeted smart-glass checks at a facility with recurring evidence gaps.

## 10. Evidence integrity

Every alert/prediction/strategy must resolve to source events and evidence.

Do not allow model output to overwrite source evidence.

Recommended linkage:

`Alert → TriggerEvent → EvidenceRefs → Prediction → Strategy → Human/Authority Action → CAPA → Reverification → Outcome`

## 11. Role-based views

### GHSCL operator

Broad operational view within contractual/lawful scope.

### JAKIM authorised authority role

Authority-relevant evidence/status, human decision workflow and audit trail according to actual mandate/interface permissions.

### Manufacturer

Own facility/product/material/evidence/CAPA view.

### Laboratory

Sample/method/result/custody scope.

### Sinotrans

Warehouse/logistics/custody/telemetry scope.

### Port/customs

Minimum necessary shipment/trust/inspection/hold/release scope.

### GCC importer/buyer

Destination product/batch/shipment/receiving scope.

### Finance/Takaful

Purpose-specific trust/trade evidence only.

## 12. Data / event requirements

Each command-center event should have:

- stable event ID;
- object refs;
- actor/source system;
- timestamp/time source;
- location where appropriate;
- schema version;
- evidence refs;
- integrity hash/authentication;
- previous-event reference where applicable;
- decision class;
- state transition;
- visibility/access policy.

## 13. Resilience

Target controls:

- high availability;
- regional failover where needed;
- offline/edge buffering;
- durable event storage;
- replay/idempotency protection;
- clock/time reconciliation;
- queue backpressure;
- alert de-duplication;
- correlation recovery;
- audit trail;
- key/credential rotation;
- incident response;
- read-only degraded mode if external authority/partner APIs fail.

The system must never show a dependency failure as an implied approval/success.

## 14. UX acceptance criteria

The Command Center is incomplete unless it can demonstrate:

1. China→GCC corridor map;
2. object-level trust state;
3. separate authority/certification and supply-chain states;
4. lab/sample pipeline;
5. HCP/SCCP exceptions;
6. smart-glass findings;
7. Sinotrans warehouse/logistics;
8. container/seal/telemetry;
9. port/customs events;
10. GCC receiving;
11. predictive risk queue;
12. preemptive strategies;
13. D4 hold and human release rule;
14. CAPA/re-verification;
15. recall blast-radius traversal;
16. evidence/source drill-down;
17. role-based disclosure;
18. full audit timeline.

## 15. Production boundary

A UI prototype or synthetic event stream is not proof that the live JAKIM, Sinotrans, laboratory, port/customs, GCC or finance systems are connected.

Production status requires implemented authentication, partner/authority permissions, real data contracts, persistence, auditability, security testing, availability controls and transaction-native evidence.
