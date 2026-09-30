# China Laboratory + Traceability System — AHTE Integration Profile

## Metadata

| Field | Value |
|---|---|
| Artifact | `AHTE_CHINA_LAB_TRACEABILITY_INTEGRATION_PROFILE_2026-09-30.md` |
| Revision | v1.0.0 |
| Control date | 2026-09-30 |
| Classification | Post-freeze consolidated target integration profile |
| Supersedes | `AHTE_JAKIM_INTEGRATION_PROFILE_2026-09-26.md`; `DIRECT_JAKIM_API_ALIGNMENT_ADDENDUM_2026-09-30.md` |
| Governing topology | `../../00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md` |
| Freeze impact | None |

[PROPOSAL: consolidates China laboratory + traceability integration — path point: Evidence → Audit Test → Authority Gate → Trust State]

## 1. Purpose

Integrate the China-side food-safety traceability / anti-counterfeit platform and the participating laboratory evidence workflow into AHTE as a sovereign China-origin physical-identity, traceability and scientific-evidence plane.

The complete target relationship is:

```text
RAW-MATERIAL / PRODUCT / LOT / BATCH
        ↓
CHINA PHYSICAL IDENTITY + TRACEABILITY SYSTEM
        ├── enterprise / product identity
        ├── one-item-one-code
        ├── microdot / QR / VOID physical token
        ├── batch binding
        ├── unit → box → carton → pallet aggregation
        ├── consumer / channel verification
        ├── anti-diversion / abnormal-scan events
        └── scan / channel analytics
        ↓
CONTROLLED SAMPLE / LABORATORY WORKFLOW
        ↓
SIGNED / INTEGRITY-PROTECTED SCIENTIFIC EVIDENCE
        ↓
AHTE
        ⇅
DIRECT AUTHORISED JAKIM API
        ⇅
JAKIM AUTHORITY SYSTEM / AUTHORISED HUMAN WORKFLOW
        ↓
AUTHORITY STATUS EVENT
        ↓
AHTE TRUST-STATE PROPAGATION
        ↓
PRODUCT → BATCH → SHIPMENT → GCC
```

The traceability platform and laboratory are evidence/identity producers. AHTE is the federated evidence, standards, trust and orchestration layer. Neither a traceability result nor a laboratory result independently creates Halal certification.

## 2. Non-negotiable authority and identity separation

The following are separate objects and must not be collapsed:

1. `TraceabilitySystemIdentity`
2. `PhysicalIdentifier`
3. `OrganizationIdentity`
4. `ProductIdentity`
5. `BatchIdentity`
6. `LaboratoryIdentity`
7. `LaboratoryAccreditation`
8. `MethodScope`
9. `Sample`
10. `LaboratoryResult`
11. `EvidenceObject`
12. `HalalCertificationDecision`
13. `AuthorityDecision`
14. `TrustState`
15. `OperationalRelease`

**Hard rule:** `NOT_DETECTED ≠ HALAL`.

A QR code, microdot, VOID label, hash, blockchain/DLT anchor, AI assessment, sensor record or laboratory result is evidence/integrity infrastructure only. It cannot substitute for a competent-authority Halal decision.

The exact laboratory legal entity, site, current accreditation certificate/schedule, method/matrix scope, contractual role and authority acceptance remain controlled evidence objects and must not be inferred from similar names or legacy placeholders.

## 3. China traceability / anti-counterfeit integration

The furnished China platform provides a complementary physical/digital identity and channel-observation layer. AHTE shall support at minimum:

### 3.1 Enterprise and product master data

- legal/operating organisation reference;
- brand/product/SKU reference;
- product specification and packaging structure;
- batch/lot relationship;
- source-system object identifier;
- approved cross-system AHTE ObjectID mapping.

Existing master data should be synchronized/augmented rather than re-keyed unnecessarily. Halal-specific data such as formula/BOM, ingredient/raw-material provenance, suppliers, standards applicability, HCP/SCCP, audit evidence and authority state remain AHTE-linked objects.

### 3.2 One-item-one-code / physical trust token

Physical identity may combine:

`microdot + QR + VOID/tamper-evident construction + unique source code`

AHTE binds the source-system code to the digital object graph:

`PhysicalIdentifierID → ProductID → BatchID/LotID → PackagingParentID → ShipmentID → EvidenceRefs → CurrentState`

The physical code is an identifier and authenticity signal. It is not the Halal decision.

### 3.3 Packaging aggregation

The furnished platform's physical hierarchy shall be preserved and extended:

```text
UNIT
→ BOX
→ CARTON
→ PALLET
→ LOGISTIC UNIT
→ CONTAINER
→ SHIPMENT
→ GCC CONSIGNMENT / DESTINATION INVENTORY
```

Aggregation/de-aggregation/repack/rework events must be explicit events. A change to an existing relationship must create a correction/supersession event; history is not silently overwritten.

### 3.4 Consumer/channel verification

Source verification events may include product, origin, batch and quality-report presentation plus scan timestamp/geography and abnormal conditions. AHTE consumer/importer views expose only authorised fields.

A displayed PDF/image labelled a quality report is not automatically a verified `LabResult`. AHTE promotes it to scientific evidence only after laboratory identity, sample, method, report provenance, signature/hash and applicable scope are validated.

### 3.5 Anti-diversion / scan analytics

The source platform's scan geography, assigned market/dealer region, black/white-list, repeated-code and abnormal-scan signals should enter AHTE as evidence/risk events. They may support AI/ML detection of:

- possible code cloning;
- impossible scan geography;
- destination mismatch;
- channel leakage/diversion;
- suspicious scan velocity;
- batch-level anomaly clustering;
- recall exposure;
- China→GCC route inconsistency.

These signals feed predictive analytics and the 24/7 Command Center; they do not autonomously change certification status.

## 4. Laboratory state machine

The controlled target state machine is:

`CREATED → SAMPLE_REGISTERED → IN_TRANSIT_TO_LAB → RECEIVED → ACCESSIONED → TESTING → RESULT_DRAFT → TECHNICAL_REVIEW → REPORT_SIGNED → AHTE_RECEIVED → HASH_VERIFIED → EVIDENCE_ACCEPTED → AUTHORITY_REVIEW → AUTHORITY_DECISION → TRUST_STATE_UPDATED`

Exception states include:

`REJECTED_SAMPLE`, `CHAIN_OF_CUSTODY_BREAK`, `METHOD_OUT_OF_SCOPE`, `QC_FAILURE`, `RESULT_CORRECTION`, `REPORT_WITHDRAWN`, `SIGNATURE_INVALID`, `HASH_MISMATCH`, `OBJECT_BINDING_MISMATCH`, `DUPLICATE_OR_REPLAY`, `AUTHORITY_HOLD`, `RE-TEST_REQUIRED`, `RECALL`.

## 5. Complete sample chain of custody

A signed report alone is insufficient. The required chain is:

`Sampling authorisation → sample plan → sample ID → physical sample label → collection event → collector identity → time/location → seal → custody transfer(s) → transport condition → laboratory receipt → condition check → accession ID → aliquot/sub-sample relationship → method execution → QC/controls → technical review → authorised signatory → report issuance → AHTE evidence receipt`.

A broken/unexplained chain creates `CHAIN_OF_CUSTODY_BREAK` and routes the applicable object to HOLD pending authorised review.

## 6. Method governance

Each analytical method must have machine-readable governance containing, where applicable:

- method ID;
- method version/date;
- analyte/target;
- matrix;
- equipment/instrument requirements;
- calibration/qualification requirements;
- reference materials/positive/negative/internal controls;
- validation/verification status;
- detection/quantification characteristics;
- authorised laboratory scope;
- competent analyst/reviewer/signatory role;
- applicable standard/instrument reference;
- product/material applicability;
- destination-market acceptance where relevant.

A generic phrase such as `tested according to JAKIM Halal Standard` is not an adequate substitute for exact method and scope identity.

## 7. Laboratory evidence envelope

The production-target object model shall include at least:

```json
{
  "labEventId": "LAB-...",
  "sampleId": "SMP-...",
  "objectRefs": ["MATERIAL-...", "BATCH-...", "SKU-..."],
  "laboratory": {
    "legalEntityId": "...",
    "facilityId": "...",
    "accreditationBody": "...",
    "accreditationId": "...",
    "accreditationValidFrom": "...",
    "accreditationValidUntil": "...",
    "scopeReference": "..."
  },
  "method": {
    "methodId": "...",
    "methodVersion": "...",
    "methodSource": "...",
    "scopeStatus": "IN_SCOPE|OUT_OF_SCOPE|PENDING"
  },
  "sample": {
    "matrix": "...",
    "collectedAt": "...",
    "receivedAt": "...",
    "condition": "...",
    "custodyRefs": ["..."],
    "sealId": "..."
  },
  "result": {
    "status": "DETECTED|NOT_DETECTED|QUANTIFIED|INCONCLUSIVE|INVALID",
    "value": null,
    "unit": "...",
    "qualifier": "...",
    "uncertainty": "...",
    "interpretation": "..."
  },
  "report": {
    "reportId": "...",
    "reportVersion": "...",
    "issuedAt": "...",
    "reportHash": "sha256:..."
  },
  "integrity": {
    "canonicalisation": "AHTE-CANONICAL-JSON-V1",
    "contentHash": "sha256:...",
    "signatureAlgorithm": "...",
    "signature": "...",
    "keyId": "...",
    "signedAt": "...",
    "previousEvidenceHash": "sha256:..."
  },
  "jurisdiction": "CN",
  "purpose": "HALAL_ANALYTICAL_EVIDENCE",
  "status": "SIGNED"
}
```

The canonical executable proposal contract is held under `../../master-standards-stack/CHINA_EXECUTION_PACK/api/china-food-security-lab-openapi-extension.yaml`.

## 8. Evidence integrity / corrections

Use:

`Raw report → canonical representation → SHA-256/content digest → signed evidence manifest → append-only/tamper-evident event record → retention-controlled source reference → optional external/DLT anchor`.

A hash proves content integrity after creation; it does not make the source truthful or make certification.

Correction/withdrawal pattern:

`Original report → correction/withdrawal event → reason → authorised actor → new version → new signature/hash → supersession link`.

The prior record remains verifiable and is not silently deleted/overwritten.

## 9. Direct JAKIM API topology

For this project, the public and system topology is:

```text
CHINA LAB / TRACEABILITY EVIDENCE
        ↓
AHTE
        ⇅
DIRECT JAKIM API
        ⇅
JAKIM
        ↓
PHC + JAKIM AUTHORISED HUMAN WORKFLOW
        ↓
FORMAL STATUS / DECISION EVENT
        ⇅
DIRECT JAKIM API
        ⇅
AHTE
```

Do not insert NurAI or an unnecessary external middleware institution in this topology.

Internal code may use a logical `JakimAuthorityAdapter` interface to isolate the actual production protocol, but that interface is an implementation abstraction — not a separate authority gateway or an official external endpoint.

Target functions may include:

- submit authorised evidence bundle;
- obtain authority receipt/correlation reference;
- resolve application/case/status;
- receive formal certification/status reference;
- receive/subscribe to authority events where the official interface supports it;
- enforce idempotency/replay protection;
- preserve provenance/audit metadata.

`[SOURCE-LOCKED: JAKIM production endpoint/authentication/schema/event contract/permissions — required: authorised JAKIM interface specification or executed integration agreement]`

## 10. Project human-decision workflow

For this project's operating architecture, formal approval/disapproval remains in the authorised **PHC + JAKIM human workflow**, including Mufti/scholars/authorised halal officers/decision-makers as applicable to the implemented authority process.

AI/AHTE may classify, correlate, detect gaps, surface contradictions, prioritise risk and route evidence. They do not issue the formal certification decision.

D5/D6 remain human/authority-controlled. A D4 hold cannot be automatically released where the governing policy requires human release.

## 11. AI/ML + preemptive assurance

AI/ML may analyse traceability and laboratory evidence to detect/predict:

- missing method/scope metadata;
- sample/batch mismatch;
- chain-of-custody anomaly;
- recurrent QC failures;
- unusual result distributions;
- increasing inconclusive/retest rate;
- signature/hash mismatch;
- duplicate/replay evidence;
- abnormal scan/geography behaviour;
- supplier/material-specific risk trend;
- evidence expiry;
- likely pre-audit evidence gaps.

AHTE's Preemptive Strategy Engine may recommend targeted re-sampling, additional evidence, supplier review, targeted smart-glass audit, re-test, increased monitoring or operational hold according to policy. Recommendations remain evidence-linked and auditable.

## 12. 24/7 Command Center

All material laboratory, traceability and authority events must be routable to the **24/7 Command Center jointly monitored by GHSCL operational roles and authorised JAKIM authority-side roles**.

Priority incident classes include:

- chain-of-custody break;
- method out of scope;
- QC failure;
- result/report correction or withdrawal;
- signature/hash mismatch;
- sample/batch mismatch;
- evidence expiry/staleness;
- authority hold;
- re-test required;
- recurring laboratory anomaly;
- counterfeit/diversion signal;
- impossible scan geography;
- traceability-object binding fracture.

GHSCL and JAKIM do not have identical permissions: GHSCL performs digital/corridor operational monitoring and coordination; JAKIM retains authority-side monitoring and formal decision scope.

## 13. Trust-packet linkage

Laboratory/traceability evidence links into AHTE through:

`TrustAssertionID → ObjectIDs → Issuer → Scope → Validity → Status → Batch/Lot → DecisionRefs → EvidenceHashes → LabIndicators → ExceptionFlags → VerificationEndpoint → Jurisdiction → Timestamp → Signature/TrustAnchor`.

Detailed reports/source records remain in their controlled source domain unless authorised transfer is necessary. Cross-border exchange should preferentially use minimum-necessary signed assertions, hashes and references.

## 14. No-artificial-block implementation rule

**FULL ARCHITECTURE NOW → REAL CONNECTORS WHEN AVAILABLE → NO REDESIGN REQUIRED.**

Absence of live laboratory, JAKIM or traceability credentials does not justify removing the capability. Implement full schemas, workflows, UI, adapter contracts, connector-state handling, retries/reconciliation, access controls, evidence history and tests with a replaceable sandbox/development provider.

Sandbox state must be clearly labelled. Do not fabricate live laboratory results, authority receipts/decisions or production scan events.

## 15. Production closure inputs

Production activation requires the actual applicable inputs, including:

- exact laboratory legal identity and site;
- current accreditation certificate/schedule;
- applicable method/matrix scope;
- method validation/verification records;
- data-processing/cross-border legal basis;
- laboratory system/API specification;
- traceability system API/event/data contract;
- machine authentication/certificate exchange;
- evidence signing/key-management policy;
- report correction/withdrawal protocol;
- authorised JAKIM API specification/credentials/permissions;
- production connectivity test;
- authority workflow acceptance test;
- pilot sample/result dry run;
- Shipment 001 evidence-chain rehearsal;
- GCC destination acceptance where applicable.

These are connection/evidence dependencies, not permission to omit the target architecture.

## 16. Canonical path mapping

`Authority → Standard/Instrument → Clause/Requirement → Applicability → Control → HCP/SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

For this integration:

- **Authority:** JAKIM / applicable competent authority.
- **Standard/Instrument:** applicable current Malaysian Halal instruments and approved analytical methods.
- **Requirement:** exact test/evidence requirement for the product/material/case.
- **Applicability:** product, matrix, ingredient, risk and destination-specific applicability.
- **Control:** physical identification, controlled sampling/testing/QC/review and traceability integrity.
- **HCP/SCCP:** applicable Halal/Shariah critical control point.
- **Evidence:** signed result/report + custody + physical-code/traceability events + integrity metadata.
- **Audit Test:** verify laboratory competence/method scope/sample identity/result integrity/traceability source record.
- **Finding:** conformity/non-conformity/observation/trust fracture.
- **Corrective Action:** re-sampling, re-testing, CAPA, method/process/source correction.
- **Re-verification:** authorised follow-up.
- **Authority Gate:** direct JAKIM API to the authorised human decision workflow.
- **Trust State:** machine-readable state derived from verified evidence and authority event.
- **Operational Release:** governed operational action, never a substitute for certification.

## 17. Final integration position

The China system is treated as a **physical identity + item-level traceability + anti-counterfeit + laboratory evidence production plane** feeding AHTE.

AHTE provides **standards/applicability, evidence graph, integrity, digital twins, AI/ML assurance, predictive/preemptive analytics, direct JAKIM API linkage, trust state, cross-border verification and 24/7 Command Center orchestration**.

This is the single current China laboratory/traceability integration profile. Older split profile/addendum artifacts are retired after this content is committed.