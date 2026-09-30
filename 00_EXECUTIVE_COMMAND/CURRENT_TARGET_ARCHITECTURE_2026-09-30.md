# Current Target Architecture — 30 September 2026

## Artifact metadata

| Field | Value |
|---|---|
| Artifact | `CURRENT_TARGET_ARCHITECTURE_2026-09-30.md` |
| Folder | `00_EXECUTIVE_COMMAND/` |
| Revision | v1.0.0 |
| Control date | 2026-09-30 |
| Classification | Post-freeze target architecture consolidation |
| Freeze impact | None — `master-standards-stack/verified-2026-09-17/` remains immutable |
| Authority effect | None by itself; this file records project target architecture and source precedence |
| Supersedes | Conflicting project-level architecture statements dated before 2026-09-30, except frozen verified source artifacts and explicit competent-authority instruments |

[PROPOSAL: consolidates current target architecture — path point: Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release]

## 1. Governing project topology

The project is a **Global Halal Digital Trust & Trade / Halal Tayyib infrastructure**, not a certificate database and not a standalone blockchain application.

The operating topology is:

```text
MALAYSIAN HALAL GOVERNANCE / AUTHORITY PLANE
        │
        ├── JAKIM
        │     └── Direct authorised JAKIM API connection
        │
        └── PHC
              Perak State Government halal-industry GLC
              local + international industry role

GLOBAL HALAL SUPPLY CHAIN LIMITED — HONG KONG
        │
        ├── International operating / digital-infrastructure vehicle
        ├── China → GCC corridor orchestration
        ├── Ecosystem integration
        └── 24/7 Command Center operating function
                │
                v
               AHTE
    Standards / Evidence / Compliance / Traceability / Trust Intelligence
                │
        ┌───────┼────────┬──────────┬─────────────┐
        │       │        │          │             │
     China   Laboratory Factory   Sinotrans    Port/GCC
     origin   evidence   systems   logistics    interfaces
        │       │        │          │             │
        └───────┴────────┴──────────┴─────────────┘
                │
        Continuous attributable evidence
                │
        Cryptographic integrity anchoring
                │
       AI/ML predictive assurance
                │
       Preemptive strategy generation
                │
       24/7 human command-center oversight
                │
      Direct JAKIM API / authority workflow
                │
         Human authority decisions
                │
          Trust-state propagation
                │
           China → GCC release
```

## 2. Non-negotiable role separation

The following roles are connected but must not be collapsed:

`PHC ≠ GHSCL ≠ AHTE ≠ laboratory ≠ Sinotrans ≠ port/customs authority ≠ AI ≠ competent-authority decision`

- **PHC** is the Perak State Government halal-industry GLC operating locally and internationally within the project ecosystem.
- **GHSCL Hong Kong** is the international operating and digital-infrastructure vehicle.
- **AHTE** is the continuous standards, evidence, traceability, compliance and trust-intelligence layer.
- **JAKIM API** is the direct authority-system connectivity path specified for this project. Public and technical materials must not insert an unnecessary generic intermediary between AHTE and JAKIM where the intended topology is direct API connectivity.
- **Laboratories** create analytical evidence within their authorised/qualified scope; laboratory evidence does not independently create Halal certification.
- **Sinotrans** provides end-to-end logistics and warehouse execution plus real-time custody/telemetry evidence through integration with existing systems.
- **Port/customs authorities** retain sovereign statutory authority. AHTE provides an API/trust-resolution interface but does not create port/customs release decisions.
- **AI/ML** performs monitoring, analytics, anomaly detection, prediction and strategy recommendation subject to decision-class controls.
- **Formal authority decisions** remain human/competent-authority decisions under the applicable framework.

## 3. Canonical physical chain

Default corridor: **China → GCC direct**.

Malaysia is the governance/assurance plane unless a physical Malaysia movement is separately scoped. Do not describe the default Shipment 001 route as China → Malaysia → GCC.

```text
VERIFIED RAW-MATERIAL ORIGIN
↓
SUPPLIER / PRODUCER
↓
IDENTITY / PROVENANCE / LOT
↓
SAMPLE + SEAL + CHAIN OF CUSTODY
↓
CHINA LABORATORY SYSTEM
↓
SIGNED SCIENTIFIC EVIDENCE
↓
RAW-MATERIAL RELEASE / HOLD
↓
MANUFACTURER / FACTORY
↓
ERP / MES / QMS / WMS / LIMS / IoT / DMS / IDENTITY
↓
PRODUCT / FORMULA / BOM / PROCESS
↓
APPLICABLE STANDARDS + REQUIREMENTS
↓
HCP / SCCP / CONTROLS
↓
SMART-GLASS AI-ASSISTED SITE AUDIT
↓
FINDING / CAR / CAPA
↓
RE-VERIFICATION
↓
DIRECT JAKIM API / HUMAN AUTHORITY WORKFLOW
↓
FORMAL DECISION / AUTHORITY STATUS
↓
AHTE TRUST-STATE PROPAGATION
↓
PACKAGING / BATCH / LOT / PALLET
↓
SINOTRANS WAREHOUSE
↓
SINOTRANS END-TO-END LOGISTICS
↓
CONTAINER / SEAL / TELEMETRY / CUSTODY
↓
ORIGIN PORT / CUSTOMS API INTERFACE
↓
EXPORT / LOADING
↓
INTERNATIONAL TRANSIT
↓
GCC PORT / CUSTOMS API INTERFACE
↓
DESTINATION INSPECTION / RELEASE
↓
IMPORTER / DESTINATION WAREHOUSE
↓
DISTRIBUTION / RETAIL
↓
BUYER / CONSUMER AUTHORISED VERIFICATION
```

[PILOT: Shipment 001 — first controlled China→GCC proof-of-execution]

Shipment 001 remains uninstantiated until transaction-native evidence exists.

## 4. Four synchronized trust chains

Every operational design must preserve four synchronized chains:

1. **Physical chain** — raw material → factory → warehouse → logistics → port → GCC.
2. **Identity/custody chain** — actor → facility → product → batch → sample → pallet → container → seal → handover.
3. **Evidence chain** — certificates/references → laboratory → process → HCP/SCCP → audit → CAPA → telemetry → custody → receiving.
4. **Authority/trust-state chain** — direct authority status/decision → AHTE trust state → operational release/hold/quarantine/recall.

Minimum material event tuple:

`WHO + WHAT + WHEN + WHERE + OBJECT + REQUIREMENT/CONTROL + EVIDENCE + VERIFIER + CURRENT STATE + INTEGRITY PROOF`

## 5. AHTE functional architecture

AHTE shall contain or integrate the following logical engines:

### 5.1 Standards and applicability

- complete applicable Malaysian Halal standards corpus;
- JAKIM operative certification instruments;
- MPPHM / MHMS / applicable protocols, circulars and authority instructions;
- product/sector requirements;
- destination-market requirements;
- contractual buyer/importer requirements where applicable;
- version/effective-date/supersession handling;
- dynamic `ResolvedRequirementSet` generation.

AHTE must not be hard-coded around MS 2400 alone.

### 5.2 Control / HCP / SCCP

`Requirement → Applicability → Control → HCP/SCCP → Expected Evidence → Audit Test`

### 5.3 Evidence graph

Every material trust claim resolves to attributable evidence, object identity and integrity metadata.

### 5.4 Digital twins

Core hierarchy:

`Programme → Organisation → Facility → Product → Formula/Version → Material → Supplier → Process → HCP → Batch → Lot → Logistic Unit → Shipment → Destination Inventory → Retail Unit`

### 5.5 Trust-state engine

Primary lifecycle:

`INITIAL → EVIDENCE-COMPLETE → ASSESSED → VERIFIED → RELEASED`

Exception states include:

`HOLD · QUARANTINED · DISPUTED · CORRECTIVE-ACTION · RE-VERIFICATION · EXPIRED · SUSPENDED · REVOKED · RECALLED`

Certification state, AHTE trust state and supply-chain state must be displayed as separate objects.

## 6. AI/ML predictive and preemptive assurance

Existing AHTE assurance modules are retained:

- Evidence Gap Predictor;
- Anomaly Engine;
- Contradiction Engine;
- Trust Fracture Engine;
- Predictive Compliance Engine;
- Recall Blast-Radius Engine.

This target architecture adds an explicit **Preemptive Strategy Engine**.

```text
LIVE EVIDENCE + TELEMETRY + HISTORY
↓
FEATURE / CONTEXT ASSEMBLY
↓
RISK / FAILURE PREDICTION
↓
IMPACT + BLAST-RADIUS ANALYSIS
↓
PREEMPTIVE STRATEGY GENERATION
↓
POLICY / HUMAN REVIEW AS REQUIRED
↓
PREVENTIVE ACTION
↓
OUTCOME CAPTURE
↓
MODEL / RULE FEEDBACK
```

Preemptive strategies may include:

- targeted re-sampling;
- extra audit attention;
- supplier verification;
- route change recommendation;
- earlier maintenance/calibration;
- additional segregation checks;
- temporary hold recommendation;
- enhanced receiving inspection;
- evidence refresh before expiry;
- CAPA initiation recommendation;
- recall-readiness preparation.

AI output must retain:

`model_id + model_version + feature/input references + timestamp + score/confidence + explanation metadata + recommended action + reviewer/decision linkage`

AI may recommend, prioritize, alert and apply configured D4 HOLD controls. AI must not bypass mandatory D5/D6 decisions or automatically release a hold reserved for human decision.

## 7. 24/7 GHSCL + JAKIM Command Center target model

The Command Center is a first-class operating layer, not a dashboard-only concept.

Target monitoring domains:

- manufacturer/facility operational status;
- supplier/raw-material changes;
- laboratory/sample pipeline;
- HCP/SCCP exceptions;
- smart-glass audit findings;
- certification/authority-status synchronization;
- Sinotrans warehouse status;
- shipment/container/seal status;
- environmental telemetry;
- route/geofence deviation;
- custody completeness;
- origin/destination port status;
- GCC receiving;
- unresolved CAPA;
- evidence expiry/staleness;
- trust fractures;
- predictive risk;
- recommended preemptive strategies;
- recalls and blast radius.

Command Center operating loop:

```text
OBSERVE 24/7
↓
CORRELATE
↓
DETECT
↓
PREDICT
↓
GENERATE PREEMPTIVE STRATEGY
↓
PRIORITISE
↓
ASSIGN OWNER
↓
ALERT / ESCALATE / HOLD WHERE POLICY ALLOWS
↓
HUMAN / AUTHORITY ACTION
↓
CAPA / RE-VERIFICATION
↓
CLOSE OR ESCALATE
↓
MEASURE OUTCOME
```

GHSCL operates the digital infrastructure and continuous monitoring function. JAKIM has the direct authorised authority-system interface/view according to the implemented API scope. Exact production permissions, endpoints and credentials remain controlled implementation inputs and are not published in public website content.

## 8. Laboratory integration

Target architecture:

```text
Source lot
→ Sample ID
→ Collection
→ Seal
→ Custody transfers
→ Laboratory receipt/accession
→ Method execution
→ QC
→ Technical review
→ Signed result/report
→ Canonicalisation
→ Cryptographic digest
→ Signed evidence envelope
→ AHTE
→ Direct JAKIM API workflow where authorised
→ Human authority review
```

`NOT DETECTED ≠ HALAL` remains a hard engine rule.

The China traceability/anti-counterfeit system is a physical/digital identity source integrated with the laboratory and AHTE trust graph; it does not create certification.

## 9. Smart-glass audit

Retain the canonical wearable workflow:

`Device identity + Auditor identity + MFA + role/scope policy`

`Assigned audit → facility/scope → applicable requirements/HCPs → object scan → observation → media/document/sensor evidence → local hash → AI assist → auditor assessment → finding/CAR → re-verification → signed session → sync/reconcile`

Original media are immutable evidence objects; annotations/supersession remain separate.

## 10. Sinotrans integration

Sinotrans is the designated logistics and warehouse operating partner in the target corridor architecture.

Integration target:

`Sinotrans existing systems / Y2T / MIS / EDI / WMS / TMS / IoT → secure adapter/API → event normalizer → AHTE canonical logistics event → evidence/integrity layer → Command Center`

Required evidence domains:

- booking;
- pickup;
- vehicle/container identity;
- pallet/lot mapping;
- seal application and status;
- warehouse receipt/dispatch;
- segregation/storage evidence;
- temperature/humidity or commodity-specific telemetry;
- route/geofence;
- custody handover;
- port transfer;
- customs document references;
- proof of delivery;
- damage/tamper/route/telemetry exceptions.

Do not replace Sinotrans operational systems merely to join AHTE.

## 11. Port / customs API plane

Authorised port/customs users must be given an API/trust gateway supporting minimum-necessary operational verification.

Target resources/functions:

- shipment lookup;
- product/batch/container/seal reconciliation;
- authorised trust packet;
- certification/authority-status reference;
- laboratory evidence reference;
- document/evidence references;
- custody history;
- telemetry/condition exceptions;
- inspection/sampling events;
- hold/release event ingestion;
- signed authority/custody event return.

AHTE records and propagates official port/customs events; it does not create or override sovereign clearance decisions.

## 12. Shariah financing API / Takaful / tokenomics target plane

[PROPOSAL: extends existing Finance / Islamic Finance architecture — path point: Control / Evidence / transaction support]

The target architecture includes a **Shariah Financing API** connected to authorised transaction/trust data.

Logical services:

```text
AHTE AUTHORISED TRUST / TRADE DATA
↓
SHARIAH FINANCING API
├── Islamic trade financing
├── purchase/order financing
├── inventory / shipment financing
├── Takaful underwriting
├── Takaful claims evidence
├── collateral / asset-state verification
└── tokenomics / digital-value mechanisms where legally and Shariah approved
```

Critical separation:

- AHTE trust state is not a credit decision.
- Halal certification is not a financing approval.
- Bank/financier retains credit/legal/Shariah decision authority.
- Takaful operator retains underwriting/claim authority.
- Tokenization does not change ownership, title, regulatory, Shariah or authority status by itself.

No live bank/Takaful/tokenomics counterparty, product structure, token classification or regulatory approval is asserted by this architecture record until documented.

## 13. Cryptographic integrity

Every material evidence object should be attributable, versioned and integrity-protected.

Preferred pattern:

`Original source record → canonical representation → content hash → signed evidence manifest → append-only/tamper-evident history → optional external/DLT anchor → later verification`

A hash proves integrity after creation, not truth or competent authority.

Use:

- strong identity and authentication;
- signatures where appropriate;
- hardware-backed keys for high-value roles/services/devices where feasible;
- algorithm agility;
- revocation;
- trusted time;
- anti-replay;
- idempotency;
- append-only correction/supersession;
- selective disclosure;
- data-sovereignty controls.

## 14. API and interoperability principle

AHTE integrates with existing systems rather than forcing wholesale replacement.

System-of-record examples:

- ERP/PLM — legal entity/product/formula;
- MES — production/process execution;
- QMS — NCR/CAPA;
- WMS — inventory/warehouse state;
- LIMS — analytical evidence;
- IoT/SCADA/edge — condition telemetry;
- TMS/logistics — shipment/custody;
- authority systems — authority decisions/status;
- bank/Takaful systems — finance/underwriting decisions.

Cross-border exchange follows minimum-necessary, policy-approved assertion/proof exchange rather than uncontrolled replication of source records.

## 15. Website and public-communications requirements

All public surfaces must represent:

- China origin → GCC destination as the default physical corridor;
- Malaysia as the governance/assurance plane unless physically in route;
- manufacturer onboarding as a first-class journey;
- laboratory/sample chain before manufacturing release;
- smart-glass AI-assisted audit;
- complete standards/applicability intelligence;
- direct JAKIM API connectivity;
- 24/7 GHSCL + JAKIM Command Center;
- AI/ML predictive analytics and preemptive strategies;
- Sinotrans end-to-end warehouse/logistics integration;
- port/customs API access;
- evidence integrity / immutable hash anchoring;
- Shariah financing API / Takaful / tokenomics target plane;
- role-based transparency;
- separate trust/certification/supply-chain states.

Do not expose credentials, endpoint secrets, manufacturer formulas, laboratory confidential data or raw authority-system security details.

## 16. Source precedence for project implementation

Use the following order when project artifacts disagree:

1. `master-standards-stack/verified-2026-09-17/` for frozen verified material within its defined scope.
2. Current competent-authority instruments and controlled source registries for authority/normative claims.
3. `00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md`, machine registries and canonical-path controls.
4. This current target architecture for post-freeze project topology and user-authorised architecture decisions dated 2026-09-30.
5. Current domain specifications: Platinum, China execution, laboratory, Sinotrans, ports, website.
6. Historical/derived drafts only where not conflicting with the above.

This file does not rewrite the verified freeze and does not manufacture authority facts.

## 17. Explicit supersessions/corrections

For project implementation after 2026-09-30:

- `China → Malaysia` pilot wording in older Sinotrans material does **not** control Shipment 001; use **China → GCC direct**.
- `China → Malaysia → GCC` wording in older GHSCL corridor descriptions is replaced by **China origin → GCC destination**, with Malaysia as the governance/assurance plane unless an actual Malaysia physical hop is explicitly scoped.
- Generic public `Authority API Gateway` diagrams must not obscure the intended **direct JAKIM API** topology.
- The Command Center must not be represented as passive analytics; it is a 24/7 monitoring, escalation and intervention operating layer.
- Predictive analytics must be paired with an explicit preemptive-strategy workflow.
- Sinotrans integration includes **warehouse + end-to-end logistics real-time monitoring**, not transportation alone.
- Port authorities receive an authorised API/trust interface; sovereign decisions remain theirs.
- Finance architecture includes the Shariah Financing API target plane with Takaful and tokenomics, subject to actual legal/Shariah/regulatory/counterparty implementation.
- `platform/` reference runtime is not production infrastructure.
- `platform/web/` prototype is not the completed multi-surface website/platform.

## 18. Completion boundary

Documentation of the target architecture does not itself prove production deployment.

Production classification requires implemented and tested integrations, security controls, identity/authentication, persistence, auditability, contractual/authority permissions and transaction-native evidence.

The project target architecture, however, is now consolidated in one post-freeze control artifact for implementation, website rebuilding and Codex execution.