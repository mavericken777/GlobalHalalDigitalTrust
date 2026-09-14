# IQ300 AUTHORITY GATES + AUDIT TEST CATALOG

## Authority gates

| Gate | Function | Typical trigger |
|---|---|---|
| AUTH-AUDIT | Competent-authority audit/assessment | conformity assessment and evidence review |
| AUTH-CERT | Certification decision | issuance/renewal/scope decision |
| AUTH-LOGO | Halal mark permission | artwork/claim release |
| AUTH-MATERIAL | Material-origin acceptance | animal-derived / high-risk inputs |
| AUTH-SERTU | Sertu verification/release | mughallazah contamination or conversion |
| AUTH-PROTOCOL | Live slaughter/stunning rule gate | current Malaysian Protocol / circular / fatwa |
| AUTH-CHAIN | Logistics node integrity | transport/warehouse/retail certification |
| AUTH-OUTSOURCE | Outsourced activity control | CMO/lab/packer/warehouse/carrier |
| AUTH-LEGAL | Regulatory gate | NPRA / trade description / other law |
| AUTH-LAB | Laboratory evidence gate | method validity, scope and interpretation |
| AUTH-VACCINE | Vaccine/biologic authority gate | fatwa/circular/authority acceptance |
| AUTH-COMPETENCE | Professional competence gate | Halal Executive/auditor role |
| AUTH-GOV | Governance/ontology gate | terminology, Shariah QMS, source freeze |

## Audit tests

### DOC-01 - Document review
Verify controlled policy, SOP, specification, procedure, drawing/layout, certificate or regulated document. Check revision, approval, effective date and linkage to the applicable requirement.

### REC-01 - Record sampling
Sample records from a defined period. Verify identity, completeness, date/time, responsible person, lot/asset linkage, traceability and closure.

### SITE-01 - On-site inspection
Observe actual physical condition against the requirement: segregation, cleanliness, status labels, equipment, storage, personnel and facility configuration.

### INT-01 - Interview
Confirm that the responsible person understands the control, knows escalation criteria and performs the control consistently.

### TRACE-01 - Forward/backward trace
Start from an output and trace back to inputs, or from an input forward to affected outputs, preserving lot/container/seal/asset relationships.

### WIT-01 - Witness test
Observe an operational activity in real time, including cleaning, line clearance, receiving, loading, handover, HCP monitoring or other controlled action.

### COMP-01 - Competence verification
Verify qualification, training, experience, assessment, authorization, validity and role assignment for the responsible individual.

### AUTH-01 - Authority evidence check
Verify formal authority record, certificate, approval, Panel decision, verification event or other competent-authority artifact where the control requires it.

### LAB-01 - Laboratory evidence check
Verify sample identity, chain of custody, method edition/version, matrix suitability, kit/SOP, controls, validation, result and report linkage. A laboratory result is evidence, not the certification decision.

### CHANGE-01 - Change-control review
Verify change request, impact/risk assessment, approval, implementation, updated documents, training, validation and re-verification.

### RECALL-01 - Recall / withdrawal simulation
Demonstrate affected-lot identification, containment, downstream trace, upstream trace, notification and effectiveness verification.

## Finding classification logic

`No objective evidence -> HOLD / finding`
`Control failure -> NONCONFORMING`
`Potential product impact -> QUARANTINE`
`Correctable system issue -> CORRECTIVE_ACTION`
`Authority-dependent issue -> AUTHORITY-PENDING / ESCALATE`
`Effective verification -> RE-VERIFICATION COMPLETE`
