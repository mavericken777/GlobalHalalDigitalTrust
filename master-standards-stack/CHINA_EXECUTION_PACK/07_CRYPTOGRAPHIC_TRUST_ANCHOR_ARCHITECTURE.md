# 07 — CRYPTOGRAPHIC TRUST-ANCHOR ARCHITECTURE

## 1. Objective

Bind identities, evidence, physical custody and authority decisions into a tamper-evident trust graph that can be independently verified without exposing unnecessary source data.

## 2. Trust hierarchy

`ROOT TRUST AUTHORITY -> JURISDICTION TRUST DOMAIN -> ORGANISATION CA -> FACILITY / DEVICE CERTIFICATE -> USER / ROLE CREDENTIAL -> EVENT SIGNATURE`

The root should be held under multi-party governance. No single operator should control issuance, approval and emergency recovery simultaneously.

## 3. Cryptographic primitives

- SHA-256 or stronger approved hash for content/event digests.
- Ed25519 or approved equivalent for application-level signing where supported by platform policy.
- TLS 1.3 for transport.
- X.509 certificates for infrastructure identity.
- Hardware-backed keys in TPM/HSM/secure element for high-value signing keys.
- Optional Merkle batching for high-volume evidence anchoring.

## 4. Evidence integrity

For each evidence item:

`raw artifact -> canonicalisation -> content hash -> metadata hash -> evidence manifest -> actor signature -> storage pointer`.

The stored hash does not substitute for retaining the evidence where the applicable retention policy requires the original.

## 5. Event hash chain

Each event references `previous_event_hash`. The resulting chain provides sequence integrity. Periodic Merkle roots can be anchored to an independent trust service or authority-controlled ledger.

## 6. Physical-digital binding

### Seal binding
`seal_id + container_id + shipment_id + application_event + custodian + location + time + seal_image_digest + signer`.

### Pallet binding
`pallet_id + contained_lots + loading_event + loading_actor + container_id`.

### Batch binding
`batch_id + formula_version + source_materials + production_events + evidence_set + release_state`.

## 7. Credential classes

`AUTHORITY-CRED`, `AUDITOR-CRED`, `QA-CRED`, `LAB-CRED`, `LOGISTICS-CRED`, `PORT-OFFICER-CRED`, `SYSTEM-CRED`, `DEVICE-CRED`.

Every credential has issuer, subject, role, jurisdiction, start/end time, revocation pointer and permitted scopes.

## 8. Key lifecycle

`GENERATE -> REGISTER -> ACTIVATE -> MONITOR -> ROTATE -> REVOKE -> ARCHIVE`.

Emergency revocation must propagate to gateways and mobile devices. New keys must not retroactively invalidate already-signed events; verification uses the certificate state at event time.

## 9. Selective disclosure

Create signed assertions that expose only required fields, e.g. `batch identity`, `status`, `authority decision`, `seal integrity`, `test result class`, without exposing the complete factory dossier.

The verifier receives an assertion plus proof that it was issued under a trusted credential and references the underlying evidence object.

## 10. Data-zone architecture

China-resident source records remain in the China-controlled zone when required. Malaysia and GCC zones retain their own authoritative or locally required records. A cross-border trust gateway exchanges signed assertions, hashes, identifiers and authorised evidence packets.

## 11. Anti-replay controls

Every command/event includes unique ID, issuer, issued-at, expiry where appropriate, nonce/idempotency key and monotonic sequence. Duplicate events are rejected or safely de-duplicated.

## 12. Key ceremonies

Root creation, organisation onboarding, authority credential issuance and disaster recovery use documented multi-person ceremonies with recorded approvals, offline recovery material and independent witnesses where governance requires.

## 13. Verification API

`GET /trust/v1/verify/{assertion_id}` returns issuer, subject, status, issued-at, expiry, signature verification state, underlying object references and policy scope.

`POST /trust/v1/verify-bundle` verifies a shipment evidence package and returns a structured verification report.

## 14. Security event model

`E-KEY-ISSUED`, `E-KEY-ROTATED`, `E-KEY-REVOKED`, `E-CREDENTIAL-SUSPENDED`, `E-EVIDENCE-SEALED`, `E-ANCHOR-CREATED`, `E-ANCHOR-VERIFIED`, `E-VERIFICATION-FAILED`.

## 15. Recovery

Backup keys and recovery procedures are jurisdiction-aware. Recovery cannot create a new authority decision; it only restores the ability to verify or issue under already-approved authority.
