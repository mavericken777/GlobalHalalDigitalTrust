# 07 — Cryptographic Trust-Anchor Architecture

## 1. Objective

Create a verifiable trust layer that binds identities, evidence, authority decisions and critical physical events without making a blockchain ledger the trust root.

## 2. Trust hierarchy

```text
ROOT TRUST AUTHORITY
        ↓
JURISDICTION TRUST ANCHOR
        ↓
ORGANISATION TRUST DOMAIN
        ↓
SYSTEM / SERVICE CERTIFICATE
        ↓
DEVICE / USER KEY
        ↓
SIGNED EVENT / ASSERTION
        ↓
EVIDENCE HASH / OBJECT PROOF
```

## 3. Key classes

| Key class | Purpose | Rotation |
|---|---|---|
| Root signing key | Root-of-trust certificate/signing | Rare, ceremony controlled |
| Jurisdiction anchor key | National/authority trust domain | Policy-defined |
| Organisation CA key | Issue organisational certificates | Controlled lifecycle |
| Service key | API/event signing | Frequent |
| Device key | Smart-glass/port device identity | Frequent / on compromise |
| User signing key | Human signature where required | Role-controlled |
| Evidence hash key | Integrity/authentication functions | Cryptoperiod policy |

## 4. Hardware protection

High-value authority and organisational keys should be stored in HSMs or equivalent hardware-backed security modules. Field-device keys should use secure elements/TPM/TEE capabilities where available.

## 5. Algorithms

The implementation profile shall use current, widely supported cryptographic primitives approved by the deployment security authority. Recommended baseline:

- SHA-256 or stronger approved hash for content integrity.
- Ed25519/ECDSA or approved equivalent for signatures where ecosystem compatibility allows.
- TLS 1.3 for transport where supported.
- AES-256-GCM or approved equivalent for symmetric encryption.

The exact algorithm profile is frozen in the security standard and may be updated without changing business object identifiers.

## 6. Evidence integrity

```text
RAW EVIDENCE
   ↓
CANONICAL SERIALISATION
   ↓
CONTENT HASH
   ↓
EVIDENCE MANIFEST
   ↓
SIGNATURE
   ↓
EVIDENCE OBJECT
```

Any derivative annotation is linked to the original evidence hash rather than replacing it.

## 7. Event signature

Critical events use:

`CanonicalEvent → PayloadHash → EventDigest → Sign(Device/User/Service key) → SignatureEnvelope`.

The event carries `PreviousEventID` and, for critical chains, `PreviousEventHash` to make alteration/reordering detectable.

## 8. Authority decision object

An authority decision contains:

- DecisionID.
- IssuerAuthorityID.
- IssuerRole.
- Scope.
- EffectiveFrom/Until.
- DecisionType.
- Related application/case.
- Product/batch/lot references.
- Supporting evidence references.
- Conditions/exceptions.
- Signature.
- KeyID.
- Trust-anchor chain.

## 9. Trust assertion

A cross-border trust assertion is intentionally smaller than the source evidence package.

```json
{
  "TrustAssertionID":"TA-SHP001-0001",
  "Issuer":"AUTH-...",
  "SubjectObjects":["LOT-...","CONT-...","SHIP-001"],
  "Scope":"Shipment 001 China → GCC",
  "ValidFrom":"...",
  "ValidUntil":"...",
  "State":"VERIFIED|RELEASED|HOLD|...",
  "DecisionRefs":[],
  "EvidenceHashes":[],
  "ExceptionFlags":[],
  "VerificationEndpoint":"...",
  "Jurisdiction":"CN→SA|CN→AE",
  "IssuedAt":"...",
  "Signature":{ "keyId":"...","value":"..." }
}
```

## 10. Selective disclosure

A verifier should be able to prove:

- the issuer is trusted;
- the assertion is current;
- a specific lot/container belongs to the shipment;
- the referenced decision is active;
- evidence hashes match;
- no unresolved exception is hidden in the disclosed scope.

The verifier should not automatically receive detailed employee data, internal production records or unrelated supplier information.

## 11. Revocation

Support:

- key revocation;
- device revocation;
- organisation credential suspension;
- authority decision withdrawal;
- trust assertion invalidation;
- certificate status update.

Use OCSP/CRL or an ecosystem-appropriate status service for certificates and a dedicated signed status event model for business trust objects.

## 12. Time integrity

Critical events require:

- trusted source timestamp;
- local device timestamp;
- reconciliation timestamp;
- time-source metadata.

Clock drift beyond policy creates `E-TIME-EXCEPTION` and may force review for high-value events.

## 13. Key compromise response

```text
DETECT
 ↓
REVOKE KEY
 ↓
ISOLATE DEVICE/SERVICE
 ↓
IDENTIFY AFFECTED EVENTS
 ↓
REVALIDATE TRUST CHAIN
 ↓
RE-ISSUE ASSERTIONS WHERE REQUIRED
 ↓
INVESTIGATE
 ↓
CLOSE INCIDENT
```

## 14. Blockchain policy

AHTE may optionally anchor event/evidence digests into a distributed ledger for additional tamper-evidence, but the business source of truth remains the governed AHTE event/evidence store and the authority decision registry.

## 15. Cross-border trust

The trust packet crosses jurisdictions as a signed assertion. Detailed source evidence remains accessible through controlled verification endpoints or lawful request workflows.

China's Network Data Security Management Regulation requires security measures including encryption, backup, access control and authentication, and sets governance obligations for data provision and processing. citeturn748828search0 The CAC's 2024 cross-border data provisions also require lawful processing and security safeguards for regulated data transfers. citeturn164534search0

## 16. Trust-anchor registry

```text
TrustAnchorID
Jurisdiction
Authority/Organisation
KeyID
Algorithm
CertificateChain
ValidFrom
ValidUntil
RevocationEndpoint
Status
PolicyVersion
```

## 17. Security acceptance tests

- Invalid signature rejected.
- Expired credential rejected.
- Revoked credential rejected.
- Altered evidence hash detected.
- Event-chain break detected.
- Wrong issuer rejected.
- Wrong scope rejected.
- Replay attempt detected.
- Key rotation preserves historical verification.
- Selective disclosure excludes unapproved fields.
