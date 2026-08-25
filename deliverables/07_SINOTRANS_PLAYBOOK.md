# Sinotrans Halal Digital Trust Playbook

## Purpose

This playbook proposes how Sinotrans could become a preferred logistics trust node within the Global Halal Digital Trust Ecosystem. It is a strategic proposal, not a statement that Sinotrans has agreed to participate.

## Why Sinotrans is a strong candidate

Sinotrans publicly describes integrated logistics capabilities across sea, air, rail, road, warehousing and distribution, customs-related services and digital logistics. Its published material also describes EDI integration, information sharing, IoT-based visibility, Big Data, Cloud Computing, AI and Blockchain capabilities, and the Y2T digital logistics platform. Source: Sinotrans official website, accessed August 2026. See repository source register.

## Strategic proposition

Position the Sinotrans relationship as:

**Halal Trusted Logistics Corridor + Digital Evidence Node**

The objective is not to replace Sinotrans systems. The objective is to add a Halal/Tayyib trust layer over existing logistics workflows through APIs and event adapters.

## Operating model

### Stage 1 — Origin intake

Capture:
- manufacturer identity;
- product identity;
- batch/lot;
- raw-material evidence reference;
- Halal status reference;
- laboratory evidence reference where applicable;
- shipment order.

Create a trusted shipment ID.

### Stage 2 — Booking & documentation

Link:
- booking;
- bill of lading / airway bill / delivery order;
- packing list;
- customs references;
- container ID;
- seal ID;
- product/batch mapping.

Do not copy full documents into a global trust database. Retain document references and cryptographic hashes with sovereign source storage.

### Stage 3 — Pickup and loading

Generate a signed event for:
- pickup;
- vehicle identity;
- driver/authorized operator;
- loading location;
- timestamp;
- seal verification;
- load condition;
- exceptions.

### Stage 4 — Transport

Where relevant, capture:
- route milestones;
- container tracking;
- transfer points;
- temperature/environment telemetry;
- delay exceptions;
- tamper/seal alerts;
- handovers.

### Stage 5 — Port / border / customs

Link authorized customs and transport evidence. Record discrepancies and corrective action.

### Stage 6 — Warehousing

Digital controls should reflect the supplied MS 2400-2 requirements for integrity, segregation/separation, storage conditions, handling, records and outsourced service control.

### Stage 7 — Final delivery

Record:
- dispatch;
- destination;
- authorized receiver;
- proof of delivery;
- condition exception;
- evidence hash.

### Stage 8 — Consumer/retail verification

The final product identity links the logistics events to the consumer scan. The consumer sees only the authorized public view.

## Sinotrans system integration

Use an adapter-first approach:

`Sinotrans/Y2T/MIS/EDI/IoT -> Secure API gateway -> Event normalizer -> Halal Trust event -> Evidence hash -> Sovereign evidence store`

No replacement of existing Sinotrans systems is required for a pilot.

## Halal control mapping

The supplied MS 2400-1 transportation standard highlights documented policy, internal Halal committee responsibility, source identification, risk assessment, control measures, monitoring, corrective action, recall/withdrawal and records. These should be implemented as logistics control objects and automated evidence checks.

## Exceptions

Examples:
- missing Halal evidence;
- damaged seal;
- route deviation;
- unplanned handling point;
- temperature deviation;
- mixed/unclear load;
- documentation mismatch;
- unauthorized handover;
- warehouse segregation breach.

The AI should classify the risk, preserve evidence, notify authorized parties and recommend corrective action. It must not silently change certification status.

## KPI dashboard

Operational KPIs:
- shipment visibility coverage;
- percentage of events cryptographically evidenced;
- evidence completeness;
- on-time delivery;
- exception rate;
- average exception resolution time;
- temperature excursion rate where applicable;
- chain-of-custody completeness;
- recall trace time;
- audit preparation time;
- duplicate data-entry reduction.

## Pilot proposal

### Pilot corridor

China -> Malaysia, initially for a controlled set of Halal-sensitive products/raw materials.

### Pilot participants

- selected manufacturer;
- Sinotrans operating unit;
- authorized laboratory/testing provider where applicable;
- Global Halal platform operator;
- JAKIM/competent authority only through formal agreed channels;
- selected destination warehouse/retailer.

### 90-day pilot phases

**Days 1-30:** mapping, data dictionary, security review, API design, process validation.

**Days 31-60:** controlled live shipment, evidence capture, dashboard and exception workflow.

**Days 61-90:** multi-shipment validation, audit rehearsal, KPI review and scale decision.

## Commercial value for Sinotrans

- differentiated Halal logistics offering;
- stronger chain-of-custody evidence;
- customer trust;
- audit readiness;
- reduced manual evidence handling;
- premium service opportunities;
- access to new Halal trade corridors;
- ESG and traceability services.

## Important boundary

This playbook does not confer Halal certification on Sinotrans or any shipment. Certification/recognition remains a matter for the competent authority and applicable legal framework.
