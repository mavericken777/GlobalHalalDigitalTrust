# Master Requirements Register

## Scope

The platform shall support the complete Halal Tayyib ecosystem from origin through consumer, while preserving national sovereignty and human regulatory authority.

## Functional requirements

### Manufacturer and producer
- Multilingual onboarding and education.
- Digital account and organisation profile.
- Product, ingredient, supplier and packaging registers.
- Evidence/document submission.
- AI readiness assessment.
- Corrective-action guidance.
- Quotation and service configuration.
- Traceability from source through production and shipment.
- Operational/lean intelligence using authorized data.

### Laboratory
- Laboratory identity and accreditation/authorization metadata.
- Test request and specimen chain of custody.
- Test result record and source document.
- Digital attestation/signature.
- Report delivery to authorized manufacturer and regulators.
- Evidence hash generation.
- Long-term evidence reference.

### Regulator
- Case intake and triage.
- Evidence verification.
- Controlled human decision workflow.
- Audit trail.
- Non-conformance and corrective action.
- Recall/withdrawal support.
- Cross-jurisdiction information exchange under policy.

### Logistics / Sinotrans or equivalent
- Shipment identity.
- Container/package identity.
- Chain-of-custody events.
- Loading/unloading events.
- Route and handoff data.
- Temperature/environment evidence where relevant.
- Customs/transport documentation references.
- Exception management.
- Proof of delivery.

### Warehousing
- Inbound integrity check.
- Storage zone identity.
- Segregation/separation controls.
- Temperature/humidity and other product-specific conditions.
- Cleaning/sanitation records.
- Handling events.
- Dispatch evidence.
- Outsourced-party monitoring.

### Retail
- Supplier monitoring.
- Receiving integrity checks.
- Product separation/identification.
- Storage condition monitoring.
- Inventory intelligence.
- Recall alerts.
- Product provenance display.
- Proof of collection/delivery where applicable.
- Consumer-facing scan/verification.

### Consumer
- Product scan.
- Verified provenance view.
- Halal/Tayyib educational content.
- ESG information.
- Recycling participation.
- Voluntary points/gamification.
- Feedback and issue reporting.

## Non-functional requirements

- Sovereign-by-design data architecture.
- API-first interoperability.
- Zero-trust security architecture.
- Strong authentication and authorization.
- Encryption in transit and at rest.
- Tamper-evident critical evidence.
- Long-term archival capability.
- Multi-region resilience.
- Fine-grained auditability.
- Explainable AI for consequential workflows.
- Human approval for regulated/religious decisions.
- Multilingual UX.
- Accessibility.
- High availability and disaster recovery.
- Data minimisation and purpose limitation.

## Governance requirements

- Country sovereignty boundaries.
- Jurisdiction-specific policies.
- Role-based and attribute-based access controls.
- Independent oversight.
- Appeals/correction pathways.
- Versioned standards and policies.
- Explicit legal basis for each cross-border exchange.
- Separation of regulatory authority from platform operation.

## Evidence requirements

Every critical event should have:

- event ID;
- entity ID;
- timestamp;
- source system;
- actor/service identity;
- event type;
- payload/reference;
- cryptographic hash;
- signature/attestation where required;
- previous-event reference where applicable;
- jurisdiction;
- retention class.

## Status taxonomy

Each requirement must be marked as:

- `PROPOSED` — architectural proposal;
- `SOURCE-DERIVED` — derived from supplied standards/audit materials;
- `FORMALLY-VERIFIED` — confirmed by authoritative documentation;
- `CONTRACTUAL` — only effective after signed agreement;
- `IMPLEMENTATION-BACKLOG` — required engineering work.

This taxonomy prevents strategic assumptions from being presented as existing permissions or commitments.
