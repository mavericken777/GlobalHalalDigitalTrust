# AMANAH HALAL TRUST ECOSYSTEM (AHTE)
## A-Z End-to-End Platform Mapping to the JAKIM/JSM Halal Standards Stack

AHTE is the end-to-end sovereign/federated digital trust platform layer for Halal/Tayyib assurance. It does not replace JAKIM, JAIN, JSM, laboratories, regulators, certification panels, or other competent authorities. It operationalises evidence, controls, audit execution, traceability, risk management, authority gates, and trusted information exchange around applicable Malaysian Halal standards and related instruments.

## Canonical control chain
`Shariah/Fatwa -> Competent Authority -> Applicable Standard Set -> Requirement -> Applicability Decision -> Control Objective -> Control -> HCP -> Evidence -> Audit Test -> Finding -> Corrective Action -> Re-verification -> Authority Gate -> Trust State -> Physical/Digital Release`

## Standards universe represented
- MS 1500:2019 - Halal food - General requirements
- MS 2400-1:2019 - Halal supply chain management system - Transportation
- MS 2400-2:2019 - Halal supply chain management system - Warehousing
- MS 2400-3:2019 - Halal supply chain management system - Retailing
- MS 2424:2019 - Halal pharmaceuticals - General requirements
- MS 2634:2019 - Halal cosmetics - General requirements
- MS 2738:2023 - Halal consumable goods - General requirements
- MS 2803:2025 - Usage of animal bone, skin and hair - General requirements for halal products
- MS 2809:2025 - Authentication of products using chemometric techniques
- MS 2810:2025 - Consumable goods - Test method - Identification of pig skin and hair
- MS 2393:2023 - Islamic and halal terminologies - Definitions and interpretations
- MS 2627:2017 - Detection of porcine DNA - Test method - Food and food products
- MS 2627-2:2025 - Detection of porcine DNA - Test method - Part 2: Cosmetics
- MS 1900:2025 - Shariah-based quality management system - Requirements
- MS 2691:2021 - Halal profession - General requirements
- MS 2610:2015 - Muslim-friendly hospitality services (supporting context)

Historical/replaced standards are retained as lineage metadata, not current production requirements.

## A-Z platform decomposition

### A - Authority & Accountability
Authority registry, role matrix, mandate, delegation, approval, panel-case and decision objects. Certification authority remains external/competent-authority controlled.

### B - Batch, Lot & Boundary Identity
Product/SKU/batch/lot/pallet/container/unit/sample identity, genealogy, status and affected-scope boundaries.

### C - Compliance Knowledge Graph
Standards, editions, clauses, applicability rules, controls, HCPs, evidence rules, audit tests, dependencies and authority relationships.

### D - Digital Audit Twin
Facility/site/process/asset/control digital representation for planning, audit execution and continuous assurance.

### E - Evidence Fabric
Document, record, image/video, sensor, certificate, lab result, interview, observation and trace-log evidence with provenance, timestamps and integrity metadata.

### F - Facility, Premise & Flow Control
Premise zoning, material/person/product flows, sanitation, segregation and controlled areas.

### G - Governance & Change Control
Policy ownership, document control, change requests, impact analysis, approval, implementation and re-verification.

### H - Halal Control Point Engine
HCP identification, risk scoring, monitoring, verification, exceptions and re-verification.

### I - Identity, Access & Islamic Integrity Roles
RBAC, responsible persons, Halal Executive/Supervisor profiles, professional competence and authority-linked roles.

### J - Journey / Case Orchestration
Onboarding, application, audit, certification, surveillance, change, incident, complaint and recall cases.

### K - Knowledge & Competency
Qualification, training, competence assessment, role authorisation, expiry, renewal and professional development.

### L - Laboratory & Analytical Evidence
Sample management, method/version, matrix, controls, validation, result interpretation and limitations. Laboratory results are evidence, not certification.

### M - Material & Ingredient Provenance
Ingredient/source genealogy, supplier, origin, certificates, specifications, animal/plant/mineral classification and transformation/route provenance.

### N - Nonconformity, CAR & Re-verification
NCR classification, containment, root cause, corrective action, effectiveness check, re-verification and authority escalation.

### O - Order, Transport & Custody
Movement planning, carrier qualification, vehicle/container suitability, custody transfer, seal and route exception controls.

### P - Product & Process Assurance
Formula/version, manufacturing/process steps, packaging, labelling, handling and product lifecycle controls.

### Q - Quality & Shariah-based QMS
Objectives, process management, internal audit, management review and continual improvement.

### R - Risk, Resilience & Recall
Risk scoring, scenario analysis, containment, withdrawal/recall, trace-back, trace-forward and blast-radius analysis.

### S - Segregation, Sertu & Sanitation
Halal/non-halal separation, contamination prevention, sanitation and sertu lifecycle with authority verification where required.

### T - Traceability & Trust Graph
Product genealogy, custody graph, evidence graph, authority decisions and trust-state transitions.

### U - User, Stakeholder & Consumer Verification
Controlled disclosure, certificate/status presentation, stakeholder portals and consumer verification views.

### V - Vehicle, Warehouse & Retail Control
Fleet/vehicle controls, warehouse status/zoning and retail receiving/display/handling.

### W - Workflow, Work Instruction & Witnessing
Controlled SOP/work-instruction execution, assignments, checklists, witnessing and operational records.

### X - eXception & Escalation Management
Rule violations, analytical alerts, supply-chain breaks, missing evidence, overdue actions and authority referrals.

### Y - Yard, Port, Customs & Border Trust Gateway
Shipment authentication, seal verification, inspection, exception handling and release/hold status.

### Z - Zero-Knowledge / Selective Disclosure / Evidence Sovereignty
Purpose-limited disclosure, data sovereignty, tamper evidence and minimum-necessary verification data.

## Standard-to-AHTE mapping

| Standard | Main AHTE domains | Core HCP families | Evidence / audit | Authority gate |
|---|---|---|---|---|
| MS 1500:2019 | C,D,E,F,H,M,P,Q,R,S,T,W | materials, processing, sanitation, equipment, storage, packaging, labelling | specs, supplier evidence, certificates, site/record/interview/test | MATERIAL, CERTIFICATION, SERTU, SLAUGHTER/STUNNING as applicable |
| MS 2400-1:2019 | B,C,D,E,H,O,R,T,V,W,X,Y | vehicle, loading, seals, custody, segregation, handover | vehicle/seal/custody records, inspection, traceability | TRANSPORT, EXCEPTION, RELEASE |
| MS 2400-2:2019 | B,C,D,E,H,R,T,V,W,X | receiving, quarantine/release/reject/return, storage, dispatch | stock/zoning/seal/trace records | WAREHOUSE, DISPOSITION |
| MS 2400-3:2019 | B,C,D,E,H,P,R,T,U,V,W,X | receiving, display, handling, opened packs, returns | receiving/store/label/staff evidence | RETAIL, PRODUCT RELEASE |
| MS 2424:2019 | C,D,E,F,G,H,I,K,L,M,P,Q,R,S,T,W,X | API/raw material/excipients, manufacturing, storage, transport, packaging, outsourced activities, vaccine dependencies | material origin, GMP/HMS records, certificates, lab | PHARMA MATERIAL, OUTSOURCE, CERTIFICATION |
| MS 2634:2019 | C,D,E,F,H,K,L,M,P,R,S,T,W,X | ingredient source/route, animal-derived materials, ethanol, manufacturing, packaging, OEM | INCI/source evidence, supplier certs, lab and site evidence | COSMETIC MATERIAL, OEM, CERTIFICATION |
| MS 2738:2023 | C,D,E,F,H,K,M,P,R,S,T,W,X | material sourcing, manufacture, handling, storage, packaging | specifications, certificates, process records, inspections | CONSUMABLE CERTIFICATION |
| MS 2803:2025 | C,E,H,L,M,P,R,S,T | animal species/source/slaughter-or-origin/segregation | source, species, slaughter/origin, supplier/test evidence | ANIMAL MATERIAL, CERTIFICATION |
| MS 2809:2025 | C,E,L,R,T | analytical dataset, chemometric model, validation, sample/result | dataset, model metadata, validation, report | LAB METHOD, AUTH DECISION |
| MS 2810:2025 | C,E,L,M,T | pig-origin skin/hair identification | sample chain, method metadata, analytical result | ANALYTICAL EVIDENCE |
| MS 2393:2023 | C,I,J,T,U | controlled terminology and semantics | ontology/definition evidence | TERMINOLOGY FREEZE |
| MS 2627:2017 | C,E,L,M,R,T | porcine DNA evidence in food | sample chain, PCR controls, result | LAB EVIDENCE, AUTH DECISION |
| MS 2627-2:2025 | C,E,L,M,R,T | porcine DNA evidence in cosmetics | sample chain, qPCR controls/validation, result | LAB EVIDENCE, AUTH DECISION |
| MS 1900:2025 | A,C,G,I,J,K,Q,R,T,W,X | organisation-level Shariah QMS | policies, objectives, audits, reviews, records | MANAGEMENT REVIEW / CERTIFICATION AS APPLICABLE |
| MS 2691:2021 | A,C,I,K,J,U | professional competence | qualification, training, assessment, authorisation | PROFESSIONAL RECOGNITION AS APPLICABLE |
| MS 2610:2015 | C,F,K,P,S,U,V,W | accommodation/service environment | premises/service/staff/guest-facing evidence | HOSPITALITY AS APPLICABLE |

## Core data model
Authority; Organisation; Facility; Person/Role/Competence; Product/SKU/Formula; Ingredient/Raw Material; Supplier; Animal/Source Provenance; Process/Process Step; HCP; Control; Evidence; Laboratory Sample/Result; Audit; Finding/NCR; Corrective Action; Certificate/Application/Panel Case; Shipment/Pallet/Container/Seal; Warehouse Inventory Status; Retail Execution; Incident/Recall; Trust State; Standard/Edition/Clause/Version; Policy/Fatwa/Protocol/Circular; Digital Event.

## Canonical events
`E-ORG-ONBOARD`, `E-SCOPE-CLASSIFIED`, `E-STANDARD-APPLIED`, `E-REQUIREMENT-MAPPED`, `E-HCP-OPEN`, `E-HCP-MONITOR`, `E-EVIDENCE-CAPTURED`, `E-SAMPLE-COLLECTED`, `E-LAB-RESULT`, `E-AUDIT-OPEN`, `E-AUDIT-OBSERVATION`, `E-FINDING`, `E-CAR-OPEN`, `E-CAR-CLOSE`, `E-REVERIFICATION`, `E-AUTHORITY-DECISION`, `E-CERTIFICATE-ISSUED`, `E-CERTIFICATE-SUSPENDED`, `E-TRUST-STATE-CHANGED`, `E-LOT-RELEASE`, `E-CUSTODY-TRANSFER`, `E-SEAL-APPLIED`, `E-SEAL-BROKEN`, `E-PORT-INSPECTION`, `E-SHIPMENT-RELEASE`, `E-RECALL-OPEN`, `E-RECALL-CLOSE`.

## Trust state
`PENDING -> EVIDENCE-COMPLETE -> ASSESSED -> VERIFIED -> VERIFIED-WITH-EXCEPTION -> RELEASED`
Failure/hold states include HOLD, QUARANTINED, DISPUTED, CORRECTIVE_ACTION, RE-VERIFICATION, EXPIRED, SUSPENDED, REVOKED and RECALLED.

**No AI model, laboratory result, QR code, blockchain record, manufacturer declaration or platform event independently creates Malaysian Halal certification.**

## Production freeze
Every production rule must carry exact standard number/edition, confirmation or revision status, effective date, supersession lineage, MPPHM/MHMS edition, current protocol, applicable circular/Pekeliling/fatwa/law/regulator requirement, laboratory method version where applicable, authority owner, source provenance/hash and implementation test evidence.

## Visual and process assets
The package includes full Mermaid process flows and SVG architecture/coverage visuals. Complete source package is also preserved as an archive in the `master-standards-stack` tree for zero-content-loss transport and auditability.
