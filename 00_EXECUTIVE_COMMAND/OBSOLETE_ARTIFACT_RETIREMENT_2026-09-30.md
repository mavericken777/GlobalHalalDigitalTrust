# Obsolete Artifact Retirement Register — 30 September 2026

## Metadata

| Field | Value |
|---|---|
| Artifact | `OBSOLETE_ARTIFACT_RETIREMENT_2026-09-30.md` |
| Revision | v1.0.0 |
| Control date | 2026-09-30 |
| Classification | Repository consolidation / supersession control |
| Governing requirements | `CURRENT_TARGET_ARCHITECTURE_2026-09-30.md`; `PLATFORM_REQUIREMENTS_TRACEABILITY_2026-09-30.md`; `IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md` |
| Freeze impact | None — `master-standards-stack/verified-2026-09-17/` untouched |

[PROPOSAL: repository consolidation — path point: source/evidence governance]

## 1. Retirement rule

An artifact is deleted from the active tree only when its unique substantive requirements have been preserved in the replacement, active references are repointed, historical provenance remains available through Git history and the verified freeze is unaffected.

Historical audit/reconciliation artifacts are not deleted merely because they describe an older project state. They remain evidence of what was reviewed at that time unless they create an active control collision.

## 2. China execution-pack consolidation

The former duplicate lowercase lineage has been retired after its richer/unique content was moved into the canonical uppercase pack.

| Retired active-tree path | Current replacement | Reason / preservation |
|---|---|---|
| `master-standards-stack/china-execution-pack/README.md` | `master-standards-stack/CHINA_EXECUTION_PACK/00_README.md` | Rich current README moved into sole canonical pack |
| `.../00_MASTER_CHINA_EXECUTION_MODEL.md` | `CHINA_EXECUTION_PACK/00_MASTER_CHINA_EXECUTION_MODEL.md` | Same richer current content promoted |
| `.../01_CHINA_HOD_RACI.md` | `CHINA_EXECUTION_PACK/01_CHINA_HOD_RACI.md` | Rich HOD/RACI retained |
| `.../02_RULE_PRECEDENCE_ENGINE.md` | `CHINA_EXECUTION_PACK/02_RULE_PRECEDENCE_ENGINE.md` | Rich rule-precedence model retained |
| `.../03_shipment_workflow_EVENT_CATALOGUE.md` | `CHINA_EXECUTION_PACK/03_shipment_workflow_EVENT_CATALOGUE.md` | Full event catalogue retained |
| `.../04_FACTORY_SYSTEM_API_CONTRACTS.md` | `CHINA_EXECUTION_PACK/04_FACTORY_SYSTEM_API_CONTRACTS.md` | Full factory contract retained |
| `.../05_SMART_GLASS_AUDIT_SPEC.md` | `CHINA_EXECUTION_PACK/05_SMART_GLASS_AUDIT_SPEC.md` | Full smart-glass spec retained |
| `.../06_PORT_OFFICER_UI_WORKFLOW.md` | `CHINA_EXECUTION_PACK/06_PORT_OFFICER_UI_WORKFLOW.md` | Full port workflow retained |
| `.../07_CRYPTOGRAPHIC_TRUST_ANCHOR_ARCHITECTURE.md` | `CHINA_EXECUTION_PACK/07_CRYPTOGRAPHIC_TRUST_ANCHOR_ARCHITECTURE.md` | Full cryptographic architecture retained |
| `.../08_CHINA_PILOT_shipment_workflow_GCC_RELEASE_PLAYBOOK.md` | `CHINA_EXECUTION_PACK/08_CHINA_PILOT_shipment_workflow_GCC_RELEASE_PLAYBOOK.md` | Full China→GCC playbook retained |
| `.../api/ahtE-factory-openapi.yaml` | `CHINA_EXECUTION_PACK/api/ahtE-factory-openapi.yaml` | API contract retained |
| `.../api/china-food-security-lab-openapi-extension.yaml` | `CHINA_EXECUTION_PACK/api/china-food-security-lab-openapi-extension.yaml` | Lab API contract retained |
| `.../schemas/*.schema.json` | `CHINA_EXECUTION_PACK/schemas/*.schema.json` | Execution schemas retained |
| `.../data/*.csv` | `CHINA_EXECUTION_PACK/data/*.csv` | Implementation registers retained |
| `master-standards-stack/china-execution-pack/CANONICAL_POINTER.md` | `NOTICE.md` + this register | Duplicate-lineage pointer no longer needed after physical consolidation |

The following shorter competing files in the uppercase pack were retired because their richer replacements now control:

| Retired path | Replacement |
|---|---|
| `master-standards-stack/CHINA_EXECUTION_PACK/01_DEPARTMENT_RACI.md` | `01_CHINA_HOD_RACI.md` |
| `master-standards-stack/CHINA_EXECUTION_PACK/05_SMART_GLASS_AUDIT_SPECIFICATION.md` | `05_SMART_GLASS_AUDIT_SPEC.md` |
| `master-standards-stack/CHINA_EXECUTION_PACK/08_CHINA_shipment_workflow001_GCC_RELEASE_PLAYBOOK.md` | `08_CHINA_PILOT_shipment_workflow_GCC_RELEASE_PLAYBOOK.md` |

Retained canonical upper-pack assets not replaced by the lowercase lineage include `09_MASTER_STANDARDS_FULL_MATRIX.md` and `10_MACHINE_READABLE_EXECUTION_PACK.json`.

## 3. China laboratory / traceability profile consolidation

| Retired path | Replacement | Reason |
|---|---|---|
| `partners/china-food-security-lab/AHTE_JAKIM_INTEGRATION_PROFILE_2026-09-26.md` | `partners/china-food-security-lab/AHTE_CHINA_LAB_TRACEABILITY_INTEGRATION_PROFILE_2026-09-30.md` | Consolidated lab + traceability + direct JAKIM topology, predictive/preemptive and Command Center details |
| `partners/china-food-security-lab/DIRECT_JAKIM_API_ALIGNMENT_ADDENDUM_2026-09-30.md` | same consolidated 30-Sep profile | Addendum content merged into single current artifact |

The current partner README points only to the consolidated profile and the canonical uppercase OpenAPI path.

## 4. Website specification consolidation

| Retired path | Replacement | Reason |
|---|---|---|
| `docs/WEBSITE_REBUILD_MASTER_SPEC_2026-09-30.md` | `docs/WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md` | v1 was only a supersession pointer; v2+ is current and carries the full target architecture |

Git history preserves the v1 pointer and earlier website architecture.

## 5. Explicitly retained historical / controlled material

The following classes are **not** to be deleted merely because newer project architecture exists:

- `master-standards-stack/verified-2026-09-17/` — frozen verified package;
- source-ingestion manifests and source provenance records;
- historical repository/readiness/completion/reconciliation audits;
- executed or source-evidentiary instruments;
- quarantine records required to explain damaged/retired source assets;
- historical mission packs where needed for audit lineage and clearly labelled as historical;
- Git history of all retired artifacts.

## 6. Current controlling architecture after retirement

The active implementation chain is governed by:

1. `master-standards-stack/verified-2026-09-17/` within its frozen scope;
2. current authority/source registries for normative claims;
3. `IQ300_DOCTRINE.md` + decision/schema/machine registries;
4. `CURRENT_TARGET_ARCHITECTURE_2026-09-30.md`;
5. `current-target-architecture-2026-09-30.json`;
6. `PLATFORM_REQUIREMENTS_TRACEABILITY_2026-09-30.md`;
7. `IMPLEMENTATION_COMPLETENESS_RULE_2026-09-30.md`;
8. current domain specifications including Command Center, canonical China pack, consolidated lab/traceability, Sinotrans, ports, finance and website/Codex.

## 7. Post-retirement validation requirement

Before this consolidation is merged into `main`:

- repository integrity validation must pass;
- AHTE runtime/reference tests must pass;
- gateway/OPA verification must pass where triggered;
- no tracked file under `master-standards-stack/verified-2026-09-17/` may change;
- active current docs must not point to deleted paths;
- no current implementation document may reintroduce the lowercase China execution-pack lineage.
