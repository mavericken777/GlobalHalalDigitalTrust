# Official-trip retailer pack — Lulu, Carrefour (MAF), Tamimi, noon

Control date: 2026-09-30  
Status: **outreach-ready templates and dossiers**. No executed instrument with any of the four is on file.

[PROPOSAL: aligns retailer destination-layer wording to current target architecture — path point: Receiving Verification → Trust State → Operational Release]

These four names are the **GCC destination receiving / listing layer** of the **China → GCC direct** corridor. Malaysia is the governance/assurance plane unless an explicit physical Malaysia movement is separately scoped. These retailers do not replace JAKIM, SFDA, Saudi Halal Center, MoIAT, national customs or other competent authorities. They decide whether a lot is **listed, received, stocked or sold** within their own commercial responsibility and applicable law.

[PILOT: Shipment 001 — GCC receiving / retail]

## Who you actually write to

| Banner | Do not address | Address instead (confirm in the room) | First market |
|---|---|---|---|
| Lulu | “Lulu Group” as one legal person | **Lulu Retail Holdings PLC** for group protocol; identify the exact destination operating/import entity for the transaction | KSA + UAE |
| Carrefour | Carrefour SA (France) | **Majid Al Futtaim Retail / applicable operating entity** for the destination market; confirm current banner/legal entity before contracting | UAE first |
| Tamimi | “Tamimi Group” holding only | **Tamimi Markets Company / exact importing or buying entity** for the transaction | KSA |
| noon | the app name | The **noon operating / seller legal entity** for UAE or KSA applicable to the seller/listing route | UAE, optional KSA lane |

Volatile corporate/banner details must be verified against the current counterparty and primary sources before external use. Do not treat this trip pack as proof of a current legal name, import licence, listing approval or executed commercial relationship.

## Target digital receiving model

The destination layer should be able to consume an authorised AHTE trust view containing, as permitted:

- product / SKU identity;
- manufacturer/facility identity;
- batch/lot/shipment identity;
- formal certification/authority-status reference;
- AHTE trust state;
- origin/material provenance summary;
- laboratory evidence reference;
- Sinotrans custody milestones;
- container/seal state;
- port/customs release reference;
- material exceptions and disposition;
- evidence-integrity verification;
- last verified timestamp.

Complete traceability does not mean unrestricted disclosure of confidential manufacturing, pricing, supplier or personal information. Use role-based authorised transparency.

## Sequence on an official trip

1. Confirm China-origin manufacturer/SKU family and evidence readiness.
2. Confirm Sinotrans named warehouse/site/lane or written deferral.
3. Confirm the intended GCC country/importer/receiving route.
4. Prepare one SKU family with the complete evidence pack (`COMMON_RECEIVING_PACK.md`).
5. Buyer meeting: category, import compliance, trust-record fields and receiving requirements — not an assumed signing ceremony.
6. Capture exact destination document requirements, data/API expectations, responsible owners and next date.
7. MoA only if requested/agreed by the counterparty; empty annexes or unresolved scope are not execution evidence.

## What “complete” means for this layer

A retailer file is complete when it contains the correct legal/operating entity, market, category, required document/evidence list validated by the counterparty, focal contacts, integration/receiving requirements and an agreed next action/date.

A signed/chopped document with no SKU, no receiving requirements, no importer path and no evidence/data definition is not a complete operational route.

## Command Center / API relationship

Retailer/importer receiving events should feed AHTE and the 24/7 GHSCL + JAKIM-connected Command Center through the authorised integration model. A retailer/importer event does not replace a competent-authority decision; it records destination commercial/receiving state and evidence.

Governing project architecture: `../../00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md`.
