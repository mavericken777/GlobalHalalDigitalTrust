# Global Halal Digital Trust — Website Rebuild Master Specification v2

## Artifact metadata

| Field | Value |
|---|---|
| Artifact | `WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md` |
| Revision | v2.2.0 |
| Control date | 2026-09-30 |
| Classification | Post-freeze public website / portal architecture |
| Freeze impact | None |
| Authority effect | None |
| Governing project architecture | `00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md` v1.2+ |
| Machine architecture registry | `00_EXECUTIVE_COMMAND/current-target-architecture-2026-09-30.json` v1.2+ |
| Requirements traceability | `00_EXECUTIVE_COMMAND/PLATFORM_REQUIREMENTS_TRACEABILITY_2026-09-30.md` |
| Implementation completeness | `00_EXECUTIVE_COMMAND/IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md` |
| Supersedes | All earlier website specifications; the v1 pointer has been retired from the active tree |

[PROPOSAL: closes website/public-platform parity gap — path point: Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release]

## 0. Implementation principle — full target system, no artificial blocks

**FULL ARCHITECTURE NOW → REAL CONNECTORS WHEN AVAILABLE → NO REDESIGN REQUIRED.**

The website/platform rebuild must not remove, disable, downgrade, hide, defer or omit an intended capability merely because an external API, credential, partner feed, authority connection, laboratory interface, sensor stream, production dataset, financial counterparty or live shipment is unavailable in the development environment.

For every unavailable external dependency, implement:

1. complete production domain model;
2. complete production adapter/interface contract;
3. complete UI/workflow/state machine;
4. replaceable development/sandbox/mock provider at the same boundary;
5. explicit connection-state labelling so development data is never represented as live production evidence.

Development mocks substitute **connectivity/data only**. They do not substitute away capability.

Do not use `coming soon`, permanent feature flags, blank pages, disabled navigation or demo-only reductions as substitutes for required target functionality.

Do not fabricate live JAKIM decisions, laboratory results, Sinotrans telemetry, customs release, GCC acceptance, financing approval, Takaful underwriting, token legal/Shariah status or shipment workflow transaction evidence.

## 1. Purpose

The website must represent the **complete Global Halal Digital Trust Ecosystem**, not a generic halal logistics site, not an MS 2400 microsite, not a blockchain-certification site, not a laboratory site and not a brochure-only corporate page.

Primary goals:

1. Explain the complete China-origin → GCC-destination operating model.
2. Convert manufacturers/producers into qualified onboarding candidates.
3. Explain PHC, GHSCL, AHTE, direct JAKIM API, China traceability/lab, smart-glass audit, Sinotrans, ports, GCC and finance roles without conflation.
4. Demonstrate raw-material-to-retail traceability, live trust state, evidence integrity and authority connectivity.
5. Show China physical identity/serialization, anti-counterfeit and packaging aggregation as part of the evidence graph.
6. Expose role-based public/partner verification experiences.
7. Present AI/ML predictive analytics and preemptive strategies as decision-support infrastructure.
8. Present the **jointly monitored 24/7 GHSCL + authorised JAKIM Command Center** as a first-class operating layer.
9. Preserve the complete target architecture even where production connectors are not yet provisioned.

Core proposition:

> **Complete traceability. Live Halal trust state. Immutable evidence. Predictive assurance. Human authority. From verified raw-material origin in China to GCC destination.**

## 2. Mandatory system roles

| Layer | Actor | Public description |
|---|---|---|
| Malaysian halal-industry institutional layer | PHC | Perak State Government halal-industry GLC operating locally and internationally |
| International operating layer | GHSCL Hong Kong | International operating/digital-infrastructure vehicle; 24/7 corridor/platform operations |
| Intelligence layer | AHTE | Standards, applicability, evidence, compliance, traceability, trust-state and AI/ML intelligence |
| Authority connectivity | Direct JAKIM API | Direct authorised JAKIM-system connectivity; no NurAI or generic public intermediary hop |
| Formal human authority workflow | PHC + JAKIM authorised humans | Project approve/disapprove workflow with Mufti/scholars/authorised halal officers/decision-makers as applicable; AI/AHTE do not make the formal decision |
| China physical identity / traceability | China traceability / anti-counterfeit system | One-item-one-code, microdot/QR/VOID where deployed, product/batch binding, packaging aggregation, consumer/channel verification, anti-diversion/scan analytics |
| Scientific evidence | China laboratory pathway | Sample, seal, custody, method/QC, technical review, signed result and evidence integrity |
| Field audit | Smart-glass workflow | Requirement-guided AI-assisted physical evidence capture with human auditor accountability |
| Logistics | Sinotrans | End-to-end warehouse + logistics execution and real-time custody/telemetry integration |
| Port/border | Origin/GCC authorities | Sovereign inspection/clearance/release with authorised AHTE API/trust interface |
| Destination | GCC importers/authorities/warehouses/retail | Destination acceptance, receiving and market verification |
| Transaction support | Shariah Financing API | Islamic financing, Takaful and approved tokenomics integrations under separate legal/Shariah/regulatory decision authority |

Never imply that GHSCL/AHTE, AI, blockchain/DLT, laboratory testing, QR/NFC/microdot/VOID, hashes or telemetry independently creates official Halal certification.

## 3. Global navigation

### Primary

- Home
- How It Works
- AHTE
- Manufacturer Onboarding
- Smart-Glass Audit
- Lab & Origin
- Real-Time Monitoring
- Command Center
- China → GCC
- Standards & Governance
- Port & Customs
- Shariah Finance
- Ecosystem
- About GHSCL

### Utility

- Verify Trust Record
- Apply / Onboard
- Partner / API
- Portal Login
- EN | 中文 | العربية | BM

## 4. Homepage information architecture

### Hero

**Eyebrow:** GLOBAL HALAL DIGITAL TRUST INFRASTRUCTURE

**Headline:** From China Origin to GCC Destination. Every Material. Every Evidence. Every Handover. Verifiable.

**Subheadline:** GHSCL operates an international digital-trust infrastructure connecting verified raw-material origin, China product identity and laboratory evidence, manufacturers, AI-assisted smart-glass audits, real-time Sinotrans warehousing/logistics, direct JAKIM API authority connectivity, joint 24/7 monitoring and GCC market verification through AHTE.

**Trust line:** Complete traceability · Live trust state · Immutable evidence · Predictive assurance · Human authority

Primary CTA: **Onboard a Manufacturer**
Secondary CTA: **Verify a Trust Record**

Hero visual must show **China → GCC direct** as the physical corridor and Malaysia as governance/assurance/authority connectivity, not forced physical transshipment.

### Source-to-destination chain

Interactive chain:

`Raw-material origin → Producer/supplier → physical identity → sample/chain of custody → China traceability + laboratory → factory → standards/HCP/SCCP → smart-glass audit → direct JAKIM API → PHC+JAKIM human authority workflow → packaging/aggregation → Sinotrans warehouse → Sinotrans logistics → origin port → transit → GCC port → importer → destination warehouse → retail / verification`

Each node exposes authorised subsets of:

- object identity;
- actor/source system;
- applicable requirement/control;
- evidence type;
- timestamp/location where applicable;
- integrity proof;
- AHTE trust state;
- supply-chain state;
- exceptions/holds;
- formal authority state where applicable.

### Institutional architecture

Use separated, non-hierarchical cards:

- PHC
- GHSCL Hong Kong
- AHTE
- Direct JAKIM API / JAKIM authority system
- PHC + JAKIM authorised human workflow
- China Traceability + Laboratory
- Sinotrans
- Port/Customs Authorities
- GCC Authorities / Importers
- Shariah Finance / Takaful

Do not draw JAKIM as a subsidiary of GHSCL/PHC/AHTE.

### Manufacturer onboarding

Lifecycle:

`Enterprise application → KYB/due diligence → facility qualification → product/SKU → formula/BOM → raw materials/suppliers → origin provenance → existing evidence/certification references → ERP/MES/QMS/WMS/LIMS/DMS/IoT inventory → digital twins → applicability resolution → HCP/SCCP → evidence gaps → remediation/training → lab/sample plan → smart-glass audit → findings/CAR/CAPA → re-verification → direct JAKIM API + PHC/JAKIM human workflow → formal status → continuous monitoring → China→GCC release`

### China physical identity / traceability

Dedicated visual:

`Enterprise/Product → unique physical code → batch binding → Unit → Box → Carton → Pallet → Logistic Unit → Container → Shipment → GCC Destination Inventory`

Explain source capabilities where deployed:

- one-item-one-code;
- microdot / QR / VOID/tamper evidence;
- product/batch/code binding;
- packaging aggregation/de-aggregation events;
- consumer/channel scan verification;
- anti-diversion / black-list / abnormal scan events;
- scan geography/velocity analytics;
- AHTE extension from product identity into lab, manufacturing, custody, shipment and authority-linked trust graph.

A physical code authenticates/binds an object; it does not itself certify Halal.

### Smart-glass audit

Display:

`Authenticate device/auditor → load audit → verify facility/scope → requirements/HCPs → scan object → capture media/document/voice/sensor evidence → local hash/signature → AI assist → auditor assessment/finding → CAR/CAPA → re-verification → sign/sync`

Capabilities:

- QR/DataMatrix/OCR/NFC;
- still/video evidence;
- voice notes/commands;
- GNSS/location where permitted;
- offline-first encrypted queue;
- device identity and hardware-backed keys where available;
- immutable original media + separate annotations;
- AI evidence-gap/anomaly/contradiction support;
- human auditor sign-off.

If physical smart-glass hardware is unavailable during development, the complete wearable workflow remains implemented using a development device provider.

### Lab and origin

Visual:

`Origin lot → sample plan/ID → collection → seal → custody → lab receipt/accession → method/QC → technical review → authorised signatory → signed result/report → hash/signature → AHTE → direct JAKIM linkage where authorised → material/trust state`

Message: scientific evidence is bound to sample identity, chain of custody and method scope; **NOT DETECTED ≠ HALAL**.

A displayed quality-report PDF is not automatically a verified laboratory result until provenance, sample, method, scope, signature/hash and object binding are validated.

### Standards intelligence

Show the canonical path:

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP/SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

The site must dynamically represent the complete applicable Malaysian standards/JAKIM operating framework and destination rules. Do not hard-code MS 2400 as the whole system.

### Immutable evidence fabric

Explain:

`Actor + Object + Event + Evidence + Timestamp + Device/System + Requirement + Hash + Authentication/Signature + Previous-event reference`

Clarify that hashing proves integrity after creation; it does not by itself prove truth, authority or Halal status. Corrections/supersessions append history rather than silently rewriting it.

### Platinum real-time monitoring

Show live domains:

- raw material/supplier/origin changes;
- China traceability / anti-counterfeit / scan anomalies;
- lab/sample status;
- HCP/SCCP exceptions;
- production batch state;
- warehouse/inventory status;
- container/seal;
- GPS/geofence;
- environmental telemetry;
- custody handovers;
- port/customs status;
- GCC receiving;
- evidence expiry;
- CAPA/re-verification;
- suspension/revocation/recall.

### AI/ML predictive + preemptive

Display AHTE modules:

- Evidence Gap Predictor
- Anomaly Engine
- Contradiction Engine
- Trust Fracture Engine
- Predictive Compliance Engine
- Recall Blast-Radius Engine
- Preemptive Strategy Engine

Visual flow:

`Observe → Correlate → Detect → Predict → Model impact/blast radius → Generate preemptive strategy → Decision-class/policy check → Human/authority review where required → Preventive action → Outcome feedback`

Do not portray model confidence as authority.

### 24/7 GHSCL + JAKIM Command Center

This is a dedicated homepage section and dedicated page.

The target is **jointly monitored 24/7 by GHSCL operational roles and authorised JAKIM authority-side roles**, with distinct permissions.

Show a control-room style interface with:

- live China→GCC corridor map;
- manufacturer/facility status;
- supplier/material risk;
- traceability/anti-counterfeit anomaly queue;
- lab/sample queue;
- evidence freshness/integrity;
- HCP/SCCP alerts;
- smart-glass findings/CAPA;
- Sinotrans warehouse/logistics status;
- shipment/container/seal/telemetry state;
- port/GCC events;
- predictive risk queue;
- preemptive strategy queue;
- exception/CAPA ownership;
- escalation status;
- recall blast radius;
- direct JAKIM API synchronization/authority state;
- finance/Takaful support state where authorised.

Operating loop:

`24/7 observe → correlate → detect → predict → impact analysis → strategy → assign → escalate/hold where policy allows → human/authority action → CAPA/re-verify → close/escalate/recall → learn`

### Direct JAKIM API + human authority workflow

Public diagram:

`AHTE ⇄ DIRECT JAKIM API ⇄ JAKIM → PHC + JAKIM authorised human workflow → formal decision/status → Direct JAKIM API → AHTE`

Do not insert NurAI or a generic public gateway.

The project formal approve/disapprove workflow remains human and includes Mufti/scholars/authorised halal officers/decision-makers as applicable. AI/AHTE may assist and route but do not make the formal decision.

No public endpoint names, credentials, private schemas or security-sensitive details.

The full direct-JAKIM workflow must exist in development through a replaceable provider if production credentials are unavailable; UI must distinguish development/sandbox from production-connected state.

### Sinotrans

Dedicated section:

`Factory/warehouse → Sinotrans WMS/TMS/Y2T/MIS/EDI/IoT → secure adapter/API → canonical AHTE events → evidence/trust graph → Command Center → port/GCC`

Show warehouse + end-to-end logistics, not transport alone:

- warehouse receipt/dispatch;
- zone/segregation/storage;
- inventory/batch genealogy;
- booking/pickup/loading;
- vehicle/pallet/container/seal;
- route/geofence/telemetry;
- custody handover;
- port transfer;
- destination delivery/proof;
- tamper/damage/route/condition exceptions.

If live Sinotrans APIs are unavailable, keep the complete workflow operational against a development provider and clearly label provider state.

### Port & Customs API

Show authorised officer journey:

`Authenticate → scan/lookup shipment → reconcile product/batch/container/seal → view authorised trust packet/evidence refs → inspect/sample → hold/release under sovereign authority → signed event returned to AHTE`

Origin and GCC destination officer surfaces must be fully implemented even before live sovereign endpoints are connected.

### Shariah Finance / Takaful / Tokenomics

Target-state section:

`Authorised AHTE trust/trade data → Shariah Financing API → bank/financier/Takaful/tokenomics services`

Show:

- Islamic trade finance;
- purchase/order financing;
- inventory/shipment financing;
- Takaful underwriting;
- claims evidence;
- asset/shipment state verification;
- tokenomics/digital-value mechanisms where legally, regulatorily and Shariah approved.

Clearly state:

- AHTE trust state is not credit approval;
- Halal certification is not financing approval;
- Takaful operator retains underwriting/claim decision;
- tokenisation does not itself create title, regulatory approval or Shariah compliance.

The complete finance/Takaful/tokenomics integration architecture and UI must be built even where live counterparties are not yet connected; use development providers without representing them as live institutions.

## 5. Required pages

### `/how-it-works`

Explain physical chain, four synchronized trust chains, digital twins, evidence/trust graph, trust state, authority propagation and role-based transparency.

### `/ahte`

Modules: standards/applicability, HCP/SCCP, evidence graph, trust graph, digital twins, AI/ML, CAPA, direct JAKIM API, cryptographic integrity, trust packets and recall traversal.

### `/manufacturers`

Full qualification/onboarding journey, enterprise/facility/product/formula/material data, systems inventory, lab plan, smart-glass audit, CAPA, authority workflow, monitoring and GCC readiness.

### `/smart-glass-audit`

Device + auditor identity, scope, requirement-guided inspection, offline capture, integrity, AI assist, findings/CAPA/re-verification and signed reconciliation.

### `/lab-origin`

Origin/provenance + physical identity/serialization + packaging aggregation + traceability scans + anti-diversion + sample/custody + LIMS/API + method/QC + result/integrity + direct-JAKIM linkage + downstream graph.

### `/monitoring`

Platinum profiles, sensors/edge, manufacturer/lab, warehouse/logistics, container/seal, route/geofence, traceability anomalies, exceptions, CAPA, receiving and recall.

### `/command-center`

Joint 24/7 GHSCL operational + authorised JAKIM authority-side monitoring, role separation and predictive/preemptive operating loop.

### `/standards-governance`

Separate:
1. Shariah/fatwa
2. competent authority
3. certification operating instruments
4. Malaysian Standards/test methods
5. AHTE digital assurance

### `/china-gcc`

China origin + traceability/lab + manufacturer + direct JAKIM/human authority workflow + Sinotrans + ports + GCC receiving. Mark shipment workflow as pilot.

### `/ports-customs`

Officer API/trust gateway, custody/inspection/release and sovereign decision boundary.

### `/shariah-finance`

Shariah financing API, Takaful and tokenomics plane with external decision boundaries and complete development-mode workflows.

### `/ecosystem`

Partner cards distinguish project role, executed status, public/source status and authority boundary.

### `/verify`

Inputs:
- Trust Record ID
- product/SKU
- physical code / QR/NFC
- batch/lot
- shipment ID
- certificate reference

Results separate:
1. identity / authenticity status where authorised
2. formal certification/authority status
3. AHTE trust state
4. supply-chain state
5. provenance
6. lab evidence summary
7. custody timeline
8. exceptions/holds
9. integrity verification
10. last verified timestamp

### `/about`

GHSCL role, China→GCC mission, AHTE architecture, joint 24/7 Command Center and principle: AI assists; humans/authorities decide.

### `/apply` + `/contact`

Routes: manufacturer; laboratory; logistics; GCC importer/buyer; government/institutional; port/customs; finance/Takaful; technology/API; media/general.

## 6. Authenticated portal surfaces

The production architecture must provide separate role-based applications for:

- Manufacturer
- Auditor / Smart Glass
- Laboratory + Traceability
- Sinotrans / Logistics Control Tower
- GHSCL Command Center
- JAKIM Authority View
- PHC authorised workflow view as applicable
- Port / Customs Officer
- GCC Importer / Buyer
- Finance / Takaful
- Administrator / Governance

Do not force these into a single generic dashboard. Do not omit a portal because its external production connector is unavailable; use the corresponding development provider.

## 7. State vocabulary

### AHTE trust state

`INITIAL · EVIDENCE-COMPLETE · ASSESSED · VERIFIED · VERIFIED-WITH-EXCEPTION · HOLD · CORRECTIVE-ACTION · RE-VERIFICATION · QUARANTINED · DISPUTED · EXPIRED · SUSPENDED · REVOKED · RECALLED`

### Certification / authority state

Display separately and map to actual authority-system values when production connected. Development/sandbox values must be visibly identified as such.

### Supply-chain state

`origin verified · sample/lab · manufactured · packed · warehouse received · shipment created · sealed · in transit · port hold/release · GCC arrived · received · accepted · exception`

### Port/customs, finance, Takaful and token state

Keep each separate from certification/AHTE trust/supply-chain state.

### Connector state

Every external integration exposes one of:

`development-provider-active · sandbox-connected · production-connected · production-credentials-required`

Connector state must never be conflated with authority/trust/supply-chain state.

## 8. Design direction

The visual language is **critical digital infrastructure / institutional trust technology**.

Use:
- dark institutional base;
- emerald/green operational trust accents;
- restrained gold for authority/verified events;
- dense but legible data visualization;
- event nodes/graph paths;
- physical-chain imagery;
- command-center views;
- smart-glass HUD visualizations;
- lab/sample/physical-code visualization;
- logistics/port/GCC maps.

Avoid:
- generic mosque/minaret clichés as primary identity;
- cryptocurrency visual language;
- certificate-stamp aesthetics as the entire product;
- decorative blockchain cubes implying blockchain certification;
- fake live dashboards or fake authority marks.

## 9. Technical architecture

Preferred implementation:

- Next.js / React / TypeScript unless current local stack dictates an equivalent architecture;
- server-rendered/static public pages;
- authenticated apps separated from public marketing surfaces;
- governed content objects sourced from repository registries;
- API gateway/BFF for verification/status queries;
- RBAC/ABAC/purpose-aware access;
- auditable access/events;
- multilingual routing;
- structured metadata/SEO;
- privacy/security headers;
- accessibility;
- staging/production separation;
- telemetry/observability;
- typed production adapter contracts;
- replaceable development/sandbox providers;
- explicit connector-state metadata;
- event-first domain architecture;
- no UI/domain redesign when a real connector replaces a development provider.

Public content should consume governed data from:

- `00_EXECUTIVE_COMMAND/current-target-architecture-2026-09-30.json`;
- `00_EXECUTIVE_COMMAND/PLATFORM_REQUIREMENTS_TRACEABILITY_2026-09-30.md`;
- `partner-registry.json`;
- standards registries / verified stack;
- `corridor-registry.json`;
- `port-authority-registry.json`;
- `trust-packet-schemas.json`;
- website-specific controlled-copy files.

## 10. Security and disclosure

Never expose:

- JAKIM endpoint/credential secrets;
- laboratory confidential source records;
- manufacturer formulas/BOM where not authorised;
- internal risk features/sensitive model data;
- raw cross-border data outside approved policy;
- private finance/underwriting data;
- authority security controls.

Use minimum-necessary selective disclosure.

Security requirements must not become arbitrary feature deletion. Preserve complete capability with correct identity, permissions, disclosure and connector-state controls.

## 11. Acceptance criteria

The rebuild is not complete until all are demonstrable:

1. China→GCC direct is the visible physical corridor.
2. Malaysia governance/assurance is not confused with mandatory physical transit.
3. PHC, GHSCL, AHTE, JAKIM, traceability/lab, Sinotrans, ports, GCC and finance roles are separated.
4. Raw-material origin starts the traceability chain.
5. Manufacturer onboarding is first-class.
6. China one-item-one-code / physical identity / unit-box-carton-pallet aggregation / anti-diversion is represented.
7. Laboratory/sample chain precedes manufacturing release.
8. Smart-glass AI-assisted audit is first-class.
9. Complete standards/applicability logic is represented.
10. Direct JAKIM API is the intended authority connectivity path; no NurAI/generic intermediary hop.
11. PHC + JAKIM authorised human approve/disapprove workflow is represented accurately.
12. Joint 24/7 GHSCL operational + authorised JAKIM authority-side Command Center monitoring is first-class.
13. AI/ML predictive analytics are visible.
14. Preemptive Strategy Engine is visible.
15. Sinotrans warehouse + end-to-end logistics monitoring are represented.
16. Port/customs API workflow is represented.
17. GCC receiving is represented.
18. Shariah Financing API / Takaful / tokenomics target plane is represented with boundaries.
19. Evidence hashing/signatures/integrity are explained without claiming hashes certify Halal.
20. Formal authority, AHTE trust, supply-chain, port/customs, finance and Takaful/token states are distinct.
21. Verification supports product/batch/shipment/physical-code/trust-record views.
22. Role-based transparency is explicit.
23. Mobile, accessibility and EN/中文/العربية/BM architecture are supported.
24. No stale China→Malaysia pilot language controls current narrative.
25. No prototype/reference runtime is described as production.
26. Every required external integration has a complete production adapter contract.
27. Every unavailable production integration has a replaceable development/sandbox provider rather than an omitted feature.
28. No required target capability is hidden behind permanent feature flags, disabled navigation or `coming soon`.
29. Public/portal screens distinguish development/sandbox/production connection state.
30. Complete target journeys execute in development mode without falsely claiming real-world approvals/events.
31. `master-standards-stack/CHINA_EXECUTION_PACK/` is the sole canonical China pack; no retired lowercase references are used.

## 12. Implementation order

### Wave 0 — repository/content parity

- ingest current target architecture registry v1.2+;
- ingest platform requirements traceability;
- reconcile stale routes/copy/references;
- establish controlled content source;
- build shared design/status vocabulary;
- establish typed external adapter contracts/connector-state model.

### Wave 1 — public platform

Home → How It Works → AHTE → Manufacturers → Smart Glass → Lab & Origin → Monitoring → Command Center → Standards/Governance → China→GCC → Ports/Customs → Shariah Finance → Ecosystem → About → Contact/Apply.

### Wave 2 — verification

Trust Record lookup → product/physical-code/batch/shipment result pages → QR/NFC route → evidence integrity verification.

### Wave 3 — authenticated role apps

Manufacturer → Auditor → Laboratory/Traceability → Sinotrans Logistics → GHSCL Command Center → JAKIM view → PHC workflow → Port/Customs → GCC Importer → Finance/Takaful → Admin/Governance.

### Wave 4 — complete development integration providers

Implement replaceable development providers for JAKIM, China traceability/lab/LIMS, Sinotrans, origin port/customs, GCC port/customs, importer/retailer, finance, Takaful and tokenomics where production connectors are absent.

## 13. Master public narrative

> **Global Halal Supply Chain Limited operates the international digital infrastructure for a complete China-origin to GCC-destination Halal trust chain. AHTE continuously links applicable standards, verified raw-material provenance, China physical identity and laboratory evidence, manufacturer controls, AI-assisted smart-glass audits, cryptographic evidence integrity, Sinotrans warehousing and end-to-end logistics, port/border events and GCC receiving into a live evidence and trust graph. AI/ML predicts risk and generates preemptive strategies for governed human action. The 24/7 Command Center is jointly monitored by GHSCL operational roles and authorised JAKIM authority-side roles under distinct permissions, while AHTE connects directly to JAKIM through the authorised JAKIM API and formal approval/disapproval remains in the PHC + JAKIM human workflow. The platform also provides controlled port-authority interfaces and a complete Shariah-financing/Takaful/tokenomics integration plane without conflating digital trust with certification, customs authority, credit approval or underwriting decisions. Where production connectors are not yet provisioned, the full capability remains implemented through replaceable development providers so the real connector can be introduced without architectural redesign.**
