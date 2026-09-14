# MS 2636:2019 - AHTE Control Map

**Malaysian Standard:** MS 2636:2019 - Halal medical device - General requirements

## Current catalogue basis

JSM MySOL lists MS 2636:2019 under NSC 09 - Halal, status **1st Confirmation**, published, with approval dated 30/08/2019. The MySOL description states that it specifies requirements for manufacturing and handling particular medical devices as specified by the halal competent authority for halal certification. The preview identifies a 24-page standard and a committee including JAKIM, JSM, Medical Device Authority, NPRA, Department of Chemistry, DVS, Customs and industry representatives.

Sources:
- https://mysol.jsm.gov.my/preview-file/eyJpdiI6IndpcDdZS0ZNQzVtZ2t0Y3VMTTF5c2c9PSIsInZhbHVlIjoiOUg0aHJlSnoxUWhHc2hlanBIMWlGZz09IiwibWFjIjoiYmZjY2M4OWE2OTAyYmY0MGJiYzViOGZmZjcwMDJkZDA5MzVhYWM1Njg3MGUzMjVjYThjYTIyYTY3MGVlNzExMSJ9
- https://mysol.jsm.gov.my/getPdfFileForAdmin/eyJpdiI6InM3SUpWa0RDNVJ4SWdXMXM...  (MySOL preview source; see catalogue entry above)

## Requirement family map

The preview contents identify these principal sections:

| Section | AHTE implementation family |
|---|---|
| 1 Scope | Product/scheme eligibility + applicability engine |
| 2 Normative references | Standards dependency registry |
| 3 Terms and definitions | Controlled terminology / ontology |
| 4.1 Quality management | QMS objectives, process control, records |
| 4.2 Management responsibility | Accountability, role and decision ownership |
| 4.3 Halal Management System | Halal governance, HCP, evidence and monitoring |
| 4.4 Fundamentals for halal medical devices | Halal-built-in product/process controls |
| 4.5 Halal quality control | Material/process verification and release controls |
| 4.6 Personnel and responsibility | Role assignment and competence |
| 4.7 Training | Training and competency records |
| 4.8 Personal hygiene | Personnel hygiene controls |
| 4.9 Manufacturing premise and equipment | Site twin, zoning and equipment state |
| 4.10 Manufacturing and storage areas | Controlled areas and material/product status |
| 4.11 Transportation | Transport suitability and custody |
| 4.12 Quality control areas | Laboratory/QC workflow |
| 4.13 Ancillary areas | Supporting facility controls |
| 4.14 Documentation | Controlled document/evidence system |
| 4.15 Manufacturing | Process/HCP execution |
| 4.16 Materials | Material provenance and source controls |
| 4.17 Packaging and labelling | Packaging/label identity and change control |
| 4.18 Outsourced activities | Supplier/CMO/outsourced process controls |
| 4.19 Internal audit | Audit plan, evidence and findings |
| 4.20 Legal requirements | Regulatory linkage and compliance register |
| 5 Compliance | Conformance evaluation |
| 6 Halal certificates | Certificate/decision objects |
| 7 Halal certification mark | Mark/use controls |
| Annex A | Sertu procedure lifecycle where applicable |

## AHTE flow

`Scope eligibility -> medical-device regulatory baseline -> product/material inventory -> supplier/source provenance -> facility/process twin -> HCP map -> HMS/QC controls -> manufacturing evidence -> packaging/labelling -> outsourced-activity controls -> audit -> corrective action -> re-verification -> authority workflow -> certificate/mark reference -> supply-chain traceability`

## Key integration objects

`MedicalDevice; DeviceFamily; Material; Supplier; ManufacturingSite; Equipment; ProcessStep; HCP; Evidence; Batch; Lot; Packaging; LabelVersion; OutsourcedActivity; Audit; Finding; CorrectiveAction; Certificate; AuthorityDecision; Shipment; TrustAssertion`

## Critical cross-links

- **Medical Device Act / MDA interface:** regulatory product safety and performance obligations should be represented separately but linked in the product compliance graph; the MS 2636 introduction states that medical devices must comply with the Medical Device Act 2012 before halal certification.
- **JAKIM/JAIN authority layer:** halal scope, assessment and decision objects connect to AHTE authority workflows.
- **MDA / MOH:** medical-device regulatory status and device classification become required product metadata.
- **NPRA:** linked where a product/process also crosses pharmaceutical regulatory boundaries.
- **Laboratory:** analytical/QC evidence is connected to exact sample, method and batch.
- **Supply chain:** MS 2400 transport/warehousing/retailing controls bind downstream movement to the device/batch graph when applicable.

## Digital control design

Every critical MS 2636 object should carry: `StandardID; Edition; RequirementID; Applicability; ControlID; HCPID; EvidenceRule; AuditTest; Owner; Status; Version; EffectiveFrom; SourceHash`.
