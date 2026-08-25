# Reference Architecture

## 1. Logical layers

### Layer 0 — Sovereignty & Governance
National legal domains, regulatory authorities, policy engines, approved cloud/data-centre choices and cross-border data-sharing rules.

### Layer 1 — Identity & Trust
Organisation identity, person/service identity, credentials, roles, attestations, key management, trust registries and revocation.

### Layer 2 — API & Interoperability Fabric
Secure API gateway, event bus, schema registry, policy enforcement, adapter layer for legacy systems and modern systems, and audit logging.

### Layer 3 — Operational Systems
Manufacturer, laboratory, logistics, warehousing, customs, retailer, financing and consumer systems remain authoritative for their own operational data.

### Layer 4 — Trust Evidence Layer
Cryptographic event fingerprints, signed evidence manifests, provenance graph, chain-of-custody references and evidence-retention metadata.

### Layer 5 — AI & Intelligence
Knowledge concierge, process advisor, quotation engine, anomaly detection, risk prediction, operational intelligence, market intelligence and ESG analytics.

### Layer 6 — Experience Layer
Government portal, manufacturer portal, laboratory portal, logistics portal, retailer dashboard, consumer scan experience and regulator command centre.

## 2. Data residency pattern

Sensitive business records are retained in the jurisdiction selected by the data controller and required by law. Cross-border data exchange is policy-driven. The default is minimum necessary disclosure. A receiving party can verify a claim without receiving unrelated source data.

## 3. Federated evidence pattern

A country node maintains its operational records and a local evidence index. Global trust nodes may retain cryptographic fingerprints and selected metadata required for network verification and resilience. Full replication is not the default.

## 4. Event architecture

Each material event is represented as a canonical event:

```json
{
  "event_id": "evt_...",
  "entity_id": "product_...",
  "event_type": "LAB_RESULT_ISSUED",
  "jurisdiction": "CN",
  "occurred_at": "2026-01-01T00:00:00Z",
  "source_system": "lab.example",
  "actor": "did:example:...",
  "payload_ref": "sovereign://cn/...",
  "content_hash": "sha256:...",
  "attestation": "sig:...",
  "previous_event": "evt_..."
}
```

## 5. Trust graph

The core graph connects:

`Material -> Supplier -> Lab Test -> Product -> Batch -> Facility -> Shipment -> Container -> Warehouse -> Retail Location -> Consumer Scan`

Each edge can carry authorization, evidence and timestamps.

## 6. Public versus restricted views

A single product can have multiple views:

- **Public consumer view:** safe provenance and verified milestones.
- **Commercial view:** supplier, shipment and operational information for authorized parties.
- **Regulator view:** complete evidence within legal scope.
- **Laboratory view:** testing and chain-of-custody scope.
- **Security/audit view:** integrity and access records.

## 7. Resilience

Target pattern:

- at least three independent evidence/availability zones for critical services;
- multiple infrastructure providers where feasible;
- immutable backups;
- offline or logically isolated recovery copies;
- tested recovery procedures;
- regional failover;
- key-compromise recovery.

## 8. Design rule

No single database, cloud provider, country, laboratory, regulator, or AI model should become a single point of systemic trust failure.
