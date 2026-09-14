# IQ300 MASTER STANDARDS REGISTER

## 1. Governance stack

```text
Shariah / Fatwa / Law
        |
        v
Competent Halal Authority / JAKIM / JAIN / MAIN
        |
        v
MPPHM + MHMS + Protocols + Pekeliling / Circulars
        |
        +------------------------------+
        |                              |
        v                              v
Product / Service MS             Supply-chain MS
        |                              |
        +--------------+---------------+
                       |
                       v
             IQ300 Requirement Object
                       |
                       v
             Control / HCP / Risk
                       |
                       v
                 Evidence Fabric
                       |
                       v
                  Audit Test
                       |
                       v
             Finding / CAR / Re-test
                       |
                       v
                Authority Gate
                       |
                       v
                  Trust State
```

## 2. Current core library

| Standard | Functional class | Current/source status used by IQ300 | Primary IQ300 role |
|---|---|---|---|
| MS 1500:2019 | Product | 1st Confirmation 2024 per supplied compendium / MySOL check | Food and nutrient supplement halal requirements |
| MS 2400-1:2019 | Chain | 1st Confirmation 2024 | Transportation integrity |
| MS 2400-2:2019 | Chain | 1st Confirmation 2024 | Warehouse integrity |
| MS 2400-3:2019 | Chain | 1st Confirmation 2024 | Retail integrity |
| MS 2424:2019 | Product | 1st Confirmation | Halal pharmaceuticals |
| MS 2634:2019 | Product | 1st Confirmation 2025 | Halal cosmetics |
| MS 2738:2023 | Product | Original | Halal consumable goods |
| MS 2803:2025 | Product/material | Original | Animal bone, skin and hair |
| MS 2393:2023 | Terminology | 1st Revision | Controlled Islamic/Halal vocabulary |
| MS 2627:2017 | Test method | Published | Porcine DNA PCR for food |
| MS 2627-2:2025 | Test method | Original | Porcine DNA qPCR for cosmetics |
| MS 1900:2025 | System | 2nd Revision | Organisation-wide Shariah QMS |
| MS 2691:2021 | Profession | Original | Halal professional competence |
| MS 2610:2015 | Service | Referenced | Muslim-friendly hospitality |
| MS 2809:2025 | Authentication/test support | Original | Chemometric product authentication |
| MS 2810:2025 | Test method | Original | Identification of pig skin and hair |

JSM MySOL currently surfaces MS 2809:2025 and MS 2810:2025 in its Halal-sector catalogue. Source: https://mysol.jsm.gov.my/search-catalogue?is-advance=1&page=1&sector=204

## 3. MS 1500:2019 - Halal food

### Requirement domains
- Scope: manufacturing and handling of halal foods, including nutrient supplements.
- Normative references and controlled definitions.
- Management responsibility: halal integrity, records, religious practice, staff participation.
- Premises and facilities: layout, effective cleaning/inspection, pest control, potable water, waste management, Muslim facilities, prevention of halal/non-halal cross-contamination.
- Devices, utensils, machines and processing aids: halal status and contamination prevention; authority-verified sertu where mughallazah contact occurs.
- Hygiene, sanitation and food safety: operational hygiene and toyyib conditions.
- Processing: ingredients, additives, aids, preparation, cooking, packing and storage preserve halal status.
- Storage, transport, display, sale and serving: downstream integrity controls.
- Packaging, labelling and advertising: no misleading halal claim; mark only after competent-authority grant.
- Legal requirements and authority inspection.
- Annex: sertu method for najs al-mughallazah.

### Revision boundary
The 2019 revision deleted the standalone slaughtering-process clause and annex from the old standard. New digital logic must point slaughter/stunning controls to the current Malaysian Protocol for Halal Meat and Poultry Production plus applicable JAKIM circulars/fatwa, not the old 2009 numeric tables.

### High-risk objects
Animal-origin ingredients, meat-derived inputs, gelatin/collagen, contact equipment, shared lines, mughallazah contamination, mixed-load/storage interfaces, packaging claims, and slaughter/stunning controls.

## 4. MS 2400 series - Halal supply chain management system

### Common system architecture
- Scope
- Normative references
- Terms and definitions
- Organisational context
- Leadership and halal policy
- Roles and responsibilities
- Planning: risks, opportunities, HCPs and objectives
- Support: resources, competence, awareness, communication, documented information
- Operational planning and control
- Segregation and identification
- Traceability
- Preservation
- Nonconforming outputs
- Outsourced processes
- Monitoring and measurement
- Internal audit
- Management review
- Nonconformity and corrective action
- Continual improvement

### MS 2400-1:2019 Transportation
Control the halal integrity of goods/cargo through road, sea, air, rail and multimodal transport. IQ300 objects include vehicle/container status, cleaning and sertu records, cargo segregation, seal and custody events, loading/delivery handover evidence, temperature/condition controls where toyyib requires them, driver/handler competence, outsourced carrier controls and mixed-load exception logic. Loading and delivery interfaces are critical HCPs.

### MS 2400-2:2019 Warehousing
Control receiving, quarantine, released/rejected/returned states, storage segregation, pest/hygiene controls, floor/rack cleanability, seal/document checks, FIFO/FEFO where relevant, returns/damage/spills, outsourced warehouse controls and dispatch interface. Nonconforming product must not return to the halal stream without authorised disposition.

### MS 2400-3:2019 Retailing
Control receiving, display, serving/sale, separation from non-halal activities, utensils/surfaces/equipment, staff competence/hygiene, honest labelling/advertising, opened packs, tasting samples, returns and retail traceability.

### Certification boundary
A product certificate does not automatically certify an independent transporter, warehouse or retailer. Each claimed halal node is a separate control and certification object under the applicable scheme.

## 5. MS 2424:2019 - Halal pharmaceuticals

### Clause-family map represented in IQ300
- 4.1 Halal pharmaceutical quality system.
- 4.2 Management responsibility.
- 4.3 Halal Management System.
- 4.4 Fundamentals for halal pharmaceuticals.
- 4.5 Halal quality control.
- 4.6 Personnel and responsibility.
- 4.7 Training.
- 4.8 Personal hygiene.
- 4.9 Manufacturing premise and equipment.
- 4.10 Manufacturing and storage areas.
- 4.11 Transportation.
- 4.12 Quality-control areas.
- 4.13 Ancillary areas.
- 4.14 Documentation.
- 4.15 Manufacturing.
- 4.16 Materials.
- 4.17 Packaging and labelling.
- 4.18 Outsourced activities.
- 4.19 Self-inspection.
- 4.20 Legal requirements.
- Clause 5 compliance.
- Clause 6 halal certificates.
- Clause 7 halal certification mark.
- Annex A sertu.
- Annex B typical vaccine HCPs.

### Material and process graph
API -> API starting material -> excipient -> solvent/buffer/preservative/stabiliser/process aid -> capsule -> packaging/contact materials -> manufacturing/filling -> QC -> release. Each node carries origin evidence and applicable halal decisions.

### Synthetic-material assessment
Source and synthesis route are both control objects: catalyst, solvent, enzyme and other processing aids must be evaluated rather than assuming that chemical identity alone proves halal provenance.

### Vaccine / biologics HCP graph
Cell/seed accession -> media/sera/trypsin/peptone -> adjuvant/carrier protein -> culture/harvest -> purification resins/enzymes/buffers -> formulation -> filling lot -> animal-house controls where present -> waste/rejected lots. The compendium explicitly requires the official Annex B table to be pulled from the JSM standard before a vaccine rule set is frozen.

## 6. MS 2634:2019 - Halal cosmetics

### Core control domains
Management; material provenance; hygiene/safety; manufacturing/handling/distribution; equipment/lines; packaging/labelling/advertising; legal/NPRA interface; OEM/contract manufacturing; sertu; laboratory evidence.

### High-risk ingredient classes explicitly represented
- animal fats and tallow derivatives
- collagen and gelatin
- keratin
- placenta and musk
- lanolin
- ethanol/alcohol source where fatwa-sensitive
- glycerin
- stearates/emulsifiers with unknown fat origin
- carmine/cochineal
- human-derived materials not permitted under applicable Shariah/fatwa
- enzymes and fermentation media involving animal peptone
- animal-hair brushes/applicators

Each INCI line should resolve to source organism or synthesis route, supplier and acceptable halal evidence. Syubhah is treated as a blocking state until cleared.

### OEM logic
The brand owner cannot bypass control of the actual manufacturing process. The contract manufacturer must be controllable under the applicable cosmetics halal scheme and be represented in the trust graph.

### Laboratory support
MS 2627-2:2025 is the cosmetics qPCR method. The food method is not automatically transferable to cosmetic matrices without validation.

## 7. MS 2738:2023 - Halal consumable goods

Applies to halal consumable goods outside the classic food/pharmaceutical/cosmetic scopes. IQ300 maps scope, references, terms, management, materials, premises/equipment, process controls, packaging/labelling, legal compliance, certification and authority decision. Product boundaries are determined case-by-case under the relevant MPPHM consumer-goods scheme.

## 8. MS 2803:2025 - Animal bone, skin and hair

Current JSM catalogue identifies this as requirements for relevant industries using bone, skin and hair in accordance with Shariah law and fatwa. IQ300 maps species/origin, slaughter status where applicable, processing integrity, najs prevention, segregation, traceability and certification-file evidence. Brushes, hair, skins and related animal-derived inputs connect to material-provenance and test-method objects.

## 9. MS 2393:2023 - Islamic and halal terminologies

Controlled vocabulary layer for definitions and interpretations used throughout the Halal standards system. IQ300 treats terms such as halal, haram, najs, sertu, fatwa, competent authority, syubhah and mutlaq water as ontology objects with source/version metadata.

## 10. MS 2627:2017 and MS 2627-2:2025 - Porcine DNA evidence

### MS 2627:2017 food
Qualitative PCR identification/confirmation of porcine DNA in food matrices. The compendium identifies raw, processed and highly processed matrices, homogeneous/heterogeneous samples, validated method modifications for difficult matrices, required analytical controls and the need to reject invalid runs rather than report false negatives.

### MS 2627-2:2025 cosmetics
Current MySOL states qualitative porcine-DNA detection for solid, semi-solid and liquid cosmetics using qPCR, with validated adjustment permitted for unique matrices. Surfactants, pigments, ethanol and waxes can affect extraction/yield.

### Interpretation boundary
Not detected != bovine origin and not detected != halal certification. Gelatin and highly refined materials may be DNA-poor. Source/species/slaughter/recognised halal evidence remains decisive. Analytical evidence is a support object, not an authority decision.

## 11. MS 1900:2025 - Shariah-based quality management system

Organisation-wide generic Shariah QMS for consistent conformity with Shariah law/fatwa, stakeholder needs and applicable statutory/regulatory requirements, plus improvement. It is distinct from Malaysia-specific Halal Management System / HAS and does not itself confer a product halal mark.

## 12. MS 2691:2021 - Halal profession

Competence framework for halal professionals. IQ300 uses it to model qualifications, training, experience, competence assessment and role authorization for Halal Executives, auditors, consultants and related roles. Human competence is itself a trust object.

## 13. MS 2610:2015 - Muslim-friendly hospitality

Referenced service standard for accommodation, tour packages and tourist guides. IQ300 connects its service controls to the relevant manual procedure and authority pathway rather than assuming that a general product certificate covers hospitality services.

## 14. MS 2809:2025 - Chemometric authentication

Current JSM MySOL describes mathematical modelling and statistical analysis of quantitative chemical datasets for product authentication. IQ300 maps dataset provenance, analytical method, modelling, statistical validation, software configuration, model versioning and authentication evidence. This is analytical evidence, not a standalone halal certification decision.

## 15. MS 2810:2025 - Pig skin and hair identification

Current MySOL describes identification of pig-origin skin and hair for raw hides/skins/leather products, brushes, loose hair and fur, with a stated non-applicability to highly processed leather and hair. IQ300 maps sample-scope eligibility, sample identity, method execution, result, limitations and linkage to the relevant material/halal authority decision.

## 16. Supporting / historical references

Supporting references identified by the supplied compendium include MS 1480, MS 1514 and MS 2594. Historical/replaced instruments include MS 1500:2009, MS 2424:2012, MS 2200-1:2008, MS 2200-2:2013, earlier MS 2400 series and MS 2565. These are retained for migration/version control only and must not be used as current requirements when a replacement exists.

## 17. Cross-standard control families

1. Material origin/provenance.
2. Animal species/slaughter eligibility.
3. Segregation.
4. Equipment status.
5. Sertu.
6. Hygiene/sanitation/toyyib.
7. HCP identification and risk assessment.
8. Chain of custody and seals.
9. Traceability.
10. Nonconforming output and quarantine.
11. Outsourced provider control.
12. Personnel competence.
13. Documented information.
14. Internal audit and management review.
15. Corrective action and re-verification.
16. Laboratory evidence and method validity.
17. Packaging/labelling/claim control.
18. Authority/certificate/logo separation.
19. Version freeze.
20. Physical/digital asset binding.

## 18. IQ300 trust states

`PENDING -> EVIDENCE-COMPLETE -> ASSESSED -> AUTHORITY-PENDING -> VERIFIED`

Exception states:
`HOLD | QUARANTINED | NONCONFORMING | CORRECTIVE_ACTION | RE-VERIFICATION | DISPUTED | VERIFIED-WITH-EXCEPTION | EXPIRED | REVOKED | RECALLED`

No analytical result, AI inference, QR code, blockchain record, private certificate, or manufacturer declaration can independently create a competent-authority Halal certification state.
