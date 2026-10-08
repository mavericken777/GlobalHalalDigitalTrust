# Master Discussion & Decision Log — August/September 2026 Working Baseline

## Purpose

Preserve the strategic decisions and working concepts arising from the project discussion so that future deliverables remain consistent and do not silently drift.

## 30 September 2026 current architecture overlay



### Current operating decisions

1. **Default physical corridor is China → GCC direct.** Malaysia is the governance/assurance plane unless a Malaysia physical hop is separately scoped. Older China→Malaysia pilot language does not control shipment workflow.
2. **JAKIM integration is direct JAKIM API.** Public architecture should not insert an unnecessary generic gateway between AHTE and JAKIM. Exact production endpoints, credentials, schemas and permissions remain controlled implementation inputs.
3. **24/7 GHSCL + JAKIM Command Center is a first-class operating layer.** It continuously monitors manufacturer, laboratory, HCP/SCCP, authority status, Sinotrans warehouse/logistics, shipment/container/seal, ports, GCC receiving, CAPA, evidence freshness, trust fractures, predictive risk and recall state.
4. **AI/ML predictive analytics are paired with preemptive strategy.** Existing Evidence Gap, Anomaly, Contradiction, Trust Fracture, Predictive Compliance and Recall Blast-Radius engines are extended by an explicit Preemptive Strategy Engine. AI may recommend/escalate and apply configured D4 holds; it must not bypass authorised certification decision workflow or auto-release human-reserved holds.
5. **Sinotrans integration includes end-to-end logistics and warehouse real-time monitoring.** Integrate existing Y2T/MIS/EDI/WMS/TMS/IoT and related systems through secure adapters/APIs rather than replacing them.
6. **Port authorities receive an authorised API/trust interface.** AHTE supports identity, trust packet, container/seal, evidence, inspection/sampling and official hold/release event exchange. Port/customs statutory authority remains sovereign.
7. **Shariah Financing API is part of the target platform.** The target plane includes Islamic financing, trade finance, Takaful underwriting/claims evidence and tokenomics/digital-value mechanisms where legally, contractually, regulatorily and Shariah approved. AHTE trust is not credit approval; Halal certification is not financing approval; tokenization does not by itself change title, regulatory or Shariah status.
8. **China laboratory and traceability integration is a China-side evidence/identity plane feeding AHTE.** Laboratory evidence remains evidence, not automatic certification. `NOT DETECTED != HALAL` remains a hard rule.
9. **Website/platform implementation must represent the full ecosystem**, not a generic halal logistics site, not MS2400-only and not a blockchain-certification narrative.
10. **The reference runtime is not production.** The FastAPI reference implementation and `platform/web` prototype do not prove production deployment.
11. **No artificial implementation blocks or feature limits.** The complete production-target architecture must be built now. Missing external APIs, credentials, partner feeds, authority connections, laboratory interfaces, sensor streams, production datasets or financial counterparties must be handled by replaceable development/sandbox providers at the real integration boundary—not by deleting, disabling, hiding, downgrading or indefinitely feature-flagging the intended capability. Development state must remain clearly distinguishable from live production evidence.

Current controlling target-architecture artifacts:

- `CURRENT_TARGET_ARCHITECTURE_2026-09-30.md`
- `current-target-architecture-2026-09-30.json` v1.1.0+
- `IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md`

## Core architecture decisions

1. The programme is **Global Halal Digital Trust & Trade / Halal Tayyib infrastructure**, not a simple certification database.
2. The platform is an orchestration and evidence layer; it does not replace sovereign regulators, certification authorities, laboratories, manufacturers or logistics operators.
3. **Certificate != Trust.** Trust requires linking the certified identity to the actual product/batch and preserving relevant custody, condition and evidence events.
4. Halal and Tayyib must be treated together, with a strict distinction: Halal certification is a legal/religious determination; Tayyib monitoring covers product integrity, safety/quality/environmental and custody conditions relevant to the applicable risk model.
5. Sovereign data remains with the appropriate source system where possible. The global layer should use APIs, selective disclosure and cryptographic integrity references.
6. **External readiness gates are not product feature blocks.** Architecture and user journeys remain complete while live external activation is represented through explicit connector-state metadata.

## China enterprise strategy

The China strategy is to create a repeatable route for manufacturers/producers into the Halal export economy:

`enterprise mobilisation -> qualification -> laboratory evidence -> Halal readiness -> digital trust -> real-time monitoring -> Halal logistics -> GCC market access -> transaction`

CODA is positioned as a **proposed China Enterprise Mobilisation & Export Enablement Backbone**. Exact institutional mandate, funding authority and programme eligibility must be verified before external claims are made.

## CODA support concept

The discussion established a policy concept in which Chinese manufacturers should not feel the full financial burden of entering the new trust infrastructure. Potential support areas include real-time monitoring hardware, integration, training, onboarding and pilot enablement, subject to actual CODA/Chinese programme rules and approvals.

No subsidy amount or guaranteed financing commitment is established by this log.

## Platinum monitoring decision

Platinum is defined as **full-stack real-time monitoring**, rather than a single sensor or device. The stack spans:

- product/SKU/batch identity;
- source and laboratory evidence references;
- Halal status reference;
- site/factory controls;
- temperature/humidity and other applicable environment sensors;
- tamper/seal/open-close;
- GPS/geofencing;
- shock/vibration where relevant;
- device identity and gateway;
- connectivity;
- event streaming;
- rules and alerts;
- anomaly/exception handling;
- cryptographic evidence;
- chain of custody;
- logistics system integration;
- GCC receiving;
- Digital Product Passport/trust record;
- audit export.

Sensor selection is risk-based. Not every commodity requires every sensor.

## Laboratory / China Trust integration

The intended chain is:

`origin evidence -> appropriate China laboratory -> test result -> evidence reference -> Halal/Tayyib assurance workflow -> digital trust -> shipment -> Platinum monitoring -> logistics -> GCC verification`

Laboratory systems remain authoritative for their own results. The trust layer should consume authorised references and integrity metadata.

If production laboratory/LIMS connectivity is not available during development, the complete sample/custody/method/result/integrity workflow is still implemented through a replaceable development provider. No synthetic result is represented as real laboratory evidence.

## Sinotrans strategy

Sinotrans is treated as a potential Halal Trusted Logistics Corridor + Warehouse/Digital Evidence Node. Existing Sinotrans systems should be integrated through adapters/APIs rather than replaced for the pilot.

The operating scope covers transportation, warehousing, handling, handovers, documentation, telemetry, exceptions and evidence mapped to the complete applicable control framework, including relevant MS 2400 requirements where applicable.

Default physical pilot corridor: **China → GCC direct**.

If production Sinotrans APIs are unavailable during development, the complete WMS/TMS/Y2T/MIS/EDI/IoT adapter contracts, event model and role UI remain implemented with development providers.

## Port/customs strategy

Port/customs users require an authorised minimum-necessary trust interface capable of resolving shipment identity, container/seal, custody, document/evidence references, authority status references, exceptions and inspection/sampling/release events.

AHTE records and propagates official port/customs events; it does not manufacture official clearance/release.

Absence of a live sovereign endpoint must not remove the port/customs application. Use a development provider until production access exists and label its state accordingly.

## AI/ML strategy

The assurance stack includes:

- Evidence Gap Predictor;
- Anomaly Engine;
- Contradiction Engine;
- Trust Fracture Engine;
- Predictive Compliance Engine;
- Recall Blast-Radius Engine;
- Preemptive Strategy Engine.

Target operating loop:

`observe -> correlate -> detect -> predict -> impact analysis -> preemptive strategy -> authorised action -> outcome -> feedback`

AI confidence must not bypass mandatory human/authority decision classes.

## 24/7 Command Center strategy

GHSCL operates the digital infrastructure and continuous monitoring function. The Command Center is designed for 24/7 visibility, alerting, escalation, predictive analysis and preemptive strategy across the complete corridor. JAKIM is connected through the direct authorised API path according to actual production scope.

The Command Center must remain fully represented in development through controlled data providers if live partner/authority feeds are absent; development events must not be represented as production events.

## Shariah financing / Takaful / tokenomics strategy

The target platform includes a controlled Shariah Financing API plane fed by authorised trust/trade data.

Potential services:

- Islamic trade finance;
- purchase/order financing;
- inventory/shipment financing;
- Takaful underwriting and claims evidence;
- asset/shipment state verification;
- tokenomics/digital-value mechanisms where legally and Shariah approved.

No specific bank, Takaful product, token classification, token economics or regulatory approval is established by this log unless separately documented.

The complete integration plane, portal flows and adapter contracts should nevertheless be built without artificial product limitation; real external decisions remain with the competent financial/Shariah/regulatory actors.

## October 2026 mission

The 12–17 October itinerary is an implementation mission. Each meeting must have a defined decision agenda, required output, owner and follow-up.

The ultimate target is to create the conditions for the first fully controlled, traceable China-to-GCC Halal B2B transaction.

## First-transaction logic

A transaction candidate should not proceed simply because a product is certified. It must have:

- identity;
- evidence;
- applicable Halal status/reference;
- required laboratory evidence;
- logistics route and custody controls;
- monitoring profile where required;
- destination-market requirements;
- importer/buyer;
- legal/commercial documentation;
- evidence/audit trail;
- exception/corrective-action mechanism.

A development-mode platform may simulate the workflow with synthetic data for implementation/testing, but it must not claim that the transaction has occurred.

## Repository architecture direction

The repository should progressively segregate the programme into governance, partner, Halal/Tayyib, Platinum monitoring, China Trust/laboratory, logistics, DPP, traceability, GCC access, B2B trade, finance/support, pilot, October mission, playbooks, SOPs, diagrams/infographics, commercial, legal, research, technical, API, database, command center and dashboards.

## Evidence discipline

The project must explicitly label:
- established facts;
- source-derived facts;
- proposals;
- assumptions;
- items requiring verification;
- signed/contracted commitments;
- development/sandbox data;
- live/production data.

Do not represent a future partner, regulator, laboratory or programme as confirmed merely because discussions, development adapters or invitations exist.
