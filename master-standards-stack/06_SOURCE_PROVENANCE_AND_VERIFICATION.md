# 06 - SOURCE PROVENANCE, VERSION CONTROL AND VERIFICATION

## 1. Source register

| ID | Supplied source | Class | Use |
|---|---|---|---|
| S1 | `ms2400 1.pdf` | primary supplied standard | MS 2400-1 Transportation |
| S2 | `Ms2400 2.pdf` | primary supplied standard | MS 2400-2 Warehousing |
| S3 | `ms2400 3.pdf` | primary supplied standard | MS 2400-3 Retailing |
| S4 | `halal audit.pdf` | training/secondary | audit lifecycle, audit domains, competence |
| S5 | `halal.pdf` | training/secondary | halal fundamentals, awareness, compliance orientation |
| S6 | `JAKIM_MS_Halal_Standards_Compendium_Exhaustive_Reference.pdf` | secondary synthesis | standards catalogue and cross-cutting interpretation |
| S7 | `JAKIM_MS_Halal_Standards_MAXIMUM_DEPTH_Compendium.pdf` | secondary synthesis | expanded clause maps and IQ300 control synthesis |

## 2. Evidence confidence classes

- **A - Authority-confirmed:** checked against the current competent-authority instrument.
- **B - Primary supplied standard:** directly supported by a supplied standard PDF.
- **C - Supplied compendium:** supported by a supplied synthesized compendium.
- **D - Training material:** supported by supplied training slides.
- **E - IQ300 design:** an implementation architecture proposed by the project.

## 3. Version freeze

Every production requirement must store:

`Authority + instrument type + document number + edition + confirmation/status + effective date + superseded relationship + official source reference + acquisition date + hash/integrity reference + reviewer + verification date.`

## 4. Current-source verification gates

Before production hard-freeze, verify:

1. current status and confirmation of every Malaysian Standard from the official JSM/MySOL source;
2. current MPPHM and MHMS requirements;
3. current Malaysian Protocol / JAKIM documents for slaughter and stunning;
4. current sertu procedure and authority-supervision requirements;
5. official MS 2424 Annex B vaccine HCP table before implementing every row;
6. current international manufacturing certification procedure and portal rules;
7. current NPRA legal prerequisites for pharmaceutical/cosmetic applications;
8. current laboratory method edition, matrix applicability, kit/instrument/SOP details;
9. authority certificate status and revocation/suspension information.

## 5. Historic standard handling

Historical or replaced editions remain in the knowledge graph as superseded objects. They are not deleted and are not treated as active controls without explicit applicability.

## 6. Production rule promotion

```mermaid
flowchart TD
    A[Source-derived rule] --> B[Version identified]
    B --> C[Official source check]
    C --> D{Confirmed current?}
    D -- No --> E[RESEARCH / HOLD]
    D -- Yes --> F[Applicability review]
    F --> G[Control mapping]
    G --> H[Production-active]
```

## 7. Critical non-inference rules

- Negative PCR/qPCR does not automatically establish halal status.
- A certificate image does not establish live certificate status unless resolved to the authority credential.
- Product certification does not automatically certify every logistics node.
- Sertu cannot be inferred solely from laboratory evidence.
- Old slaughter/stunning values must not be carried into production simply because they appear in historic material.
- AI confidence is not a legal/certification decision.

## 8. Repository integrity

All source-derived claims should identify the exact source class. Any future correction must supersede an earlier claim rather than silently editing its historical meaning.

## 9. 2026-09-18 attached-source ingestion

[PROPOSAL: closes source-provenance gap - canonical path point: Standard / Instrument -> Evidence]

| ID | Supplied source | SHA12 | Class | Use |
|---|---|---|---|---|
| S8 | `market_validation.pdf` | `5aeff302514c` | secondary synthesis / market | Advisory market/ROI/risk model; not authority evidence |
| S9 | `compliance_manual.pdf` | `e27bb840b400` | secondary synthesis / compliance | Cross-reference only; primary/authority sources prevail |
| S10 | `MS1500_2019_BM_.pdf` | `01b75d2486a1` | primary supplied standard | MS 1500:2019 BM source-depth upgrade candidate |
| S11 | `MS1500_2019_BM.pdf` | `a5573441ebce` | encrypted source candidate | Password-protected; no content equivalence assumed |
| S12 | `MS2400-1_2019.pdf` | `1e5c635cbb43` | primary supplied standard | MS 2400-1 corroboration |
| S13 | `MS2400-2_2019.pdf` | `d6369596a188` | primary supplied standard | MS 2400-2 corroboration; licensed-copy notice present |
| S14 | `MS2400-3_2019_fromDL.pdf` | `8e757fa1821e` | primary supplied standard | MS 2400-3 corroboration |
| S15 | `MS2610_2015.pdf` | `03c6d9e4ff35` | primary supplied standard | MS 2610 source-depth upgrade candidate |
| S16 | `MS2683_2017.pdf` | `247b1f69bcc1` | primary supplied supplemental standard | Kelulut honey specification |
| S17 | `MS2691_2021.pdf` | `07d3b127358b` | primary supplied standard | MS 2691 source-depth upgrade candidate |

The secondary PDFs' 14-standard framing and references to `MPPHM 2020 Pindaan 2026` do not override the controlled 17-standard catalogue or establish exact authority text. Those issues remain explicit conflict/source gates.

[OPEN GATE: SOURCE CONFLICT - secondary-14-vs-controlled-17 - owner: Department of Standards Malaysia/JAKIM as applicable - blocking: Standard / Instrument]

[OPEN GATE: MPPHM-2026-PRIMARY-SOURCE - owner: JAKIM - blocking: Standard / Instrument]
