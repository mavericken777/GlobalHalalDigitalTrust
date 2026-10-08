# China-to-GCC operating workflows

This folder describes the end-to-end China-origin to GCC-destination operating journey and the interfaces used by the Amanah / AHTE platform. China-to-GCC is the direct physical corridor; Malaysia provides parallel state and federal governance and authority connectivity.

## End-to-end journey

```text
Organisation and premises onboarding
→ SKU, supplier and material registration
→ applicable requirements and operating controls
→ sample identity, collection, seal and custody
→ JAKIM-certified laboratory method, quality controls, result and signed review
→ smart audit, evidence review and certification decisions by competent human authorities
→ production, batch and lot monitoring
→ certified warehouse and Sinotrans custody / telemetry
→ origin port and customs processes
→ direct movement to GCC destination
→ destination receiving, warehousing, distribution, retail and verification
→ continuous monitoring, corrective action, re-verification and recall support
```

The 24/7 Command Center connects evidence, custody, status, exceptions and predictions across this journey. AI/ML supports monitoring and preemptive strategy; JAKIM/JAIN/JAIM, muftis, scholars and authorised halal auditors make certification award and revocation decisions. Authority connectivity follows **AHTE ⇄ Direct JAKIM API ⇄ JAKIM**.

## Technical references

| File | Purpose |
|---|---|
| `00_MASTER_CHINA_EXECUTION_MODEL.md` | End-to-end operating model and roles |
| `02_RULE_PRECEDENCE_ENGINE.md` | Applicable requirement resolution across operating jurisdictions |
| `03_SHIPMENT_EVENT_CATALOGUE.md` | Product, shipment, custody and monitoring event definitions |
| `04_FACTORY_SYSTEM_API_CONTRACTS.md` | ERP/MES/QMS/WMS/LIMS/IoT interface contracts |
| `05_SMART_GLASS_AUDIT_SPEC.md` | Field audit and evidence-capture workflow |
| `06_PORT_OFFICER_UI_WORKFLOW.md` | Port/customs inspection and interface workflow |
| `07_CRYPTOGRAPHIC_TRUST_ANCHOR_ARCHITECTURE.md` | Evidence integrity, signatures and selective disclosure |
| `08_CHINA_CORRIDOR_RELEASE_PLAYBOOK.md` | Operational sequence from onboarding through GCC receiving |
| `09_MASTER_STANDARDS_FULL_MATRIX.md` | Applicability references and control mapping |
| `schemas/` and `api/` | Machine-readable event, trust, custody and interface schemas |

Connector definitions describe interfaces; a connector is reported as live only when the corresponding provider is configured and verified. Exact legal, authority, destination and laboratory requirements must be sourced from their current authoritative materials in the relevant implementation.
