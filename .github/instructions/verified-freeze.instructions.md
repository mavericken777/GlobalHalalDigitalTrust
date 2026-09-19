---
applyTo: "master-standards-stack/verified-2026-09-17/**/*"
---

# Verified Package Immutability Instructions

- Artifact: `.github/instructions/verified-freeze.instructions.md`
- Revision: `v1.0.0`
- Control date: `2026-09-19`
- Suggested commit: `docs(agent): protect verified standards snapshot [DOCTRINE-CRITICAL]`

The matched path is the controlled standards snapshot dated 17 September 2026,
declared in `master-standards-stack/verified-2026-09-17/00_README.md` and
indexed by `master-standards-stack/verified-2026-09-17/MANIFEST.json`.

**16 content modules (`00`–`15`) + `MANIFEST.json`.**

Treat all matched files as immutable.

Do not edit, overwrite, rename, move or delete a matched artifact.

If a correction is required:

1. preserve the frozen artifact unchanged;
2. create a versioned post-freeze correction or successor artifact outside the
   snapshot;
3. identify the original artifact and exact conflict;
4. apply `[PROPOSAL]`, `[SOURCE-LOCKED]` or `[OPEN GATE]` as applicable;
5. use `[FREEZE-UPDATE]` only when an authorized new verified-date snapshot is
   being created;
6. preserve a complete supersession and source-provenance trail.

Reading, auditing, validating hashes and linking to the frozen artifacts are
permitted.

Copying unavailable licensed normative wording into another path is prohibited.

Note: licensed MS 2400-1:2019, MS 2400-2:2019 and MS 2400-3:2019 source copies
are held as project corpus (613 numbered requirement objects total). Their
clause structure is source-verified; their full normative text must not be
reproduced into public-facing artifacts.
