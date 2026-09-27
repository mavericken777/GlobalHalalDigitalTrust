# Platinum compilations — duplicate and reliability review (28 September 2026)

## Identity and scope

The newly attached `platinum_tier_ms_master(1).pdf` (43 PDF pages, SHA-256 `4f1240560664c9a90caec6359d9715608d972e4d537b1cc7f2519a77d4c95893`) is byte-identical to the earlier `platinum_tier_ms_master.pdf`. The newly attached `platinum_tier_v2_illustrated.pdf` (30 PDF pages, SHA-256 `f3696b038f419c24b94eb0da62e967a345bd2c3c5b70e2ea9c9ceb513f7f3c7e`) is also byte-identical to the prior copy. Both hashes and page counts were already in the [27 September holdings](source-holdings-2026-09-27.json). This batch adds **no new source edition or archive payload**. Both are internally authored secondary compilations, not the published Malaysian Standards or a certification decision.

## Concrete discrepancies

| Location in supplied compilation | Finding | Controlling comparison and disposition |
|---|---|---|
| Master p. 2 contents | Entries point to p. 46 through p. 90, but the PDF has only 43 pages. | The contents list is not a reliable PDF navigation map. Use actual PDF pages and the primary standard. |
| Illustrated p. 3 contents | Entries point to p. 31 through p. 51, but the PDF has only 30 pages. | Navigation is unreliable; its 30 distinct numbered figure labels do appear in the extract, but figure count does not verify normative accuracy. |
| Master pp. 3, 18; illustrated pp. 4, 16 | Characterises MS 2565:2014 as a former cosmetics/consumables hybrid while discussing MS 2738:2023 succession. | The supplied MS 2565:2014 cover and scope (PDF pp. 1, 6) identify **Halal packaging — General guidelines**. The relationship to MS 2738 needs separate authoritative edition-history evidence. Do not infer replacement from these compilations. |
| Illustrated p. 1 | Says `MS 2610:2014`. | The supplied primary `MS2610_2015.pdf` cover is **MS 2610:2015**; illustrated p. 2 and its own catalogue p. 4 also use 2015. Correct the cover reference in future editions of the illustration. |
| Both references: master p. 42; illustrated p. 30 | Source index describes `MS 2610:2014 (Halal packaging)`. | This conflicts with supplied MS 2610:2015 (hospitality) and MS 2565:2014 (packaging). Treat the source-index label as a transposition, not a new standard. |
| Master p. 1; illustrated p. 2 | “Complete verbatim” / “Verbatim Standards” labels. | These are 43- and 30-page summaries of many standards, procedures and protocol documents, not the licensed full texts. Do not feed their prose to a normative clause engine as exact text. |
| Both references: 2026 circular and present-edition assertions | Date-specific regulatory claims appear throughout. | No corresponding official circular or complete official edition set was supplied in this duplicate batch. Mark these claims `SOURCE-LOCKED` pending primary publication and applicability checks. |

The supplied `ms.2393.2010.pdf` is the 2010 Malay edition, so it does not substantiate these compilations’ `MS 2393:2023` account. The supplied `MS2424-2019.pdf` and `MS1480.pdf` are image-only scans; their presence does not establish error-free, exhaustive machine extraction. Refer to the [batch reconciliation](19_SUPPLIED_PDF_RECONCILIATION_2026-09-28.md) for source classifications.

## Archive action

The three broken legacy archives were already removed from the current tree in [the 27 September retirement](../00_EXECUTIVE_COMMAND/artifact-quarantine-2026-09-26.json). A fresh read of the current MS 2400 locator tarball and the remaining historical warehouse gzip succeeded. Neither platinum PDF is a source archive, and there is no additional damaged archive to delete. The licensed primary PDFs and these duplicate compilations have not been copied into the public Git repository.
