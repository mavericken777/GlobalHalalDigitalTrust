---
name: ahte-source-governance
description: Enforces AHTE source provenance, freeze immutability, authority boundaries, and flag syntax during any repository task that touches standards, evidence, certification, pilot, partner, or corridor content. Use when the task involves IQ300, AHTE, JAKIM, MS 2400, halal certification, Shipment 001, or any deliverable that could be interpreted as an authority claim.
---

# AHTE Source Governance

## When this skill activates

Load this skill whenever the task involves:

- any file under `master-standards-stack/verified-2026-09-17/`
- any reference to JAKIM, MAIN, JAIN, MS 2400, GSO 2055, or other standards
- any deliverable mentioning certification, approval, audit, or trust state
- any `[PILOT: Shipment 001]` content
- any partner-facing or public-facing asset
- any corridor or port architecture

## Mandatory reading order

1. `AGENTS.md`
2. `.github/copilot-instructions.md`
3. `00_EXECUTIVE_COMMAND/ABSOLUTE_MODE_SYSTEM_INSTRUCTION_v14.1.md`
4. `00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md`
5. `master-standards-stack/verified-2026-09-17/00_README.md`
6. `master-standards-stack/verified-2026-09-17/MANIFEST.json`

## Core rules

- Never invent normative text, clause numbers, certificates, laboratory
  results, approvals, or shipment events.
- Never reproduce licensed MS 2400 normative wording.
- Enforce `NOT DETECTED != HALAL`.
- Never imply automatic certificate recognition or market access.
- Never present Shipment 001 as instantiated.
- Never blur pilot material into permanent architecture.
- Never silently resolve a source conflict.
- Use exact flag syntax from the current Absolute Mode instruction.

## Missing-source response

Begin with:

`DATA NOT AVAILABLE — SOURCE-LOCKED.`

Then list: missing input, blocked canonical-path point, source owner, retrieval
action, and what work can continue.

## Freeze boundary

`master-standards-stack/verified-2026-09-17/` is immutable
(16 content modules `00`–`15` + `MANIFEST.json`).
Do not edit, rename, move, or delete anything inside it.
Create post-freeze successors outside the snapshot.

## Authority boundary

AHTE is an evidence and decision-support layer. JAKIM/MAIN/JAIN retain
certification authority. Destination GCC authorities retain import and halal
acceptance authority. AI never issues certificates.
