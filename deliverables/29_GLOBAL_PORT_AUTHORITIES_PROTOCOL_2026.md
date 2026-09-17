# 29 — GLOBAL PORT AUTHORITIES PROTOCOL 2026

## ARTIFACT METADATA
| Field | Value |
|---|---|
| Artifact | `29_GLOBAL_PORT_AUTHORITIES_PROTOCOL_2026.md` |
| Target folder | `deliverables/` |
| Control date | 17 September 2026 |
| Freeze boundary | `master-standards-stack/verified-2026-09-17/` |
| Supersedes | None |
| Companion artifacts | `00_EXECUTIVE_COMMAND/port-authority-registry.json`, `00_EXECUTIVE_COMMAND/corridor-registry.json` |
| Commit message | `docs(deliverables): add 29 — Global Port Authorities Protocol for China-GCC corridor [DOCTRINE-CRITICAL]` |

[PILOT: Shipment 001 — port/border]

## 1. PURPOSE
Define the structured engagement protocol for origin-China and destination-GCC port, customs, inspection and related border authorities for the China → GCC direct corridor pilot. The protocol establishes evidence gates, authority boundaries, custody hand-over points, document sets, exception handling, escalation paths and verification requirements.

## 2. SCOPE
- Origin ports: selected China export ports used for Shipment 001.
- Destination ports: selected GCC entry ports in Saudi Arabia, UAE or another specifically scoped GCC member state.
- Related entities: customs, border control, quarantine/inspection/food authorities and authorised logistics operators including Sinotrans where selected.
- Out of scope: non-GCC destination corridors unless separately scoped.

## 3. AUTHORITY BOUNDARY
- Port/customs clearance decisions remain solely with competent national/local authorities.
- No AI output, platform event, partner declaration, lab result or AHTE trust state creates official clearance, release or Halal certification.
- Port/customs decisions are distinct from Malaysia Halal certification decisions and from destination halal/product acceptance decisions.
- AHTE records official custody/release evidence; it does not manufacture or override it.

## 4. PORT ENGAGEMENT CHAIN
`Origin port selection → Export-document readiness → Container stuffing/seal → Origin customs/inspection clearance → Loading confirmation → Transit custody/telemetry → Destination arrival notice → Destination customs/food/quarantine inspection → Border release → Receiving verification → AHTE E4/E5 evidence linkage`

## 5. EVIDENCE GATES
| Gate | Owner | Evidence Required | Status |
|---|---|---|---|
| Origin port selection | Project + logistics operator | capability, cut-offs, handling requirements | EXTERNAL-GATE / TRANSACTION-GATE |
| Export documentation | Manufacturer/exporter + importer + logistics | invoice, packing list, origin, declaration, category-specific documents | TRANSACTION-GATE |
| Container/seal integrity | Logistics operator + terminal | seal ID, stuffing/condition record | TRANSACTION-GATE |
| Origin clearance | GACC/competent China authority | official export clearance/release | EXTERNAL-GATE |
| Transit custody | Sinotrans/designated operator | custody events, telemetry where risk requires | TRANSACTION-GATE |
| Destination arrival | Terminal/operator | arrival/terminal record | TRANSACTION-GATE |
| Destination inspection | Destination authority | inspection/sampling/hold/release evidence | EXTERNAL-GATE |
| Border release | Customs/border authority | official clearance/release | EXTERNAL-GATE |
| Receiving verification | Importer/warehouse | goods receipt, seal/condition reconciliation | TRANSACTION-GATE |

## 6. ORIGIN — CHINA
Before shipment release:
- select the actual export port/terminal;
- validate applicable GACC/customs/export requirements for the SKU;
- obtain container stuffing and seal records;
- obtain phytosanitary/health/commodity certificates where applicable;
- coordinate terminal/carrier cut-offs with the designated logistics operator.

## 7. DESTINATION — GCC

### 7.1 Saudi Arabia
Verify current transaction-specific requirements across:
- ZATCA customs clearance;
- SFDA food/product/import controls;
- Saudi Halal Center requirements where applicable;
- Arabic/GSO labelling rules applicable to the exact product;
- destination sampling/inspection/hold procedures.

### 7.2 United Arab Emirates
Verify current transaction-specific requirements across:
- UAE ICP federal customs/port-security reference plus emirate-level customs procedures;
- MoIAT halal/conformity requirements where applicable;
- local food/import authority requirements for the selected emirate/port and SKU.

**Governance correction:** ESMA is historical as a standalone entity; its functions were merged into MoIAT. Do not use obsolete ESMA/FCA endpoints as current primary control sources.

### 7.3 Other GCC Members
Do not infer Saudi/UAE equivalence. Resolve exact national customs, food/product, standards and halal-recognition requirements before route approval.

## 8. ENGAGEMENT SEQUENCE
1. Corridor and port-pair selection.
2. Origin-terminal capability/cut-off confirmation.
3. Export-document package preparation.
4. Stuffing, sealing and origin clearance.
5. Loading/departure confirmation.
6. In-transit custody/telemetry and exception monitoring.
7. Destination arrival/terminal assignment.
8. Destination inspection/sampling/clearance.
9. Border release and goods receipt.
10. Evidence linkage into AHTE.
11. Post-shipment reconciliation, findings and corrective improvement.

## 9. DOCUMENT SET REFERENCE

### 9.1 Origin Document Set
| Document | Typical Issuer | Purpose |
|---|---|---|
| Commercial invoice | Seller/manufacturer | value/customs basis |
| Packing list | Seller/manufacturer | item-level contents |
| Certificate of origin | competent issuing body | origin evidence |
| Export declaration | exporter/customs process | China export clearance |
| Bill of lading | carrier/logistics operator | transport contract/evidence |
| Halal certificate copy where required | relevant certification body | destination acceptance input |
| Phytosanitary certificate if applicable | competent China authority | plant-product compliance |
| Health certificate if applicable | competent authority | category-specific compliance |
| Container stuffing/seal record | logistics/terminal | custody/condition evidence |

### 9.2 Destination Document Set
| Document | Typical Issuer | Purpose |
|---|---|---|
| Bill of lading | carrier | cargo release/consignee evidence |
| Import declaration | importer/broker | customs clearance |
| Import/product registration | competent authority/importer | eligibility evidence |
| Inspection/sampling result | destination authority | compliance evidence |
| Border release/clearance | customs/border authority | official operational release |
| Goods receipt | importer/warehouse | custody hand-over |
| Condition report | importer/warehouse | seal/damage/condition reconciliation |

### 9.3 Alignment Rule
A deviation from the planned document set requires applicability review and an explicit evidence-gap/open-gate decision. Missing documents are never presumed satisfied.

## 10. EXCEPTION HANDLING

### 10.1 Origin Hold
`[OPEN GATE: ORIGIN HOLD — owner: origin customs/competent authority — blocking: Authority Gate/Origin Clearance]`

### 10.2 Destination Hold
`[OPEN GATE: DESTINATION HOLD — owner: destination authority — blocking: Authority Gate/Border Release]`

### 10.3 Seal Breach
`[OPEN GATE: SEAL BREACH — owner: custody operator — blocking: Evidence/Custody]` — quarantine and re-verify before release.

### 10.4 Telemetry Excursion
`[OPEN GATE: TELEMETRY EXCURSION — owner: logistics/quality — blocking: Tayyib/condition verification]` — assess against commodity risk profile.

### 10.5 Document Discrepancy
`[OPEN GATE: DOCUMENT DISCREPANCY — owner: document issuer/importer/exporter — blocking: Applicability/Evidence]`

### 10.6 Damage
`[OPEN GATE: DAMAGE — owner: carrier/insurer/receiver — blocking: Receiving Verification]`

## 11. ESCALATION MATRIX
| Issue | Primary Owner | Escalation |
|---|---|---|
| Origin customs hold | customs broker/exporter | Sinotrans/designated operator → project commercial layer |
| Destination customs hold | importer of record | importer → competent destination authority |
| Halal certificate/status question | certificate issuer/competent halal authority | issuer/authority channel |
| Destination halal acceptance | importer + destination authority | SFDA/Saudi Halal Center, MoIAT or other competent authority as applicable |
| Document discrepancy | exporter + importer | logistics → commercial owners → authority if required |
| Seal/telemetry breach | custody operator | project + importer + insurer/quality as applicable |
| Damage/loss | carrier + insurer | logistics → carrier → insurer |
| Border release refusal | destination authority | importer → authority appeal/remediation route |

## 12. PLANNING WINDOWS
The following are internal planning windows only, not authority SLAs:
- document preparation: T-14 to T-7 days;
- stuffing: T-5 to T-3 days;
- origin clearance: T-3 to T-1 days;
- loading: T-0;
- destination arrival-to-initial inspection planning assumption: 0–72 hours;
- inspection-to-release: per authority;
- release-to-receipt planning assumption: 24–72 hours.

Actual timing is controlled by authority decisions, carrier schedules and transaction conditions.

## 13. OPEN GATES
- exact origin port/terminal;
- exact destination country/emirate/port;
- exact SKU/document set;
- destination sampling/inspection requirements;
- telemetry configuration by commodity risk;
- actual customs/authority clearance events;
- actual goods receipt/reconciliation.

## 14. CANONICAL PATH MAPPING
`Authority → Instrument/requirement → Applicability → Port/custody control → Evidence → Audit/inspection test → Finding/hold → Corrective action → Re-verification → Authority Gate → Trust State → Operational Release`

## 15. AUTHORITY BOUNDARY AFFIRMATION
Port/customs authorities retain sovereign decision authority. AHTE captures evidence and state transitions but does not issue or modify official clearance, release or Halal certification.
