# Platinum Tier v2 Illustrated Edition — Delta / Diagram / Source Verification Audit

**Control date:** 2026-09-26  
**Source:** user-supplied `platinum_tier_v2_illustrated.pdf`  
**Pages:** 30  
**SHA-256:** `f3696b038f419c24b94eb0da62e967a345bd2c3c5b70e2ea9c9ceb513f7f3c7e`  
**Comparator source:** `platinum_tier_ms_master.pdf` SHA12 `4f1240560664` (43 pages)  
**Frozen comparator:** `master-standards-stack/verified-2026-09-17/`  
**Prior post-freeze package:** `master-standards-stack/verified-2026-09-26/`  
**Repository baseline inspected:** `main@073424900566e7c6a2d96b747473a36193005b03`

[PROPOSAL: ingest illustrated v2 as a post-freeze visual/candidate-control source — path point: Standard/Instrument -> Applicability -> Control -> Evidence -> Audit Test]

## 1. Executive determination

The illustrated edition is not a new authority instrument. It is a condensed visual derivative of the 43-page master with 30 process-flow diagrams and several additional derived operational statements embedded directly into diagrams.

The visual layer materially increases implementation risk because a diagram can make a secondary, historical, or context-specific statement look like a current universal rule. Therefore the visual edition must be governed more strictly than ordinary prose:

`DIAGRAM CLAIM -> SOURCE CLASSIFICATION -> SOURCE/VERSION CHECK -> APPLICABILITY -> CONTROL INTENT -> EVIDENCE -> AUTHORITY GATE`.

No diagram node, arrow, threshold, cadence, role qualification, release condition, or rejection branch is production-normative merely because it appears in a flowchart.

## 2. Structural delta vs 43-page master

The v2 edition compresses the 24-section master into 15 sections and 30 figures. It preserves the same broad standards universe but reorganises it into visual execution clusters:

- Figure 01 regulatory/document hierarchy;
- Figure 02 certification journey;
- Figures 03-05 food / sertu / IHCS-HAS;
- Figures 06-08 MS 2400 transport / warehouse / retail;
- Figures 09-10 pharmaceuticals / high-risk animal-derived materials;
- Figures 11-14 cosmetics / halal-built-in / medical-device / internal-audit cycle;
- Figures 15-16 consumable goods / MS 2803 HCP;
- Figures 17-18 porcine-DNA laboratory workflow / Ct decision tree;
- Figures 19-20 MS 1900 SCCP and Shariah-governance operating model;
- Figure 21 MS 2691 competency progression;
- Figures 22-24 MPPHM/MHMS/2026 amendment operationalisation;
- Figures 25-27 slaughter/stunning/imported-meat flows;
- Figures 28-30 NCR / audit-management-review / fatwa decision flows.

The diagram layer adds implementation assertions not safe to promote without source binding.

## 3. Internal source inconsistencies in v2

### 3.1 MS 2610 edition-year conflict

The cover metadata lists `MS 2610:2014`, while the body standards table lists `MS 2610:2015`.

The controlled IQ300 catalogue uses `MS 2610:2015`.

[OPEN GATE: SOURCE CONFLICT — V2-MS2610-YEAR — owner: Department of Standards Malaysia — blocking: illustrated-source metadata accuracy]

Repository action: do **not** alter the controlled catalogue from the cover typo. Record the inconsistency as a source-quality defect.

### 3.2 “Verbatim” / “live-crawl verified” overclaim

The v2 title/source language describes the visual corpus as “Verbatim Standards” and “live-crawl verified”, while the document itself incorporates derived diagrams, secondary Taqyid/al-Barakah material, academic sources, old MS 1500:2009 stunning parameters and author-generated acceptance criteria.

Repository action: classify v2 as mixed-source compiled visual evidence, not authority-issued normative text.

## 4. Live verification performed 2026-09-26

The controlled live-source registry was consulted before crawl.

### 4.1 JAKIM 2026 amendment search

A live search restricted to `islam.gov.my` for the claimed `Pekeliling Pensijilan Halal Malaysia Bilangan 1 Tahun 2026` / `Pindaan MPPHM 2020` returned no official indexed result in this session.

[OPEN GATE: PRIMARY SOURCE FOR MPPHM 2020 PINDAAN 2026 — owner: JAKIM — blocking: exact amendment text, effective date, scope and applicability]

### 4.2 Department of Standards Malaysia MySOL

The official MySOL NSC 09 catalogue endpoint returned HTTP 200 and currently exposes, among others:

- MS 1900:2025 — 2nd Revision;
- MS 2627-2:2025 — Original;
- MS 2803:2025 — Original;
- MS 2809:2025 — Original;
- MS 2810:2025 — Original;
- MS 2393:2023 — 1st Revision;
- MS 2738:2023 — Original;
- MS 2691:2021 — Original;
- MS 2400-3:2019 (BM) — 1st Confirmation / confirmed 2024;
- MS 1500:2004 — withdrawn.

This independently supports the existing repository status/revision architecture for those items. Catalogue metadata remains advisory for edition/status discovery and does not substitute for licensed normative clauses.

[LIVE CRAWL: https://mysol.jsm.gov.my/search-catalogue?is-advance=1&sector=204&page=1 — 2026-09-26 — Department of Standards Malaysia — advisory — hash12: NOT_CAPTURED — method: live scrape — connector: Firecrawl — status: HTTP 200]

## 5. Figure-by-figure adjudication

| Fig. | Subject | Adjudication | Required repository treatment |
|---:|---|---|---|
| 01 | Five-layer regulatory pyramid | Conceptually useful; mixes constitutional/statutory/technical/operational layers and adds universal 2-year/annual-surveillance output | Keep as architecture inspiration only; source-lock cadence/validity |
| 02 | Certification journey | High-risk derived flow; hard-codes 14-day review, 2+2 audit days, 14-day CAPA, 3-month records, branch executive, 2-year validity, annual surveillance | Candidate workflow only; all timing/cadence nodes source-locked |
| 03 | Food manufacturing | Useful process topology; `PCR swab high-risk`, `Ct >=40 negative`, `dedicated truck`, `pre-wash + PCR` are not universal MS 1500 rules | Split process intent from analytical/logistics profiles |
| 04 | Sertu | Core 7-wash concept aligns with controlled architecture; officer-signature/release form and exact operational witness path require authority procedure applicability | Keep lifecycle; source-bind witness/release roles |
| 05 | IHCS/HAS | Correct high-level profile separation; `JKHD min 3`, annual audit, 2-year validity, annual surveillance are not automatically universal from the available primary sources | Retain profile distinction; source-lock numbers/cadence |
| 06 | Transportation | Process model useful; Muslim-driver, PCR-swab-negative, fixed dedicated/shared logic, pre-wash certificate conditions may be over-generalised | Candidate controls; bind to MS 2400 requirement objects and operator profile |
| 07 | Warehousing | Useful receiving/quarantine/storage topology; any fixed spacing, PCR, dedicated-bay or release criteria must be source-bound | Candidate WMS control flow |
| 08 | Retail | Useful retail receiving/display/withdrawal topology; do not universalise lab/segregation details | Candidate retail flow |
| 09 | Pharmaceuticals | Useful material-approval topology; animal-derived ingredient decision must remain product/material/source specific | Evidence/support flow only |
| 10 | Gelatin/insulin/heparin | High-risk jurisprudential/material provenance tree; cannot replace fatwa/NPRA/JAKIM determination | HITM escalation flow only |
| 11 | Cosmetics | Material decision tree useful; alcohol/GMO/animal-derived branches need exact clause/fatwa applicability | Candidate control flow |
| 12 | Halal-Built-In | Project implementation method, not Malaysian Standard certification rule | [PROPOSAL] transformation architecture |
| 13 | Medical devices | Useful QMS/halal overlay; MS ISO 13485 and MS 2636 responsibilities must be separately applicable | Candidate integrated QMS flow |
| 14 | Annual self-inspection | Annual cadence is not automatically proven by the displayed clause reference | Source-lock frequency |
| 15 | Consumable goods | Useful flow; relationship to MS 2738 is consistent at catalogue level | Candidate sector flow |
| 16 | MS 2803 HCP | Useful HCP methodology concept; not every depicted step/frequency is necessarily verbatim | Candidate HCP process |
| 17 | Lab workflow | Useful evidence lifecycle; labs/methods/sample custody require accreditation/method scope | Evidence-only workflow |
| 18 | Ct decision tree | Exact Ct cut-offs / re-extraction logic are method/lab validation dependent | [SOURCE-LOCKED] analytical thresholds |
| 19 | MS 1900 SCCP | SCCP concept consistent with public MySOL scope; quarterly SAC review / >=1-year records not established by live catalogue | Source-lock cadence/retention |
| 20 | SAC + Shariah Officer | High-risk derived governance model: >=3 members incl. mufti, full-time Muslim, HPB certification, 24h reporting, quarterly review | [SOURCE-LOCKED] unless licensed MS 1900/current authority source establishes each element |
| 21 | MS 2691 ladder | General competency architecture useful; mandatory branch coverage derives from unverified 2026 amendment claim | Keep competency context; source-lock branch mandate |
| 22 | HAS vs IHCS | High-level distinction retained; records >=3 years, 2-year validity, annual surveillance remain blocked | Candidate decision tree only |
| 23 | Raw material masterlist | Strong operational evidence concept; 30-day reminder and specific NCR classification/notification timing are derived | [PROPOSAL] configurable control, not normative constant |
| 24 | Halal Executive branch coverage | Entire branch/qualification/training cadence depends materially on unresolved 2026 primary source | [SOURCE-LOCKED] / OPEN GATE |
| 25 | Slaughter | Process topology useful; embeds old numerical stunning values from MS 1500:2009 | Preserve rule precedence; do not promote historical settings as current MS 1500:2019 |
| 26 | Stunning parameters | Explicitly sourced to MS 1500:2009 Table A1; historical parameters must not be relabelled current MS 1500:2019 requirements | Historical/versioned reference only |
| 27 | Imported meat approval | Conceptual DVS/JAKIM/port sequence useful; actual establishment, recognition and import release require live authority evidence | Candidate authority workflow |
| 28 | NCR | Good CAPA topology; 14-day closure, KECIL/BESAR handling and 3-year retention need primary authority source | Source-lock exact deadlines/classification |
| 29 | Annual audit/review | General improvement loop useful; annual/quarterly cadence claims require exact source | Configurable audit workflow |
| 30 | Fatwa decision tree | Correctly signals escalation, but visual must not imply AHTE/SAC can create fatwa; gazettement/applicability varies | HITM/authority escalation only |

## 6. Highest-risk visual claims

### 6.1 Historical stunning settings represented in current flow

Figures 25-26 use numerical parameters explicitly labelled `MS 1500:2009 Table A1` while the current food standard in the project is MS 1500:2019 and the freeze already states that old 2009 slaughter/stunning settings must not be back-ported as current numbered MS 1500:2019 requirements.

Repository rule remains:

`current law/fatwa -> current JAKIM/DVS protocol/instruction -> MPPHM annex/guidance -> MS 1500:2019 -> validated facility SOP/settings`.

[SOURCE-LOCKED: v2 stunning numerical parameters for current use — required: current JAKIM/DVS authority source and facility applicability]

### 6.2 Laboratory thresholds embedded as binary gates

Figure 03 includes `PCR Ct >=40 = negative`; Figure 18 embeds Ct cut-offs and re-extraction loops. These are not safe universal Halal-release gates.

Required engine rule:

`LAB METHOD + MATRIX + VALIDATION + CONTROLS + RESULT -> ANALYTICAL EVIDENCE`, never `Ct -> HALAL`.

### 6.3 Governance cadence and composition embedded as facts

Figures 19-20 hard-code quarterly SAC review, >=3 members including a mufti/equivalent, full-time Muslim Shariah executive, HPB certification, 24-hour deviation reporting and periodic management review.

The official MySOL catalogue confirms MS 1900:2025 is a generic Shariah-based QMS standard; the live catalogue did not establish those exact diagram constants.

[SOURCE-LOCKED: v2 MS1900 governance constants — required: licensed MS 1900:2025/current competent-source clauses]

### 6.4 2026 amendment-dependent workflow

Figures 02, 21-24 and 28 repeatedly operationalise the claimed 2026 amendment as settled primary law. The official JAKIM source was not retrieved in this session.

Repository must continue to block these nodes from production policy.

## 7. Positive architecture value from v2

The visual edition is valuable in four bounded ways:

1. **Visual control design:** swimlane separation of actor, control, evidence, decision and release.
2. **HITM interface design:** clear places where machine detection should hand off to Halal Executive, JKHD/SAC, auditor, laboratory or competent authority.
3. **Evidence UX:** visualises raw-material records, batch records, seal/custody, audit evidence, CAPA and lab reports.
4. **Training / process-flow atlas:** the 30 diagrams can seed a controlled infographic library once each node is source-tagged.

[PROPOSAL: convert the 30 diagrams into source-tagged AHTE infographic specifications — path point: Control -> Evidence -> Audit Test]

## 8. Required diagram governance schema

Every future diagram node should carry machine-readable metadata:

```json
{
  "node_id": "FIGXX-NNN",
  "claim_type": "normative|derived|historical|proposal|evidence|authority_action",
  "source_id": "...",
  "source_version": "...",
  "clause": "...",
  "applicability": "...",
  "effective_date": "...",
  "jurisdiction": "...",
  "control_id": "...",
  "evidence_required": [],
  "authority_gate": "...",
  "status": "VERIFIED|SOURCE_LOCKED|PROPOSAL|HISTORICAL",
  "supersedes": null
}
```

Rendering must visually distinguish normative, historical, proposal and source-locked nodes.

## 9. Repository changes required by this audit

1. Add a versioned post-freeze `verified-2026-09-26-v2/` package rather than overwrite the prior 26 September package.
2. Add a 30-figure machine-readable risk/adjudication register.
3. Update `POST_FREEZE_VERIFICATION.md` so the illustrated package is the latest delta while `verified-2026-09-17/` remains frozen doctrine.
4. Update repository status with the v2 source fingerprint and major open gates.
5. Do not alter the 17-standard controlled catalogue from the v2 cover's `MS 2610:2014` typo.
6. Do not alter runtime OPA thresholds or authority logic from v2 diagrams.
7. Preserve the prior post-freeze package as predecessor/superseded-by relationship, not deletion.

## 10. Canonical path mapping

The v2 visual corpus is only usable through:

`Authority -> Standard/Instrument -> Clause/Requirement -> Applicability -> Control -> HCP/SCCP -> Evidence -> Audit Test -> Finding -> Corrective Action -> Re-verification -> Authority Gate -> Trust State -> Operational Release`.

The most important missing step in many diagrams is **Applicability**. The most dangerous compressed step is **Authority Gate**.

## 11. Final adjudication

The illustrated edition is a stronger **training, interface, process-modelling and gap-discovery artifact** than the master PDF, but a weaker standalone normative source because it compresses context and turns prose into deterministic-looking flow logic.

Adopt the visuals only as source-tagged candidate controls and evidence flows. Reject direct diagram-to-policy compilation until every material node is source/version/applicability bound.
