# China Food Safety Innovation Center / Laboratory — Proposed AHTE Role

> **UNEXECUTED / PROPOSED INTEGRATION.** The repository does not currently hold the exact legal laboratory identity, current accreditation certificate/schedule, method scope, JAKIM approval/recognition instrument, executed contract, or production API agreement.

The broader National Food Safety (Hengqin) Innovation Project has an official historical government-backed basis: China's Ministry of Science and Technology reported in 2014 that the project was jointly established by the Ministry of Science and Technology, Guangdong Province and Zhuhai and included a national food-safety science and technology innovation centre and a third-party inspection/testing centre. This does **not** by itself identify the exact testing laboratory or establish JAKIM recognition.

**Status code:** `PROPOSED-INTEGRATION / UNEXECUTED-ROLE`

**Do not imply:**
- Chinese government sponsorship of the exact laboratory unless the legal/institutional evidence is attached;
- CNAS accreditation without the current certificate and schedule;
- JAKIM recognition/approval of the exact laboratory without a written JAKIM instrument;
- direct production connectivity to JAKIM without an official interface specification and executed integration authorisation;
- that a laboratory result creates Halal certification.

## Intended role

`China-side laboratory + traceability evidence producer → AHTE evidence graph → HITM / authority workflow → JAKIM authority gate where formally authorised`

The laboratory is intended to test raw materials, ingredients, products and other defined matrices using the applicable validated methods within its authorised scope and transmit signed evidence to AHTE with cryptographic integrity metadata.

## Required evidence gates

- Exact legal entity and laboratory facility identity.
- Current accreditation status and full schedule/scope for each proposed test.
- Method validation/verification and competence evidence.
- Sampling and chain-of-custody controls.
- Authorised analyst/signatory roles.
- JAKIM audit/pre-assessment and any resulting recognition/approval instrument.
- Data-transfer/legal basis and retention requirements.
- AHTE API specification and authentication profile.
- JAKIM interface specification, if direct connectivity is authorised.
- Report correction, withdrawal and re-test protocol.
- Production connectivity and end-to-end verification test.

## Cryptographic evidence rule

`Raw report → canonical serialisation → SHA-256 digest → signed evidence manifest → append-only/tamper-evident record → AHTE evidence object`

A hash proves content integrity; it does not by itself make a storage system immutable. Corrections create new versions and signed supersession/withdrawal events.

## Authority boundary

Does not create Halal certification. **NOT DETECTED ≠ HALAL.**

JAKIM/MAIN/JAIN remain the competent Malaysian Halal decision authorities within their applicable jurisdiction and mandate. AHTE records and verifies evidence; it does not convert laboratory evidence into a certificate.

## Integration profile

See [`AHTE_JAKIM_INTEGRATION_PROFILE_2026-09-26.md`](./AHTE_JAKIM_INTEGRATION_PROFILE_2026-09-26.md) for the complete laboratory, cryptographic, chain-of-custody, HITM, API and authority-gate architecture.

## Contractual basis

`[OPEN GATE: CONTRACTUAL BASIS — owner: Project — blocking: Evidence]`

`[SOURCE-LOCKED: JAKIM production API endpoint/authentication/schema — required: official JAKIM interface specification or executed integration agreement]`

`[SOURCE-LOCKED: JAKIM recognition/approval status of exact Chinese laboratory — required: JAKIM written decision/instrument]`
