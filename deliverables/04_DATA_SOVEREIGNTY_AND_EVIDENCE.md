# Data Sovereignty, Evidence & 100-Year Trust Model

## Principle

**Data stays where it belongs. Trust travels.**

## Sovereign data domains

Each national node defines:
- legal jurisdiction;
- data controller/processor roles;
- approved storage locations;
- cross-border transfer rules;
- retention policies;
- access policies;
- incident notification obligations.

## Data classes

### Class A — Public
Verified information suitable for consumers and public discovery.

### Class B — Ecosystem
Operational information exchanged among authorized partners.

### Class C — Regulatory
Evidence accessible to competent authorities and approved assurance actors.

### Class D — Restricted/Confidential
Trade secrets, personal data and security-sensitive information held under strict purpose limitation.

## Evidence record

For each critical event:

`event_id + timestamp + actor + source + payload/reference + hash + signature/attestation + previous_event + jurisdiction + retention_class`

## Snapshot architecture

The trust layer should normally store a cryptographic snapshot of the relevant source record rather than a second copy of the full data. This reduces duplication and supports efficient integrity verification.

## Dispute reconstruction

When authorized:
1. retrieve the original sovereign record;
2. validate access authorization;
3. calculate the current content hash;
4. compare with the historical evidence hash;
5. validate signature/attestation;
6. reconstruct the chain of events;
7. issue an evidence verification result.

## Long-term preservation

A 100-year preservation objective should use multiple mechanisms:
- cryptographic agility;
- periodic re-hashing with stronger algorithms if needed;
- key rotation and archival key custody;
- format migration;
- independent archival copies;
- integrity checks;
- legal retention schedules.

Long-term evidence is not equivalent to retaining personal data forever. Data minimisation and statutory deletion/retention requirements remain applicable.

## Federated nodes

Target architecture: minimum three independent nodes for critical trust services, with no requirement that all business records be replicated. Nodes can independently verify event fingerprints and support recovery.

## Evidence lifecycle

`Capture -> validate -> hash -> attest -> store -> replicate evidence metadata -> monitor -> archive -> periodically revalidate -> retrieve on authorized demand`
