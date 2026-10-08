# Repository guide

This repository contains the Global Halal Digital Trust architecture, reference platform, public website source, and implementation specifications.

## Start here

| Area | Controlling reference |
|---|---|
| Current platform architecture | [Target architecture](00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md) |
| Authority and trust doctrine | [IQ300 doctrine](00_EXECUTIVE_COMMAND/IQ300_DOCTRINE.md) |
| Current standards source map | [Master standards register](master-standards-stack/iq300-all-jakim-ms/01_MASTER_STANDARDS_REGISTER.md) |
| Public site | [Amanah / GHSCL website](https://mavericken777.github.io/Amanah/) |
| Website specification | [Website rebuild specification](docs/WEBSITE_REBUILD_MASTER_SPEC_v2_2026-09-30.md) |
| Runtime and implementation status | [Repository status](STATUS.md) |
| Partner-facing system roles | [Ecosystem roles](partners/README.md) |

## End-to-end operating path

```text
China origin → manufacturer and suppliers → standards and controls → laboratory evidence → human audit and corrective action → competent-authority decision → AHTE trust state → warehouse and logistics custody → ports and customs → GCC importer and receiving → distribution, retail, verification, and ongoing monitoring
```

The physical corridor is China → GCC direct. Malaysia is the governance, assurance, standards, and authority-connectivity plane unless a specific transaction defines otherwise.

## Repository layout

| Directory | Contents |
|---|---|
| `00_EXECUTIVE_COMMAND/` | Architecture, doctrine, registries, and schemas |
| `master-standards-stack/` | Standards references, control models, and China-to-GCC integration assets |
| `platform/` and `reference-runtime/` | Reference services, policy, and runtime components |
| `ghscl-website/` | Public site source and presentation assets |
| `partners/` | Public descriptions of target partner roles and interfaces |
| `deliverables/` | Platform and operating-model specifications |
| `docs/` | Website, architecture, and implementation references |

Public repository materials describe the platform and its interfaces. Commercial agreements, trip administration, signatory records, and private negotiations are managed outside this repository.
