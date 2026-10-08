# China-to-GCC operating model

## Purpose

Amanah/AHTE connects the full product and premises assurance journey from China origin to GCC destination. The operating model covers manufacturer onboarding, materials, laboratory evidence, audits, certification records, production, warehouses, logistics, customs, receiving, distribution, retail and verification.

## Governance and platform roles

- **PHC and JAKIM** work in parallel across Perak/state and federal Malaysian governance.
- **JAKIM/JAIN/JAIM, muftis, scholars and authorised halal auditors** make certification award and revocation decisions through their applicable processes.
- **Global Halal Supply Chain Limited** operates the international digital-infrastructure and coordination layer and 24/7 Command Center.
- **Amanah/AHTE** connects product/SKU, premises, suppliers/materials, controls, evidence, events, audit records, certification status, custody and destination workflows.
- **AI/ML** assists real-time monitoring, anomaly detection, predictive analytics, impact assessment and preemptive strategy recommendations. It does not make certification decisions.

Authority connectivity is **AHTE ⇄ Direct JAKIM API ⇄ JAKIM**. The physical route is **China → GCC direct**. Malaysia is the parallel governance, assurance and authority-connectivity plane, not a physical transit leg.

## Product journey

```text
Organisation and premises onboarding
→ product/SKU and supplier/material registration
→ applicable requirements and controls
→ laboratory sampling, custody, method, QC, result and authorised review
→ audit, findings, corrective action and re-verification
→ competent human certification decisions and status records
→ production, batch and lot monitoring
→ JAKIM-certified warehouse and logistics custody / telemetry
→ origin port and customs processes
→ direct China-to-GCC movement
→ GCC receiving, warehouse, distribution and retail
→ verification, continuous monitoring and recall support
```

## Event and evidence model

Represent each material action with ObjectID, EventID, EvidenceID, ActorID, timestamp and integrity proof, with applicable location, scope, method, parent/child objects, reviewer, issuer and provenance. Link evidence to the affected product, premises, batch, sample, shipment or custody event. Preserve original records; corrections supersede rather than overwrite. Integrity checks protect record identity and integrity; they do not establish the truth of a claim.

Laboratory evidence follows sample identity → collection/seal → custody → method and quality controls → result → technical review/signature → report → linked assurance evidence. A laboratory result is not certification. JAKIM-certified laboratory, logistics-provider and warehouse status and scope are represented from the applicable JAKIM records.

## Monitoring and action

The monitoring system correlates changes across product, premises, suppliers, laboratory, production, warehouse, logistics, port and GCC destination records. Analytics can identify anomalies, predict potential risk, map impact and recommend preventive action. People responsible for operations and the competent authorities act on findings and certification decisions.

Keep certification, platform assurance, operational custody, customs and finance/Takaful records connected but attributable to their respective issuers and decision makers. Exceptions, containment, corrective action, re-verification, suspension, revocation and recall are recorded as operational events with linked evidence.

## Technical documents

Use this operating model with the event catalogue, factory API contracts, smart-glass audit specification, port/customs workflow, evidence integrity design, laboratory interface and machine-readable schemas in this directory. Interfaces describe the target workflow; production responses are recorded only when received from configured systems.
