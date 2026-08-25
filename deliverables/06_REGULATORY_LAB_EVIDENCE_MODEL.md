# Regulatory, Laboratory & Evidence Operating Model

## Scope

This document describes the proposed digital workflow between raw-material origin, laboratory testing, manufacturer evidence, Global Halal evidence services and competent regulators.

## Source basis

The uploaded source materials include:
- MS 2400-1:2019 — Halal supply chain management system, transportation.
- MS 2400-2:2019 — Halal supply chain management system, warehousing.
- MS 2400-3:2019 — Halal supply chain management system, retailing.
- Halal audit training material supplied in the project files.
- Halal awareness training material supplied in the project files.

The model below is a digital implementation proposal; it does not replace the controlling legal standard, JAKIM procedure, country law or accreditation requirements.

## Regulatory evidence chain

`Raw-material source -> approved/test-capable laboratory -> scientific result -> manufacturer evidence pack -> regulator review -> decision/status -> production -> logistics -> retail -> consumer`

## Laboratory event

Minimum canonical fields:

- specimen/sample ID;
- product/material ID;
- batch/lot ID;
- submitting organisation;
- sampling details;
- collection timestamp;
- chain-of-custody details;
- test method/reference;
- laboratory identity;
- analyst/authorized signatory;
- result;
- report number/version;
- issue timestamp;
- supporting document reference;
- digital signature/attestation;
- evidence hash.

## Manufacturer evidence pack

The audit training source highlights document and on-site evidence including company profile, factory location, product information, ingredient declaration, manufacturer/supplier identity, ingredient Halal certificates/product specifications, invoices for critical ingredients, traceability programme, Halal assurance system and laboratory test reports. The digital system should convert these into structured evidence objects while preserving the original documents.

## Audit workflow

The supplied audit material describes an opening meeting, document review, on-site inspection, review of findings, closing meeting, confidentiality, evidence collection, non-conformance reporting and corrective-action timing. The platform should digitize these steps without changing the auditor's authority.

## MS 2400 design mapping

### Transportation
MS 2400-1 emphasizes a documented Halal Management System, internal Halal committee, traceable records, source identification, risk management, control measures, monitoring, corrective action, recall/withdrawal and document/record control. These become data objects and workflow controls in the logistics module.

### Warehousing
MS 2400-2 informs storage controls, segregation/separation, integrity during handling, documentation, monitoring and outsourced-party controls. The digital warehouse module should record zones, conditions, handling events and evidence.

### Retailing
MS 2400-3 informs supplier monitoring, receiving checks, storage conditions, product identification and separation, preparation/dispatch, proof of delivery and record control. These become retail event types and audit evidence.

## Regulatory boundary

JAKIM, foreign certification bodies, government agencies, accredited laboratories and other competent authorities retain their own legal mandates. The platform provides interoperability and evidence management; it does not grant certification merely because data is present on the platform.

## Evidence states

`SUBMITTED -> VALIDATED -> VERIFIED -> AUTHORIZED -> EXPIRED/SUPERSEDED -> WITHDRAWN`

Every state transition is logged.

## Dispute model

A dispute can be reconstructed through the evidence graph. Authorized investigators retrieve original source records from the relevant sovereign domain, validate the historical hash, inspect signatures/attestations, compare versions and reconstruct custody and decisions.
