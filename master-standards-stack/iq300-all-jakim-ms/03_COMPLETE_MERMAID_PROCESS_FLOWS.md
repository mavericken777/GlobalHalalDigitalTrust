# IQ300 COMPLETE MERMAID PROCESS FLOWS

## A. Master regulatory-to-trust flow
```mermaid
flowchart TD
 A[Shariah / Fatwa / Law] --> B[JSM / NSC 09 Malaysian Standard]
 B --> C[MPPHM / MHMS / Protocol / Pekeliling]
 C --> D{Scope + Applicability Engine}
 D --> E[Requirement Object]
 E --> F[Control Objective]
 F --> G[Control Object]
 G --> H[Halal Control Point / Risk]
 H --> I[Evidence Plan]
 I --> J[Evidence Capture]
 J --> K[Audit Test]
 K --> L{Finding?}
 L -->|No| M[Assessment Complete]
 L -->|Yes| N[Contain / Quarantine]
 N --> O[Corrective Action]
 O --> P[Re-verification]
 P --> K
 M --> Q[Authority Gate]
 Q -->|Pass| R[Authority Decision]
 Q -->|Hold| S[HOLD / DISPUTED / QUARANTINED]
 R --> T[Trust State]
 T --> U[Digital Twin]
 U --> V[Physical / Digital Release]
```

## B. Standard selection router
```mermaid
flowchart TD
 A[Entity / Product / Service / Material] --> B{Primary scope}
 B -->|Food / nutrient supplement| C[MS 1500]
 B -->|Transport| D[MS 2400-1]
 B -->|Warehouse| E[MS 2400-2]
 B -->|Retail| F[MS 2400-3]
 B -->|Pharmaceutical| G[MS 2424]
 B -->|Cosmetics| H[MS 2634]
 B -->|Other consumable good| I[MS 2738]
 B -->|Bone / skin / hair| J[MS 2803]
 B -->|Halal terminology| K[MS 2393]
 B -->|Porcine DNA food| L[MS 2627]
 B -->|Porcine DNA cosmetics| M[MS 2627-2]
 B -->|Organisation Shariah QMS| N[MS 1900]
 B -->|Halal professional role| O[MS 2691]
 B -->|Muslim-friendly hospitality| P[MS 2610]
 B -->|Chemometric authentication| Q[MS 2809]
 B -->|Pig skin / hair identification| R[MS 2810]
 C --> S[Cross-cutting MPPHM / MHMS / authority rules]
 D --> S
 E --> S
 F --> S
 G --> S
 H --> S
 I --> S
 J --> S
 K --> S
 L --> S
 M --> S
 N --> S
 O --> S
 P --> S
 Q --> S
 R --> S
```

## C. MS 2400 chain-of-custody flow
```mermaid
flowchart LR
 A[Origin] --> B[Loading HCP]
 B --> C[Seal / Digital ID]
 C --> D[Transport]
 D --> E[Receiving HCP]
 E --> F[Warehouse]
 F --> G[Dispatch]
 G --> H[Retail]
 H --> I[Consumer / End-use]
 D --> X[Exception / Incident]
 E --> X
 F --> X
 G --> X
 X --> Y[Hold / Quarantine]
 Y --> Z[Investigation / CAR]
 Z --> W[Re-verification]
 W --> F
```

## D. Warehouse state machine
```mermaid
stateDiagram-v2
 [*] --> QUARANTINE
 QUARANTINE --> RELEASED: Evidence + receiving verification pass
 QUARANTINE --> REJECTED: Nonconformity
 RELEASED --> RETURNED: Return received
 RETURNED --> QUARANTINE: Reassessment
 RELEASED --> HOLD: Incident / integrity breach
 HOLD --> RELEASED: Corrective action + authority/verification pass
 HOLD --> REJECTED: Failure / authorised disposition
 REJECTED --> [*]
```

## E. Sertu lifecycle
```mermaid
flowchart TD
 A[Potential mughallazah contact] --> B[E-SERTU-OPEN]
 B --> C[Identify affected equipment / surface / lot]
 C --> D[Define procedure + competent supervision]
 D --> E[Execute prescribed sertu washing]
 E --> F[Record water / soil material / sequence / responsible persons]
 F --> G[E-SERTU-EVIDENCE]
 G --> H[Authority verification]
 H -->|Pass| I[E-SERTU-CLOSE]
 H -->|Fail| E
 I --> J[E-ASSET-RELEASE]
```

## F. Slaughter / stunning boundary
```mermaid
flowchart TD
 A[Halal species + healthy animal] --> B[Applicable current Protocol / fatwa]
 B --> C{Stunning used?}
 C -->|No| D[Halal slaughter by competent Muslim]
 C -->|Yes| E[Reversible stunning only]
 E --> F[Animal alive at slaughter]
 F --> D
 D --> G[Tasmiyah + prescribed slaughter act]
 G --> H[Death confirmation HCP]
 H --> I[Downstream dressing / processing]
 B -.-> J[Do not hard-code withdrawn 2009 MS 1500 numeric table]
```

## G. Pharmaceutical / vaccine HCP dependency graph
```mermaid
flowchart TD
 A[API / starting material] --> B[Excipient / solvent / buffer]
 B --> C[Process aid / enzyme / preservative / stabiliser]
 C --> D[Manufacturing]
 D --> E[QC]
 E --> F[Packaging]
 F --> G[Release]
 V0[Cell / seed accession] --> V1[Media / sera / trypsin / peptone]
 V1 --> V2[Adjuvant / carrier protein]
 V2 --> V3[Culture / harvest]
 V3 --> V4[Purification resins / enzymes / buffers]
 V4 --> V5[Formulation]
 V5 --> V6[Filling lot]
 V6 --> V7[QC / disposition]
 V7 --> V8[Authority / fatwa gate]
```

## H. Laboratory evidence boundary
```mermaid
flowchart LR
 A[Sample] --> B[Identity + chain of custody]
 B --> C[Method version]
 C --> D[Matrix suitability]
 D --> E[Controls valid?]
 E -->|No| F[INVALID / REPEAT]
 E -->|Yes| G[Analytical result]
 G --> H[Method-limited interpretation]
 H --> I[Evidence object]
 I --> J[Human assessment]
 J --> K[Authority decision]
 K --> L[Trust state]
```

## I. Smart-glass audit flow
```mermaid
flowchart TD
 A[Audit scope] --> B[Applicable requirements]
 B --> C[HCP checklist]
 C --> D[Smart-glass identify asset / room / material]
 D --> E[Capture observation]
 E --> F[Link evidence]
 F --> G[AI gap / anomaly support]
 G --> H[Auditor assessment]
 H --> I{Finding?}
 I -->|No| J[Pass / evidence-complete]
 I -->|Yes| K[NCR / CAR]
 K --> L[Correction + re-check]
 L --> H
 J --> M[Authority workflow]
```

## J. Recall blast-radius flow
```mermaid
flowchart TD
 A[Incident / nonconformity] --> B[Affected batch / material / asset]
 B --> C[Forward trace]
 B --> D[Backward trace]
 C --> E[Customers / warehouses / retailers]
 D --> F[Suppliers / inputs / upstream nodes]
 E --> G[Containment]
 F --> G
 G --> H[Authority notification / decision as applicable]
 H --> I[Recall / withdrawal]
 I --> J[Effectiveness verification]
```
