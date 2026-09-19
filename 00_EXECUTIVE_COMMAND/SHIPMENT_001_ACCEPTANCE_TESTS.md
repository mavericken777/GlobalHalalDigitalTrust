# Shipment 001 Acceptance Tests — Architecture Only

| Field | Value |
|---|---|
| Artifact | `SHIPMENT_001_ACCEPTANCE_TESTS.md` |
| Revision | v0.1.0 |
| Control date | 2026-09-20 |
| Classification | post-freeze proposal / [PILOT: Shipment 001] |
| Authority effect | none |
| Status | TRANSACTION-GATE — no live events exist |

[PILOT: Shipment 001 — acceptance tests]
[TRANSACTION-GATE: SKU / PO / certificate / lab / custody / border evidence]

These tests define *what must be true before promotion or operational release*. Passing a documentation checklist is not a shipment.

## A. Identity and commercial

- [ ] Legal entity documented (GHSCL / counterparties) with source
- [ ] Factory identity verified (not public-claim only)
- [ ] SKU / formula / batch identifiers exist as transaction-native records
- [ ] Importer / buyer and PO exist (E4)

## B. Authority gates (D5)

- [ ] Current Malaysia Halal certificate (if in scope) verified with issuer / scope / validity — E5 from JAKIM/MAIN/JAIN, not AHTE
- [ ] Destination GCC acceptance path identified for that SKU
- [ ] Assessment objects are not labelled E5
- [ ] `NOT DETECTED != HALAL` enforced on any lab packet

## C. Evidence and HITM

- [ ] Evidence objects hashed (12-char SHA-256 prefix) with class E1–E5 correct
- [ ] D5/D6 actions denied by OPA fixtures F08–F09 regardless of high confidence
- [ ] D4 hold allowed; D4 release requires human_determination (F05–F07)
- [ ] Fracture events cannot auto-release

## D. Custody (EPCIS-shaped)

- [ ] Each corridor segment has a real event or remains TRANSACTION-GATE
- [ ] Seal id present on custody objects
- [ ] No invented loading / arrival / release timestamps

## E. Trust vector

- [ ] Hard-gates evaluated before any score
- [ ] Score marked non-sovereign
- [ ] Operational release object has `is_certification: false`

## F. Promotion ban

Do not mark Shipment 001 instantiated until A–D have transaction-native evidence. Architecture completeness is not operational completeness.
