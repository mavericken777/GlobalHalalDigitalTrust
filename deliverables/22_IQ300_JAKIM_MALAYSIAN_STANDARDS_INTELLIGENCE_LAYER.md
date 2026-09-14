# IQ300 — JAKIM / Malaysian Halal Standards Intelligence Layer

## Status

**Architecture baseline derived from the two supplied JAKIM / Malaysian Halal standards compendia.**

This document converts the supplied compendia into an IQ300 regulatory-intelligence and digital-trust architecture. It is intentionally a **secondary-source architecture layer**. The compendia are structured reference summaries, not substitutes for authoritative JSM/MySOL standards, JAKIM/JAIN/MAIN instruments, MPPHM, MHMS, Malaysian protocols, circulars, fatwa or applicable law.

## 1. Core regulatory model

IQ300 shall keep five layers distinct:

1. **Shariah / fatwa layer** — Islamic rulings, interpretations and applicable authoritative decisions.
2. **Competent-authority layer** — JAKIM/JAIN/MAIN and other competent authorities within their mandates.
3. **Certification operating layer** — MPPHM, MHMS, HAS/IHCS, procedures, circulars and protocols.
4. **Technical standards layer** — Malaysian Standards and applicable test-method standards.
5. **Digital assurance layer** — evidence, audit, laboratory results, custody events, decisions and trust states.

### Non-negotiable rule

A Malaysian Standard, laboratory result, AI output, QR/NFC/RFID record, blockchain record, manufacturer declaration or platform record does **not by itself create Malaysian Halal certification status**. Authority decisions remain with the competent authority under its mandate.

## 2. Master Malaysian standards catalogue represented by the compendia

| Domain | Standard | IQ300 function |
|---|---|---|
| Food | MS 1500:2019 | Food/product and process controls |
| Transportation | MS 2400-1:2019 | Halal transport integrity and custody |
| Warehousing | MS 2400-2:2019 | Storage, segregation and handling integrity |
| Retailing | MS 2400-3:2019 | Receiving, storage, retail handling and records |
| Pharmaceuticals | MS 2424:2019 | Pharmaceutical material/process assurance |
| Cosmetics | MS 2634:2019 | Cosmetic ingredient/process assurance |
| Consumable goods | MS 2738:2023 | Broader consumable-goods assurance |
| Animal bone/skin/hair | MS 2803:2025 | Animal-derived material provenance |
| Terminology | MS 2393:2023 | Controlled Islamic/Halal vocabulary |
| Food DNA testing | MS 2627:2017 | Porcine-DNA analytical evidence |
| Cosmetic DNA testing | MS 2627-2:2025 | Porcine-DNA analytical evidence for cosmetics |
| Shariah QMS | MS 1900:2025 | Organisation-level Shariah-based quality management |
| Halal profession | MS 2691:2021 | Professional competence layer |
| Hospitality | MS 2610:2015 | Muslim-friendly hospitality controls |

Historical/replaced standards identified by the compendia should be retained only as versioned historical references and never silently treated as current requirements.

## 3. IQ300 regulatory object model

Every requirement shall be represented as structured data rather than only a PDF attachment.

```text
STANDARD
 ├─ standard_id
 ├─ title
 ├─ edition_year
 ├─ confirmation_status
 ├─ effective_date
 ├─ supersedes
 ├─ jurisdiction
 ├─ source_authority
 └─ CLAUSE / REQUIREMENT
     ├─ requirement_statement
     ├─ applicability
     ├─ control_id
     ├─ HCP_id
     ├─ required_evidence
     ├─ verification_method
     ├─ responsible_actor
     ├─ finding_type
     ├─ corrective_action
     └─ authority_decision_gate
```

No exact clause number or normative wording should be fabricated from a secondary compendium. Exact clause mapping is a controlled verification task against the authoritative edition.

## 4. Version-freezing requirement

Every regulatory rule used by IQ300 must preserve:

- standard identifier;
- edition/year;
- confirmation/status where applicable;
- effective date;
- superseded/replaced relationship;
- jurisdiction;
- authoritative source;
- MPPHM/MHMS version where relevant;
- protocol/circular/fatwa reference where relevant;
- laboratory method/version where relevant.

Historical decisions must remain attached to the rule version applicable when the event occurred. Regulatory updates create new versions; they do not rewrite historical evidence.

## 5. MS 1500:2019 intelligence model

The compendia describe MS 1500:2019 as the foundational food standard covering areas including management responsibility, premises/facilities, equipment/utensils, hygiene, sanitation, food safety, processing, storage, transportation, display, sale/serving, packaging, labelling, advertising and legal requirements.

The compendia also emphasize that the 2019 revision does not contain the former detailed slaughter clause/annex structure from MS 1500:2009. Detailed slaughter/stunning controls are instead connected to the Malaysian Protocol for Halal Meat and Poultry Production and other authoritative JAKIM/fatwa/circular instruments.

**IQ300 rule:** do not hard-code old MS 1500:2009 slaughter parameters as current MS 1500:2019 rules.

Slaughter controls should be represented dynamically:

```text
SLAUGHTER CONTROL
 ├─ species
 ├─ method
 ├─ stunning parameters where applicable
 ├─ protocol version
 ├─ circular/fatwa reference
 ├─ effective date
 ├─ operator competence
 └─ authority verification
```

## 6. Sertu as a lifecycle control

The compendia distinguish prescribed sertu from laboratory testing. Laboratory evidence cannot be treated as a substitute for the prescribed cleansing process.

IQ300 event pattern:

```text
CONTAMINATION / NAJS EVENT
        ↓
AFFECTED ASSET IDENTIFIED
        ↓
QUARANTINE / HOLD
        ↓
SERTU PROCEDURE
        ↓
EXECUTION EVIDENCE
        ↓
COMPETENT-AUTHORITY VERIFICATION WHERE REQUIRED
        ↓
RELEASE
```

Recommended event codes:

- `E-SERTU-OPEN`
- `E-SERTU-PROCEDURE`
- `E-SERTU-EVIDENCE`
- `E-SERTU-CLOSE`
- `E-AUTHORITY-VERIFY`
- `E-ASSET-RELEASE`

## 7. MS 2400 supply-chain intelligence layer

### MS 2400-1 — Transportation

Represent transport as a custody lifecycle including source identification, documented controls, segregation, traceability, monitoring, verification, corrective action, recall/withdrawal and record control.

### MS 2400-2 — Warehousing

Represent warehouse integrity through receiving, verification, segregation/separation, storage, handling, condition monitoring, outsourced-party controls, dispatch and records.

### MS 2400-3 — Retailing

Represent retail integrity through supplier monitoring, receiving checks, storage, identification/separation, preparation/dispatch, proof of delivery and retail records.

### Supply-chain graph

```text
MANUFACTURER
   ↓
LOADING
   ↓
CONTAINER + SEAL
   ↓
TRANSPORT
   ↓
PORT / BORDER
   ↓
WAREHOUSE
   ↓
DISTRIBUTION
   ↓
RETAIL
```

Each transition is an event and each event can preserve or degrade trust.

## 8. MS 2424 pharmaceutical intelligence

The compendia identify a broad pharmaceutical material universe, including APIs, API starting materials, excipients, solvents, buffers, preservatives, stabilisers, process aids, growth media, adjuvants, carrier proteins, capsules, stoppers, inks, packaging, enzymes and other inputs.

IQ300 must therefore represent pharmaceutical provenance as a dependency graph rather than a finished-product certificate only.

```text
PRODUCT
  ↓
MANUFACTURING LOT
  ├─ API
  ├─ EXCIPIENTS
  ├─ PROCESS AIDS
  ├─ SOLVENTS
  ├─ ENZYMES
  └─ PACKAGING
       ↓
SOURCE → SUPPLIER → MANUFACTURING ROUTE → EVIDENCE → DECISION
```

For synthetic materials, the compendium supports route-level assessment involving source, catalyst, solvent, enzyme/processing aid, intermediates and final material.

For outsourced activities, IQ300 must retain relationships between the responsible organisation and contract manufacturers, laboratories and packers. Outsourcing does not erase the responsibility of the accountable organisation.

## 9. Biologics / vaccine control model

The second compendium identifies HCP domains including cell/seed accession, media, sera, trypsin, peptone, adjuvants, carrier proteins, culture, harvest, purification, resins, enzymes, buffers, filling lots, animal-house controls, rejected lots and waste.

IQ300 should model this as a multi-tier process-dependency graph:

```text
VACCINE / BIOLOGIC LOT
 ├─ seed / accession
 ├─ cell system
 ├─ growth media
 ├─ processing aids
 ├─ adjuvant
 ├─ harvest
 ├─ purification
 ├─ formulation
 ├─ filling
 └─ packaging
```

Detailed annex values must be frozen only after authoritative source verification.

## 10. MS 2634 cosmetics intelligence

The compendia identify ingredient-origin concerns including glycerin, stearates, emulsifiers, collagen, gelatin, keratin, placenta, lanolin, tallow derivatives, carmine/cochineal, alcohol/ethanol source, enzymes, fermentation media and animal-derived brushes/applicators.

IQ300 principle:

**Chemical/INCI identity is not equivalent to Halal provenance.**

```text
INCI / MATERIAL
   ↓
SUPPLIER
   ↓
SOURCE / ORIGIN
   ↓
MANUFACTURING ROUTE
   ↓
PROCESSING AIDS
   ↓
HALAL EVIDENCE
   ↓
AUTHORITY STATUS
```

## 11. MS 2803 animal-derived materials

Animal bone, skin and hair are to be treated as provenance-sensitive material classes and linked to downstream product domains such as cosmetics and consumable goods where applicable.

Core data:

- species;
- source;
- slaughter status where applicable;
- processor;
- origin;
- supplier;
- batch;
- segregation;
- evidence;
- certification/authority status.

## 12. MS 2393 terminology / ontology layer

MS 2393:2023 should inform the controlled vocabulary layer of IQ300.

```text
CONCEPT
 ├─ canonical term
 ├─ Malay term
 ├─ Arabic term where relevant
 ├─ English term
 ├─ definition
 ├─ jurisdiction
 ├─ source standard
 ├─ version
 └─ interpretation notes
```

This prevents different participants from using materially different meanings for the same Halal/Shariah concept.

## 13. MS 2627 / 2627-2 scientific evidence layer

The compendia make a critical distinction:

**PCR/qPCR is an analytical evidence method, not a Halal certification mechanism.**

The IQ300 decision engine must never implement:

```text
PCR negative → HALAL
```

Instead:

```text
ANALYTICAL RESULT
 + SOURCE PROVENANCE
 + CERTIFICATION EVIDENCE
 + PROCESS EVIDENCE
 + SERTU EVIDENCE WHERE APPLICABLE
 + HUMAN / AUTHORITY ASSESSMENT
 = TRUST DECISION
```

A "not detected" result may be supporting evidence but cannot alone establish species, slaughter status, processing integrity or Halal certification.

## 14. High-risk material classes

The compendia particularly support heightened provenance controls for:

- gelatin;
- collagen;
- animal-derived ingredients;
- capsules;
- enzymes;
- fermentation media;
- animal-origin cosmetic inputs;
- complex pharmaceutical excipients;
- synthetic-route inputs.

### Gelatin model

```text
GELATIN
 ├─ species
 ├─ source
 ├─ slaughter evidence where applicable
 ├─ supplier
 ├─ processor
 ├─ manufacturing route
 ├─ batch
 ├─ recognised Halal evidence
 └─ analytical evidence where relevant
```

Analytical evidence remains one component of the evidence package.

## 15. MS 1900 versus MHMS

MS 1900:2025 is an organisation-level Shariah-based quality-management standard. It should not be collapsed into the Malaysian Halal Management System.

IQ300 should model:

```text
ORGANISATIONAL SHARIAH QMS
        ↓
      MS 1900

PRODUCT HALAL MANAGEMENT
        ↓
MHMS / HAS / IHCS
        ↓
MPPHM / CERTIFICATION PROCESS
```

These layers may interact but remain distinct.

## 16. MS 2691 human-competence layer

Human competence is a first-class trust object.

```text
PERSON
 ├─ role
 ├─ organisation
 ├─ training
 ├─ competence
 ├─ credential
 ├─ issuer
 ├─ scope
 ├─ validity
 └─ revocation status
```

This is particularly relevant to Halal Executives, auditors, consultants, laboratory personnel and smart-glass audit users.

## 17. MPPHM / MHMS certification operating layer

The compendia identify operational themes including:

- IHCS;
- HAS;
- Internal Halal Committee;
- Halal Executive;
- training;
- material control;
- HCP registers;
- sertu SOP;
- traceability;
- recall;
- internal audit;
- management review;
- outsourced activities.

IQ300 shall map these as management-system objects and workflow controls rather than treating the MS standard as the complete certification process.

## 18. International manufacturer onboarding

The compendia describe an international-manufacturing arrangement and related applicant/document/audit requirements. These details must be independently checked against the current JAKIM process before operational use.

IQ300 lifecycle:

```text
CANDIDATE
  ↓
DUE DILIGENCE
  ↓
ELIGIBILITY REVIEW
  ↓
APPLICATION
  ↓
AUDIT
  ↓
FINDINGS / CAR
  ↓
PANEL / AUTHORITY DECISION
  ↓
CERTIFIED / NOT CERTIFIED
```

A Chinese factory is never to be represented as JAKIM-certified merely because it entered the platform.

## 19. IQ300 evidence object

Minimum evidence fields:

- evidence ID;
- evidence type;
- source organisation;
- object/product/batch relationship;
- creator;
- timestamp;
- governing rule/version;
- document/report reference;
- signature/attestation;
- integrity hash;
- validity;
- supersession/revocation state;
- access policy;
- jurisdiction;
- chain-of-custody reference where relevant.

## 20. IQ300 audit event model

Recommended canonical events include:

- `E-AUDIT-OPEN`
- `E-AUDIT-DOC-REVIEW`
- `E-AUDIT-OBSERVATION`
- `E-AUDIT-FINDING`
- `E-CAR-OPEN`
- `E-CAR-CLOSE`
- `E-SAMPLE`
- `E-LAB-RESULT`
- `E-PANEL-DECISION`
- `E-CERT-ISSUE`
- `E-CERT-STATUS`
- `E-SURVEILLANCE`
- `E-RECALL`

## 21. Physical/digital binding

IQ300 binds physical identifiers to digital twins:

```text
PRODUCT
 ↓
BATCH / LOT
 ↓
PALLET
 ↓
CONTAINER
 ↓
SEAL
```

and links these to:

```text
DIGITAL TWIN
 ↓
CERTIFICATION STATE
 ↓
EVIDENCE
 ↓
CUSTODY EVENTS
 ↓
INSPECTIONS
 ↓
TRUST STATE
```

Unexpected physical changes generate investigation events and may degrade trust.

## 22. IQ300 trust-state machine

The binary "Halal / Non-Halal" model is insufficient for an operational trust infrastructure.

```text
PENDING
   ↓
EVIDENCE-COMPLETE
   ↓
ASSESSED
   ├──────────────→ VERIFIED
   │                   ↓
   │             VERIFIED-WITH-EXCEPTION
   │                   ↓
   │                 HOLD
   │                   ↓
   │           CORRECTIVE ACTION
   │                   ↓
   │            RE-VERIFICATION
   │
   └──────────────→ QUARANTINED

Other states:
DISPUTED / EXPIRED / REVOKED / RECALLED
```

Every transition records actor, timestamp, reason, evidence, governing rule/version and authority where applicable.

## 23. Smart-glass audit architecture

```text
PRE-AUDIT
 ↓
SCOPE / STANDARD PROFILE
 ↓
HCP MAP
 ↓
EVIDENCE PLAN
 ↓
SMART-GLASS ON-SITE
 ↓
IDENTIFY ASSET
 ↓
CAPTURE OBSERVATION
 ↓
LINK EVIDENCE
 ↓
AI GAP / ANOMALY ASSIST
 ↓
AUDITOR ASSESSMENT
 ↓
FINDING / CAR
 ↓
AUTHORITY WORKFLOW
```

AI is advisory. The accountable auditor and competent authority retain their respective decision roles.

## 24. Port / customs trust gateway

```text
SHIPMENT ID
 ↓
OFFICER / DEVICE AUTHENTICATION
 ↓
AUTHORIZED TRUST VIEW
 ↓
PHYSICAL-DIGITAL ID CHECK
 ↓
CUSTODY CHECK
 ↓
EXCEPTION CHECK
 ↓
INSPECTION
 ↓
SIGNED EVENT
 ↓
RELEASE / HOLD UNDER AUTHORITY
```

IQ300 provides evidence interoperability; it does not replace statutory customs or border authority.

## 25. China → GCC Shipment 001 control chain

```text
CHINA MANUFACTURER
 ↓
MATERIAL / SOURCE PROVENANCE
 ↓
AUDIT + LAB EVIDENCE
 ↓
CERTIFICATION / AUTHORITY RECORD
 ↓
BATCH
 ↓
PALLET
 ↓
CONTAINER + SEAL
 ↓
CHINA LOGISTICS
 ↓
PORT
 ↓
TRANSIT
 ↓
GCC PORT / CUSTOMS
 ↓
WAREHOUSE
 ↓
DISTRIBUTION
 ↓
RETAIL
 ↓
CONSUMER VERIFICATION
```

Shipment 001 is the primary physical proof-of-execution and acceptance test for the architecture.

## 26. AI assurance modules

Recommended IQ300 modules:

### Evidence Gap Predictor
Predict missing evidence before audit or shipment release.

### Anomaly Engine
Detect deviations from expected process or custody patterns.

### Contradiction Engine
Compare certificates, specifications, batch records, audit evidence, laboratory results and logistics events for inconsistency.

### Trust Fracture Engine
Identify events capable of materially weakening the trust chain.

### Predictive Compliance Engine
Prioritise facilities, materials, processes and suppliers likely to create nonconformity.

### Recall Blast-Radius Engine
Trace affected products, batches, containers, warehouses and retailers after a trust-fracturing event.

AI recommendations must remain explainable, confidence-scored and subject to human escalation.

## 27. Regulatory Knowledge Graph

```text
AUTHORITY
   ↓
STANDARD / FATWA / PROTOCOL / CIRCULAR
   ↓
CLAUSE / REQUIREMENT
   ↓
CONTROL
   ↓
HCP
   ↓
EVIDENCE
   ↓
ASSESSMENT
   ↓
FINDING
   ↓
CORRECTIVE ACTION
   ↓
AUTHORITY DECISION
   ↓
TRUST STATE
```

This graph is the regulatory brain of IQ300.

## 28. Stakeholder authority boundary

| Actor | IQ300 role | Authority boundary |
|---|---|---|
| JAKIM/JAIN/MAIN | Authoritative certification/governance record | Retains statutory/competent authority |
| Qualified Shariah governance | Interpretation/approval where mandated | Does not become an AI function |
| JSM / standards source | Technical standard source | Standard authority remains with source |
| Auditor | Assessment/evidence/finding | Human accountability remains |
| Laboratory | Scientific evidence | Test result is not automatic certification |
| Manufacturer | Production/source evidence | Manufacturer remains responsible for claims |
| Logistics provider | Custody/transport events | Does not certify product |
| Port/customs | Border/inspection events | Statutory powers remain |
| Bank | Financing decision | Independent credit/legal/Shariah decision |
| Takaful operator | Underwriting/claim | Independent policy decision |
| Retailer | Receiving/sale/recall | Retail responsibility remains |
| IQ300 | Connects evidence and trust events | Must not assume authority it has not been granted |

## 29. Clause-to-control master matrix target

The next normative build should contain one record per verified requirement:

| Field | Purpose |
|---|---|
| Standard | Source standard |
| Edition | Version freeze |
| Clause | Exact clause only after authoritative verification |
| Requirement | Normative requirement |
| Applicability | Product/process/jurisdiction scope |
| Control | Operational control |
| HCP | Halal Control Point |
| Risk | Critical/high/medium/low |
| Evidence | Required evidence |
| Test | Analytical method where applicable |
| Responsible actor | Human/system responsibility |
| Authority gate | Competent-authority decision |
| Event | Canonical digital event |
| Physical object | Asset/product/batch/container |
| AI check | Predictive/anomaly rule |
| Failure state | Hold/quarantine/etc. |
| Corrective action | Remediation |
| Re-verification | Closure evidence |
| Trust state | Resulting state |
| Source | Authoritative source |

## 30. Verification register

Before production or external publication, independently verify:

1. Current official edition/status of each applicable Malaysian Standard.
2. Exact clause text and annexes used in the IQ300 rule engine.
3. Current MPPHM edition and applicable scheme.
4. Current MHMS/HAS/IHCS requirements.
5. Current Malaysian meat/poultry protocol and applicable stunning/slaughter parameters.
6. Current JAKIM circulars and relevant fatwa/authority instruments.
7. Current status and scope of laboratories and analytical methods.
8. Current international-manufacturer application requirements.
9. Destination-country/GCC requirements for each Shipment 001 SKU.
10. Data-protection, cybersecurity, cross-border data and evidence-retention requirements.

## 31. Architectural conclusion

The two compendia support a transformation from a conventional Halal certification database into a governed digital-trust infrastructure:

```text
REGULATORY KNOWLEDGE
        +
EVIDENCE FABRIC
        +
DIGITAL AUDIT TWIN
        +
PHYSICAL / DIGITAL BINDING
        +
GLOBAL TRUST GRAPH
        +
AUTHORITY DECISION LAYER
        =
GLOBAL HALAL DIGITAL TRUST INFRASTRUCTURE
```

The strategic proposition is therefore not "put Halal certificates on blockchain". The proposition is to create a **versioned, evidence-linked, authority-aware trust fabric** capable of carrying Halal/Tayyib assurance from source material through production, logistics, border, warehousing and retail.

## 32. Source integrity statement

This document is derived from the two supplied JAKIM/Malaysian Halal standards compendia and the architecture analysis performed from those materials. Where the compendia themselves identify the need for authoritative verification, this document preserves that status rather than manufacturing certainty.

**IQ300 doctrine: source provenance first; authority boundaries explicit; evidence versioned; AI advisory; decisions accountable; physical and digital trust continuously linked.**
