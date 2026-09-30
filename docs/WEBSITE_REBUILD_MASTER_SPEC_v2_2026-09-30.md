# Global Halal Digital Trust — Website Rebuild Master Specification v2

## Artifact metadata

| Field | Value |
|---|---|
| Artifact | `WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md` |
| Revision | v2.1.0 |
| Control date | 2026-09-30 |
| Classification | Post-freeze public website / portal architecture |
| Freeze impact | None |
| Authority effect | None |
| Governing project architecture | `00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md` |
| Machine architecture registry | `00_EXECUTIVE_COMMAND/current-target-architecture-2026-09-30.json` v1.1.0+ |
| Supersedes | `docs/WEBSITE_REBUILD_MASTER_SPEC_2026-09-30.md` where inconsistent |

[PROPOSAL: closes website/public-platform parity gap — path point: Authority → Standard / Instrument → Applicability → Control → Evidence → Audit → Authority Gate → Trust State → Operational Release]

## 0. Implementation principle — full target system, no artificial blocks

**FULL ARCHITECTURE NOW → REAL CONNECTORS WHEN AVAILABLE → NO REDESIGN REQUIRED.**

The website/platform rebuild must not remove, disable, downgrade, hide, defer or omit an intended capability merely because an external API, credential, partner feed, authority connection, laboratory interface, sensor stream, production dataset, financial counterparty or live shipment is unavailable in the development environment.

For every unavailable external dependency, implement:

1. the complete production domain model;
2. the complete production integration interface/adapter contract;
3. the complete UI/workflow/state machine;
4. a replaceable development/sandbox/mock provider at the same boundary;
5. explicit connection-state labelling so development data is never represented as live production evidence.

Development mocks substitute **connectivity/data only**. They must never substitute away capability.

Do not use `coming soon`, permanent feature flags, blank pages, disabled navigation or demo-only reductions as substitutes for required target functionality.

Do not fabricate live JAKIM decisions, laboratory results, Sinotrans telemetry, customs release, GCC acceptance, financing approval, Takaful underwriting, token regulatory/Shariah status or Shipment 001 transaction evidence.

## 1. Purpose

The website must represent the **complete Global Halal Digital Trust Ecosystem**, not a generic halal logistics site, not an MS 2400 microsite, not a blockchain-certification site, and not a brochure-only corporate page.

Primary goals:

1. Explain the complete China-origin → GCC-destination operating model.
2. Convert manufacturers/producers into qualified onboarding candidates.
3. Explain PHC, GHSCL, AHTE, JAKIM, laboratory, Sinotrans, ports, GCC and finance roles without conflation.
4. Demonstrate raw-material-to-retail traceability, live trust state, evidence integrity and authority connectivity.
5. Expose role-based public/partner verification experiences.
6. Present AI/ML predictive analytics and preemptive strategies as decision-support infrastructure.
7. Present the 24/7 GHSCL + JAKIM Command Center as a first-class operating layer.
8. Preserve the complete target architecture even where production connectors are not yet provisioned.

Core proposition:

> **Complete traceability. Live Halal trust state. Immutable evidence. Predictive assurance. Human authority. From raw-material origin in China to GCC destination.**

## 2. Mandatory system roles

| Layer | Actor | Public description |
|---|---|---|
| Malaysian halal-industry institutional layer | PHC | Perak State Government halal-industry GLC operating locally and internationally |
| International operating layer | GHSCL Hong Kong | International operating and digital-infrastructure vehicle; 24/7 monitoring/command-center operator |
| Intelligence layer | AHTE | Standards, evidence, compliance, traceability, trust-state and AI/ML intelligence |
| Authority connectivity | Direct JAKIM API | Direct authorised authority-system connectivity according to actual implementation scope |
| Human authority | JAKIM / authorised human authority workflow | Formal authority decision and certification/status control under applicable mandate |
| Scientific evidence | China laboratory pathway | Sample, method, result and evidence integrity |
| Field audit | Smart-glass workflow | Requirement-guided AI-assisted evidence capture with human auditor accountability |
| Logistics | Sinotrans | End-to-end warehouse + logistics execution and real-time custody/telemetry integration |
| Port/border | Origin/GCC authorities | Sovereign inspection/clearance/release with authorised AHTE API/trust interface |
| Destination | GCC importers/authorities/warehouses/retail | Destination acceptance, receiving and market verification |
| Finance | Shariah Financing API target plane | Financing, Takaful and tokenomics integrations subject to competent legal/Shariah/regulatory decisions |

Never imply that GHSCL/AHTE, AI, blockchain/DLT, laboratory testing, QR/NFC or telemetry independently creates official Halal certification.

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

**Subheadline:** GHSCL operates an international digital-trust infrastructure connecting raw-material origin, manufacturers, laboratories, AI-assisted smart-glass audits, real-time Sinotrans logistics, direct JAKIM API authority connectivity and GCC market verification through AHTE.

**Trust line:** Complete traceability · Live trust state · Immutable evidence · Predictive assurance · Human authority

Primary CTA: **Onboard a Manufacturer**
Secondary CTA: **Verify a Trust Record**

Hero visual must show **China → GCC direct** as the physical corridor and Malaysia as the governance/assurance plane, not a forced physical transshipment.

### Source-to-destination chain

Interactive chain:

`Raw-material origin → Supplier → Sample → Laboratory → Factory → Smart-glass audit → Human authority workflow → Packaging → Sinotrans warehouse → Sinotrans logistics → Origin port → Transit → GCC port → Importer → Destination warehouse → Retail / verification`

Each node exposes:

- object identity;
- actor;
- applicable requirement/control;
- evidence type;
- timestamp;
- integrity proof;
- current trust state;
- exceptions/holds;
- authority status where applicable.

### Institutional architecture

Use separated, non-hierarchical cards:

- PHC
- GHSCL Hong Kong
- AHTE
- Direct JAKIM API / Human Authority
- China Laboratory
- Sinotrans
- GCC Authorities / Importers

Do not draw JAKIM as a subsidiary of GHSCL.

### Manufacturer onboarding

Lifecycle:

`Enterprise application → KYB/due diligence → facility qualification → product/SKU → formula/BOM → raw materials/suppliers → origin provenance → system inventory → digital twins → applicability resolution → HCP/SCCP → evidence gaps → remediation/training → lab/sample plan → smart-glass audit → findings/CAR → re-verification → direct JAKIM API/human authority workflow → continuous monitoring → China→GCC release`

### Smart-glass audit

Display:

`Authenticate device/auditor → load audit → verify facility/scope → requirements/HCPs → scan object → capture media/document/sensor evidence → local hash → AI assist → auditor finding → CAR → re-verification → sign/sync`

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

`Origin lot → sample → seal → custody → lab receipt/accession → method/QC → technical review → signed result → hash/signature → AHTE → material release/hold`

Message: scientific evidence is bound to sample identity, chain of custody and method scope; **NOT DETECTED ≠ HALAL**.

### Standards intelligence

Show the canonical path:

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP/SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

The site must dynamically represent the complete applicable Malaysian standards/JAKIM operating framework and destination rules. Do not hard-code MS 2400 as the whole system.

### Immutable evidence fabric

Explain:

`Actor + Object + Event + Evidence + Timestamp + Device/System + Requirement + Hash + Authentication/Signature + Previous-event reference`

Clarify that hashing proves integrity after creation; it does not by itself prove truth, authority or Halal status.

### Platinum real-time monitoring

Show live domains:

- raw material/supplier changes;
- lab/sample status;
- HCP/SCCP exceptions;
- production batch state;
- warehouse status;
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

`Observe → Correlate → Detect → Predict → Model impact → Generate preemptive strategy → Human/policy review → Preventive action → Outcome feedback`

Do not portray model confidence as authority.

### 24/7 GHSCL + JAKIM Command Center

This is a dedicated homepage section and dedicated page.

Show a control-room style interface with:

- live corridor map;
- manufacturer/facility status;
- lab/sample queue;
- evidence freshness;
- HCP/SCCP alerts;
- Sinotrans warehouse/logistics status;
- shipment/container/seal state;
- port/GCC events;
- predictive risk queue;
- preemptive strategy queue;
- exception/CAPA ownership;
- escalation status;
- recall blast radius;
- authority/API synchronization state.

Operating loop:

`24/7 observe → detect → predict → recommend → assign → escalate/hold where policy allows → human/authority action → re-verify → close → learn`

### Direct JAKIM API

Public diagram:

`AHTE ⇄ Direct JAKIM API ⇄ JAKIM authority system / authorised human workflow`

No public endpoint names, credentials, internal schemas, secret keys or security-sensitive details.

The full direct-JAKIM workflow must exist in development through a replaceable provider if production credentials are unavailable; the UI must clearly distinguish development/sandbox from production-connected state.

### Sinotrans

Dedicated section:

`Factory/warehouse → Sinotrans WMS/TMS/Y2T/MIS/EDI/IoT → secure adapter/API → canonical AHTE events → Command Center → port/GCC`

Show warehouse + end-to-end logistics, not transport alone. If live Sinotrans APIs are unavailable, keep the complete workflow operational against a development provider and clearly label provider state.

### Port & Customs API

Show authorised officer journey:

`Authenticate → scan/lookup shipment → reconcile container/seal → view authorised trust packet → inspect documents/evidence/exceptions → record inspection/sampling → hold/release under sovereign authority → signed event returned to AHTE`

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
- tokenomics/digital-value mechanisms where legally and Shariah approved.

Clearly state:

- AHTE trust state is not credit approval;
- Halal certification is not financing approval;
- Takaful operator retains underwriting/claim decision;
- tokenisation does not itself create title, regulatory approval or Shariah compliance.

The complete finance/Takaful/tokenomics integration architecture and UI must be built even where live counterparties are not yet connected; use development providers without representing them as live institutions.

## 5. Required pages

### `/how-it-works`

Must explain:
- physical chain;
- four synchronized trust chains;
- digital twins;
- event/evidence graph;
- trust state;
- authority status propagation;
- role-based transparency.

### `/ahte`

Modules:
- standards/applicability;
- HCP/SCCP;
- evidence graph;
- trust graph;
- digital twins;
- AI/ML;
- CAPA;
- direct JAKIM API;
- cryptographic integrity;
- trust packet;
- recall traversal.

### `/manufacturers`

Full qualification/onboarding journey, required enterprise/facility/product/material data, integration inventory, lab plan, smart-glass audit, CAR, authority workflow, monitoring and GCC readiness.

### `/smart-glass-audit`

Device + auditor identity, assigned scope, requirement-guided inspection, offline capture, immutable evidence, AI assist, finding/CAR/re-verification, signed synchronization.

### `/lab-origin`

Origin identity, sample/custody, LIMS/API, method scope, result, hash/signature, material release/hold and downstream graph.

### `/monitoring`

Platinum profiles, sensors, edge, warehouse, logistics, container/seal, route/geofence, exceptions, CAPA, receiving, recall.

### `/command-center`

24/7 GHSCL/JAKIM monitoring experience and predictive/preemptive operating loop.

### `/standards-governance`

Separate:
1. Shariah/fatwa
2. competent authority
3. certification operating instruments
4. Malaysian Standards/test methods
5. AHTE digital assurance

### `/china-gcc`

China origin + laboratory + manufacturer + direct authority integration + Sinotrans + ports + GCC receiving. Mark Shipment 001 as pilot wherever shown.

### `/ports-customs`

Officer API/trust gateway, custody/inspection/release and sovereign decision boundary.

### `/shariah-finance`

Target Shariah financing API, Takaful and tokenomics plane with clear external decision boundaries and complete development-mode workflows.

### `/ecosystem`

Partner cards must distinguish:
- project role;
- executed status;
- public-source status;
- authority boundary.

### `/verify`

Inputs:
- Trust Record ID
- product/SKU
- batch/lot
- shipment ID
- QR/NFC
- certificate reference

Results separate:
1. AHTE trust state
2. formal certification/authority status
3. supply-chain state
4. exceptions/holds
5. last verified timestamp
6. integrity verification

### `/about`

GHSCL operating role, China→GCC mission, AHTE architecture, 24/7 command center and governance principle: AI assists; humans/authorities decide.

### `/apply` + `/contact`

Routes:
- manufacturer;
- laboratory;
- logistics;
- GCC importer/buyer;
- government/institutional;
- port/customs;
- finance/Takaful;
- technology/API;
- media/general.

## 6. Authenticated portal surfaces

The production architecture must provide separate role-based applications for:

- Manufacturer
- Auditor / Smart Glass
- Laboratory
- Sinotrans / Logistics Control Tower
- GHSCL Command Center
- JAKIM Authority View
- Port / Customs Officer
- GCC Importer / Buyer
- Finance / Takaful
- Administrator / Governance

Do not force these into a single generic dashboard. Do not omit a portal because its external production connector is not yet available; use the corresponding development provider.

## 7. State vocabulary

### AHTE trust state

`INITIAL · EVIDENCE-COMPLETE · ASSESSED · VERIFIED · VERIFIED-WITH-EXCEPTION · HOLD · CORRECTIVE-ACTION · RE-VERIFICATION · QUARANTINED · DISPUTED · EXPIRED · SUSPENDED · REVOKED · RECALLED`

### Certification / authority state

Display separately and map to actual authority-system values when production connected. Development/sandbox values must be visibly identified as such.

### Supply-chain state

`origin verified · sample/lab · manufactured · packed · warehouse received · shipment created · sealed · in transit · port hold/release · GCC arrived · received · accepted · exception`

### Connector state

Every external integration must expose one of:

`development-provider-active · sandbox-connected · production-connected · production-credentials-required`

Connector state must never be conflated with authority/trust/supply-chain state.

## 8. Design direction

The visual language is **critical digital infrastructure / institutional trust technology**.

Use:
- dark institutional base;
- emerald/green operational trust accents;
- restrained gold for authority/verified events;
- dense but legible data visualization;
- event nodes and graph paths;
- physical-chain imagery;
- command-center views;
- smart-glass HUD visualizations;
- lab/sample visualization;
- logistics/port/GCC maps.

Avoid:
- generic mosque/minaret clichés as primary identity;
- cryptocurrency visual language;
- certificate-stamp aesthetics as the entire product;
- decorative blockchain cubes implying blockchain certification.

## 9. Technical architecture

Preferred implementation:

- Next.js / React / TypeScript;
- server-rendered/static public pages;
- authenticated apps separated from public marketing surfaces;
- governed content objects sourced from repository registries;
- API gateway/BFF for verification/status queries;
- RBAC/ABAC as required;
- immutable/auditable access events;
- multilingual routing;
- structured metadata/SEO;
- privacy/security headers;
- accessibility;
- separate staging/production;
- telemetry/observability;
- typed production adapter contracts;
- replaceable development/sandbox providers for unavailable external systems;
- explicit connector-state metadata;
- event-first domain architecture;
- no UI/domain redesign required when a real external connector replaces a development provider.

Public content should consume governed data from:

- `00_EXECUTIVE_COMMAND/current-target-architecture-2026-09-30.json`;
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
- internal risk features or sensitive model data;
- raw cross-border data outside approved policy;
- private finance/underwriting data;
- authority security controls.

Use minimum-necessary selective disclosure.

Security requirements must not be implemented as arbitrary feature deletion. Preserve complete capability with correct identity, permission, disclosure and connector-state controls.

## 11. Acceptance criteria

The rebuild is not complete until all of the following are demonstrable:

1. China→GCC direct is the visible physical corridor.
2. Malaysia governance/assurance is not confused with mandatory physical transit.
3. PHC, GHSCL, AHTE, JAKIM, lab, Sinotrans, ports and GCC roles are separated.
4. Raw-material origin starts the traceability chain.
5. Manufacturer onboarding is first-class.
6. Laboratory/sample chain precedes manufacturing release.
7. Smart-glass AI-assisted audit is first-class.
8. Complete standards/applicability logic is represented.
9. Direct JAKIM API is visible as the intended authority connectivity path.
10. 24/7 GHSCL + JAKIM Command Center is a first-class surface.
11. AI/ML predictive analytics are visible.
12. Preemptive Strategy Engine is visible.
13. Sinotrans warehouse + end-to-end logistics monitoring are represented.
14. Port/customs API workflow is represented.
15. Shariah Financing API / Takaful / tokenomics target plane is represented with boundaries.
16. Evidence hashing/signatures/integrity are explained without claiming that hashes certify Halal.
17. AHTE trust state, authority/certification state and supply-chain state are separate.
18. Verification supports product/batch/shipment/trust-record views.
19. Role-based transparency is explicit.
20. Mobile, accessibility and EN/中文/العربية/BM architecture are supported.
21. No stale China→Malaysia pilot language controls current public narrative.
22. No prototype/reference runtime is described as production.
23. Every required external integration has a complete production adapter contract.
24. Every unavailable production integration has a replaceable development/sandbox provider rather than an omitted feature.
25. No required target capability is hidden behind a permanent feature flag, disabled navigation or `coming soon` placeholder.
26. Public/portal screens truthfully distinguish development/sandbox/production connection state.
27. The platform can execute the complete target journeys in development mode without falsely claiming real-world approvals or events.

## 12. Implementation order

### Wave 0 — repository/content parity

- ingest current target architecture registry v1.1.0+;
- reconcile stale routes/copy;
- establish controlled content source;
- build shared design system and status vocabulary;
- establish typed external adapter contracts and connector-state model.

### Wave 1 — public platform

Home → How It Works → AHTE → Manufacturers → Smart Glass → Lab & Origin → Monitoring → Command Center → Standards/Governance → China→GCC → Ports/Customs → Shariah Finance → Ecosystem → About → Contact/Apply.

### Wave 2 — verification

Trust Record lookup → product/batch/shipment result pages → QR/NFC route → evidence integrity verification.

### Wave 3 — authenticated role apps

Manufacturer → Auditor → Laboratory → Logistics → GHSCL Command Center → JAKIM view → Port/Customs → GCC Importer → Finance/Takaful → Admin/Governance.

### Wave 4 — complete development integration providers

Implement end-to-end replaceable development providers for JAKIM, laboratory/LIMS, Sinotrans, origin port/customs, GCC port/customs, importer/retailer, finance, Takaful and tokenomics where production connectors are absent.

## 13. Master public narrative

> **Global Halal Supply Chain Limited operates the international digital infrastructure for a complete China-origin to GCC-destination Halal trust chain. AHTE continuously links applicable standards, raw-material provenance, laboratory evidence, manufacturer controls, AI-assisted smart-glass audits, cryptographic evidence integrity, Sinotrans warehousing and logistics, port/border events and GCC receiving into a live trust graph. AI/ML predicts risk and generates preemptive strategies for authorised human review. A 24/7 GHSCL and JAKIM-connected Command Center monitors the operating chain, while direct JAKIM API connectivity propagates authorised status and human authority decisions. The platform also provides controlled interfaces for port authorities and a complete target Shariah-financing/Takaful/tokenomics integration plane without conflating digital trust with certification, customs authority, credit approval or underwriting decisions. Where production connectors are not yet provisioned, the full capability remains implemented through replaceable development providers so the production connector can be introduced without architectural redesign.**
