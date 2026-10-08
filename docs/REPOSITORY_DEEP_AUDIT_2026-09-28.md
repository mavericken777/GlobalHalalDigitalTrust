# Repository-wide audit — 28 September 2026

## Scope and method

The baseline at GitHub `main` commit `c294c03e12e0b4a11daeefe0c83c3f7ec4f059ed` had **361 tracked files**. This correction adds three tracked files (the audit report and two tools), for **364 inventory entries**; the inventory artifact excludes itself to avoid recursive hashing. The [point-in-time inventory](repository-inventory-2026-09-28.json) records those paths, byte lengths and SHA-256 values, plus format checks where practical. This automated sweep inspects every tracked file's identity and readable format; it is **not** a human clause-by-clause reading of 231 Markdown documents or an external/independent audit. Markdown relative targets (128 links in the corrected tree) were checked against the worktree. Licensed standards, private bookings and third-party agreements are not embedded in the repo.

| Area | Inventory / evidence | Finding and action |
|---|---|---|
| Project governance and root docs | `README.md`, `STATUS.md`, `GOVERNANCE.md`, `ADOPTION.md`, `REPO_INDEX.md`, `NOTICE.md`, `AGENTS.md` | `REPO_INDEX.md` still said corrupt archives remain quarantined and `ADOPTION.md` lacked a current overlay for later MoU summaries/reference OPA. Updated both; preserved dated historical claims as history. Documented the escrow file's distinct SPDX header. |
| Executive control | `00_EXECUTIVE_COMMAND/` including 27-gate readiness register, source retirement, partner/instrument registries and historical audits | Structural status remains `NOT_TRAVEL_READY`; 27 evidence gates are not automatically closed. Historical 26/27 September audits retain their as-of findings. |
| Trip and partner packs | `CHINA_TRIP_2026/`, `partners/`, `03_ECOSYSTEM_PARTNERS/` | Ten controlled signing drafts are proposals; actual entity, signer, site, venue, booking and instrument evidence is external. The Sinotrans Oct 15 acceptance worksheet is prepared, not accepted. |
| Standards and licensed sources | `master-standards-stack/` | Two active landing pages still presented **613** derived MS 2400 objects and a **684** aggregate as current. Corrected to identify these as historical incomplete counts; current safe index has **628 clause/page locators** and no normative text. Frozen 17 September snapshot was not changed. |
| Reference code and schemas | `platform/`, `runtime/`, `schemas/`, `contracts/`, `circuits/` | Python compiles and structured JSON parses. These are reference/demo or specification assets; this sweep does not establish runtime behavior, deployment, smart-contract security or trusted setup. The Solidity sample carries `Apache-2.0` SPDX, distinct from the root MIT notice. |
| Automation and tools | `.github/workflows/`, `tools/`, `tests/` | Integrity workflow ran non-strict validation. Changed it to `--strict` and added local Markdown link validation. Validator now fails on a missing tracked file instead of silently skipping it. |
| Archives | Retired three corrupt legacy paths, remaining historical warehouse gzip and locator tarball | Current remaining gzip decodes and tarball opens with expected members. The source-held Platinum and Sinotrans ZIPs pass CRC but are not normative/production inputs. |

## Verification and limits

- `python tools/audit_repository_files.py` records the snapshot. JSON, gzip JSON, SVG, Python syntax, tar and CSV checks passed. YAML parsing passed in the local environment; CI's core integrity step does not require PyYAML.
- `python tools/check_local_links.py` found no missing relative Markdown targets in tracked documents.
- `python tools/validate_repository.py --strict` passes repository structural controls; `python -m unittest discover -s tests -p test_trip_controls.py` passes five readiness tests.
- The broader FastAPI/pytest/OPA/Compose suite could **not** be executed in this scratch runtime because `fastapi`, `pytest`, `opa` and `docker` are unavailable here. GitHub workflows define those dependency-installed checks; their results must be inspected independently. Python compilation is not an integration test.

## Remaining work that cannot be closed from repository edits

The [27 September execution-board snapshot](../CHINA_TRIP_2026/archive/execution-board-2026-09-27.md) recorded travel T01–T13/G01–G02, signing S01–S05/G03, demonstration/communications D01–D02 and production P01–P04. This paragraph describes that historical audit date; it is not current trip or software status.

The next repository change should be tied to a specific evidence record or tested implementation. It must not declare travel, certification, third-party endorsement or production release from document completeness.
