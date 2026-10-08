# Website implementation alignment — 8 October 2026

**Classification:** post-freeze implementation/status alignment; no standards or authority effect.  
**Canonical implementation repository:** [mavericken777/Amanah](https://github.com/mavericken777/Amanah).  
**Canonical architecture and source controls:** this repository, `mavericken777/GlobalHalalDigitalTrust`.

## Current implementation

Amanah PR [#130](https://github.com/mavericken777/Amanah/pull/130), head commit `91a19decf3ff429dee7cfaec7f6a6a5b24aab764`, contains the latest public-site and journey experience. It replaces an oversized, non-informative shield presentation with an animated, inspectable process journey and names **Global Halal Supply Chain Limited**. It applies a neutral Arial/Helvetica-style sans-serif system and carries the full origin-to-market story through onboarding, standards applicability, evidence, laboratory, smart audit, CAPA/re-verification, authority workflow, production, custody, logistics, ports/customs, GCC receiving, distribution, retail, verification, finance/Takaful context and Command Center monitoring.

The detailed implementation and assets remain in Amanah. This repository records the cross-project architecture and release binding; it does not fork or duplicate the site source.

## Required architecture and claim boundaries

- Authority topology: **AHTE ⇄ Direct JAKIM API ⇄ JAKIM**.
- Default physical corridor: **China → GCC direct**. Malaysia is the governance, assurance and authority-connectivity plane unless a separately scoped movement applies.
- **AI assists; authorised humans and competent authorities decide.** AI, laboratories, QR/NFC, blockchain, sensors and platforms do not certify Halal or make sovereign release decisions.
- **Evidence before trust; trust before operational release.** Integrity proofs demonstrate integrity of recorded bytes, not factual truth.
- Lab workflow is sample → custody → method/QC → result → review/signature → evidence; **NOT_DETECTED ≠ HALAL**.
- shipment workflow is a pilot and remains **NOT-INSTANTIATED** until real transaction evidence exists.
- Public and portal workflows may show complete connector interfaces; development/sandbox state must remain labelled and must not fabricate authority, partner or transaction responses.

## Release state observed 8 October 2026

| Release surface | State | Evidence |
|---|---|---|
| Amanah PR #130 | Open | [PR #130](https://github.com/mavericken777/Amanah/pull/130) |
| GitHub code, build, browser and quality checks | Passed | [Amanah CI run 37798085100](https://github.com/mavericken777/Amanah/actions/runs/37798085100) |
| Vercel preview checks | Rate-limited | Both Vercel contexts report a build-rate limit; previews are not available for this head. |
| GitHub Pages production | Previous release still served | Live root was inspected; it still displays the previous title/brand shell and does not contain the new journey or company name treatment. |
| Merge / deployment | Not completed | PR remains open. No merge SHA or new production deployment exists for this revision. |

The site implementation work can continue independently of these deployment conditions. Describe the current revision as under review until the merge and published-byte verification are complete.
