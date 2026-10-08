# AHTE assurance and monitoring plane

## Purpose

The AHTE assurance plane connects evidence and operational events for a certified product/SKU and its premises across origin, production, laboratory, warehouse, logistics, ports and GCC destination. It provides a real-time view for operating teams and certification decision makers.

## Event contract

Every event carries:

| Field | Meaning |
|---|---|
| ObjectID | Product, SKU, premises, batch, sample, shipment or equipment identity |
| EventID | Stable identity of the recorded event |
| EvidenceID | Evidence record linked to the event |
| ActorID | Responsible source, person or system |
| Timestamp | Event time and ingestion time where available |
| IntegrityProof | Hash/signature material for change detection |
| Provenance | Origin system, method, scope and source reference |

Correction creates a superseding record and preserves the prior event. IntegrityProof establishes byte integrity after capture; it does not establish factual truth.

## Connected operations

The plane connects:

1. organisation, premises, product, SKU, supplier and material onboarding;
2. applicable requirements, controls and attributable evidence;
3. laboratory sample identity, custody, method, QC, result and reviewer record;
4. audit observations, findings, corrective action and re-verification;
5. production, batch, sensors, IoT and digital-twin events;
6. Sinotrans warehouse, logistics, seals, route and telemetry events;
7. origin/destination port, customs and receiving interfaces;
8. GCC warehouse, distribution, retail, product verification and recall;
9. Command Center alerts, predictive analytics and preemptive recommendations.

## Decision roles

AI/ML supports monitoring, evidence review, anomaly detection, prediction, impact analysis and recommendations. JAKIM/JAIN/JAIM, muftis, scholars and authorised halal auditors decide certification award and revocation through their applicable processes. AHTE records and propagates verified source decisions. The platform does not fabricate institutional or partner responses.

The topology is **AHTE ⇄ Direct JAKIM API ⇄ JAKIM**. PHC and JAKIM work in parallel across Perak/state and federal governance. The physical corridor is **China → GCC direct**.

## State ownership

Certification status, platform assurance, operational custody, customs disposition and finance decisions have separate owners and state histories. Each connector preserves the provider's source and reports its actual environment and response state. Shariah finance and Takaful records are connected through their responsible providers.

## Schemas and policy

See `machine-spec/README.md`, `machine-spec/11-trust-fracture-taxonomy.json`, `machine-spec/12-autonomous-state-machine.json`, `machine-spec/14-authority-aware-api.md`, `machine-spec/15-agent-runtime-permissions.json`, `../hitm-decision-class-registry.json` and `../trust-packet-schemas.json`.
