# Amanah / Global Halal Digital Trust — Current Platform Architecture

## Operating model

Global Halal Supply Chain Limited operates the international digital-infrastructure layer. Amanah and AHTE connect and continuously monitor the complete halal product-assurance journey from producer and premises through GCC destination and verification. The platform maintains one connected view of product/SKU identity, supplier and material evidence, applicable requirements, laboratory and audit records, production, warehouse and logistics custody, ports, certification status, exceptions, risk and corrective action.

```text
China producer + premises
→ organisation, facility, product, SKU, suppliers and materials
→ applicable Malaysian/JAKIM framework and destination requirements
→ premises readiness, controls, HCP/SCCP and attributable evidence
→ JAKIM-certified laboratory sampling, custody, method, QC and results
→ JAKIM halal audit, review and certification decision
→ corrective action and re-verification
→ production, batch, warehouse and logistics custody
→ port/customs interfaces and China → GCC direct transit
→ GCC importer, receiving, distribution, retail and verification
→ real-time monitoring, predictive analytics, preemptive strategies and recall support
```

## Malaysia governance and platform roles

PHC and JAKIM work in parallel across Perak/state and federal functions within Malaysia’s shared Islamic governance and Shariah framework. Certification award and revocation decisions are made by JAKIM/JAIN/JAIM, muftis, scholars and authorised halal auditors through the applicable governance and certification process. The platform supplies the connected evidence, workflow, real-time monitoring, analytics, prediction and preemptive strategy support for that work, then records and propagates decision outcomes across relevant premises, products, SKUs and supply-chain events.

The system topology is **AHTE ⇄ Direct JAKIM API ⇄ JAKIM**. The physical corridor is **China → GCC direct**. GHSCL Hong Kong coordinates the international operating and digital-infrastructure layer and the 24/7 Command Center. Laboratories generate analytical evidence within their JAKIM certification and technical scope; Sinotrans provides warehouse and logistics operations with connected custody and telemetry; ports/customs and destination systems provide their operational records and interfaces.

## Real-time assurance and AI/ML

The Command Center correlates product, premises, certification, laboratory, audit, production, warehouse, logistics, port and destination events. AI/ML supports evidence review, anomaly detection, risk prediction, impact analysis, recall blast-radius mapping and preemptive strategy recommendations. Responsible operators and the named certification decision makers act on those insights through their assigned workflows. The system records who acted, when, on what evidence, and how the status propagated.

Evidence remains attributable to its source, object and event. Corrections supersede prior records while preserving the record history. Integrity proofs help detect changes to recorded evidence; they do not independently validate the underlying observation. Laboratory findings are interpreted with method, scope, sample identity and reviewer context.

## Standards and product scope

Use the complete applicable Malaysian/JAKIM framework, including MPPHM, MHMS, HAS, IHCS, protocols, circulars, applicable Malaysian Standards, destination requirements and laboratory methods. Applicability follows the actual product, premise, process, destination and activity. Keep one maintained, extensible standards register and do not present any dated standards snapshot as the controlling package.

## Platform domains

- China origin, producer, suppliers, ingredients, materials and premises onboarding.
- Product, SKU, formula, batch, facility and certification-scope records.
- Laboratory sample planning, chain of custody, methods, QC, results, review and signed records.
- Premises and halal audit, smart-glasses evidence capture, findings, corrective action and re-verification.
- Production, sensors, IoT, digital twins, event fabric and real-time assurance.
- Warehouse, Sinotrans logistics, seals, routes, custody and telemetry.
- Ports/customs interfaces, GCC importer and receiving, warehouse, distribution, retail and verification.
- Command Center, predictive and preemptive analytics, risk, exceptions and recall.
- Shariah finance, Takaful, claims evidence and tokenization workflows where approved by the relevant providers and regulators.

## Connector delivery

Build each connector interface and workflow in full, with explicit configuration and environment state. A missing credential or partner endpoint is represented as an integration state, not as a reason to remove the capability or redesign it. Never fabricate a live authority, laboratory, logistics, customs or finance response.
