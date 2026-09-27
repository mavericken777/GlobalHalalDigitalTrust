# Platinum Tier v2 ZIP — integrity and source triage (28 September 2026)

## What was checked

The user supplied `Platinum_Tier_v2_Complete_Bundle.zip` has SHA-256 `16e1a0a3e64c4a4a3151510c7dfebdb9f6f09c1b8a95a2af3c54053d3955e03e`. Its central directory opens and every member passes ZIP CRC validation. All 69 non-directory paths are unique and relative. The eight PDFs open, all 30 SVGs parse as XML, and all 30 PNGs decode. The [member inventory](source-bundle-holdings-2026-09-28.json) preserves each name, size and hash without placing the source archive or PDF/diagram content in the public repository.

| Category | Actual | Claim in `INDEX.md` | Disposition |
|---|---:|---:|---|
| PDFs | 8 | 8 | Open successfully; secondary compilations, not published MS source editions. |
| SVG diagrams | 30 | 30 | Parse successfully; process content remains unvalidated. |
| PNG diagrams | 30 | 30 | Decode successfully; source claims remain unvalidated. |
| Editable HTML | **0** | **12** | Missing from ZIP. The index's editable-source promise is unfulfilled. |
| `INDEX.md` | 1 | Omitted from its own count | Navigation and claims require correction. |
| All non-directory files | **69** | **80** | Counts disagree because 12 claimed HTML files are absent while index itself is present. |

The bundle's Platinum master and illustrated PDFs have the same extractable text on all 43 and 30 corresponding pages as the previously reviewed standalone copies, although the binary hashes differ. The earlier [compilation review](20_PLATINUM_COMPILATION_REVIEW_2026-09-28.md) therefore applies. The six other PDFs are `compliance_manual` (74 pages), `market_validation` (48), `ultra_deep_standards` (56), `fatwa_clause_matrix` (23), `primer_probes_ms2627_2` (19) and `sccp_matrices` (36). These titles and cover claims do not confer JAKIM/JSM authorship, official status, laboratory validation or a market study's independently verified data.

## Specific content conflicts

- `INDEX.md`, under “17 Malaysian Standards,” labels **MS 2610:2014 as Halal Packaging**. The supplied primary edition is **MS 2610:2015 Muslim friendly hospitality services**; the supplied packaging source is **MS 2565:2014**.
- The same index labels **MS 2393:2023 as Halal-related services**. Its catalogue description in this repository is Islamic and halal terminology. The supplied 2010 terminology PDF does not verify the 2023 edition's text.
- `deep_dive_expansion/sccp_matrices.pdf`, PDF p. 2 contents, labels **MS 2738:2023 as Halal Medical Devices**. The catalogue identifies MS 2738:2023 as consumable goods and MS 2636:2019 as medical devices. Do not rely on that matrix's sector routing without line-by-line review.
- `deep_dive_expansion/fatwa_clause_matrix.pdf` and `sccp_matrices.pdf` also repeat `MS 2610:2014` in body references. This is an edition error, not a distinct uploaded primary standard.
- `ultra_deep/ultra_deep_standards.pdf` and the master claim complete/verbatim clause coverage. The bundle contains derived summaries, and no full set of authorized primary editions. The qPCR primer/probe PDF claims validated sequences and thresholds; no laboratory validation package or cited licensed annex was independently authenticated by this archive. Treat these as proposals pending specialist verification.
- The 2025 market report has business assumptions and risk analysis; its ROI and market estimates are not bankable evidence solely because they appear in the ZIP.
- `MS2627_ct_cutoff_decision_tree_reextraction_loops.svg` uses fixed Ct bands (including `Ct < 32`, `Ct 32-40` and `Ct ≥ 40`) and labels an undetected branch `PASS — NEGATIVE`. Those bands are not established as universal validated cutoffs by this bundle. A negative analytical result cannot independently establish halal status (`NOT DETECTED ≠ HALAL`). Block this diagram from an automated release rule until a laboratory validates its assay-specific interpretation and the authority/evidence gate is separate.
- `MS2400_1_transportation_four_swimlanes.svg` implies a pre-wash certificate plus negative PCR swab and a generic seven-wash sertu path. That is a proposed workflow, not evidence that PCR testing is a required or sufficient MS 2400 transport control. Review the applicable contamination case and authorized sertu procedure before deploying it.

## Source handling and archive disposition

The ZIP is **intact**, so it must not be deleted as a damaged archive. The three actually damaged legacy archives were already removed from the current Git tree and remain traceable in the [retirement ledger](../00_EXECUTIVE_COMMAND/artifact-quarantine-2026-09-26.json). The remaining MS 2400 locator tarball and historical warehouse gzip still pass integrity checks. The bundle's licensed-source-derived prose and figures are withheld from this public repository until redistribution rights and normative accuracy are reviewed. The useful update is its member-level provenance, the discrepancies above and explicit source locks; no operational control, lab assay or certification gate is closed by this ZIP.
