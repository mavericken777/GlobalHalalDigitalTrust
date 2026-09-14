# China Sovereign Deployment & HOD Debrief

## 1. Executive mandate

The China phase is an execution architecture for a sovereign/federated Halal/Tayyib trust infrastructure across the physical movement of goods and the digital movement of evidence and trust. The operating model is built around two synchronized planes:

- **Physical plane:** facility, materials, production, packaging, batch/lot, pallet, container, seal, custody, port, customs, warehouse, retail and recall.
- **Digital plane:** authority, standards, requirement, applicability, HCP, evidence, audit, laboratory result, corrective action, authority decision, trust state, APIs, events and selective disclosure.

The binding object is the auditable identity chain.

`Authority -> Requirement -> Control/HCP -> Physical execution -> Evidence -> Audit -> Authority decision -> Trust state -> Movement / release`

## 2. What must be materialised

| Layer | Material outcome | System consequence |
|---|---|---|
| Governance | Authority, mandate, decision and escalation model | Authority registry and signed decision objects |
| Standards | Machine-readable requirements and applicability | Standards/requirement/control knowledge graph |
| Manufacturer readiness | Factory, ingredient, process and personnel readiness | Digital Audit Twin + HCP/evidence plans |
| Physical integrity | Identity, segregation, sealing, custody and exceptions | Batch/pallet/container/seal twin |
| Analytical integrity | Sampling, method, result provenance | Sample chain + laboratory result objects |
| Cross-border exchange | Structured trust packets | Trust API/event interface |
| GCC admission | Destination-specific compliance and import workflow | Jurisdiction-specific rule packs |
| Continuous assurance | Monitoring, anomaly, incident and recall | Trust graph + incident graph |

## 3. Physical operating layer

### China -> GCC chain

`Manufacturer onboarding -> facility/process qualification -> material/supplier provenance -> production batch -> HCP monitoring -> packaging/lot -> palletisation -> container loading -> seal -> origin verification -> China logistics custody -> export/port -> transit -> GCC port/customs -> destination warehouse -> distribution/retail -> verification/recall`

### Critical physical objects

| Object | Digital binding | Core control |
|---|---|---|
| Facility | Facility ID + site twin | Scope, zoning, equipment, hygiene, HCP map |
| Material | Material ID + source genealogy | Origin, supplier, species/source, evidence |
| Batch/Lot | Batch ID + SKU + process version | Production genealogy and release state |
| Pallet | Pallet ID + lot aggregation | Quantity and lot reconciliation |
| Container | Container ID + shipment ID | Loading, segregation, custody |
| Seal | Serialized/cryptographic Seal ID | Apply, transfer, verify, break event |
| Warehouse location | Location ID + inventory state | Quarantine/release/reject/return |
| Retail unit | SKU/lot identity | Handling, label and recall readiness |

### Port/customs gateway

1. Officer/device authentication.
2. Shipment/container/batch resolution.
3. Minimum-necessary trust packet presentation.
4. Physical seal/package/count/condition verification.
5. Inspection observation capture.
6. Exception -> hold/quarantine/discrepancy event.
7. Signed release or hold transition.
8. Complete audit trail.

## 4. Digital trust architecture

### Core graph

`Authority -> Standard/Edition -> Requirement -> Applicability -> Control Objective -> HCP -> Evidence -> Audit Test -> Finding -> CAR -> Re-verification -> Authority Gate -> Trust State -> Physical/Digital Release`

### Core objects

Authority; AuthorityRole; Mandate; Decision; Standard; Edition; Clause; Requirement; ApplicabilityRule; Control; HCPDefinition; HCPInstance; Organisation; Facility; Person; Role; Competence; Supplier; Material; Product; SKU; Formula; Batch; Lot; Pallet; Shipment; Container; Seal; EvidenceObject; Sample; LaboratoryMethod; LabResult; Audit; Finding; CorrectiveAction; Certificate/Application/PanelCase; TrustState; Incident; Recall; DigitalEvent.

### Canonical events

`E-ORG-ONBOARD`, `E-SCOPE-CLASSIFIED`, `E-STANDARD-APPLIED`, `E-REQUIREMENT-MAPPED`, `E-HCP-OPEN`, `E-HCP-MONITOR`, `E-EVIDENCE-CAPTURED`, `E-SAMPLE-COLLECTED`, `E-LAB-RESULT`, `E-AUDIT-OPEN`, `E-AUDIT-OBSERVATION`, `E-FINDING`, `E-CAR-OPEN`, `E-CAR-CLOSE`, `E-REVERIFICATION`, `E-AUTHORITY-DECISION`, `E-LOT-RELEASE`, `E-CUSTODY-TRANSFER`, `E-SEAL-APPLIED`, `E-SEAL-BROKEN`, `E-PORT-INSPECTION`, `E-SHIPMENT-RELEASE`, `E-RECALL-OPEN`, `E-RECALL-CLOSE`.

## 5. Standards integration

The current AHTE implementation stack contains the existing Malaysian Halal standards library plus **MS 2636:2019 Halal medical device - General requirements**. The 17-flow infographic atlas reflects this set.

| Standard | Primary integration |
|---|---|
| MS 1500:2019 | Food facility, materials, processing, hygiene, storage, transport, packaging, labelling |
| MS 2400-1:2019 | Transport, loading, seals, custody, segregation, handover |
| MS 2400-2:2019 | Warehouse receiving, quarantine, zoning, stock state, dispatch, returns |
| MS 2400-3:2019 | Retail receiving, display, handling, sale, opened packs, returns, recall |
| MS 2424:2019 | Pharma materials, manufacturing, HMS, QC, outsourced activities, packaging, transport |
| MS 2634:2019 | Cosmetic ingredients/source, animal-derived materials, ethanol, manufacturing, OEM |
| MS 2738:2023 | Consumable goods product boundary, sourcing, manufacture, handling, packaging |
| MS 2803:2025 | Bone/skin/hair species/source/origin/slaughter, segregation |
| MS 2809:2025 | Chemometric authentication, datasets, models, validation, results |
| MS 2810:2025 | Pig skin/hair identification, sample chain and analytical evidence |
| MS 2393:2023 | Controlled terminology and semantic interoperability |
| MS 2627:2017 | Porcine DNA testing in food, matrix, controls and sample chain |
| MS 2627-2:2025 | Porcine DNA testing in cosmetics, qPCR and matrix validation |
| MS 1900:2025 | Organisation-level Shariah QMS, governance and management review |
| MS 2691:2021 | Halal profession competency, training, assessment and authorisation |
| MS 2610:2015 | Muslim-friendly hospitality operating context |
| MS 2636:2019 | Halal medical-device manufacturing/handling scope and evidence |

## 6. Chinese counterpart interface architecture

The exact counterpart list should be aligned to the formal itinerary and meeting mandates. The implementation architecture should be able to address:

| Functional domain | Chinese interface | AHTE interaction |
|---|---|---|
| Standardisation | Standardization Administration of China (SAC) | Standards interoperability and semantic mapping |
| Market / food safety | State Administration for Market Regulation (SAMR) | Food-safety traceability and supervision interfaces |
| Customs / border | General Administration of Customs of China (GACC) | Export, inspection, quarantine, shipment identity |
| Foreign trade | Ministry of Commerce (MOFCOM) | Trade facilitation and international economic cooperation |
| Data governance | Cyberspace Administration of China (CAC) | Cross-border data, data classification and risk controls |
| Industrial digitalisation | MIIT / relevant industrial authorities | Factory systems, industrial digitisation, platform integration |
| Conformity / accreditation | Chinese certification/accreditation ecosystem | Assessment/certification interoperability |
| Local execution | Beijing / provincial / municipal bodies as applicable | Pilot-site execution and local operating approvals |

This is an interface map, not a claim that every institution must approve or operate the programme. Each interface should receive a named owner, a defined question, required data, decision output and escalation path.

## 7. HOD decision matrix

| Decision | Required resolution | Output |
|---|---|---|
| Programme governance | Who convenes and owns the Chinese programme interface? | Sponsor + coordinating office |
| Pilot | Which factories/products enter wave one? | Named pilot roster |
| Data | What remains in China and what trust assertions may cross border? | Data-domain policy |
| Customs | What trust packet is usable at the border? | Gateway specification |
| Standards | How are Malaysian requirements represented alongside Chinese rules? | Crosswalk + precedence model |
| Certification workflow | How are competent authority decisions represented digitally? | Credential/decision schema |
| Logistics | How do carrier and port custody events bind to AHTE? | Custody integration protocol |
| Industry systems | What can ERP/MES/WMS/QMS/LIMS expose? | Integration plan |
| Laboratories | Which facilities and methods participate? | Lab network + method registry |
| Scale | How does pilot become repeatable infrastructure? | Phase-gate roadmap |

## 8. China data sovereignty architecture

China's Data Security Law applies to data-processing activities in China and defines processing broadly, including collection, storage, use, processing, transmission, provision and disclosure. The Personal Information Protection Law governs personal-information processing and includes cross-border rules. The Network Data Security Management Regulation took effect on 1 January 2025. CAC continues to publish active cross-border data guidance in 2026. These developments favour a federated architecture rather than a single uncontrolled global database.

### Recommended zones

| Zone | Examples | Default approach |
|---|---|---|
| China sovereign data zone | detailed factory, personnel, production and sensitive business records | Keep in China unless lawful cross-border mechanism applies |
| Global trust assertion zone | issuer, scope, validity, status, hashes, references | Exchange only minimum necessary trust assertions |
| GCC destination zone | importer, destination inspection, warehouse/retail release | Process according to destination requirements |
| Shared evidence pointer zone | object ID, issuer, timestamp, integrity proof | Selective disclosure |
| Analytics zone | aggregated risk/performance indicators | Minimise/de-identify where feasible |

### Minimum trust packet

`TrustAssertionID; ObjectID(s); Issuer; Scope; Validity; Status; Batch/Lot; Certificate/Decision reference; Evidence hash; Inspection/Lab indicators; Exception flags; Verification endpoint; Jurisdiction marker; Timestamp; Signature/TrustAnchor`

### Security controls

- Zero-trust human, device and machine identity.
- Strong key protection for high-value signing roles.
- Cryptographic signatures for authority decisions, release events and critical custody transitions.
- Tamper-evident event logging.
- Attribute/role/jurisdiction/purpose-based access control.
- Encryption in transit and at rest, with jurisdiction-aware key management.
- API gateway controls, schema validation, authentication, authorisation and audit logging.
- Secure offline inspection mode with later reconciliation for ports, warehouses and field environments.

## 9. GCC destination integration

### Saudi Arabia

SFDA states that imported food must meet Saudi requirements and that food items are registered by importers; relevant consignments may require halal and slaughter certificates. Its Saudi Halal Center describes eligibility review, audit and decision-committee issuance processes.

`China evidence -> AHTE trust packet -> importer/SFDA workflow -> inspection/clearance -> warehouse -> retail`

### United Arab Emirates

MoIAT describes the UAE Halal National Mark as granted after verification against approved requirements and provides a digital application/assessment process. The mark is positioned to support movement of halal products into UAE markets and onwards to global markets.

`China evidence -> AHTE trust packet -> UAE conformity/halal workflow -> customs/import release -> warehouse -> retail`

## 10. CODA manufacturer activation

`Candidate -> scope classification -> product shortlist -> supplier/material onboarding -> standards mapping -> document ingestion -> site twin -> HCP design -> evidence collection -> remediation -> audit -> lab plan -> authority pathway -> production readiness -> shipment reservation`

### Factory integration

| System | AHTE interface |
|---|---|
| ERP | Supplier, PO, item, batch and transaction references |
| MES | Work orders, process steps, production records, genealogy |
| QMS | NCR, CAPA, inspections, audits, change control |
| WMS | Inventory state, location, quarantine/release, dispatch |
| LIMS | Samples, methods, controls, results |
| IoT | Temperature/location/equipment/condition events where relevant |
| Document management | Certificates, specifications, SOPs, training records |
| HR/identity | Role, competence and authorisation |

## 11. Logistics integration

### Custody chain

`Booking -> vehicle/container qualification -> loading HCP -> seal applied -> digital custody transfer -> departure -> monitoring -> port handover -> destination arrival -> seal verification -> receiving inspection -> warehouse status`

### Shipment 001 graph

`Manufacturer -> Batch -> Pallet -> Container -> Seal -> Shipment -> Carrier -> Origin Port -> Transit -> GCC Port -> Importer -> Warehouse -> Retail -> Verification`

### Failure containment

When an integrity break occurs, calculate the smallest reliable affected graph first. Expand only where evidence demonstrates broader exposure. This supports targeted hold, withdrawal or recall actions.

## 12. AI assurance

Evidence Gap Predictor; Anomaly Engine; Contradiction Engine; Trust Fracture Engine; Predictive Compliance Engine; Recall Blast-Radius Engine.

Every model result should record model ID/version, input references, timestamp and uncertainty indicators. AI outputs remain traceable to their inputs and do not overwrite source evidence or standards objects.

## 13. Governance and accountability

| Role | Accountability |
|---|---|
| Competent authority | Policy, official interpretation, certification/decision and authority gates |
| Standards owner | Standards lifecycle and technical content |
| AHTE operator | Digital infrastructure, data model, workflow, trust graph, APIs |
| Auditor/assessor | Observation, assessment, findings and re-verification evidence |
| Laboratory | Method-controlled analytical evidence |
| Manufacturer | Operational controls and evidence generation |
| Logistics operator | Custody, transport, seal and condition controls |
| Port/customs | Inspection and border process under mandate |
| Importer/warehouse/retail | Destination handling, release/hold and recall execution |

## 14. Pilot roadmap

| Phase | Target | Exit gate |
|---|---|---|
| 0 | Governance setup | Named owners and mandates |
| 1 | Digital foundation | Core objects and APIs validated |
| 2 | Manufacturer activation | Pilot facilities audit-ready |
| 3 | Shipment 001 | End-to-end physical/digital traceability demonstrated |
| 4 | GCC operations | Warehouse/retail and recall paths stable |
| 5 | Scale | Federated multi-site/multi-route operation |

### 30-day workstream

- **Week 1:** governance owners, identifiers, system map, pilots, data zones.
- **Week 2:** site twins, standards/control ingestion, HCP/evidence templates, customs trust packet.
- **Week 3:** dry-run audit, lab simulation, container/seal twin, carrier custody test, destination release simulation.
- **Week 4:** integrated Shipment 001 rehearsal, incident/recall rehearsal, authority-decision rehearsal, HOD sign-off dossier.

## 15. HOD meeting outputs

The meeting should finish with named owners and written outputs for: programme charter; governance map; pilot roster; physical architecture; digital architecture; standards bridge; customs interface; data-governance policy; implementation schedule; funding/commercial model; scale mechanism.

### Architecture questions that must be answered

1. Who owns each critical decision, and can that decision be represented as a signed digital object?
2. Can one batch resolve through ingredient -> production -> pallet -> container -> border -> warehouse without spreadsheet reconciliation?
3. What is the exact response to a broken seal, changed certificate, corrected lab result or post-export recall?
4. Which data must remain in China and what minimum trust assertion is sufficient for the receiving jurisdiction?
5. Which factory systems can publish directly into the trust layer?
6. Which destination-country authority events must be integrated?
7. What smallest pilot proves the whole physical/digital chain?

## 16. Official source basis

- China Data Security Law: https://en.spp.gov.cn/2021-06/10/c_948426.htm
- China Personal Information Protection Law: https://en.spp.gov.cn/2021-12/29/c_948419.htm
- Network Data Security Management Regulation: https://www.cac.gov.cn/2024-09/30/c_1729384452307680.htm
- CAC September 2026 cross-border data guidance: https://www.cac.gov.cn/2026-09/11/c_1790876549989064.htm
- China Standardization Law / SAC: https://www.sac.gov.cn/Law/art/2018/art_5c7c04aba2904d859d0fddce72257f6c.html
- SAMR responsibilities: https://english.samr.gov.cn/AboutSAMR/Mainresponsibility/index.html
- MOFCOM mission: https://english.mofcom.gov.cn/About/
- Saudi SFDA halal certification: https://sfda.gov.sa/en/regulations/halal-certification-issuing-requirements
- Saudi imported food controls: https://beta.sfda.gov.sa/en/imported-food
- UAE MoIAT Halal: https://moiat.gov.ae/en/programs/halal
- UAE conformity marks service: https://moiat.gov.ae/en/services/issuance-of-license-certificate-to-use-national-conformity-marks
- China-Malaysia Joint Statement: https://www.mfa.gov.cn/eng/zy/gb/202504/t20250417_11595814.html

## 17. Repository implementation package

Recommended repository structure:

```text
master-standards-stack/
  china-deployment/
    CHINA_SOVEREIGN_HOD_DEBRIEF.md
    CHINA_COUNTERPART_INTERFACE_MATRIX.md
    DATA_SOVEREIGNTY_ARCHITECTURE.md
    SHIPMENT_001_TRUST_PACKET_SCHEMA.json
    MANUFACTURER_ONBOARDING_DOSSIER.md
    PORT_CUSTOMS_GATEWAY_SPEC.md
```
