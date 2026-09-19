# AHTE HD Visual Atlas

Control date: 2026-09-20  
Classification: post-freeze visual execution layer  
Authority effect: none  
Freeze boundary: does not rewrite `verified-2026-09-17/`

> AHTE is an evidence and decision-support platform. Official Halal certification and destination regulatory decisions remain with the competent authorities.

Existing vector set (already in this folder): `00` master atlas + `01`–`17` standard process-flow SVGs generated from `STANDARDS_FLOW_SPEC.json`.

This file adds the **end-to-end mermaid graphs** that the SVG generator does not yet cover: canonical path, standard router, custody, sertu, laboratory boundary, HITM plane, China→GCC pilot corridor, exception states, recall blast-radius, and smart-glass audit.

---

## 1. Canonical 14-node path

```mermaid
flowchart LR
    A[Authority] --> B[Standard / Instrument]
    B --> C[Clause / Requirement]
    C --> D[Applicability]
    D --> E[Control]
    E --> F[HCP / SCCP]
    F --> G[Evidence]
    G --> H[Audit Test]
    H --> I[Finding]
    I --> J[Corrective Action]
    J --> K[Re-verification]
    K --> L[Authority Gate]
    L --> M[Trust State]
    M --> N[Operational Release]
```

Trust State is internal. It is not an official certificate.

---

## 2. Master regulatory-to-trust flow

```mermaid
flowchart TD
    A[Shariah / Fatwa / Law] --> B[JSM / NSC 09 Malaysian Standard]
    B --> C[MPPHM / MHMS / Protocol / Pekeliling]
    C --> D{Scope + Applicability}
    D --> E[Requirement object]
    E --> F[Control object]
    F --> G[HCP / risk]
    G --> H[Evidence plan]
    H --> I[Evidence capture]
    I --> J[Audit test]
    J --> K{Finding?}
    K -->|No| L[Assessment complete]
    K -->|Yes| M[Contain / quarantine]
    M --> N[Corrective action]
    N --> O[Re-verification]
    O --> J
    L --> P[Authority gate]
    P -->|Pass| Q[Authority decision]
    P -->|Hold| R[HOLD / DISPUTED / QUARANTINED]
    Q --> S[Trust state]
    S --> T[Digital twin]
    T --> U[Physical / digital release]
```

---

## 3. 17-standard selection router

```mermaid
flowchart TD
    A[Entity / product / service / material] --> B{Primary scope}
    B -->|Food| C[MS 1500:2019]
    B -->|Transport| D[MS 2400-1:2019]
    B -->|Warehouse| E[MS 2400-2:2019]
    B -->|Retail| F[MS 2400-3:2019]
    B -->|Pharma| G[MS 2424:2019]
    B -->|Cosmetics| H[MS 2634:2019]
    B -->|Medical device| I[MS 2636:2019]
    B -->|Consumable goods| J[MS 2738:2023]
    B -->|Bone / skin / hair| K[MS 2803:2025]
    B -->|Terminology| L[MS 2393:2023]
    B -->|Porcine DNA food| M[MS 2627:2017]
    B -->|Porcine DNA cosmetics| N[MS 2627-2:2025]
    B -->|Shariah QMS| O[MS 1900:2025]
    B -->|Profession competency| P[MS 2691:2021]
    B -->|Hospitality| Q[MS 2610:2015]
    B -->|Chemometric auth| R[MS 2809:2025]
    B -->|Pig skin / hair ID| S[MS 2810:2025]
    C --> Z[Cross-cutting MPPHM / MHMS / authority rules]
    D --> Z
    E --> Z
    F --> Z
    G --> Z
    H --> Z
    I --> Z
    J --> Z
    K --> Z
    L --> Z
    M --> Z
    N --> Z
    O --> Z
    P --> Z
    Q --> Z
    R --> Z
    S --> Z
```

---

## 4. Evidence Fabric

```mermaid
flowchart TD
    REQ[Requirement] --> CTRL[Control]
    CTRL --> HCP[HCP / SCCP]
    HCP --> OBJ[Physical object]
    OBJ --> EV[Evidence]
    EV --> ASS[Human assessment]
    ASS --> DEC[Authority decision where applicable]
    DEC --> TS[Trust state]
```

---

## 5. IQ300 assurance control plane (proposal)

```mermaid
flowchart LR
    EV[Evidence] --> AS[Assessment]
    AS --> HITM[HITM case]
    HITM --> PEP[HITM PEP / OPA default-deny]
    PEP --> AD[Authority decision D5/D6]
    AD --> TS[Trust state]
    AI[AI advisory only] -.-> AS
    AI -.-> HITM
    AI -.-x AD
```

High AI confidence cannot skip D5/D6 authority gates. AI does not issue certificates.

---

## 6. MS 2400 chain of custody

```mermaid
flowchart LR
    A[Origin] --> B[Loading HCP]
    B --> C[Seal / digital ID]
    C --> D[Transport]
    D --> E[Receiving HCP]
    E --> F[Warehouse]
    F --> G[Dispatch]
    G --> H[Retail]
    H --> I[Consumer / end-use]
    D --> X[Exception]
    E --> X
    F --> X
    G --> X
    X --> Y[Hold / quarantine]
    Y --> Z[Investigation / CAR]
    Z --> W[Re-verification]
```

---

## 7. Sertu lifecycle

```mermaid
flowchart TD
    A[Potential mughallazah contact] --> B[E-SERTU-OPEN]
    B --> C[Identify affected asset / surface / lot]
    C --> D[Procedure + competent supervision]
    D --> E[Execute prescribed sertu]
    E --> F[Record sequence / materials / persons]
    F --> G[E-SERTU-EVIDENCE]
    G --> H[Authority verification]
    H -->|Pass| I[E-SERTU-CLOSE]
    H -->|Fail| E
    I --> J[E-ASSET-RELEASE]
```

Generic sanitation does not substitute for sertu.

---

## 8. Laboratory evidence boundary

```mermaid
flowchart LR
    A[Sample] --> B[Identity + chain of custody]
    B --> C[Method version]
    C --> D[Matrix suitability]
    D --> E{Controls valid?}
    E -->|No| F[INVALID / REPEAT]
    E -->|Yes| G[Analytical result]
    G --> H[Method-limited interpretation]
    H --> I[Evidence object]
    I --> J[Human assessment]
    J --> K[Authority decision]
    K --> L[Trust state]
```

A `not detected` PCR/qPCR result does not by itself establish Halal status.

---

## 9. Smart-glass audit

```mermaid
flowchart TD
    A[Load audit scope] --> B[Load requirement set]
    B --> C[Load HCP / control map]
    C --> D[On-site auditor]
    D --> E[Identify room / asset / batch]
    E --> F[Capture observation]
    F --> G[Attach evidence]
    G --> H[AI gap / anomaly recommendation]
    H --> I[Auditor confirms or rejects]
    I --> J[Finding / NCR / CAR]
    J --> K[Authority workflow]
```

---

## 10. Port / customs gateway

```mermaid
flowchart LR
    SH[Shipment ID] --> AUTH[Officer / device authentication]
    AUTH --> VIEW[Authorized trust view]
    VIEW --> PHY[Physical identity / seal check]
    PHY --> CUST[Custody status]
    CUST --> EX[Exceptions]
    EX --> INSP[Inspection / evidence]
    INSP --> EVT[Signed event]
    EVT --> DEC[Release / hold under competent authority]
```

---

## 11. Shipment 001 corridor — PILOT architecture

`[PILOT: Shipment 001 — corridor model]`

Not instantiated until transaction-native evidence exists.

```mermaid
flowchart LR
    A[Legal entity] --> B[Factory]
    B --> C[SKU / formula]
    C --> D[Current certificate + issuer / scope / validity]
    D --> E[Destination recognition / rules]
    E --> F[Label / import registration]
    F --> G[Importer / buyer]
    G --> H[Commercial terms / PO]
    H --> I[Pilot batch]
    I --> J[Logistics qualification]
    J --> K[Container / seal]
    K --> L[Custody / telemetry]
    L --> M[Border release]
    M --> N[Receiving verification]
```

Five-segment physical model:

```mermaid
flowchart LR
    S1[1 Origin factory] --> S2[2 Inland logistics]
    S2 --> S3[3 Export port]
    S3 --> S4[4 Maritime transit]
    S4 --> S5[5 GCC port / warehouse]
```

---

## 12. Exception / trust state machine

```mermaid
stateDiagram-v2
    [*] --> PENDING
    PENDING --> EVIDENCE_COMPLETE
    EVIDENCE_COMPLETE --> ASSESSED
    ASSESSED --> VERIFIED
    ASSESSED --> HOLD
    ASSESSED --> DISPUTED
    HOLD --> CORRECTIVE_ACTION
    CORRECTIVE_ACTION --> RE_VERIFICATION
    RE_VERIFICATION --> VERIFIED
    RE_VERIFICATION --> HOLD
    VERIFIED --> EXPIRED
    VERIFIED --> REVOKED
    VERIFIED --> RECALLED
```

---

## 13. Recall blast-radius

```mermaid
flowchart TD
    A[Incident / nonconformity] --> B[Affected batch / material / asset]
    B --> C[Forward trace]
    B --> D[Backward trace]
    C --> E[Customers / warehouses / retailers]
    D --> F[Suppliers / inputs]
    E --> G[Containment]
    F --> G
    G --> H[Authority notification as applicable]
    H --> I[Recall / withdrawal]
    I --> J[Effectiveness verification]
```

---

## 14. Warehouse states

```mermaid
stateDiagram-v2
    [*] --> QUARANTINE
    QUARANTINE --> RELEASED: Evidence + receiving verification pass
    QUARANTINE --> REJECTED: Nonconformity
    RELEASED --> RETURNED: Return received
    RETURNED --> QUARANTINE: Reassessment
    RELEASED --> HOLD: Incident / integrity breach
    HOLD --> RELEASED: CAR + verification pass
    HOLD --> REJECTED: Failure / authorised disposition
    REJECTED --> [*]
```

---

## Provenance

| Item | Source |
|---|---|
| Canonical path | README.md / IQ300 doctrine |
| 17-standard set | verified-2026-09-17 catalogue |
| Mermaid A–J | iq300-all-jakim-ms/03_COMPLETE_MERMAID_PROCESS_FLOWS.md |
| Evidence / twin / port | 05_IQ300_EVIDENCE_TRUST_PROCESS_FLOWS.md |
| HITM plane | IQ300_ASSURANCE_CONTROL_PLANE_SPEC_v0.1.md — proposal only |
| Shipment 001 | README China → GCC pilot — gated |

## Remaining gates

- Licensed MS normative wording: SOURCE-LOCKED (not drawn as clauses).
- MPPHM 2020 Pindaan 2026 primary text: OPEN GATE.
- Shipment 001 events / contracts / POs: TRANSACTION GATE.
- Raster HD frames generated in session remain local unless separately uploaded.
