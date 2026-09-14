# AHTE China Data Sovereignty Architecture

## 1. Design objective

Operate AHTE as a federated trust network rather than a single cross-border database. Detailed source data remains with its authoritative system of record. Cross-border exchange carries minimum-necessary, verifiable trust assertions.

## 2. Data classes

| Class | Examples | Default location | Cross-border treatment |
|---|---|---|---|
| Operational source data | production records, detailed personnel files, local audit workpapers | China / system of record | Restricted; governed transfer only |
| Commercial source data | pricing, supplier commercial terms, contracts | Owner jurisdiction | Need-to-know |
| Product traceability | product/SKU/batch/lot/pallet/container/seal identifiers | Federated | Exchange as required for traceability |
| Authority assertions | decision ID, issuer, scope, validity, status | Authority system | Exchange signed assertion |
| Evidence references | evidence ID, hash, timestamp, issuer | Evidence system | Prefer pointer/hash over raw evidence |
| Analytical result | sample ID, method/version, result/status | Laboratory system | Exchange result summary + provenance |
| Personal information | names, contact, identity, device/location records | Jurisdiction of collection | Apply China cross-border requirements and destination rules |
| Aggregated analytics | risk scores, performance metrics | Federated analytics zone | Minimise/de-identify where practical |

## 3. China control baseline

China's Data Security Law applies to data-processing activities in China and treats data processing broadly. China's PIPL governs personal-information processing and contains specific cross-border provisions. The Network Data Security Management Regulation took effect on 1 January 2025. CAC continues to publish cross-border data guidance in 2026. AHTE should therefore implement classification, access control, provenance, purpose limitation, data minimisation and controlled cross-border pathways as architecture primitives.

Official sources:
- https://en.spp.gov.cn/2021-06/10/c_948426.htm
- https://en.spp.gov.cn/2021-12/29/c_948419.htm
- https://www.cac.gov.cn/2024-09/30/c_1729384452307680.htm
- https://www.cac.gov.cn/2026-09/11/c_1790876549989064.htm

## 4. Recommended federation model

```text
China authoritative systems
    |  local evidence / source records
    v
AHTE China Trust Gateway
    |  signed assertions / controlled evidence pointers
    v
Global Trust Graph
    |  jurisdiction-aware presentation
    +----> GCC Trust Gateway
    +----> Malaysia Trust Gateway
    +----> Approved stakeholder interfaces
```

## 5. Minimum trust assertion

```json
{
  "trustAssertionId": "TA-...",
  "objectIds": ["BATCH-...", "SHIPMENT-..."],
  "issuer": {"authorityId": "..."},
  "scope": "...",
  "jurisdiction": "CN",
  "validFrom": "...",
  "validTo": "...",
  "status": "...",
  "decisionReference": "...",
  "evidenceHashes": ["..."],
  "exceptionFlags": [],
  "verificationEndpoint": "...",
  "issuedAt": "...",
  "signature": "...",
  "trustAnchor": "..."
}
```

## 6. Security controls

- Zero-trust identity for users, devices, gateways and service accounts.
- Strong key management for high-value signing roles.
- Signed authority decisions and critical custody events.
- Tamper-evident audit log with correlation IDs.
- Role + organisation + purpose + jurisdiction access rules.
- Encryption in transit and at rest.
- API schema enforcement and replay protection.
- Device attestation where appropriate for ports and audit equipment.
- Offline operation with controlled reconciliation for low-connectivity sites.
- Security incident response connected to trust-state and shipment hold workflows.

## 7. Data-release decision tree

`Need data? -> Is it necessary? -> Is it source data or assertion? -> Can minimum assertion satisfy the purpose? -> Is cross-border transfer legally permitted? -> Apply approved mechanism -> Transfer -> Log -> Verify recipient use`

## 8. Governance

AHTE should maintain a data register with: owner; controller/processor role; purpose; data class; source; retention; jurisdiction; permitted recipients; transfer mechanism; security classification; integrity controls; deletion/archival rule; and incident owner.
