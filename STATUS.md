# Platform overview

Updated: 2026-10-09

This repository contains the Global Halal Digital Trust target architecture and its reference software. It describes system capability and integration contracts; it does not issue Halal certification or replace a competent authority.

## Operating model

- Physical corridor: **China → GCC direct**.
- Authority connectivity: **AHTE ⇄ Direct JAKIM API ⇄ JAKIM**.
- Malaysia provides the governance, standards, assurance, and authority-connectivity plane unless a transaction explicitly scopes a physical movement.
- AI supports evidence review and risk analysis. Authorized humans and competent authorities retain decisions.
- Evidence is provenance-linked and integrity-protected; an integrity hash alone does not establish truth.

## Platform domains

The target platform covers manufacturer onboarding, current standards applicability, supplier and material traceability, laboratory evidence and custody, smart audit and corrective action, production monitoring, warehouse and transport custody, ports and customs interfaces, GCC receiving, retail verification, the 24/7 Command Center, and finance/Takaful integration contracts.

## Source and release practice

Use the current source-controlled standards register for normative applicability. The 17 September standards package remains a dated source reference; on 9 October 2026, project-specific transaction labels and trip-administration material were removed from the public repository at the owner's direction. Public repository content focuses on platform architecture and implementation interfaces. Agreements, signatory records, and private commercial negotiations are maintained outside this repository.

See the [repository guide](REPO_INDEX.md), [architecture](00_EXECUTIVE_COMMAND/CURRENT_TARGET_ARCHITECTURE_2026-09-30.md), and [standards register](master-standards-stack/iq300-all-jakim-ms/01_MASTER_STANDARDS_REGISTER.md).
