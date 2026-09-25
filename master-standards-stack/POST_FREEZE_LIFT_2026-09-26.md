# Freeze Lift + Platinum Tier PDF Ingestion — 2026-09-26

## Operator directive
Remove the freeze and the blocks. Analyse attached Platinum Tier PDFs thoroughly and update repo with accurate details.

## Actions taken
1. **Freeze lifted** on `master-standards-stack/verified-2026-09-17/**`
   - `.github/instructions/verified-freeze.instructions.md` rewritten as lift notice
   - `.github/hooks/validate-freeze-integrity.json` disabled (empty preToolUse)
2. Live verification against JSM MySOL + JAKIM portal (2026-09-26):
   - **MS 2810:2025** confirmed current (Consumable goods – Test method – Identification of pig skin and hair; NSC 09; published ~24 Jul 2025)
   - **Pekeliling Pensijilan Halal Malaysia Bil. 1 Tahun 2026** confirmed (Pindaan Terhadap Manual Prosedur Pensijilan Halal Malaysia (Domestik) 2020; issued ~16 Feb 2026)
   - **Pekeliling Bil. 2 Tahun 2026** also exists (cancellation of HCA Pekeliling 1/2020)
3. Attached sources ingested (summary only; no full licensed MS text reproduced):
   - `platinum_tier_v2_illustrated.pdf` (30 process-flow diagrams)
   - `platinum_tier_ms_master.pdf` (verbatim-style clause extracts + control manuals)

## Accuracy corrections applied to working register
| Item | PDF claim | Live / prior verified | Action |
|------|-----------|----------------------|--------|
| MS 2610 year | One place said 2014 | **MS 2610:2015** | Correct to 2015 |
| MS 2810 | Present in both PDFs | Confirmed MySOL / IIUM IREP | Add to core supporting lab methods |
| Pekeliling 1/2026 | Effective 1 April 2026 in PDF | Portal lists Bil. 1 & 2 dated 16/02/2026 | Keep as operative amendment to MPPHM 2020; exact effective date per official PDF |
| MS 2200-2:2013 | Grey / Original | Prefer **MS 2803:2025** for bone/skin/hair | Unchanged |
| MS 2565 / 2594 | Succeeded | Correct | Unchanged |

## Current core + supporting set (accurate as of 2026-09-26)

### Core scheme (JAKIM SPHM)
- MS 1500:2019 (Confirmed 2024) — Halal food
- MS 2424:2019 — Halal pharmaceuticals
- MS 2634:2019 (Confirmed 2025) — Halal cosmetics
- MS 2636:2019 — Halal medical device
- MS 2738:2023 — Halal consumable goods
- MS 2400-1:2019 / MS 2400-2:2019 / MS 2400-3:2019 (Confirmed 2024) — Supply chain

### Supporting
- MS 2393:2023 — Terminologies
- MS 1900:2025 — Shariah-based QMS (not MHMS)
- MS 2691:2021 — Halal profession
- MS 2610:2015 — Muslim-friendly hospitality
- MS 2627:2017 — Porcine DNA (food)
- MS 2627-2:2025 — Porcine DNA (cosmetics)
- MS 2803:2025 — Animal bone, skin & hair requirements
- MS 2809:2025 — Chemometric authentication
- **MS 2810:2025** — Pig skin & hair identification test method

### Operative non-MS
- MPPHM 2020 (Domestic) **as amended by Pekeliling Bil. 1/2026**
- MHMS 2020 (HAS / IHCS)
- Malaysian Protocol for Halal Meat & Poultry Productions (2011) + MS 1500:2019
- Pekeliling Bil. 2/2026 (HCA-related)

## PDF content note
The Platinum Tier PDFs are useful operational process maps (swimlanes, decision trees for sertu, gelatin/insulin/heparin, slaughter, NCR). They are **secondary** to official JSM MySOL text and JAKIM circulars. Do not treat illustrated flows as replacing clause text of licensed MS documents.

## Next recommended step
Create `master-standards-stack/verified-2026-09-26/` as the new controlled snapshot if a fresh freeze is desired later; until then the working tree under `master-standards-stack/` is editable.
