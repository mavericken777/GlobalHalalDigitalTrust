# Sinotrans Halal Digital Trust Playbook

## Artifact status

- Revision: v2.0.0
- Control date: 2026-09-30
- Governing architecture: `00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md`
- Default corridor: **China → GCC direct**
- Pilot: `[PILOT: Shipment 001 — Sinotrans warehouse/logistics]`
- Supersedes: prior China→Malaysia pilot wording in this file

[PROPOSAL: aligns Sinotrans operating model to current project architecture — path point: Control → Evidence → Trust State → Operational Release]

## Purpose

Define how Sinotrans integrates its **end-to-end logistics and warehouse real-time monitoring** into the Global Halal Digital Trust Ecosystem as a logistics trust node and digital evidence source.

The objective is not to replace Sinotrans operational systems. The objective is to bind Sinotrans warehouse, transport, custody, telemetry, container, seal, port and delivery events into AHTE through secure adapters/APIs.

## Strategic proposition

**Halal Trusted Logistics Corridor + Warehouse and Digital Evidence Node**

```text
MANUFACTURER / ORIGIN
        ↓
SINOTRANS WAREHOUSE
        ↓
SINOTRANS END-TO-END LOGISTICS
        ↓
ORIGIN PORT / CUSTOMS
        ↓
INTERNATIONAL TRANSIT
        ↓
GCC PORT / CUSTOMS
        ↓
DESTINATION WAREHOUSE / IMPORTER
        ↓
RETAIL / RECEIVING
```

Across the chain:

`identity + batch/lot + custody + seal + telemetry + evidence + timestamp + actor + location + integrity proof + exception state`

## System integration

Preferred pattern:

`Sinotrans Y2T / MIS / EDI / WMS / TMS / IoT / operational systems → secure adapter/API → schema validation → policy check → event normalizer → AHTE canonical event → evidence/integrity layer → trust graph → 24/7 Command Center`

AHTE becomes the cross-system trust graph. Sinotrans operational systems remain authoritative for their own logistics and warehouse source records.

## Stage 1 — Origin intake

Capture and reconcile:

- manufacturer identity;
- facility identity;
- product/SKU;
- batch/lot;
- raw-material provenance reference;
- formal Halal authority-status reference where applicable;
- laboratory evidence reference;
- shipment/order identity;
- destination market/importer;
- handling/risk profile.

Create/bind the AHTE shipment object without inventing transaction events that have not occurred.

## Stage 2 — Warehouse receipt and qualification

Capture:

- warehouse/facility ID;
- receiving timestamp;
- inbound shipment/lot/pallet IDs;
- seal/condition check where applicable;
- halal/non-halal segregation controls;
- quarantine/released/rejected status;
- zone/bin location;
- temperature/humidity or product-specific environment where applicable;
- storage handling evidence;
- responsible operator;
- exceptions and corrective action.

Warehouse evidence is a first-class real-time monitoring domain, not a secondary transport document.

## Stage 3 — Booking and documentation

Bind:

- booking reference;
- carrier/mode;
- bill of lading / airway bill / delivery order as applicable;
- packing list;
- customs references;
- container identity;
- seal identity;
- product/batch/pallet mapping;
- planned route;
- origin/destination port;
- importer/consignee.

Full confidential documents should remain in the appropriate source system where possible. AHTE should exchange controlled references, hashes, signatures and minimum necessary metadata.

## Stage 4 — Pickup, loading and sealing

Generate attributable events for:

- pickup;
- vehicle/driver or authorised operator identity;
- loading location;
- timestamp;
- pallet/container mapping;
- seal application;
- load condition;
- photographic/device evidence where required;
- custody handover;
- exception state.

Critical events should be integrity protected and idempotent.

## Stage 5 — Transport / international movement

Where applicable, capture:

- route milestones;
- GNSS/geofence events;
- container tracking;
- temperature/humidity/cold-chain data;
- tamper/door/open-close signals;
- shock/vibration or other product-specific telemetry;
- delays;
- route deviation;
- transfers/transshipment only where explicitly scoped;
- custody handovers;
- seal state.

Sensor selection is risk-based. Not every shipment requires every sensor.

## Stage 6 — Port / border / customs

AHTE should provide an authorised port/customs trust interface supporting:

- shipment identity;
- product/batch/container/seal reconciliation;
- authorised trust packet;
- evidence/document references;
- certification/authority-status reference;
- laboratory evidence reference;
- custody history;
- telemetry/condition exceptions;
- inspection/sampling events;
- official hold/release event return.

Port/customs authorities retain sovereign decision authority. Sinotrans/AHTE do not manufacture or override official release.

## Stage 7 — GCC destination receiving

Capture:

- arrival;
- terminal/port status;
- seal reconciliation;
- inspection/sampling outcome where available and authorised;
- customs/border release reference;
- destination warehouse receipt;
- condition report;
- importer/receiver identity;
- discrepancies/damage;
- custody transfer;
- acceptance/hold status.

## Stage 8 — Retail / buyer / consumer verification

The final product identity may expose an authorised view of:

- origin provenance;
- current certification/authority-status reference;
- AHTE trust state;
- batch/shipment identity;
- custody milestones;
- integrity verification;
- material exceptions and disposition.

Public views must not disclose confidential contracts, pricing, private supplier records or unrelated personal data.

## Real-time Command Center integration

Sinotrans events feed the 24/7 GHSCL + JAKIM-connected Command Center.

Priority monitored conditions:

- warehouse segregation exception;
- inventory status mismatch;
- temperature/environment excursion;
- seal/tamper event;
- route/geofence deviation;
- unplanned handling point;
- missing custody handover;
- documentation mismatch;
- delayed port handoff;
- destination hold;
- damage/loss.

Operational loop:

`event → validation → correlation → anomaly/prediction → alert/hold where policy permits → owner assignment → corrective action → re-verification → closure`

## AI/ML role

AI/ML may:

- detect missing logistics/warehouse evidence;
- detect anomalous routes, handovers or dwell time;
- predict likely temperature/condition failure;
- identify trust-graph fractures;
- calculate recall blast radius;
- prioritise inspection;
- recommend preemptive route, handling, sampling or receiving strategies.

AI may not silently change an official certification, customs decision or destination-authority decision.

## Halal/Tayyib control mapping

Apply the complete applicable control framework, including relevant MS 2400 transport/warehouse requirements and any other applicable Malaysian/JAKIM or destination requirements.

Do not use the reviewed derived Sinotrans MS 2400 training bundle as a substitute for the verified source/control stack where that bundle conflicts with source evidence.

## Exceptions

Examples:

- missing/expired authority evidence;
- damaged or mismatched seal;
- route deviation;
- unplanned handling point;
- temperature/humidity excursion;
- mixed/unclear load;
- documentation mismatch;
- unauthorised handover;
- warehouse segregation breach;
- missing custody event;
- destination hold;
- damage/loss.

Exceptions are append-only events. Do not overwrite history to hide a discrepancy.

## KPIs

Operational KPIs may include:

- shipment visibility coverage;
- warehouse event coverage;
- percentage of critical events integrity evidenced;
- evidence completeness;
- chain-of-custody completeness;
- exception rate;
- mean exception detection time;
- mean exception resolution time;
- temperature/condition excursion rate where applicable;
- route deviation rate;
- seal/tamper exception rate;
- recall trace time;
- audit preparation time;
- duplicate data-entry reduction;
- API/event latency and availability.

KPIs must be based on real telemetry/transactions; no synthetic KPI is to be represented as production performance.

## Shipment 001 pilot

[PILOT: Shipment 001 — China → GCC direct]

The pilot physical corridor is **China → GCC direct**. Malaysia is the governance/assurance plane unless a Malaysia physical hop is separately authorised and scoped.

Pilot phases:

### Phase 1 — Interface and site definition

- exact Sinotrans legal/operating entity;
- warehouse/site;
- lane;
- system owner;
- API/event fields;
- security review;
- evidence/control mapping.

### Phase 2 — Controlled origin and warehouse rehearsal

- manufacturer/batch identity;
- warehouse receipt;
- storage/segregation;
- pallet/container mapping;
- seal application;
- synthetic/offline rehearsal only where live transaction evidence does not yet exist.

### Phase 3 — Live Shipment 001 when transaction gates close

- actual booking;
- actual batch/lot;
- actual pickup/loading;
- actual container/seal;
- actual telemetry/custody;
- origin port/customs;
- transit;
- GCC port/import;
- destination receiving.

### Phase 4 — Post-shipment assurance

- evidence reconciliation;
- KPI review;
- exception review;
- audit export;
- lessons learned;
- scale decision.

## Commercial value

Potential value to Sinotrans:

- differentiated Halal/Tayyib logistics and warehousing offering;
- stronger custody evidence;
- real-time exception management;
- faster audit preparation;
- reduced manual evidence handling;
- trusted China→GCC corridor services;
- integration with manufacturer, laboratory, authority and GCC verification layers;
- premium monitoring and assurance services where commercially agreed.

## Authority boundary

Sinotrans provides logistics/warehouse execution and evidence. It does not create Malaysian Halal certification, GCC destination acceptance or sovereign customs release.

The controlling path is:

`Authority → Standard/Instrument → Applicability → Logistics/Warehouse Control → Evidence → Audit/Analytics → Finding/CAPA → Re-verification → Authority Gate → Trust State → Operational Release`.
