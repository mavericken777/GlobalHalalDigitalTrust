# China Laboratory Integration — Direct JAKIM API Alignment Addendum

## Metadata

- Control date: 2026-09-30
- Classification: post-freeze architecture alignment
- Companion: `AHTE_JAKIM_INTEGRATION_PROFILE_2026-09-26.md`
- Governing topology: `../../00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md`
- Authority effect: none

[PROPOSAL: aligns laboratory target topology — path point: Evidence → Authority Gate]

## 1. Alignment rule

The project target topology is:

```text
CHINA LABORATORY / TRACEABILITY SYSTEM
        ↓
SIGNED / INTEGRITY-PROTECTED LABORATORY EVIDENCE
        ↓
AHTE
        ⇅
DIRECT AUTHORISED JAKIM API
        ⇅
JAKIM AUTHORITY SYSTEM / HUMAN AUTHORITY WORKFLOW
```

The earlier internal proposal route `/v1/authority-adapters/jakim/evidence` remains an **AHTE-internal adapter abstraction only**. It must not be presented as an official JAKIM endpoint or as a separate institutional gateway between AHTE and JAKIM.

## 2. Laboratory event chain

```text
Source lot
→ Sample plan
→ Sample ID
→ Collection
→ Seal
→ Custody transfer(s)
→ Lab receipt / accession
→ Method execution
→ QC
→ Technical review
→ Authorised signatory
→ Report issuance
→ Canonicalisation
→ Content hash
→ Signature / authenticated provenance
→ AHTE evidence object
→ Direct JAKIM API submission/status path where authorised
→ Human authority review
→ Authority status event
→ AHTE trust-state update
```

## 3. Hard rules

- `NOT DETECTED != HALAL`.
- A laboratory result is evidence, not automatic certification.
- A hash proves integrity after creation, not truth or authority.
- AHTE does not invent authority decisions when the direct JAKIM API is unavailable.
- Offline or unavailable authority connectivity must surface an explicit dependency/error state rather than implied success.
- Corrected/withdrawn lab reports create versioned supersession events; prior evidence is not silently overwritten.

## 4. Direct API adapter implementation pattern

Application code should expose a logical `JakimAuthorityAdapter` interface whose production implementation is configured from the actual authorised JAKIM specification.

The internal adapter may provide functions such as:

- submit evidence bundle;
- obtain authority receipt;
- resolve case/application status;
- obtain formal certification/status reference;
- receive/subscribe to authority events where supported;
- validate correlation IDs and idempotency;
- record full audit/provenance metadata.

Do not commit production credentials or unverified external URLs.

## 5. Command Center integration

Laboratory and authority events feed the 24/7 GHSCL + JAKIM-connected Command Center.

Priority alert classes include:

- chain-of-custody break;
- method out of scope;
- QC failure;
- report withdrawal/correction;
- signature/hash mismatch;
- sample/batch mismatch;
- evidence expiry;
- authority hold;
- re-test required;
- recurring laboratory anomaly.

AI/ML may predict likely evidence gaps or inconsistencies and recommend preemptive action. It may not convert the analytical result into a formal Halal decision.

## 6. Closure inputs

Production closure still requires the actual technical/authority inputs for the implemented direct API, including authentication, authorization, endpoint/schema/event model, error semantics, availability/SLA, revocation/credential lifecycle and permitted authority actions.

This addendum changes the **project topology** to direct JAKIM API. It does not fabricate the production interface specification.
