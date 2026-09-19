# 13 — Cryptographic Event / Decision Binding

[PROPOSAL] [ENGINEERING-GATE] [TOOL-SPEC UNVERIFIED at runtime]

## Bindings

| Object | Binding | Must not mean |
|---|---|---|
| evidence_object | SHA-256 prefix (12 hex) + optional SCITT receipt (RFC 9943) | Certification |
| assessment_object | model_id + prompt_hash12 + asset hash | E5 |
| authority_decision_object | External issuer signature / optional W3C VC 2.0 wrap | AHTE-issued SPHM |
| generated media | C2PA 2.4 manifest | Authority mark |
| custody | EPCIS 2.0 event + seal_id | Destination Halal decision |

AHTE may **hold and verify**. AHTE may **not issue** a VC typed as Malaysia Halal Certificate.

SCRAPI remains an Internet-Draft; treat HTTP API as evolving.
