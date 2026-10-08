# Global Halal Digital Trust — End-to-End Platform Architecture

## Purpose

Global Halal Supply Chain Limited develops and operates the international digital-infrastructure layer for Amanah and the Global Halal Digital Trust ecosystem. AHTE connects the complete assurance journey for each certified product/SKU and its premises, suppliers, materials, laboratories, audits, production, storage, logistics and destination operations.

The platform maintains real-time evidence, certification status, custody, risk, exception, analytics and corrective-action context from origin through the GCC market. The Command Center presents that connected operational picture and supports authorised teams with predictive analytics and preemptive strategies.

## Governance and topology

```text
PHC — Perak/state governance     JAKIM — federal governance
                 work in parallel

AHTE ⇄ Direct JAKIM API ⇄ JAKIM

China origin → GCC destination (direct physical corridor)
```

PHC and JAKIM work in parallel across Perak/state and federal Malaysian governance within the shared Islamic framework. JAKIM/JAIN/JAIM, muftis, scholars and authorised halal auditors decide certification award and revocation through their applicable processes. AHTE provides the evidence, workflow, monitoring and analytics context, then records and propagates verified decision outcomes.

AI/ML assists with evidence review, anomaly detection, continuous monitoring, risk prediction, impact analysis, recall scope and preemptive strategy recommendations. AI does not award or revoke certification. Laboratories produce analytical evidence within their JAKIM certification and technical scope; laboratory results support the applicable review and do not substitute for a certification decision.

## End-to-end process

```text
1. Organisation and premises onboarding
2. Product, SKU, formula, supplier and material registration
3. Applicable Malaysian/JAKIM framework and destination requirements
4. Premises controls, HCP/SCCP and attributable evidence
5. Laboratory sample planning, custody, method, QC, result and review
6. Smart audit, findings, corrective action and re-verification
7. Certification status and decision records from the responsible authority process
8. Production, batch, sensor and digital-twin events
9. Certified warehouse and Sinotrans logistics custody/telemetry
10. Port and customs interfaces
11. GCC importer, receiving, storage, distribution and retail
12. Verification, continuous monitoring, predictive insights and recall support
```

Each stage is connected to the relevant product/SKU and premises record. Changes in evidence, certification status, custody, environment or destination state update the monitoring and exception context for the affected scope.

## Platform architecture

| Layer | Responsibility |
|---|---|
| Source and identity | Organisation, premises, SKU, batch, supplier, material, equipment and shipment identifiers |
| Standards applicability | Applicable Malaysian/JAKIM instruments, MPPHM, MHMS, HAS, IHCS, protocols, circulars, lab methods and destination requirements |
| Evidence and event fabric | Source-linked evidence, custody events, timestamps, actors, signatures, corrections and supersession history |
| Assurance intelligence | Rules, anomaly detection, predictive analytics, impact analysis, recall scope and preemptive recommendations |
| Command Center | Real-time operational picture, role-specific alerts, case routing and decision context |
| Connector plane | JAKIM, laboratory, ERP/MES/QMS/WMS/LIMS/IoT/DMS, Sinotrans, ports/customs, GCC parties, finance and Takaful |
| Experience and verification | Role-based onboarding, operations, monitoring, audit, receiving and product verification views |

## Evidence and status semantics

Every evidence record links its object, event, actor, timestamp and integrity proof. Corrections supersede prior records without erasing their history. An integrity proof supports change detection; it does not prove the underlying observation is true. Laboratory findings retain sample identity, method, scope and reviewer context. `NOT_DETECTED ≠ HALAL`.

Authority certification status, platform assurance status, operational custody, customs disposition and finance decisions remain separate source-owned records. A verified source update may be propagated to relevant product, premises and operational views with its provenance intact.

## Connector behaviour

Connector interfaces and workflows are implemented for development, sandbox, authorization and production environments. The interface reports the provider's actual state and never fabricates a response. Partner credentials, endpoint scopes and source-owned records are configured with the relevant provider while the product workflow remains available for integration and testing.

## Shariah finance and Takaful

The platform connects Shariah finance, Takaful and claims-evidence workflows to verified supply-chain records. Financial approval, coverage, claims decisions and tokenization operate only through the responsible providers and their applicable legal, Shariah and regulatory processes.
