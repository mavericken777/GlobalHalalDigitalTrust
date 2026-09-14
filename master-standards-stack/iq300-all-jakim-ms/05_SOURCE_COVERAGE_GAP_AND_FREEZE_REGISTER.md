# IQ300 SOURCE COVERAGE, GAP AND PRODUCTION-FREEZE REGISTER

## 1. Purpose
This register prevents the digital standards layer from appearing more authoritative than its source corpus. Each standard must carry a source class, edition/status, extraction confidence and freeze requirement.

## 2. Fully numbered / source-complete in the supplied corpus

### MS 2400-1:2019
187 unique numbered requirement objects parsed from the supplied PDF. Nested numbering is preserved. These objects are already stored in `master-standards-stack/iq300-full-matrix/` and form the transportation clause backbone.

### MS 2400-2:2019
201 unique numbered requirement objects parsed from the supplied PDF. These form the warehousing clause backbone.

### MS 2400-3:2019
225 unique numbered requirement objects parsed from the supplied PDF. These form the retailing clause backbone.

**Total fully numbered MS 2400 objects: 613.**

## 3. Source-summary / family-map standards

The supplied maximum-depth compendium provides detailed, source-supported summaries and clause-family maps for:

- MS 1500:2019
- MS 2424:2019
- MS 2634:2019
- MS 2738:2023
- MS 2803:2025
- MS 2393:2023
- MS 2627:2017
- MS 2627-2:2025
- MS 1900:2025
- MS 2691:2021
- MS 2610:2015

These are represented in IQ300 as control families and explicit requirement objects, but the supplied compendium does not contain the complete licensed numbered normative text. IQ300 therefore does not manufacture missing clause numbers.

## 4. Current catalogue-only additions

### MS 2809:2025
JSM MySOL currently lists this as an original Malaysian Standard covering authentication of products using chemometric techniques, including mathematical modelling and statistical analysis of quantitative chemical data and data from chromatography, spectroscopy and spectrometry.

### MS 2810:2025
JSM MySOL currently lists this as an original Malaysian Standard covering identification of pig skin and hair for raw hides/skins/leather products, brushes, loose hair and fur, with an explicit stated exclusion for highly processed leather and hair.

Source checked: https://mysol.jsm.gov.my/search-catalogue?is-advance=1&page=1&sector=204

## 5. Supporting standards

The supplied compendium references MS 1480, MS 1514 and MS 2594 as supporting standards/references where applicable.

## 6. Historical/replaced standards

- MS 1500:2009 -> replaced by MS 1500:2019
- MS 2424:2012 -> replaced by MS 2424:2019
- MS 2200-1:2008 -> replaced by MS 2634:2019
- MS 2200-2:2013 -> replaced by MS 2803:2025
- historical MS 2400 series -> replaced by 2019 revisions
- MS 2565 historical packaging guidance -> do not treat as the current stand-alone control without verifying its current disposition

## 7. Production freeze sequence

```text
Obtain official current JSM text
        |
        v
Record exact edition/revision/confirmation + source hash
        |
        v
Parse every numbered clause and annex item
        |
        v
Create one IQ300 requirement object per applicable subclause/item
        |
        v
Map control / HCP / risk / evidence / audit test
        |
        v
Map MPPHM / MHMS / Protocol / Pekeliling / fatwa dependencies
        |
        v
Shariah + regulatory review
        |
        v
Machine QA + duplicate / missing-field checks
        |
        v
Authority review / approval where required
        |
        v
Version freeze -> production ruleset
```

## 8. Prohibited shortcuts

- Do not infer a Halal certificate from MS compliance alone.
- Do not treat a laboratory 'not detected' result as a certification decision.
- Do not use the withdrawn 2009 slaughter annex as a live numeric ruleset.
- Do not treat a private sertu declaration as equivalent to authority verification where authority verification is required.
- Do not silently reuse food PCR procedures for cosmetic matrices without validating method fitness.
- Do not treat chemical identity as sufficient proof of Halal provenance.
- Do not allow AI to make the authority decision.
