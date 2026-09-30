# Current Target Architecture — 30 September 2026

## Artifact metadata

| Field | Value |
|---|---|
| Artifact | `CURRENT_TARGET_ARCHITECTURE_2026-09-30.md` |
| Folder | `00_EXECUTIVE_COMMAND/` |
| Revision | v1.2.0 |
| Control date | 2026-09-30 |
| Classification | Post-freeze target architecture consolidation |
| Freeze impact | None — `master-standards-stack/verified-2026-09-17/` remains immutable |
| Authority effect | None by itself; records the project target architecture and source precedence |
| Companion controls | `current-target-architecture-2026-09-30.json`; `IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md`; `PLATFORM_REQUIREMENTS_TRACEABILITY_2026-09-30.md` |
| Supersedes | Conflicting project-level architecture statements dated before this revision, except frozen verified source artifacts and explicit competent-authority instruments |

[PROPOSAL: consolidates current target architecture — path point: Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release]

## 1. Governing project topology

The project is a **Global Halal Digital Trust & Trade / Halal Tayyib infrastructure**, not a certificate database, not an MS 2400-only system, not a standalone blockchain application and not a generic logistics dashboard.

```text
MALAYSIAN HALAL GOVERNANCE / AUTHORITY PLANE
        │
        ├── JAKIM
        │     └── DIRECT AUTHORISED JAKIM API
        │
        └── PHC
              Perak State Government halal-industry GLC
              local + international industry role
              │
              └── PHC + JAKIM authorised human certification workflow
                  including Mufti / scholars / authorised officers as applicable

GLOBAL HALAL SUPPLY CHAIN LIMITED — HONG KONG
        │
        ├── International operating / digital-infrastructure vehicle
        ├── China → GCC corridor orchestration
        ├── Ecosystem and partner integration
        └── 24/7 Command Center operating role
                │
                v
               AHTE
 Standards / Applicability / Controls / Evidence / Traceability / Trust Intelligence
                │
        ┌───────┼────────┬──────────┬─────────────┬──────────────┐
        │       │        │          │             │              │
     China   Laboratory Factory   Sinotrans    Port/GCC      Finance/Takaful
     origin   + trace    systems   logistics    APIs          API plane
        │       │        │          │             │              │
        └───────┴────────┴──────────┴─────────────┴──────────────┘
                │
        Continuous attributable evidence
                │
        Cryptographic integrity + append-only history
                │
        Digital twins + evidence/trust graph
                │
        AI/ML anomaly + predictive assurance
                │
        Preemptive Strategy Engine
                │
        24/7 GHSCL + authorised JAKIM joint monitoring
                │
        Human / authority action where required
                │
        Direct JAKIM API / authority status
                │
        AHTE trust-state propagation
                │
             China → GCC
```

## 2. Non-negotiable role separation

`PHC ≠ GHSCL ≠ AHTE ≠ laboratory ≠ Sinotrans ≠ port/customs authority ≠ AI ≠ bank ≠ Takaful operator ≠ competent-authority decision`

- **PHC** — Perak State Government halal-industry GLC operating locally and internationally within the project ecosystem.
- **GHSCL Hong Kong** — international operating and digital-infrastructure vehicle; corridor and 24/7 platform-operation role.
- **AHTE** — continuous standards, applicability, control, evidence, traceability, compliance and trust-intelligence fabric.
- **Direct JAKIM API** — the project authority-system connectivity path. Do not insert NurAI or an unnecessary external middleware layer in public/system topology.
- **Project formal certification workflow** — approval/disapproval is performed through the authorised **PHC + JAKIM human workflow**, including Mufti/scholars/authorised halal officers or other authorised decision-makers as applicable. AI/AHTE assists but does not make the formal certification decision.
- **Laboratory** — creates scientific/analytical evidence within its applicable competence/scope; a result is not certification.
- **Sinotrans** — end-to-end logistics and warehouse execution with real-time custody/telemetry evidence integration.
- **Port/customs authority** — retains sovereign release/inspection power; AHTE provides an authorised trust/API interface and records returned official events.
- **Bank/financier** — retains credit/legal/Shariah financing decision authority.
- **Takaful operator** — retains underwriting/claims authority.
- **AI/ML** — monitoring, correlation, anomaly detection, prediction, impact analysis and strategy recommendation under D0–D6 controls.

## 3. Default corridor and physical chain

Default physical corridor: **China → GCC direct**.

Malaysia is the governance/assurance and authority-connectivity plane unless a physical Malaysia movement is explicitly and separately scoped.

[PILOT: Shipment 001 — first controlled China→GCC proof-of-execution]

Shipment 001 remains a pilot object until transaction-native evidence exists.

```text
VERIFIED RAW-MATERIAL ORIGIN
↓
PRODUCER / SUPPLIER / LOT / PROVENANCE
↓
PHYSICAL + DIGITAL IDENTITY
↓
SAMPLE PLAN / SAMPLE ID / COLLECTION / SEAL / CHAIN OF CUSTODY
↓
CHINA LABORATORY + TRACEABILITY / ANTI-COUNTERFEIT SYSTEM
↓
METHOD / QC / TECHNICAL REVIEW / SIGNED SCIENTIFIC EVIDENCE
↓
RAW-MATERIAL RELEASE / HOLD
↓
MANUFACTURER / FACILITY
↓
ERP / MES / QMS / WMS / LIMS / IoT / DMS / IDENTITY
↓
PRODUCT / SKU / FORMULA / BOM / MATERIAL / SUPPLIER / PROCESS
↓
APPLICABLE MS + JAKIM OPERATING REQUIREMENTS + DESTINATION REQUIREMENTS
↓
CONTROL → HCP / SCCP → EXPECTED EVIDENCE
↓
SMART-GLASS AI-ASSISTED SITE AUDIT
↓
FINDING → CAR / CAPA → RE-VERIFICATION
↓
DIRECT JAKIM API
↓
PHC + JAKIM AUTHORISED HUMAN REVIEW / APPROVE-DISAPPROVE WORKFLOW
↓
FORMAL AUTHORITY STATUS EVENT
↓
AHTE AUTHORITY-LINKED TRUST-STATE PROPAGATION
↓
UNIT / BOX / CARTON / BATCH / LOT / PALLET
↓
SINOTRANS WAREHOUSE
↓
SINOTRANS END-TO-END LOGISTICS
↓
VEHICLE / CONTAINER / SEAL / CUSTODY / TELEMETRY / GEOFENCE
↓
CHINA PORT / CUSTOMS API
↓
EXPORT / LOADING
↓
INTERNATIONAL TRANSIT
↓
GCC PORT / CUSTOMS API
↓
DESTINATION INSPECTION / HOLD / RELEASE
↓
IMPORTER / DESTINATION WAREHOUSE
↓
DISTRIBUTION / RETAIL
↓
BUYER / CONSUMER AUTHORISED VERIFICATION
```

## 4. Four synchronized chains

Every material object/event must preserve four linked chains:

1. **Physical** — raw material → factory → warehouse → logistics → port → GCC → retail.
2. **Identity/custody** — actor → facility → material/product → sample/batch → pallet → container/seal → handover.
3. **Evidence** — source/certificate references → lab → process/HCP/SCCP → audit → CAPA → telemetry/custody → receiving.
4. **Authority/trust-state** — direct authority decision/status → AHTE trust state → operational release/hold/quarantine/recall.

Minimum material event tuple:

`WHO + WHAT + WHEN + WHERE + OBJECT + REQUIREMENT/CONTROL + EVIDENCE + VERIFIER + CURRENT STATE + INTEGRITY PROOF`

## 5. AHTE functional architecture

### 5.1 Standards / regulatory intelligence

AHTE resolves the complete applicable Malaysian/JAKIM framework, not MS 2400 alone:

- applicable Malaysian Standards and editions;
- JAKIM operative certification instruments;
- MPPHM / MHMS / HAS / IHCS as applicable;
- protocols, circulars, fatwa/authority instructions as applicable;
- sector/product requirements;
- laboratory method/version requirements;
- GCC destination-market requirements;
- buyer/importer contractual controls where lawful/applicable;
- version/effective-date/supersession history.

Output: versioned `ResolvedRequirementSet` / applicability object.

### 5.2 Control / HCP / SCCP

`Requirement → Applicability → Control → HCP/SCCP → Expected Evidence → Audit Test`

### 5.3 Evidence graph

Every material trust claim resolves to source identity, object identity, timestamp, actor/system/device, evidence reference, applicable requirement/control, verification state and integrity metadata.

### 5.4 Digital twins and object genealogy

`Programme → Organisation → Facility → Product → Formula/Version → Material → Supplier → Process → HCP/SCCP → Batch → Lot → Unit/Box/Carton/Pallet → Logistic Unit → Container/Seal → Shipment → Destination Inventory → Retail Unit`

### 5.5 Trust-state engine

Primary lifecycle:

`INITIAL → EVIDENCE-COMPLETE → ASSESSED → VERIFIED → RELEASED`

Exception/lifecycle states include:

`HOLD · QUARANTINED · DISPUTED · CORRECTIVE-ACTION · RE-VERIFICATION · EXPIRED · SUSPENDED · REVOKED · RECALLED`

Certification/authority state, AHTE trust state, supply-chain state, port/customs state and finance/Takaful state are distinct objects.

## 6. Manufacturer onboarding factory

Manufacturer onboarding is a first-class workflow:

`Manufacturer identified → legal entity/KYB → facility qualification → product/SKU → formula/BOM → ingredients/raw materials → suppliers → origin provenance → existing certification/evidence → ERP/MES/QMS/WMS/LIMS/IoT system inventory → AHTE digital twin → applicable requirements → HCP/SCCP → evidence gap → remediation/training → laboratory/sample plan → smart-glass pre-audit/site audit → findings/CAPA → re-verification → direct JAKIM API/human authority workflow → formal status → continuous monitoring → China→GCC shipment/market enablement`.

The architecture must scale to many manufacturers/products/facilities without arbitrary caps or bespoke redesign per participant.

## 7. China traceability / anti-counterfeit + laboratory plane

The China physical/digital identity plane supports:

- enterprise/product identity;
- one-item-one-code;
- microdot / QR / VOID/tamper-evident physical token where deployed;
- product/batch/code binding;
- unit → box → carton → pallet aggregation;
- consumer/channel verification;
- anti-diversion/abnormal-scan events;
- scan/channel analytics.

AHTE extends that identity chain through container/shipment/GCC objects.

Laboratory target chain:

`Sampling authorisation → SampleID → collection → collector/time/location → seal → custody transfers → lab receipt → condition → accession → aliquot/sub-sample → method execution → QC → technical review → authorised signatory → signed report/result → canonicalisation → content hash → signed evidence manifest → AHTE`.

**Hard rule:** `NOT_DETECTED ≠ HALAL`.

A displayed quality-report document becomes a verified laboratory result only after source identity, sample, method/scope, report provenance and integrity controls are satisfied.

## 8. Smart-glass audit

`Device identity + Auditor identity + MFA + role/scope policy`

`Assigned audit → facility/scope → applicable requirement/HCP package → physical walkthrough → object scan → observation → image/video/document/voice/sensor evidence → local hash/signature → AI assist → auditor assessment → finding → CAR/CAPA → re-verification → signed session → offline/online reconciliation`.

Original media remain immutable evidence objects; annotations/corrections are separate linked objects.

## 9. AI/ML predictive + preemptive assurance

Required assurance engines include:

- Evidence Gap Predictor;
- Anomaly Engine;
- Contradiction Engine;
- Trust Fracture Engine;
- Predictive Compliance Engine;
- Recall Blast-Radius Engine;
- explicit **Preemptive Strategy Engine**.

```text
LIVE EVIDENCE + TELEMETRY + HISTORY
↓
CONTEXT / FEATURE ASSEMBLY
↓
ANOMALY + RISK / FAILURE PREDICTION
↓
IMPACT / BLAST-RADIUS ANALYSIS
↓
PREEMPTIVE STRATEGY GENERATION
↓
DECISION-CLASS / POLICY CHECK
↓
HUMAN / POLICY REVIEW AS REQUIRED
↓
PREVENTIVE ACTION
↓
OUTCOME CAPTURE
↓
MODEL / RULE FEEDBACK
```

Predictions/strategies are first-class auditable objects carrying model/version, inputs/evidence, horizon, score/confidence, explanation/drivers, affected objects, recommended actions, decision class, reviewer/action and outcome.

AI may perform D0/D1/D2 and configured D4 holds under policy. AI does not bypass D5/D6. Automatic D4 release is prohibited where human release is required.

## 10. 24/7 GHSCL + JAKIM Command Center

The Command Center is a first-class operating plane, **jointly monitored 24/7 by GHSCL operational roles and authorised JAKIM authority-side roles**.

Shared monitoring does not mean identical authority:

- GHSCL — digital infrastructure, corridor monitoring, partner coordination, exception ownership/orchestration and operational analytics within scope.
- JAKIM — authority-relevant monitoring, evidence/status visibility and authority workflow/actions according to actual mandate and direct API permissions.

Monitor continuously:

- manufacturer/facility/onboarding state;
- suppliers/raw-materials/origin changes;
- lab/sample/traceability/anti-counterfeit pipeline;
- HCP/SCCP/process exceptions;
- smart-glass audit/findings/CAPA;
- certification/authority status synchronization;
- Sinotrans warehouse/inventory state;
- logistics/route/custody/container/seal/telemetry;
- origin and GCC port/customs status;
- importer/GCC receiving/warehouse/retail progression;
- evidence integrity, expiry/staleness and trust fractures;
- predictive risks and preemptive strategies;
- recall/blast-radius cases;
- finance/Takaful support-state where authorised.

Operating loop:

`Observe → validate/correlate → detect → predict → model impact → generate preemptive strategy → prioritize/assign → alert/escalate/hold under policy → human/authority action → CAPA/re-verification → trust-state update → close/escalate/recall → outcome feedback`.

## 11. Sinotrans end-to-end warehouse + logistics integration

Target integration:

`Sinotrans Y2T/MIS/EDI/WMS/TMS/IoT/existing systems → secure adapter/API → schema validation → policy → event normalizer → AHTE canonical logistics event → evidence/integrity → Command Center`.

Required domains include booking/order, warehouse receipt/dispatch, zone/segregation/storage, inventory/batch genealogy, pickup, vehicle, pallet/lot, container, seal, loading, route/geofence, environmental/commodity telemetry, custody handovers, port transfer, customs document reference, proof of delivery, damage/tamper/route/telemetry exceptions.

AHTE integrates; it does not require wholesale replacement of Sinotrans systems.

## 12. Port / customs API plane

Origin-China and GCC destination port/customs users receive authorised minimum-necessary API/trust interfaces supporting:

- shipment lookup;
- product/batch/container/seal reconciliation;
- trust packet / certification-authority status reference;
- lab/evidence/document references;
- custody history;
- telemetry/condition exceptions;
- inspection/sampling events;
- hold/release event ingestion;
- signed authority/custody event return.

Port/customs authorities retain sovereign release/inspection powers. AHTE records and propagates the official state; it never manufactures clearance.

## 13. Shariah Financing API / Takaful / tokenomics plane

[PROPOSAL: post-freeze transaction-support plane — path point: Control / Evidence / transaction support]

`AHTE authorised trust/trade data → Shariah Financing API → Islamic trade/purchase/order/inventory/shipment financing + Takaful underwriting/claims evidence + asset/collateral verification + tokenomics/digital-value mechanisms where legally, regulatorily and Shariah approved`.

Separation rules:

- halal certification ≠ financing approval;
- AHTE trust state ≠ credit decision;
- financing decision remains with the financier;
- Takaful underwriting/claim decision remains with the Takaful operator;
- tokenization does not itself create title, ownership, legal status, Shariah approval or regulatory approval.

## 14. Cryptographic integrity and evidence history

Pattern:

`Original source → canonical representation → content hash → signed evidence manifest → append-only/tamper-evident history → optional external/DLT anchor → later verification`.

Use strong identity/authentication, signatures, hardware-backed keys where appropriate, algorithm agility, revocation, trusted time, anti-replay, idempotency, evidence lineage, append-only supersession/correction, selective disclosure and jurisdictional data controls.

Hashing proves integrity after creation, not truth or authority.

## 15. Interoperability / sovereign data architecture

Operational systems remain systems of record within their domain where appropriate:

- ERP/PLM — company/product/formula;
- MES — production execution;
- QMS — NCR/CAPA;
- WMS — inventory/warehouse;
- LIMS — analytical evidence;
- IoT/SCADA/edge — telemetry;
- TMS/logistics — transport/custody;
- traceability/serialization platform — physical/product code and scan events;
- JAKIM — authority decisions/status;
- port/customs — sovereign inspection/release;
- bank/Takaful — financing/underwriting decisions.

**Data stays where it belongs; trust travels.** Cross-border exchange uses policy-approved minimum-necessary assertions, evidence references, hashes, signatures and scoped metadata instead of uncontrolled replication.

## 16. Experience architecture

Do not collapse the ecosystem into one generic dashboard. Target surfaces include:

- public institutional/educational website;
- manufacturer onboarding/operations portal;
- supplier/material evidence workflows;
- laboratory/sample portal/interface;
- smart-glass auditor interface;
- Sinotrans logistics/warehouse integration and views;
- 24/7 GHSCL + JAKIM Command Center;
- port/customs API/officer interface;
- GCC importer/receiving view;
- retailer/buyer view;
- consumer verification;
- finance/Takaful purpose-specific interface;
- administration/security/governance surfaces.

Public verification exposes authorised provenance/trust/certification/custody fields, not confidential formulas, raw authority records, pricing or unrestricted personal/commercial data.

Multilingual readiness: English, Simplified Chinese, Malay and Arabic/RTL.

## 17. No-artificial-block implementation rule

**FULL ARCHITECTURE NOW → REAL CONNECTORS WHEN AVAILABLE → NO REDESIGN REQUIRED.**

Unavailable credentials/APIs/devices/data do not justify removing, hiding, permanently disabling, downgrading or arbitrarily limiting a target capability.

For an unavailable live dependency implement:

`production domain model → production adapter contract → explicit connector state → replaceable development/sandbox provider → full workflow/UI/tests → production connector replacement without redesign`.

No arbitrary caps on manufacturers, products, facilities, materials, suppliers, evidence, shipments, audits, standards, roles, jurisdictions, connectors or languages.

This does not remove legitimate authority/security gates and does not permit fabricated live JAKIM approvals, laboratory results, Sinotrans events, customs releases, GCC acceptance, finance/Takaful decisions, token approvals or Shipment 001 evidence.

## 18. Public/website requirements

All public and platform specifications must represent the complete model above, including direct JAKIM API, PHC + JAKIM authorised human certification workflow, raw-material-origin traceability, China lab/traceability identity plane, smart glass, standards/applicability, Sinotrans warehouse/logistics, port APIs, GCC destination, 24/7 joint GHSCL/JAKIM monitoring, AI/ML predictive + preemptive functions, evidence integrity and Shariah financing/Takaful/tokenomics as a distinct transaction-support plane.

Do not use `NurAI` as a platform integration hop. Do not present blockchain/QR/lab/AI/AHTE as certification authority.

## 19. Source precedence

When project artifacts disagree:

1. `master-standards-stack/verified-2026-09-17/` — frozen verified material within its defined scope.
2. Current competent-authority instruments / controlled source registries — authority/normative claims.
3. `IQ300_DOCTRINE.md`, decision-class/machine registries, schema registry and canonical-path controls.
4. This target architecture + machine target + implementation completeness + platform requirements traceability — post-freeze target topology/implementation.
5. Current domain specifications — Platinum/Command Center, canonical China execution pack, laboratory/traceability, Sinotrans, ports, finance, website/Codex.
6. Historical/derived drafts only where not conflicting.

This precedence does not rewrite frozen source evidence.

## 20. Explicit supersessions / cleanup rules

For current implementation:

- old `China → Malaysia` or mandatory `China → Malaysia → GCC` pilot wording does not control Shipment 001; use China→GCC direct;
- generic public `Authority API Gateway` must not obscure direct JAKIM API topology;
- old split China lab profile/addendum is superseded by the consolidated 30 September profile;
- the duplicate lowercase `master-standards-stack/china-execution-pack/` lineage is retired after its richer/unique content is moved into canonical `master-standards-stack/CHINA_EXECUTION_PACK/`;
- obsolete website v1 pointer/spec is removed after v2.1+ is confirmed as controlling;
- historical audits/frozen artifacts are retained when they document historical state rather than act as current control;
- `platform/` reference runtime is not production infrastructure;
- `platform/web/` reference experience is not the full authenticated platform.

Artifact retirement must preserve unique requirements and record old path → replacement in `OBSOLETE_ARTIFACT_RETIREMENT_2026-09-30.md`.

## 21. Production boundary

Target architecture completeness and external/production readiness are different facts.

Production classification requires the relevant implemented authentication, persistence, security, identity, external permissions/contracts, real interface/data contracts, auditability, availability controls and transaction-native evidence.

External dependencies are connection/evidence gates — **not artificial product-feature blocks**.