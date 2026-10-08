# AHTE machine specification

These schemas and policies implement the current AHTE operating model. They connect operational evidence, monitoring, analytics and case workflows while preserving named human certification decision-making.

| ID | Artifact | Responsibility |
|---|---|---|
| 01 | `01-agent-authority-model.md` | Actor and role model |
| 02 | `02-ai-action-authority-matrix.json` | AI assistance and action classes |
| 03 | `../hitm-decision-class-registry.json` | Decision-class definitions |
| 04 | `04-human-authority-mandate-registry.json` | Human and institutional decision roles |
| 05–10 | `../trust-packet-schemas.json` | Evidence, identity, custody and assurance records |
| 11 | `11-trust-fracture-taxonomy.json` | Exceptions and monitoring signals |
| 12 | `12-autonomous-state-machine.json` | Operational workflow transitions |
| 13 | `13-cryptographic-binding-profile.md` | Evidence integrity and signatures |
| 14 | `14-authority-aware-api.md` | Authority-service integration contract |
| 15 | `15-agent-runtime-permissions.json` | Runtime permissions |
| 16 | `16-auditability-layer.md` | Audit records and provenance |
| 17 | `../policies/hitm-default-deny.rego` | Human decision workflow permissions |

Topology: **AHTE ⇄ Direct JAKIM API ⇄ JAKIM**. Physical corridor: **China → GCC direct**. AI/ML assists monitoring, prediction and preemptive strategy; JAKIM/JAIN/JAIM, muftis, scholars and authorised halal auditors decide certification award and revocation through their applicable processes.
