# Codex Master Prompt — Global Halal Digital Trust Platform Rebuild

## Control metadata

- Revision: v2.2.0
- Control date: 2026-09-30
- Governing architecture: `00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md` v1.2+
- Machine architecture registry: `00_EXECUTIVE_COMMAND/current-target-architecture-2026-09-30.json` v1.2+
- Requirements traceability: `00_EXECUTIVE_COMMAND/PLATFORM_REQUIREMENTS_TRACEABILITY_2026-09-30.md`
- Implementation completeness: `00_EXECUTIVE_COMMAND/IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md`
- Website specification: `docs/WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md`
- Freeze: `master-standards-stack/verified-2026-09-17/` — DO NOT MODIFY
- Default pilot: `[PILOT: shipment workflow — China → GCC direct]`

---

# COPY FROM HERE INTO PC CODEX

You are rebuilding the Global Halal Digital Trust Ecosystem website/platform from the actual repository and local project, not from a generic brief.

# 0. NON-NEGOTIABLE IMPLEMENTATION PRINCIPLE — NO ARTIFICIAL BLOCKS OR LIMITS

**FULL ARCHITECTURE NOW → REAL CONNECTORS WHEN AVAILABLE → NO REDESIGN REQUIRED.**

This instruction governs the entire build.

Do **not** remove, disable, downgrade, hide, omit, defer, artificially cap or redesign an intended capability merely because an external API, credential, partner feed, authority connection, laboratory interface, sensor stream, production dataset, financing counterparty, Takaful operator, port system, logistics feed or real transaction is not presently available in the local development environment.

Build the **complete production-target architecture now**, including:

- all public routes;
- all authenticated role surfaces;
- complete domain models;
- typed interfaces;
- API contracts;
- event schemas;
- adapters;
- portal states;
- dashboards;
- command-center views;
- workflow state machines;
- error/retry/reconciliation paths;
- auditability;
- security boundaries;
- multilingual architecture;
- integration boundaries;
- predictive/preemptive analytics surfaces;
- finance/Takaful/tokenomics integration surfaces;
- complete verification flows.

Where an external dependency is unavailable:

1. implement the **real production integration boundary** as a typed adapter/interface;
2. implement a replaceable sandbox/mock/test provider at that boundary;
3. preserve the complete production workflow and user experience;
4. expose dependency state truthfully (`sandbox`, `mock`, `not connected`, `production connected`) rather than deleting the feature;
5. design the connector so the real integration can replace the development provider without rewriting domain logic or UI architecture.

A development mock may substitute **connectivity/data**, but it must not reduce **capability**.

Do not create arbitrary feature caps on:

- manufacturer onboarding volume;
- supplier/material depth;
- evidence ingestion;
- smart-glass auditing;
- lab/LIMS integration;
- traceability depth;
- digital twins;
- cryptographic evidence;
- direct JAKIM connectivity;
- Sinotrans warehouse/logistics monitoring;
- port/customs API access;
- GCC workflows;
- Command Center monitoring;
- AI/ML analytics;
- predictive risk;
- preemptive strategies;
- recall traversal;
- Shariah financing;
- Takaful;
- tokenomics;
- stakeholder portals;
- APIs;
- languages;
- geographic scale;
- future partner/corridor scale.

Do **not** use `TODO`, `coming soon`, permanent feature flags, disabled navigation, blank placeholder pages or demo-only architectural shortcuts as substitutes for the target capability. A temporary development adapter is acceptable only when the complete target workflow, interface and state model are implemented.

Do not fabricate live authority approvals, lab results, credentials, Sinotrans events, port/customs releases, GCC acceptance, financing approvals, Takaful underwriting decisions, token regulatory status, production telemetry or transaction-native shipment workflow evidence. **Truthfulness of live state is required; architectural completeness is also required. These are not contradictory.**

# 1. Working rules

1. **Inspect before editing.** Inventory the local project, framework, routes, components, assets, dependencies, build tooling, environment files, git status and deployment configuration first.
2. **Preserve user work.** Do not reset, delete or overwrite unrelated uncommitted changes.
3. **Do not modify** `master-standards-stack/verified-2026-09-17/`.
4. Use the repository as the controlled architecture source. Read at minimum:
   - `00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md`
   - `00_EXECUTIVE_COMMAND/current-target-architecture-2026-09-30.json`
   - `00_EXECUTIVE_COMMAND/PLATFORM_REQUIREMENTS_TRACEABILITY_2026-09-30.md`
   - `00_EXECUTIVE_COMMAND/IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md`
   - `00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md`
   - `00_EXECUTIVE_COMMAND/hitm-decision-class-registry.json`
   - `00_EXECUTIVE_COMMAND/trust-packet-schemas.json`
   - `00_EXECUTIVE_COMMAND/schema-registry.json`
   - `00_EXECUTIVE_COMMAND/partner-registry.json`
   - `00_EXECUTIVE_COMMAND/corridor-registry.json`
   - `00_EXECUTIVE_COMMAND/port-authority-registry.json`
   - `05_PLATINUM_REAL_TIME_MONITORING/PLATINUM_FULL_STACK_ARCHITECTURE.md`
   - `05_PLATINUM_REAL_TIME_MONITORING/AHTE_24_7_COMMAND_CENTER_SPEC_2026-09-30.md`
   - `05_PLATINUM_REAL_TIME_MONITORING/PLATINUM_COMMAND_CENTER_INTEGRATION_ADDENDUM_2026-09-30.md`
   - `master-standards-stack/CHINA_EXECUTION_PACK/00_MASTER_CHINA_EXECUTION_MODEL.md`
   - `master-standards-stack/CHINA_EXECUTION_PACK/04_FACTORY_SYSTEM_API_CONTRACTS.md`
   - `master-standards-stack/CHINA_EXECUTION_PACK/05_SMART_GLASS_AUDIT_SPEC.md`
   - `master-standards-stack/CHINA_EXECUTION_PACK/06_PORT_OFFICER_UI_WORKFLOW.md`
   - `master-standards-stack/CHINA_EXECUTION_PACK/07_CRYPTOGRAPHIC_TRUST_ANCHOR_ARCHITECTURE.md`
   - `partners/china-food-security-lab/AHTE_CHINA_LAB_TRACEABILITY_INTEGRATION_PROFILE_2026-09-30.md`
   - `deliverables/07_SINOTRANS_PLAYBOOK.md`
   - `deliverables/22_IQ300_JAKIM_MALAYSIAN_STANDARDS_INTELLIGENCE_LAYER.md`
   - `deliverables/29_GLOBAL_PORT_AUTHORITIES_PROTOCOL_2026.md`
   - `deliverables/31_SHARIAH_FINANCING_API_TAKAFUL_TOKENOMICS_ARCHITECTURE_2026.md`
   - `docs/WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md`
   - `STATUS.md`
5. Where old project-level wording conflicts with the 30 Sep current target architecture, use the current target architecture. Do not use old China→Malaysia pilot wording.
6. `master-standards-stack/CHINA_EXECUTION_PACK/` is the sole canonical China execution pack. Do not recreate or reference the retired lowercase duplicate lineage.
7. Separate **target architecture** from **production reality**. Do not claim undeployed integrations are already live merely because complete adapters/UI states exist.
8. Do not hard-code secrets, credentials, production JAKIM endpoints, lab credentials, manufacturer formulas, private authority schemas or finance data.
9. Build external integrations behind complete adapter contracts so real connectors can replace development providers without domain/UI redesign.
10. Do not interpret an unavailable external dependency as permission to omit the corresponding product capability.

# 2. Core platform proposition

Build a complete Global Halal Digital Trust & Trade / Halal Tayyib infrastructure spanning:

```text
VERIFIED RAW-MATERIAL ORIGIN
→ SUPPLIER / PRODUCER / PROVENANCE / LOT
→ PHYSICAL + DIGITAL IDENTITY
→ SAMPLE / SEAL / CHAIN OF CUSTODY
→ CHINA TRACEABILITY / ANTI-COUNTERFEIT + LABORATORY SYSTEM
→ SIGNED SCIENTIFIC EVIDENCE
→ MANUFACTURER / FACTORY SYSTEMS
→ PRODUCT / FORMULA / BOM / MATERIAL / PROCESS
→ STANDARDS / APPLICABILITY
→ HCP / SCCP / CONTROLS
→ SMART-GLASS AI-ASSISTED SITE AUDIT
→ FINDING / CAPA / RE-VERIFICATION
→ DIRECT JAKIM API
→ PHC + JAKIM AUTHORISED HUMAN REVIEW / APPROVE-DISAPPROVE WORKFLOW
→ FORMAL AUTHORITY STATUS
→ AHTE TRUST-STATE PROPAGATION
→ UNIT / BOX / CARTON / BATCH / LOT / PALLET
→ SINOTRANS WAREHOUSE
→ SINOTRANS END-TO-END LOGISTICS
→ CONTAINER / SEAL / TELEMETRY / CUSTODY
→ ORIGIN PORT / CUSTOMS API
→ INTERNATIONAL TRANSIT
→ GCC PORT / CUSTOMS API
→ IMPORTER / DESTINATION WAREHOUSE
→ DISTRIBUTION / RETAIL
→ BUYER / CONSUMER AUTHORISED VERIFICATION
```

Across the entire chain:

```text
AHTE EVENT + EVIDENCE FABRIC
+ DIGITAL TWINS / EVIDENCE GRAPH / TRUST GRAPH
+ CRYPTOGRAPHIC INTEGRITY + APPEND-ONLY HISTORY
+ 24/7 JOINT GHSCL + AUTHORISED JAKIM COMMAND CENTER MONITORING
+ AI/ML PREDICTIVE ANALYTICS
+ PREEMPTIVE STRATEGY ENGINE
+ ROLE-BASED AUTHORISED TRANSPARENCY
```

Target transaction-support plane:

```text
Authorised AHTE trust/trade data
→ Shariah Financing API
→ Islamic financing / Takaful / tokenomics
```

# 3. Non-negotiable role model

Represent these as connected but separate roles:

- **PHC** — Perak State Government halal-industry GLC operating locally and internationally.
- **GHSCL Hong Kong** — international operating and digital-infrastructure vehicle; 24/7 corridor/platform operational monitoring role.
- **AHTE** — standards, applicability, evidence, compliance, traceability, trust-state and AI/ML intelligence.
- **Direct JAKIM API** — direct authorised authority-system connectivity. Do not insert NurAI or an unnecessary public intermediary.
- **PHC + JAKIM authorised human workflow** — the project formal certification approval/disapproval workflow, including Mufti/scholars/authorised halal officers or decision-makers as applicable. AI/AHTE do not make the formal certification decision.
- **China traceability / anti-counterfeit system** — physical/product identity, serialization, packaging aggregation and scan/channel event source.
- **China laboratory** — analytical evidence producer.
- **Smart-glass auditors** — human-accountable physical verification.
- **Sinotrans** — end-to-end warehouse + logistics operator and real-time evidence source.
- **Port/customs authorities** — sovereign inspection/clearance/release decision owners; use AHTE API/trust interface.
- **GCC importers/authorities/warehouses/retail** — destination acceptance and receiving layer.
- **Finance/Takaful/tokenomics actors** — independent transaction-support decision owners.

Never visually imply that JAKIM is owned by, subordinate to or a commercial department of GHSCL.

Never claim AI, blockchain, QR, microdot, VOID labels, hashes, sensors or lab results independently create Halal certification.

# 4. Default corridor

The physical pilot corridor is:

**China → GCC direct**

Malaysia is the governance/assurance/authority-connectivity plane unless an explicit physical Malaysia movement is separately scoped.

Mark shipment workflow content as pilot where shown.

# 5. Four synchronized chains

The UI/data model must make these four chains reconcilable:

1. Physical chain
2. Identity/custody chain
3. Evidence chain
4. Authority/trust-state chain

Minimum material event tuple:

`WHO + WHAT + WHEN + WHERE + OBJECT + REQUIREMENT/CONTROL + EVIDENCE + VERIFIER + CURRENT STATE + INTEGRITY PROOF`

# 6. Canonical path

Use this everywhere in architecture/content:

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

# 7. AHTE engines

Implement modular UI/data/service boundaries for:

- Standards Registry
- Requirement Versioning
- Applicability Resolver
- Control Engine
- HCP/SCCP Engine
- Evidence Registry
- Evidence Graph
- Digital Twin Registry
- Trust Graph
- Trust State Machine
- Audit Engine
- Finding/CAPA Engine
- Re-verification Engine
- Direct JAKIM API Adapter
- Authority Status Synchronization
- Integrity/Signature Verification
- Recall Graph Traversal
- Evidence Gap Predictor
- Anomaly Engine
- Contradiction Engine
- Trust Fracture Engine
- Predictive Compliance Engine
- Recall Blast-Radius Engine
- Preemptive Strategy Engine

# 8. Decision-class enforcement

Use repository D0–D6 semantics:

- D0 operational ingest
- D1 encoded control execution
- D2 machine assessment
- D3 finding/CAPA classification with human accountability
- D4 trust-fracture hold; auto-hold may be allowed, auto-release prohibited where human release is required
- D5 competent-authority gate; human authority only
- D6 sovereign/legal/fatwa; human authority only

The UI must visibly separate recommendations, machine assessments, holds, authority decisions and operational releases. Model confidence never bypasses D5/D6.

# 9. 24/7 GHSCL + JAKIM Command Center

Create a first-class `/command-center` experience and reusable command-center components.

The target Command Center is **jointly monitored 24/7 by GHSCL operational roles and authorised JAKIM authority-side roles**, with distinct permissions and responsibilities.

GHSCL handles platform/corridor operations, correlation, partner coordination, exception orchestration and operational analytics within scope. JAKIM retains authority-side monitoring, evidence/status review and formal authority actions according to its implemented mandate/direct-API permissions.

Required views:

- global China→GCC corridor map;
- active manufacturers/facilities;
- supplier/raw-material/origin changes;
- China traceability/anti-counterfeit anomalies;
- lab/sample pipeline;
- HCP/SCCP risk matrix;
- smart-glass findings;
- authority/JAKIM synchronization;
- Sinotrans warehouse status;
- Sinotrans logistics/vehicle/container/seal status;
- telemetry/geofence exceptions;
- custody gaps;
- port/customs queues;
- GCC receiving;
- evidence integrity/expiry/freshness;
- CAPA/re-verification;
- predictive risk queue;
- preemptive strategy queue;
- recall/blast radius;
- finance/Takaful support state where authorised;
- audit/event timeline.

Operating flow:

`observe 24/7 → correlate → detect → predict → impact/blast radius → preemptive strategy → decision-class check → assign owner → alert/escalate/hold according to policy → human/authority action → CAPA/reverification → close/escalate/recall → learn`

Design it like serious critical infrastructure, not a crypto trading dashboard.

# 10. AI/ML predictive + preemptive UX

Every AI result must show:

- model name/version;
- input/evidence references;
- timestamp;
- prediction horizon where applicable;
- score/confidence;
- explanation/risk drivers;
- affected objects;
- recommended action;
- required decision class/human role;
- current review status;
- outcome when known.

Build sample cards for:

- supplier evidence expiry risk;
- predicted cold-chain excursion;
- sample/batch mismatch;
- route deviation risk;
- recurring HCP nonconformity;
- evidence completeness gap;
- possible counterfeit/diversion or impossible-scan-geography pattern;
- possible recall blast radius.

No AI output should look like an official certificate or authority decision.

# 11. Manufacturer onboarding application

Build complete journey:

`Application → KYB → Facility → Products/SKUs → Formula/BOM → Materials → Suppliers → Origin → Existing Evidence → System Inventory → Digital Twin → Requirements → HCP/SCCP → Evidence Gap → Remediation/Training → Lab Plan → Smart-Glass Audit → Findings/CAR/CAPA → Re-verification → Direct JAKIM API / PHC+JAKIM Human Authority Workflow → Continuous Monitoring → GCC Readiness`

Required data domains:

- legal entity;
- facility;
- licenses;
- management contacts;
- product/SKU;
- formula/BOM version;
- raw materials/processing aids/packaging;
- suppliers/origin;
- ERP/MES/QMS/WMS/LIMS/DMS/IoT integration inventory;
- standards/applicability;
- HCP/SCCP;
- evidence plan;
- sample/lab plan;
- audit status;
- CAPA;
- authority status;
- monitoring profile;
- destination/importer/logistics readiness.

# 12. China traceability + laboratory application

Build the physical identity / traceability functions:

- enterprise/product identity mapping;
- one-item-one-code;
- microdot / QR / VOID/tamper-evident identity where deployed;
- product/batch/code binding;
- unit → box → carton → pallet aggregation;
- extension to logistic unit → container → shipment → GCC destination inventory;
- consumer/channel verification;
- scan timestamp/geography;
- abnormal/repeated scan detection;
- anti-diversion/channel-mismatch events;
- correction/supersession rather than destructive relationship rewrite.

Build sample-centric laboratory lifecycle:

`Test request → Sample registered → Collected → Sealed → Custody transfer → In transit → Lab received/accessioned → Testing → QC → Technical review → Authorised signatory → Signed report → Hash/signature verification → AHTE evidence accepted → Direct JAKIM authority review linkage`

Exceptions:

- rejected sample;
- chain-of-custody break;
- method out of scope;
- QC failure;
- sample/object binding mismatch;
- corrected/withdrawn report;
- signature invalid;
- hash mismatch;
- duplicate/replay;
- re-test required.

Use `master-standards-stack/CHINA_EXECUTION_PACK/api/china-food-security-lab-openapi-extension.yaml` and the consolidated lab/traceability profile as target guidance, but do not treat placeholder endpoints as live production endpoints.

**Hard rule: `NOT_DETECTED != HALAL`.**

# 13. Smart-glass application

Required flow:

`device identity + auditor identity + MFA + role/scope → assigned audit → site/scope → requirements/HCPs → scan object → capture evidence → local hash → AI assist → auditor assessment → finding/CAR → re-verification → sign → sync/reconcile`

Build the complete workflow and UI states for:

- QR/DataMatrix/OCR/NFC;
- still/video capture;
- voice commands;
- sensor/location evidence where permitted;
- offline queue;
- device trust status;
- evidence hash/signature;
- object/requirement binding;
- signed session;
- synchronization/reconciliation;
- conflict detection;
- revoked/expired device state;
- finding/CAR/CAPA/re-verification.

When physical smart-glass hardware is unavailable locally, emulate the capture/device events through a development provider without removing the wearable workflow or changing its production contracts.

# 14. Sinotrans logistics control tower

Build dedicated role surface for:

- warehouse receipts;
- storage zones;
- segregation;
- quarantine/release/reject;
- stock/batch genealogy;
- bookings;
- pickup/loading;
- vehicle/pallet/container/seal;
- route/geofence;
- temperature/humidity/product-specific telemetry;
- custody handovers;
- port transfer;
- destination delivery;
- exceptions and proof of delivery.

Adapter topology:

`Sinotrans WMS/TMS/Y2T/MIS/EDI/IoT → secure adapter/API → canonical AHTE event → evidence/trust graph → Command Center`

If production Sinotrans access is unavailable, use a replaceable Sinotrans development adapter with complete event contracts and realistic state transitions. Do not remove or downgrade the logistics/warehouse capability. Do not claim development events are real Sinotrans production events.

# 15. Port/customs authority surface

Build `/ports-customs` and authenticated officer workspace.

Flow:

`authenticate officer/device → lookup/scan shipment → verify container/seal → authorised trust packet → document/evidence refs → inspection/sampling → hold/release decision under sovereign authority → signed event return`

Display clearly:

- official authority release state;
- AHTE trust state;
- custody state;
- unresolved exceptions;
- last verified time.

These must not be merged into one badge.

Implement a complete port/customs adapter contract and development provider for both origin and GCC destination paths. Do not disable the port/customs experience because live government endpoints are not connected.

# 16. Direct JAKIM API + formal human authority workflow

Architecture displayed publicly:

`AHTE ⇄ DIRECT JAKIM API ⇄ JAKIM → PHC + JAKIM authorised human review/decision workflow`

Do not insert NurAI or a generic external gateway in this topology.

Implement the complete internal production adapter interface plus development/sandbox provider.

Suggested application-side interface shape only:

```ts
interface JakimAuthorityAdapter {
  submitEvidenceBundle(input: AuthorityEvidenceBundle): Promise<AuthorityReceipt>;
  getCaseStatus(caseId: string): Promise<AuthorityCaseStatus>;
  getCertificationStatus(subjectId: string): Promise<AuthorityCertificationState>;
  subscribeToAuthorityEvents?(handler: AuthorityEventHandler): Promise<Unsubscribe>;
}
```

Do NOT hard-code an unverified official URL or credential scheme. Do NOT remove the direct-JAKIM workflow if production credentials are absent; keep the full workflow operational against the development provider with explicit connection-state labelling.

Formal approve/disapprove remains a human authority action. In the project operating model the review path is PHC + JAKIM authorised humans, including Mufti/scholars/authorised halal officers or decision-makers as applicable.

# 17. Shariah Financing API / Takaful / tokenomics

Build the **complete target integration plane**, public page, portal surfaces, domain models and adapter contracts. Do not hide this behind a permanent feature flag and do not reduce it to a “coming soon” card merely because production counterparties are not yet connected.

Required functions:

- trade-finance eligibility evidence packet;
- PO/order evidence;
- inventory/shipment state;
- trust assertion retrieval;
- financing application/evidence workflow;
- financing status callback/event model;
- Takaful underwriting evidence packet;
- policy/coverage reference model;
- claim evidence/custody/incident packet;
- claims status event model;
- asset state verification;
- tokenized/digital-value asset representation model;
- token lifecycle/state model;
- asset/evidence binding;
- transfer/encumbrance/reference hooks as applicable;
- legal/Shariah/regulatory approval-state fields;
- audit/history/integrity fields.

Decision boundary:

- AHTE does not approve financing;
- AHTE does not underwrite Takaful;
- tokenization does not create title or regulatory/Shariah approval by itself;
- bank/Takaful/regulator/human Shariah decisions stay external;
- development providers must never be represented as live financial institutions.

If counterparties are absent, provide complete sandbox adapters and end-to-end development state machines so real providers can connect without redesign.

# 18. Verification experience

Build `/verify` supporting:

- Trust Record ID;
- Product/SKU;
- Batch/Lot;
- Shipment ID;
- QR/NFC/physical-code deep link;
- Certificate reference.

Result page sections:

1. Identity
2. Formal certification/authority state
3. AHTE trust state
4. Supply-chain state
5. Provenance
6. Lab evidence summary
7. Custody timeline
8. Current exceptions/holds
9. Integrity verification
10. Last verified timestamp

Use role-based redaction for private data.

# 19. Data model foundations

Represent at minimum:

- Organisation
- Facility
- Product
- FormulaVersion
- Material
- Supplier
- PhysicalIdentifier
- PackagingAggregation
- TraceabilityScanEvent
- Requirement
- Control
- HCP/SCCP
- Evidence
- EvidenceManifest
- EvidenceIntegrityProof
- Sample
- SampleCustodyEvent
- LabResult
- Audit
- AuditObservation
- Finding
- CAPA
- Reverification
- AuthorityCase
- AuthorityDecision
- TrustAssertion
- TrustState
- Batch
- Lot
- Unit/Box/Carton/Pallet
- Container
- Seal
- Shipment
- CustodyTransfer
- TelemetryEvent
- PortEvent
- PortInspection
- FinanceEvidencePacket
- FinancingCase
- TakafulCase
- TakafulClaim
- TokenizedAssetReference
- Alert
- Prediction
- PreemptiveStrategy
- RecallCase
- CommandCenterIncident

Use stable IDs and event history. Do not silently overwrite material history; use version/supersession/compensating events.

# 20. Event architecture

Implement an event-first domain boundary. Critical state changes must be representable as attributable events with:

`event_id + object_id + actor_id + occurred_at + jurisdiction + source_system + event_type + payload_ref + evidence_refs + requirement/control refs + content_hash + signature/authentication ref + previous_event + resulting_state`

Required event families include:

- manufacturer/onboarding;
- material/supplier;
- traceability/serialization/anti-diversion;
- sample/lab;
- manufacturing/HCP/SCCP;
- audit/finding/CAPA;
- authority status;
- warehouse;
- shipment/container/seal;
- telemetry/geofence;
- custody;
- port/customs;
- GCC receiving;
- finance/Takaful/tokenomics support state;
- prediction/preemptive strategy;
- incident/recall.

Support idempotency, out-of-order handling, replay protection concepts, offline reconciliation and compensating/corrective events.

# 21. Security

Build with:

- strict typed schemas;
- RBAC/ABAC/purpose-ready permission layer;
- secure session handling;
- no secrets in client bundles;
- content security policy and secure headers;
- audit logging hooks;
- input validation;
- idempotency for event mutation APIs;
- anti-replay concepts for signed events;
- signed/hash verification interfaces;
- selective disclosure;
- data-residency aware abstractions;
- offline reconciliation patterns;
- error states that never imply success when dependency is unavailable;
- explicit provider/connection-state metadata;
- key/credential rotation abstractions;
- revocation-state handling;
- immutable/tamper-evident evidence history abstractions.

Do not bridge AHTE directly into safety-critical PLC/OT control. Use `OT/SCADA → MES/edge → validated integration gateway → AHTE`.

# 22. Web design system

Visual language:

- institutional dark base;
- emerald trust accent;
- restrained gold for authority/verified state;
- data-rich graph/node language;
- clean typography;
- premium but serious critical-infrastructure feel;
- excellent responsive/mobile behavior;
- WCAG-conscious contrast;
- keyboard navigation;
- reduced-motion mode;
- no critical status conveyed by colour only.

Avoid:

- generic mosque imagery as dominant design;
- excessive gold luxury styling;
- crypto/token trading aesthetics;
- blockchain cubes;
- fake government seals;
- fake live telemetry presented as production data.

# 23. Required public routes

Create and fully implement:

- `/`
- `/how-it-works`
- `/ahte`
- `/manufacturers`
- `/smart-glass-audit`
- `/lab-origin`
- `/monitoring`
- `/command-center`
- `/standards-governance`
- `/china-gcc`
- `/ports-customs`
- `/shariah-finance`
- `/ecosystem`
- `/verify`
- `/about`
- `/apply`
- `/contact`

Do not leave any required route as an empty shell.

# 24. Authenticated role applications

Implement the architecture and usable development-mode surfaces for:

- Manufacturer Portal
- Auditor / Smart-Glass Workspace
- Laboratory + Traceability Console
- Sinotrans / Logistics Control Tower
- GHSCL Command Center
- JAKIM Authority View
- PHC authorised workflow view as applicable
- Port / Customs Officer Workspace
- GCC Importer / Buyer Portal
- Finance / Takaful Portal
- Administrator / Governance Console

These may be nested under `/portal/*`, but they must be distinct role experiences, not one generic dashboard with renamed headings.

# 25. Languages

Prepare complete routing/content architecture for:

- English canonical copy
- Simplified Chinese
- Arabic / RTL
- Bahasa Malaysia

Do not machine-publish uncontrolled regulatory translations. Use translation resources with review/source metadata. The presence of untranslated controlled regulatory text must not disable the multilingual application architecture.

# 26. Content governance

Do not duplicate source-sensitive claims in many components.

Create governed content loaders for:

- current target architecture JSON;
- platform requirements traceability;
- partner registry;
- corridor registry;
- port authority registry;
- standards registry;
- trust schema/status vocabulary;
- controlled public copy.

Public/application copy must distinguish:

- verified source fact;
- project target architecture;
- proposal;
- pilot state;
- development/sandbox state;
- production/live state.

# 27. Required developer workflow

Before changing files, output a concise local audit:

- framework/version;
- package manager;
- current git branch/status;
- routes;
- component structure;
- styling system;
- assets;
- API/data layer;
- existing env variables by **name only**, never values;
- test/lint/build scripts;
- deployment config;
- conflicts with this specification.

Then implement in phases without stopping after the audit.

After each phase:

1. format/lint;
2. typecheck;
3. test;
4. production build;
5. inspect runtime console/server errors;
6. verify mobile layout;
7. verify navigation/deep links;
8. verify no secret exposure;
9. report changed files and remaining real external dependencies.

# 28. Implementation phases

## Phase A — foundation

- architecture/content registry;
- design tokens;
- app shell;
- navigation;
- shared types;
- provider/adapter interfaces;
- development providers for unavailable external systems;
- state vocabulary;
- identity/evidence timeline components;
- event model;
- role/permission model;
- connection-state model.

## Phase B — public website

Implement all public routes and responsive design.

## Phase C — verification

Trust lookup, result pages, QR/NFC/physical-code deep links, integrity display.

## Phase D — authenticated role applications

Manufacturer, Lab/Traceability, Smart Glass, Sinotrans, Command Center, JAKIM view, PHC workflow, Port/Customs, GCC Importer, Finance/Takaful and Admin/Governance.

## Phase E — integration architecture

Typed external adapter interfaces, development providers, event bus abstraction, observability, error semantics, idempotency and reconciliation.

## Phase F — analytics/intelligence

Predictive analytics UI/data model, Preemptive Strategy Engine workflows, incident queues, ownership/escalation and outcome capture.

## Phase G — finance/Takaful/tokenomics

Complete data models, adapters, portal workflows, evidence packet generation and sandbox state machines.

## Phase H — hardening

Accessibility, performance, security headers, tests, content-source validation, broken-link scan, production build, responsive QA and release notes.

# 29. Acceptance tests

The build is incomplete unless it demonstrates all of these:

- China→GCC direct physical corridor;
- Malaysia governance/assurance plane correctly represented;
- raw-material origin start;
- manufacturer onboarding;
- supplier/material provenance;
- China one-item-one-code / physical identity / packaging aggregation / anti-diversion traceability;
- lab/sample/custody;
- smart-glass audit;
- complete standards/applicability model;
- direct JAKIM API topology and full adapter contract;
- PHC + JAKIM authorised human approve/disapprove workflow;
- joint 24/7 GHSCL operational + authorised JAKIM authority-side Command Center monitoring;
- AI/ML predictive risk;
- preemptive strategies;
- Sinotrans warehouse + logistics;
- port/customs API workflow;
- GCC receiving;
- Shariah financing;
- Takaful;
- tokenomics integration plane;
- immutable/tamper-evident evidence explanation and verification;
- separate authority/certification, AHTE trust, supply-chain, customs, finance and Takaful states;
- role-based verification;
- D0–D6 decision-class boundaries;
- no fake live authority/partner integrations;
- complete development providers where real connectors are absent;
- no arbitrary disabled target features;
- no `coming soon` substitute for required capabilities;
- no permanent feature flag hiding required target architecture;
- no modification to the verified freeze;
- successful lint/typecheck/test/build.

# 30. Definition of done

Do not declare the rebuild complete because the homepage looks finished.

Done means:

1. required public routes are implemented;
2. required role applications are implemented to usable development-mode depth;
3. domain models exist and are typed;
4. adapter contracts exist for all external systems;
5. development providers exist where production connectors are unavailable;
6. core workflows execute end-to-end in development mode;
7. connection/live status is truthful;
8. evidence/trust/authority states remain separate;
9. predictive/preemptive workflows execute;
10. finance/Takaful/tokenomics architecture executes in sandbox mode without pretending to be live;
11. China traceability/serialization + lab evidence bind correctly into AHTE objects;
12. joint GHSCL/JAKIM Command Center role separation is enforced;
13. tests/build pass;
14. no required feature has been omitted simply because an external counterparty is not connected.

# 31. Completion report format

At the end provide:

## Implemented
Exact routes/components/services/data models completed.

## Reconciled
Old copy/routes/architecture corrected, including China→Malaysia stale wording, generic authority-gateway wording, lowercase China-pack references, split lab-profile references and any MS2400-only framing.

## Tested
Commands and pass/fail results.

## Adapter status
For each external dependency, report one of:

- `development-provider-active`
- `sandbox-connected`
- `production-connected`
- `production-credentials-required`

Cover at minimum JAKIM, China traceability/lab/LIMS, Sinotrans, origin port/customs, GCC port/customs, importer/retailer, finance, Takaful and tokenomics.

## Security
Any issues found and fixed.

## Remaining external inputs
Only inputs that genuinely require an external authority/counterparty, such as production credentials, executed agreements, official schemas, transaction data or legal/Shariah approvals. Do not convert these external inputs into disabled product features.

Do not stop after designing the homepage. Carry the rebuild through all required public routes, authenticated role surfaces, reusable system components, complete adapter interfaces, development providers, tests and production build.

# END MASTER PROMPT
