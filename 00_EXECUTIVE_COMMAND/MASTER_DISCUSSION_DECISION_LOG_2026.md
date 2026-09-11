# Master Discussion & Decision Log — August/September 2026 Working Baseline

## Purpose

Preserve the strategic decisions and working concepts arising from the project discussion so that future deliverables remain consistent and do not silently drift.

## Core architecture decisions

1. The programme is **Global Halal Digital Trust & Trade / Halal Tayyib infrastructure**, not a simple certification database.
2. The platform is an orchestration and evidence layer; it does not replace sovereign regulators, certification authorities, laboratories, manufacturers or logistics operators.
3. **Certificate != Trust.** Trust requires linking the certified identity to the actual product/batch and preserving relevant custody, condition and evidence events.
4. Halal and Tayyib must be treated together, with a strict distinction: Halal certification is a legal/religious determination; Tayyib monitoring covers product integrity, safety/quality/environmental and custody conditions relevant to the applicable risk model.
5. Sovereign data remains with the appropriate source system where possible. The global layer should use APIs, selective disclosure and cryptographic integrity references.

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

## Sinotrans strategy

Sinotrans is treated as a potential Halal Trusted Logistics Corridor + Digital Evidence Node. Existing Sinotrans systems should be integrated through adapters/APIs rather than replaced for the pilot.

The operating scope should cover transportation, warehousing, handling, handovers, documentation, telemetry, exceptions and evidence mapped to applicable supplied MS 2400 requirements.

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

## Repository architecture direction

The repository should progressively segregate the programme into governance, partner, Halal/Tayyib, Platinum monitoring, China Trust/laboratory, logistics, DPP, traceability, GCC access, B2B trade, finance/support, pilot, October mission, playbooks, SOPs, diagrams/infographics, commercial, legal, research, technical, API, database and dashboards.

## Evidence discipline

The project must explicitly label:
- established facts;
- source-derived facts;
- proposals;
- assumptions;
- items requiring verification;
- signed/contracted commitments.

Do not represent a future partner, regulator, laboratory or programme as confirmed merely because discussions or invitations exist.
