# IQ300 2026 Interoperability Stack

| Field | Value |
|---|---|
| Artifact | `IQ300_2026_INTEROP_STACK.md` |
| Revision | v0.1.0 |
| Control date | 2026-09-20 |
| Classification | post-freeze characterisation — not project authority |
| Authority effect | none |

[PROPOSAL: 2026 interop bindings — path point: Evidence / Trust State / Authority Gate]
[TOOL-SPEC UNVERIFIED at runtime until provisioned]

Presence here means characterised against public specifications retrieved 2026-09-20. It does not approve paid spend, deployment, or controlled-data upload.

## Verified bindings

### W3C Verifiable Credentials Data Model 2.0

- Status: W3C Recommendation, 15 May 2025 (family published with Data Integrity 1.0 and JOSE/COSE securing).
- Use: wrap **external** E5 authority decisions when an issuer exists.
- Ban: AHTE must not issue a VC typed as Malaysia Halal Certificate / SPHM.

### IETF RFC 9943 — SCITT architecture

- Status: Proposed Standard, June 2026.
- Use: register signed statements (evidence hash, CAPA close-out digest, seal event digest, assessment digest) and obtain receipts.
- Ban: a SCITT receipt is not certification.
- Note: SCRAPI remains an Internet-Draft; treat the HTTP API as evolving.

### GS1 EPCIS 2.0 / ISO/IEC 19987:2024

- Use: custody What/When/Where/Why events for China → GCC segments.
- Align port_custody_object.event_type to EPCIS business steps when implementing.
- Ban: do not invent shipment events to populate the log.

### EU Digital Product Passport (context only)

- CEN/CLC horizontal DPP standards reported published September 2026 (EN 18216 identifiers / carriers / exchange among them).
- Use only if a specific SKU is in a regulated DPP category. DPP ≠ Halal certification.

### Open Policy Agent

- CNCF graduated general-purpose policy engine. Rego default deny. Signed bundles. Decision logs.
- HITM PDP. Runtime is PEP. Model confidence is not an allow key for D5/D6.

### SPIFFE / SPIRE

- Workload identity via short-lived SVIDs.
- Residual: published 2026 research that a compromised Kubernetes node can mint co-located SVIDs. Node hardening is required.

### C2PA Content Credentials 2.4 (April 2026)

- Manifests on generated video, image, infographic, logo packages.
- Include digitalSourceType / AI-disclosure where the asset is synthetic or AI-modified.
- Ban: C2PA must not imitate JAKIM or GCC marks.

## Implementation order

1. Schemas + HITM registry + path map (this commit).
2. OPA default-deny policies in CI against fixture cases.
3. EPCIS event types mapped to corridor segments (empty until real events).
4. SCITT-shaped signed statement profile.
5. C2PA on public generated assets.
6. VC 2.0 profile only when an external E5 issuer exists.
7. SPIFFE when a runtime exists.
