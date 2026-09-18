# 16 - ATTACHED PDF SOURCE INGESTION AND RECONCILIATION - 2026-09-18

## Status
[PROPOSAL: closes attached-source ingestion gap - canonical path point: Standard / Instrument -> Clause / Requirement -> Evidence]

Freeze preserved: `master-standards-stack/verified-2026-09-17/`. This post-freeze ingestion does not modify the frozen package.

## Authority boundary
Malaysian Standards are technical instruments. They do not create Malaysia Halal certification. Certification decisions remain with JAKIM/MAIN/JAIN under the applicable framework. Destination decisions remain with the relevant GCC authorities/importers. Analytical evidence remains purpose-limited.

## Ingested attachments

| File | Pages | SHA-256 first 12 | Source class | Disposition |
|---|---:|---|---|---|
| market_validation.pdf | 48 | 5aeff302514c | secondary synthesis / market model | Ingested as advisory; forecasts/economic claims are not authority facts |
| compliance_manual.pdf | 74 | e27bb840b400 | secondary synthesis / compliance reference | Ingested as secondary; conflicts defer to primary standards/authority |
| MS1500_2019_BM_.pdf | 22 | 01b75d2486a1 | primary supplied standard | Readable; raises MS 1500:2019 source depth for next verified snapshot |
| MS1500_2019_BM.pdf | encrypted | a5573441ebce | primary supplied standard candidate | Password-protected; content not extracted; no equivalence assumed with readable copy |
| MS2400-1_2019.pdf | 42 | 1e5c635cbb43 | primary supplied standard | Readable; corroborates existing MS 2400-1 source-backed mapping |
| MS2400-2_2019.pdf | 43 | d6369596a188 | primary supplied standard | Readable; licensed-copy notice present; source used for internal mapping only |
| MS2400-3_2019_fromDL.pdf | 48 | 8e757fa1821e | primary supplied standard | Readable; corroborates existing MS 2400-3 source-backed mapping |
| MS2610_2015.pdf | 20 | 03c6d9e4ff35 | primary supplied standard | Readable; raises MS 2610:2015 source depth for next verified snapshot |
| MS2683_2017.pdf | 33 | 247b1f69bcc1 | primary supplied standard | Readable; supplemental Kelulut honey product specification, not added to 17-standard halal operating set |
| MS2691_2021.pdf | 17 | 07d3b127358b | primary supplied standard | Readable; raises MS 2691:2021 source depth for next verified snapshot |

## Source-derived findings

### MS 1500:2019 (BM)
Readable source identifies the third revision of `Makanan halal - Keperluan umum`, published by Department of Standards Malaysia in 2021. The contents expose scope and the main requirements architecture. This supports moving MS 1500 from public-structure-only to primary-supplied-source depth in the next controlled snapshot. Exact copyrighted normative wording is not reproduced here.

### MS 2400 series
All three 2019 parts are readable and expose numbered clause structures for transportation, warehousing and retailing. They corroborate the existing 613-object MS 2400 corpus. No replacement of the existing requirement-object library is made solely from this ingestion; any object-level delta requires controlled diff/re-verification.

### MS 2610:2015
Readable source exposes the Muslim-friendly hospitality services standard structure, including Scope, Normative references, Terms and definitions, and General requirements. This upgrades provenance from public structure to primary supplied standard for future promotion.

### MS 2683:2017
Readable source is `Kelulut (Stingless bee) honey - Specification`. Its structure includes Scope, Normative references, Terms and definitions, Requirements, Sampling, and Packaging and labelling. It is a product-quality/specification instrument and is therefore registered as a supplemental technical standard. It does not become an 18th halal operating standard and does not create halal certification authority.

### MS 2691:2021
Readable source is `Halal profession - General requirements`. Its structure includes Scope, Normative references, Terms and definitions, Basic requirements for halal profession, Pre-requisite requirements for each level, Personal attributes, and Code of conduct. This upgrades provenance to primary supplied standard for future promotion.

### compliance_manual.pdf
The manual describes itself as a 2025 reference synthesis and states that the authoritative text in a dispute is the current Malaysian Standard. It describes fourteen active standards and references an alleged `MPPHM 2020 Pindaan 2026`. These claims do not override the current project 17-standard catalogue or primary/authority sources. The 14-standard count remains rejected for current project catalogue purposes. Any exact 2026 MPPHM amendment remains authority-source gated until the official instrument is held/verified.

### market_validation.pdf
The report is a strategic/economic synthesis covering nine verticals, ROI, market sizing, risk and a 24-month roadmap. It explicitly describes forecasts as decision aids. Economic figures, market-size estimates, ROI assumptions and strategic recommendations are therefore advisory model inputs, not certification or destination-authority facts.

## Conflict and non-inference register

1. **14 vs 17 standards** - secondary compliance manual states 14; project current controlled catalogue contains 17. Do not silently merge. Primary/current catalogue governance remains controlling for the project.
2. **MPPHM 2020 Pindaan 2026** - secondary PDFs reference it; exact official amendment text is not established by these attachments alone.
3. **Encrypted MS1500 variant** - content inaccessible. Different hash from readable copy; equivalence is not assumed.
4. **MS2683:2017** - supplemental Kelulut honey specification; not classified as a halal-certification standard merely because it may apply to a halal product.
5. **Licensed standards** - source files are used for internal provenance and mapping. This repository artifact records metadata and derived control architecture, not copyrighted normative text.

[OPEN GATE: SOURCE CONFLICT - secondary-14-vs-controlled-17 - owner: Department of Standards Malaysia/JAKIM as applicable - blocking: Standard / Instrument]
[OPEN GATE: MPPHM-2026-PRIMARY-SOURCE - owner: JAKIM - blocking: Standard / Instrument]
[SOURCE-LOCKED: encrypted MS1500_2019_BM.pdf - required: password/unlocked source if byte-level comparison is required]

## Canonical path impact
`Authority -> Standard / Instrument -> Clause / Requirement -> Applicability -> Control -> HCP/SCCP -> Evidence -> Audit Test -> Finding -> Corrective Action -> Re-verification -> Authority Gate -> Trust State -> Operational Release`

Impact is limited to **Standard / Instrument provenance and Evidence**. No authority decision, certificate, shipment release or destination acceptance is created.

## Promotion recommendation
For the next verified snapshot:
- promote MS 1500:2019, MS 2610:2015 and MS 2691:2021 from public-structure depth to primary-supplied-standard/source-held depth after controlled clause-object reconciliation;
- retain MS 2683:2017 as supplemental technical/product specification;
- preserve the existing 613 MS 2400 objects unless controlled diff identifies a substantive mismatch;
- keep secondary manual/market claims subordinate to primary and authority sources.

## Binary-source handling
The attached PDFs themselves are not reproduced in the public repository by this ingestion. The GitHub connector available in this runtime writes UTF-8 repository files, not binary PDF blobs; additionally, Malaysian Standards contain copyright/licensing restrictions. Integrity references above preserve attachment identity without publishing licensed normative text.
