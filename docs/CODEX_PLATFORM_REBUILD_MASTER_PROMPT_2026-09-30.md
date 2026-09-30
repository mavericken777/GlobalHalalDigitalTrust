# Codex Master Prompt — Global Halal Digital Trust Platform Rebuild

## Control metadata

- Revision: v2.0.0
- Control date: 2026-09-30
- Governing architecture: `00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md`
- Website specification: `docs/WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md`
- Freeze: `master-standards-stack/verified-2026-09-17/` — DO NOT MODIFY
- Default pilot: `[PILOT: Shipment 001 — China → GCC direct]`

---

# COPY FROM HERE INTO PC CODEX

You are rebuilding the Global Halal Digital Trust Ecosystem website/platform from the actual repository and local project, not from a generic brief.

## 0. Working rules

1. **Inspect before editing.** Inventory the local project, framework, routes, components, assets, dependencies, build tooling, environment files, git status and deployment configuration first.
2. **Preserve user work.** Do not reset, delete or overwrite unrelated uncommitted changes.
3. **Do not modify** `master-standards-stack/verified-2026-09-17/`.
4. Use the repository as the controlled architecture source. Read at minimum:
   - `00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md`
   - `00_EXECUTIVE_COMMAND/current-target-architecture-2026-09-30.json`
   - `00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md`
   - `00_EXECUTIVE_COMMAND/hitm-decision-class-registry.json`
   - `00_EXECUTIVE_COMMAND/trust-packet-schemas.json`
   - `00_EXECUTIVE_COMMAND/schema-registry.json`
   - `00_EXECUTIVE_COMMAND/partner-registry.json`
   - `00_EXECUTIVE_COMMAND/corridor-registry.json`
   - `00_EXECUTIVE_COMMAND/port-authority-registry.json`
   - `05_PLATINUM_REAL_TIME_MONITORING/PLATINUM_FULL_STACK_ARCHITECTURE.md`
   - `05_PLATINUM_REAL_TIME_MONITORING/PLATINUM_COMMAND_CENTER_INTEGRATION_ADDENDUM_2026-09-30.md`
   - `master-standards-stack/china-execution-pack/00_MASTER_CHINA_EXECUTION_MODEL.md`
   - `master-standards-stack/china-execution-pack/04_FACTORY_SYSTEM_API_CONTRACTS.md`
   - `master-standards-stack/china-execution-pack/05_SMART_GLASS_AUDIT_SPEC.md`
   - `master-standards-stack/china-execution-pack/06_PORT_OFFICER_UI_WORKFLOW.md`
   - `master-standards-stack/china-execution-pack/07_CRYPTOGRAPHIC_TRUST_ANCHOR_ARCHITECTURE.md`
   - `partners/china-food-security-lab/AHTE_JAKIM_INTEGRATION_PROFILE_2026-09-26.md`
   - `deliverables/07_SINOTRANS_PLAYBOOK.md`
   - `deliverables/22_IQ300_JAKIM_MALAYSIAN_STANDARDS_INTELLIGENCE_LAYER.md`
   - `deliverables/29_GLOBAL_PORT_AUTHORITIES_PROTOCOL_2026.md`
   - `docs/WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md`
   - `STATUS.md`
5. Where old project-level wording conflicts with the 30 Sep current target architecture, use the current target architecture. Do not use old China→Malaysia pilot wording.
6. Separate **target architecture** from **production reality**. Do not claim undeployed integrations are already live merely because UI mocks exist.
7. Do not hard-code secrets, credentials, production JAKIM endpoints, lab credentials, manufacturer formulas, private authority schemas or finance data.
8. The platform must be built with clear adapters/mocks for external systems so real connectors can replace them without UI rewrites.

## 1. Core platform proposition

Build a complete Global Halal Digital Trust & Trade / Halal Tayyib infrastructure spanning:

```text
VERIFIED RAW-MATERIAL ORIGIN
→ SUPPLIER / PRODUCER
→ SAMPLE / SEAL / CHAIN OF CUSTODY
→ CHINA LABORATORY SYSTEM
→ SIGNED SCIENTIFIC EVIDENCE
→ MANUFACTURER / FACTORY SYSTEMS
→ STANDARDS / APPLICABILITY
→ HCP / SCCP / CONTROLS
→ SMART-GLASS AI-ASSISTED SITE AUDIT
→ FINDING / CAPA / RE-VERIFICATION
→ DIRECT JAKIM API / HUMAN AUTHORITY WORKFLOW
→ AHTE TRUST-STATE PROPAGATION
→ PACKAGING / BATCH / LOT / PALLET
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
AHTE
+ 24/7 GHSCL + JAKIM Command Center
+ AI/ML predictive analytics
+ Preemptive Strategy Engine
+ immutable/tamper-evident evidence integrity
+ role-based authorised transparency
```

Target transaction-support plane:

```text
Authorised AHTE trust/trade data
→ Shariah Financing API
→ Islamic financing / Takaful / tokenomics
```

## 2. Non-negotiable role model

Represent these as connected but separate roles:

- **PHC** — Perak State Government halal-industry GLC operating locally and internationally.
- **GHSCL Hong Kong** — international operating and digital-infrastructure vehicle; 24/7 command-center operating function.
- **AHTE** — standards, evidence, compliance, traceability, trust-state and AI/ML intelligence.
- **Direct JAKIM API** — direct authorised authority-system connectivity.
- **JAKIM / authorised human authority workflow** — formal competent-authority decision/status layer.
- **China laboratory** — analytical evidence producer.
- **Smart-glass auditors** — human-accountable physical verification.
- **Sinotrans** — end-to-end warehouse + logistics operator and real-time evidence source.
- **Port/customs authorities** — sovereign inspection/clearance/release decision owners; use AHTE API/trust interface.
- **GCC importers/authorities/warehouses/retail** — destination acceptance and receiving layer.
- **Finance/Takaful/tokenomics actors** — independent transaction-support decision owners.

Never visually imply that JAKIM is owned by, subordinate to or a commercial department of GHSCL.

Never claim AI, blockchain, QR, hashes, sensors or lab results independently create Halal certification.

## 3. Default corridor

The physical pilot corridor is:

**China → GCC direct**

Malaysia is the governance/assurance plane unless an explicit physical Malaysia movement is separately scoped.

Mark Shipment 001 content as pilot where shown.

## 4. Four synchronized chains

The UI/data model must make these four chains reconcilable:

1. Physical chain
2. Identity/custody chain
3. Evidence chain
4. Authority/trust-state chain

Minimum material event tuple:

`WHO + WHAT + WHEN + WHERE + OBJECT + REQUIREMENT/CONTROL + EVIDENCE + VERIFIER + CURRENT STATE + INTEGRITY PROOF`

## 5. Canonical path

Use this everywhere in architecture/content:

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

## 6. AHTE engines

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
- Authority Status Adapter
- Direct JAKIM API Adapter
- Integrity/Signature Verification
- Recall Graph Traversal
- Evidence Gap Predictor
- Anomaly Engine
- Contradiction Engine
- Trust Fracture Engine
- Predictive Compliance Engine
- Recall Blast-Radius Engine
- Preemptive Strategy Engine

## 7. Decision-class enforcement

Use repository D0–D6 semantics:

- D0 operational ingest
- D1 encoded control execution
- D2 machine assessment
- D3 finding/CAPA classification with human accountability
- D4 trust-fracture hold; auto-hold may be allowed, auto-release prohibited
- D5 competent-authority gate; human authority only
- D6 sovereign/legal; human authority only

The UI must visibly separate recommendations, machine assessments, holds, authority decisions and operational releases.

## 8. 24/7 Command Center

Create a first-class `/command-center` experience and reusable command-center components.

Required views:

- global China→GCC corridor map;
- active manufacturers/facilities;
- supplier/raw-material changes;
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
- evidence expiry/freshness;
- CAPA/re-verification;
- predictive risk queue;
- preemptive strategy queue;
- recall/blast radius;
- audit/event timeline.

Operating flow:

`observe → correlate → detect → predict → preemptive strategy → assign owner → alert/escalate/hold according to policy → human/authority action → CAPA/reverification → close → learn`

Design it like serious critical infrastructure, not a crypto trading dashboard.

## 9. AI/ML predictive + preemptive UX

Every AI result must show:

- model name/version;
- input/evidence references;
- timestamp;
- score/confidence;
- explanation/rationale summary;
- affected objects;
- recommended action;
- required decision class/human role;
- current review status.

Build sample cards for:

- supplier evidence expiry risk;
- predicted cold-chain excursion;
- sample/batch mismatch;
- route deviation risk;
- recurring HCP nonconformity;
- evidence completeness gap;
- possible recall blast radius.

No AI output should look like an official certificate or authority decision.

## 10. Manufacturer onboarding application

Build complete journey:

`Application → KYB → Facility → Products/SKUs → Formula/BOM → Materials → Suppliers → Origin → System Inventory → Digital Twin → Requirements → HCP/SCCP → Evidence Gap → Remediation/Training → Lab Plan → Smart-Glass Audit → Findings/CAR → Re-verification → Authority Workflow → Continuous Monitoring → GCC Readiness`

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

## 11. Laboratory application

Build sample-centric lifecycle:

`Test request → Sample registered → Collected → Sealed → In transit → Lab received/accessioned → Testing → QC → Technical review → Signed report → Hash/signature verification → AHTE evidence accepted → Authority review linkage`

Exceptions:

- rejected sample;
- chain-of-custody break;
- method out of scope;
- QC failure;
- corrected/withdrawn report;
- signature invalid;
- hash mismatch;
- re-test required.

Use the repository OpenAPI proposal as model guidance, but do not treat placeholder endpoints as live production endpoints.

## 12. Smart-glass application

Required flow:

`device identity + auditor identity + MFA + role/scope → assigned audit → site/scope → requirements/HCPs → scan object → capture evidence → local hash → AI assist → auditor assessment → finding/CAR → re-verification → sign → sync/reconcile`

Support UI mocks/components for:

- QR/DataMatrix/OCR/NFC;
- still/video capture;
- voice commands;
- offline queue;
- device trust status;
- evidence hash;
- object/requirement binding;
- signed session.

## 13. Sinotrans logistics control tower

Build dedicated role surface for:

- warehouse receipts;
- storage zones;
- segregation;
- quarantine/release/reject;
- stock/batch genealogy;
- bookings;
- pickup/loading;
- pallet/container/seal;
- route/geofence;
- temperature/humidity/product-specific telemetry;
- custody handovers;
- port transfer;
- destination delivery;
- exceptions and proof of delivery.

Adapter topology:

`Sinotrans WMS/TMS/Y2T/MIS/EDI/IoT → secure adapter/API → canonical AHTE event → trust graph → Command Center`

Do not claim any synthetic KPI or placeholder integration is live.

## 14. Port/customs authority surface

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

## 15. Direct JAKIM API

Architecture displayed publicly:

`AHTE ⇄ Direct JAKIM API ⇄ JAKIM authority system / authorised human workflow`

Internally implement an adapter interface with mock/sandbox mode.

Suggested application-side interface contract shape only:

```ts
interface JakimAuthorityAdapter {
  submitEvidenceBundle(input: AuthorityEvidenceBundle): Promise<AuthorityReceipt>;
  getCaseStatus(caseId: string): Promise<AuthorityCaseStatus>;
  getCertificationStatus(subjectId: string): Promise<AuthorityCertificationState>;
  subscribeToAuthorityEvents?(handler: AuthorityEventHandler): Promise<Unsubscribe>;
}
```

Do NOT hard-code an unverified official URL or credential scheme.

## 16. Shariah Financing API / Takaful / tokenomics

Build target-state public page plus adapter interfaces, not a fake live financial product.

Functions:

- trade-finance eligibility evidence packet;
- PO/order evidence;
- inventory/shipment state;
- trust assertion retrieval;
- Takaful underwriting evidence packet;
- claim evidence/custody/incident packet;
- asset state verification;
- tokenomics/digital-value module placeholder behind feature flag.

Decision boundary:

- AHTE does not approve financing;
- AHTE does not underwrite Takaful;
- tokenization does not create title or regulatory/Shariah approval;
- bank/Takaful/regulator/human Shariah decisions stay external.

## 17. Verification experience

Build `/verify` supporting:

- Trust Record ID;
- Product/SKU;
- Batch/Lot;
- Shipment ID;
- QR/NFC deep link;
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

## 18. Data model foundations

Represent at minimum:

- Organisation
- Facility
- Product
- FormulaVersion
- Material
- Supplier
- Requirement
- Control
- HCP/SCCP
- Evidence
- Sample
- LabResult
- Audit
- Finding
- CAPA
- AuthorityDecision
- TrustAssertion
- TrustState
- Batch
- Lot
- Pallet
- Container
- Seal
- Shipment
- CustodyTransfer
- TelemetryEvent
- PortEvent
- FinanceEvidencePacket
- Alert
- Prediction
- PreemptiveStrategy
- RecallCase

Use stable IDs and event history. Do not silently overwrite material history; use version/supersession/compensating events.

## 19. Security

Build with:

- strict typed schemas;
- RBAC/ABAC-ready permission layer;
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
- error states that never imply success when dependency is unavailable.

Do not bridge AHTE directly into safety-critical PLC/OT control. Use `OT/SCADA → MES/edge → validated integration gateway → AHTE`.

## 20. Web design system

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

## 21. Routes

Create or prepare:

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

Authenticated role apps may be nested under `/portal/*`.

## 22. Languages

Prepare architecture for:

- English canonical copy
- Simplified Chinese
- Arabic
- Bahasa Malaysia

Do not machine-publish uncontrolled regulatory translations. Use translation files with review status metadata.

## 23. Content governance

Do not duplicate source-sensitive claims in many components.

Create governed content loaders for:

- current target architecture JSON;
- partner registry;
- corridor registry;
- port authority registry;
- standards registry;
- trust schema/status vocabulary;
- controlled public copy.

Build fallbacks so the site can run in local demo mode without external APIs.

## 24. Required developer workflow

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

Then implement in phases.

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

## 25. Implementation phases

### Phase A — foundation

- architecture/content registry
- design tokens
- app shell
- navigation
- shared types
- mock adapter interfaces
- state vocabulary
- identity/evidence timeline components

### Phase B — public website

Implement all public routes and responsive design.

### Phase C — verification

Trust lookup, result pages, QR/NFC deep links, integrity display.

### Phase D — portal prototypes

Manufacturer, Lab, Smart Glass, Sinotrans, Command Center, JAKIM view, Port/Customs, GCC Importer, Finance/Takaful.

### Phase E — integration architecture

Typed external adapter interfaces, mocks/sandboxes, event bus abstraction, observability, error semantics.

### Phase F — hardening

Accessibility, performance, security headers, tests, content-source validation, broken link scan, production build.

## 26. Acceptance tests

The build is incomplete unless it demonstrates all of these:

- China→GCC direct physical corridor;
- raw-material origin start;
- manufacturer onboarding;
- lab/sample/custody;
- smart-glass audit;
- complete standards/applicability model;
- direct JAKIM API topology;
- 24/7 Command Center;
- AI/ML predictive risk;
- preemptive strategies;
- Sinotrans warehouse + logistics;
- port/customs API workflow;
- GCC receiving;
- Shariah financing/Takaful/tokenomics target plane;
- immutable/tamper-evident evidence explanation;
- separate authority/certification, AHTE trust and supply-chain states;
- role-based verification;
- D0–D6 decision-class boundaries;
- no fake live authority/partner integrations;
- no modification to the verified freeze;
- successful lint/typecheck/test/build.

## 27. Completion report format

At the end provide:

### Implemented
Exact routes/components/services/data models completed.

### Reconciled
Old copy/routes/architecture that were corrected, including China→Malaysia stale wording.

### Tested
Commands and pass/fail results.

### External integration placeholders
Only real undeployed dependencies: JAKIM production API, lab/LIMS production credentials, Sinotrans production API access, port/customs production interfaces, GCC systems, finance/Takaful/tokenomics counterparties.

### Security
Any issues found and fixed.

### Remaining gates
Only items that cannot be closed locally without external systems/authority/counterparty inputs.

Do not stop after designing the homepage. Carry the rebuild through all required public routes, reusable system components, mock adapter interfaces, tests and production build.

# END MASTER PROMPT
