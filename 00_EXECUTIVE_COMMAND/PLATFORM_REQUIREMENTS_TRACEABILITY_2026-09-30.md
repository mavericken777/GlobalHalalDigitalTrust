# Platform Requirements Traceability — 30 September 2026

## Artifact metadata

| Field | Value |
|---|---|
| Artifact | `PLATFORM_REQUIREMENTS_TRACEABILITY_2026-09-30.md` |
| Revision | v1.0.0 |
| Control date | 2026-09-30 |
| Governing architecture | `CURRENT_TARGET_ARCHITECTURE_2026-09-30.md` + `current-target-architecture-2026-09-30.json` + `IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md` |


## 1. Purpose

This is the reconciliation matrix for the complete platform architecture furnished by the project owner. It exists to prevent individual files, website builds, Codex runs or partner integrations from reducing the programme to a fragment such as certification, logistics, blockchain, laboratory, MS 2400 or a generic dashboard.

A row marked `PRESENT` means the target capability is represented in the current project architecture. It does **not** assert that a live external production connector, authority permission, commercial contract, transaction or shipment event exists.

## 2. Complete platform requirements matrix

| ID | User-furnished platform requirement | Canonical path / plane | Controlling repository coverage | Status |
|---|---|---|---|---|
| P01 | PHC is the Perak State Government halal-industry GLC operating locally and internationally in the project ecosystem | Authority / institutional | current target architecture; partner registry; `partners/phc/README.md` | PRESENT |
| P02 | GHSCL Hong Kong is the international operating and digital-infrastructure vehicle | Operating / orchestration | current target architecture; partner registry; `partners/ghsc-hk/README.md` | PRESENT |
| P03 | AHTE is the continuous standards, evidence, compliance, traceability and trust-intelligence layer | All canonical path points | IQ300 doctrine; current target architecture; Platinum stack | PRESENT |
| P04 | Complete applicable Malaysian/JAKIM framework — not an MS 2400-only platform | Standard / Applicability | standards intelligence layer; standards register; current target architecture | PRESENT |
| P05 | End-to-end traceability begins at verified raw-material origin and continues to GCC retail/verification | Physical chain / Evidence | current target architecture; China execution pack; shipment workflow model | PRESENT |
| P06 | Raw-material provenance binds producer, supplier, lot, source evidence and downstream consumption | Evidence / Digital Twin | China execution pack; AHTE object hierarchy; manufacturer onboarding | PRESENT |
| P07 | China laboratory workflow covers SampleID → collection → seal → custody → accession → method/QC → review → signed result → integrity proof | Evidence / Audit Test | China lab integration profile/API; canonical China pack | PRESENT |
| P08 | China traceability/anti-counterfeit system contributes enterprise/product identity, one-item-one-code, microdot/QR/VOID, unit→box→carton→pallet aggregation, verification, anti-diversion and scan analytics | Identity / Evidence / Traceability | China lab/traceability integration profile; target architecture lab plane | PRESENT + HARDENED IN CONSOLIDATION |
| P09 | Manufacturer onboarding covers legal entity, facility, product/SKU, formula/BOM, raw materials, suppliers, origin, systems, digital twin, applicability, HCP/SCCP, evidence gaps, remediation/training, lab, smart audit, CAPA, re-verification, authority workflow and continuous monitoring | Applicability → Operational Release | standards intelligence layer; CODA enablement model; website/Codex master specs | PRESENT |
| P10 | Smart-glass audit includes auditor/device identity, MFA, scope, scans, image/video/document/voice/sensor evidence, offline-first queue, local hash/signature, AI assist, findings, CAR/CAPA and re-verification | Evidence → Re-verification | canonical China execution pack smart-glass specification | PRESENT |
| P11 | AHTE integrates **directly with the JAKIM API**. Do not insert NurAI or an unnecessary public intermediary | certification review | current target architecture; machine target; lab direct-API alignment | PRESENT |
| P12 | Formal certification approval/disapproval in the project operating model is performed through the **PHC + JAKIM authorised human workflow**, including Mufti/scholars/authorised officers as applicable; AI/AHTE do not make the certification decision | certification review | project target architecture + this traceability control | PRESENT + EXPLICITLY HARDENED |
| P13 | Every material evidence object has attributable provenance and cryptographic integrity protection; corrections use append-only supersession rather than silent overwrite | Evidence | cryptographic trust-anchor architecture; IQ300 doctrine; current target architecture | PRESENT |
| P14 | QR/NFC/blockchain/DLT/hashes are integrity/access mechanisms, not certification authorities | Evidence / certification workflow | doctrine; cryptographic architecture; interop stack | PRESENT |
| P15 | Sinotrans integrates end-to-end warehouse + logistics real-time monitoring, not transportation alone | Evidence / custody | `deliverables/07_SINOTRANS_PLAYBOOK.md` v2; data mapping; current target architecture | PRESENT |
| P16 | Sinotrans scope includes warehouse receipt/dispatch, segregation/storage, booking, pickup, pallet/lot, vehicle/container, seal, custody, route/geofence, telemetry, port handoff and proof of delivery | Evidence / custody | Sinotrans playbook/data mapping; Platinum stack | PRESENT |
| P17 | Origin and GCC port/customs authorities receive authorised API/trust interfaces for shipment, container/seal, documents, evidence, inspection/sampling, hold/release and signed return events | Authority / custody | Global Port Authorities Protocol; Port Officer workflow; current target architecture | PRESENT |
| P18 | Port/customs sovereign decisions remain with the port/customs authority; AHTE records and propagates, never manufactures clearance | certification workflow | port protocol; doctrine | PRESENT |
| P20 | Financing, Takaful and tokenomics decisions/states remain separate from halal certification and AHTE trust state | Authority/decision separation | finance architecture; standards intelligence role matrix | PRESENT |
| P21 | 24/7 Command Center is jointly monitored by **GHSCL operational roles and authorised JAKIM authority-side roles** | Experience / Authority / Monitoring | Command Center specification; current target; this traceability control | PRESENT + EXPLICITLY HARDENED |
| P22 | Shared Command Center monitoring does not make GHSCL and JAKIM permissions identical: GHSCL handles platform/corridor operations; JAKIM retains authority-side monitoring/decision scope | Governance | Command Center specification; current target | PRESENT + HARDENED |
| P23 | Command Center continuously monitors manufacturer/facility, materials/suppliers, lab, HCP/SCCP, smart audits, authority status, Sinotrans/WMS/logistics, shipment/container/seal, telemetry, ports, GCC receiving, CAPA, evidence integrity/expiry, recalls | Evidence → Operational Release | Command Center specification; Platinum stack | PRESENT |
| P24 | AI/ML supports descriptive, diagnostic, predictive and preemptive assurance | Audit Test / prevention | target architecture; Command Center; predictive modules | PRESENT |
| P25 | AI modules include evidence-gap, anomaly, contradiction, trust-fracture, predictive-compliance and recall blast-radius functions | Audit Test / Finding | IQ300 standards intelligence; target architecture | PRESENT |
| P27 | Command Center supports alert → acknowledge → assign → investigate → intervene → CAPA/re-verification → close/escalate → outcome measurement | Finding → Re-verification | Command Center specification | PRESENT |
| P28 | D0–certification determination decision classes govern AI/human authority; authorised certification decision workflow cannot be bypassed; D4 automatic hold cannot be automatically released where human release is required | certification review | decision-class registry; action matrix; reference runtime | PRESENT |
| P29 | AHTE uses digital twins, evidence graph, trust graph, trust packets, object genealogy and recall traversal rather than a single trust-score database | Evidence / Trust State | doctrine; trust-packet schemas; China execution model | PRESENT |
| P30 | Physical/digital object hierarchy covers organisation → facility → product → formula/version → material/supplier/process/HCP → batch/lot → pallet/logistic unit → shipment → container/seal → destination inventory → retail unit | Digital Twin | China execution model; target architecture | PRESENT |
| P31 | Complete real-time monitoring analytics feed the GHSCL + JAKIM Command Center continuously | Monitoring | Platinum stack; Command Center | PRESENT |
| P32 | Consumer/importer verification exposes authorised trust/certification/custody views without publishing confidential source data | Verification / selective disclosure | reference architecture; website spec; cryptographic architecture | PRESENT |
| P33 | Data sovereignty is federated: sensitive source records stay with the responsible jurisdiction/system; minimum-necessary signed assertions/proofs may travel | Sovereignty / Evidence | reference architecture; China execution model; target architecture | PRESENT |
| P34 | China is the origin/production ecosystem; GCC is the primary destination ecosystem; Malaysia is governance/assurance unless a physical Malaysia movement is explicitly scoped | Corridor | corridor registry; current target architecture | PRESENT |
| P35 | China→GCC operating workflows connect shipment identity, evidence, custody, authority interfaces and GCC receiving | Physical chain / Evidence | China execution pack; corridor registry | PRESENT |
| P36 | Public website, verification surface and authenticated stakeholder portals are separate experience classes; do not collapse the platform into one generic dashboard | Experience | website v2; Codex master prompt; reference architecture | PRESENT |
| P37 | Roles include manufacturer, supplier, laboratory, auditor, PHC, JAKIM/authority, GHSCL Command Center, Sinotrans/logistics, warehouse, port/customs, importer/GCC, retailer, consumer, system and device identities | Identity / Experience | target architecture; website/Codex specs; RACI | PRESENT |
| P38 | No artificial feature blocks, caps or disabled architecture because a live connector/credential/data set is not available | Implementation control | `IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md` | PRESENT / MANDATORY |
| P39 | Full target architecture is implemented now with replaceable sandbox/development providers; real connectors replace them later without redesign | Implementation control | implementation completeness rule; machine target v1.1+ | PRESENT / MANDATORY |
| P40 | Architectural completeness must never fabricate live JAKIM decisions, lab results, Sinotrans telemetry, customs release, GCC acceptance, finance/Takaful approval or shipment workflow events | Evidence integrity | implementation completeness rule; honesty layer | PRESENT / MANDATORY |
| P41 | System must support multilingual readiness for English, Simplified Chinese, Malay and Arabic/RTL | Experience | website v2; Codex master prompt | PRESENT |
| P42 | Real-time architecture is event-driven and preserves identity, provenance, actor, timestamp, control/requirement, evidence, state and integrity proof on material events | Evidence / event fabric | doctrine; China event catalogue; target architecture | PRESENT |
| P43 | Laboratory result `NOT_DETECTED` is evidence only and never equals `HALAL` | Evidence / certification workflow | lab profile; doctrine; runtime | PRESENT / HARD RULE |
| P44 | Certification state, AHTE trust state, supply-chain state, customs/port release state, financing state and Takaful state are distinct | Trust State / Authority | target architecture; finance architecture; port protocol | PRESENT |
| P45 | External systems remain systems of record where appropriate: ERP/MES/QMS/WMS/LIMS/IoT/TMS/JAKIM/port/bank/Takaful; AHTE is the cross-system trust fabric | Interoperability | reference architecture; factory API contracts; target architecture | PRESENT |

## 3. Mandatory end-to-end function

The complete system shall be represented and implemented as one connected control chain:

```text
VERIFIED RAW-MATERIAL ORIGIN
→ PRODUCER / SUPPLIER / LOT / PROVENANCE
→ SAMPLE / SEAL / CHAIN OF CUSTODY
→ CHINA LAB + TRACEABILITY / SERIALISATION
→ SIGNED SCIENTIFIC EVIDENCE
→ MANUFACTURER / ERP / MES / QMS / WMS / LIMS / IoT
→ FORMULA / BOM / MATERIAL / PROCESS
→ APPLICABLE MS + JAKIM REQUIREMENTS
→ CONTROL → HCP / SCCP
→ SMART-GLASS AI-ASSISTED SITE AUDIT
→ FINDING → CAPA / CAR → RE-VERIFICATION
→ DIRECT JAKIM API
→ PHC + JAKIM AUTHORISED HUMAN REVIEW / APPROVE-DISAPPROVE WORKFLOW
→ AHTE AUTHORITY-LINKED TRUST-STATE PROPAGATION
→ BATCH / LOT / UNIT / BOX / CARTON / PALLET
→ SINOTRANS WAREHOUSE + END-TO-END LOGISTICS
→ CONTAINER / SEAL / CUSTODY / TELEMETRY
→ CHINA PORT/CUSTOMS API
→ INTERNATIONAL TRANSIT
→ GCC PORT/CUSTOMS API
→ IMPORTER / RECEIVING / DESTINATION WAREHOUSE
→ DISTRIBUTION / RETAIL
→ BUYER / CONSUMER AUTHORISED VERIFICATION
```

Across the entire chain:

```text
AHTE EVENT + EVIDENCE FABRIC
⇅
DIGITAL TWINS + EVIDENCE GRAPH + TRUST GRAPH
⇅
CRYPTOGRAPHIC INTEGRITY + APPEND-ONLY HISTORY
⇅
AI/ML ANOMALY + PREDICTIVE ANALYTICS
⇅
PREEMPTIVE STRATEGY ENGINE
⇅
24/7 GHSCL + AUTHORISED JAKIM JOINT MONITORING COMMAND CENTER
⇅
HUMAN / AUTHORITY ACTION
```

Authorised trade/trust data may additionally feed:

`AHTE → Shariah Financing API → Islamic financing / Takaful / approved tokenomics mechanisms`

Those transaction-support domains do not alter halal certification authority.

## 4. Implementation-completeness acceptance test

No capability above may be treated as complete merely because it has prose documentation. For production-target implementation, each applicable capability requires:

`domain schema + state machine + role UI/API + production adapter contract + development/sandbox provider where needed + connector state + error/retry/reconciliation + identity/access + audit history + evidence/integrity linkage + tests + no-redesign replacement path`.

This acceptance test does not remove legitimate D4/authorised certification decision workflow human/authority controls.

## 5. Deletion rule

An artifact may be deleted as obsolete only after:

1. every unique substantive requirement has been preserved in its current replacement;
2. all active references are repointed;
3. a retirement entry records old path → replacement path → reason;
4. verified source versions are left untouched;
5. historical audit records are not rewritten merely because they document an old state;
6. repository validation passes after removal.

This matrix is the controlling pre-deletion cross-check for the 30 September 2026 consolidation.
