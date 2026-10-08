# IQ300 Attached PDF Deep-Dive, Reconciliation and Source-Adjudication Register

**Control date:** 17 September 2026  
**Purpose:** ingest useful material from the two user-supplied PDFs without allowing secondary-source errors, dated claims or model assumptions to overwrite source-verified standards/control objects.

## 1. Source corpus ingested

| Source | Pages | SHA-256 | Role in this repository |
|---|---:|---|---|
| `compliance_manual.pdf` | 74 | `3cd4d9ac0ba99adcff98be7860f2a008bd1c6cc31ec99a4069e9e5784f70dc10` | secondary compliance reference; useful for cross-cutting operational modules, clause-family discovery, audit-readiness ideas and source leads |
| `market_validation.pdf` | 48 | `5aeff302514c9486fe829f14dfd7d46c0633894a396628cfd43f3da6ff01e9cc` | secondary commercial/market framework; useful for economics, supplier-risk, readiness and scenario-analysis structures |

The PDFs are reference aids, not authoritative Malaysian Standards or regulator instruments. Their own disclaimers state that official/current standards govern in a conflict.

## 2. Overall assessment

### Strong material retained

The PDFs materially strengthen the project in five areas:

1. cross-cutting operating controls beyond single-standard clause maps;
2. internal governance, supplier control, document hierarchy and traceability concepts;
3. audit-closure and self-assessment structures;
4. cost/ROI/sensitivity frameworks for manufacturer decision support;
5. a structured distinction between compliance investment and commercial market activation.

### Material not accepted as authoritative

The PDFs contain multiple claims that are outdated, over-generalised, internally inconsistent or contradicted by project-held source documents. Those claims are therefore tagged `REJECTED-AS-CONTROL`, `SECONDARY-ONLY`, or `MODEL-ASSUMPTION` below.

---

# 3. Critical reconciliation findings

## 3.1 "14 active Malaysian Halal Standards" is outdated for the project operating set

Both PDFs repeatedly describe a 14-standard universe. The current project catalogue contains 17 standards/standard contexts, including additional current Halal-sector standards already verified in the Department of Standards Malaysia catalogue:

- MS 2636:2019 - Halal medical device - General requirements;
- MS 2809:2025 - Authentication of products using chemometric techniques;
- MS 2810:2025 - Consumable goods - Test method - Identification of pig skin and hair.

**Repository rule:** retain the 17-standard controlled catalogue. The PDFs are historical/secondary references, not the current catalogue authority.

## 3.2 The PDFs' MS 2400 clause maps are not authoritative and conflict with the project-held source PDFs

The compliance PDF presents MS 2400-1/-2/-3 using a generic management-system sequence such as:

`4 Management responsibility -> 5 Resource management -> 6 Halal product realisation -> 7 Measurement, analysis and improvement`.

The project-held licensed MS 2400 source files and the existing 613-object requirement matrix show a materially different 2019 structure:

`4 Requirements -> 5 Preliminary steps to enable halal risk management -> 6 Operations -> 7 Premises/infrastructure/facilities/personnel -> 8 Maintenance of halal supply chain`, with detailed subclauses for halal risk management, chain of custody, nonconformity, isolation/notification or withdrawal/recall, traceability, monitoring equipment, emergency preparedness and outsourced service providers.

**Decision:** `REJECTED-AS-CONTROL` for the PDF MS 2400 clause numbering/structure.  
**Authority inside this repo:** the 613 source-backed MS 2400 objects in `iq300-full-matrix/` plus the canonical source-backed control maps.

## 3.3 "76 mutual-recognition partners / MRAs" is the wrong control abstraction

The market PDF describes JAKIM as having "76 mutual-recognition partners" and models export access as if a JAKIM certificate automatically activates approximately 76 markets.

Current JAKIM public material instead uses the concept of **recognised Foreign Halal Certification Bodies (FHCBs)**. JAKIM's current Malaysia Halal Council Secretariat profile states that it recognises **78 FHCBs from 45 countries**. Recognition is a controlled status and does not mean one Malaysian certificate automatically satisfies every importing country's product, food, halal, customs, registration or labelling rules.

Official source: `https://www.islam.gov.my/en/sekretariat-majlis-halal-malaysia/profil?tmpl=component`

**Repository rule:** replace generic `MRA unlock` logic with jurisdiction-specific `destination acceptance / issuer recognition / importer / product registration / border` gates.

## 3.4 The 23-day approval figure is an aspiration, not a binding control

The market PDF reports `23 days` as a JAKIM target approval period. JAKIM's official 2023 ISPHM 2.0 statement describes 23 working days as a government suggestion to be studied and refined; it is not framed there as a universal binding certification SLA. An earlier JAKIM customer-charter page states 30 working days after certification-fee payment.

Official sources:

- `https://www.islam.gov.my/ms/kenyataan-media/3917-kenyataan-media-ketua-pengarah-jabatan-kemajuan-islam-malaysia-berkenaan-pelaksanaan-inisiatif-segera-pensijilan-halal-malaysia-2-0`
- `https://www.islam.gov.my/ms/e-penerbitan/18-info-korporat?start=10`

**Repository rule:** certification lead time is a case variable, not a fixed 23-day planning assumption.

## 3.5 MPPHM 2020 Pindaan 2026 exists as a current industry-reported amendment, but the primary circular must be source-frozen before production use

The PDFs rely heavily on `MPPHM 2020 Pindaan 2026`, including:

- MS 2738:2023 application to the consumable-goods scheme;
- three-month records for first-time applications;
- minimum three-year document retention;
- training/provider requirements;
- IHCS clarification.

Current secondary industry sources identify this as **Pekeliling Pensijilan Halal Malaysia Bilangan 1 Tahun 2026**, effective 1 April 2026. The current web verification pass found consistent secondary reporting but did not obtain the official circular text from an indexed JAKIM page.

**Repository state:** `SECONDARY-VERIFIED / PRIMARY-SOURCE-LOCK`.  
**Production rule:** acquire/archive the official circular and reconcile exact amendments before a live certification ruleset is frozen.

## 3.6 MYeHALAL remains the correct system reference

The compliance PDF uses `myHID` in its application workflow. Current JAKIM materials and the project's current operating layer use **MYeHALAL**. MyHALALINGREDIENTS has been integrated with MYeHALAL from 15 August 2025.

Official source: `https://www.islam.gov.my/en/media-statement/4798-kenyataan-media-jabatan-kemajuan-islam-malaysia-jakim-berkenaan-pelaksanaan-myhalalingredients`

**Decision:** do not introduce `myHID` as the current production system name.

## 3.7 Malaysia Halal e-Certificate remains verified

JAKIM introduced electronic SPHM certificates from 5 May 2025 for applications approved by the relevant JAKIM/MAIN/JAIN panel on or after that date.

Official source: `https://www.islam.gov.my/en/media-statement/4704-kenyataan-media-ketua-pengarah-jabatan-kemajuan-islam-malaysia-berkenaan-pelaksanaan-sijil-pengesahan-halal-malaysia-sphm-secara-elektronik-e-cert`

This confirms the repository's current digital-credential overlay.

## 3.8 MS 1500:2019 slaughtering deletion is confirmed

The official Standards Malaysia preview confirms that the 2019 revision deleted the old slaughtering clause and annex from MS 1500 and cancels/replaces MS 1500:2009.

Official source: Department of Standards Malaysia / MySOL preview for MS 1500:2019.

**Repository rule remains correct:** never hard-code old MS 1500:2009 stunning/slaughter values as current MS 1500:2019 clauses. Use current protocol/fatwa/authority instruments for operative slaughter/stunning parameters.

## 3.9 Current Standards Malaysia confirmation status strengthens the 2026 baseline

Standards Malaysia's current confirmation data shows, among others:

- MS 1500:2019 - confirmed 2024;
- MS 2400-1/-2/-3:2019 - confirmed 2024;
- MS 2634:2019 - confirmed 2025;
- MS 2424:2019 - confirmed 2025;
- MS 2636:2019 - confirmed 2025.

Official sources:

- `https://www.jsm.gov.my/en/about-us/statistics/standards-statistics/ms-confirmation`
- `https://mysol.jsm.gov.my/search-catalogue?keyword=halal`

## 3.10 MS 1900 bibliography inconsistency in the PDF

The compliance PDF body analyses MS 1900:2025, but its bibliography lists `MS 1900:2005`. Standards Malaysia's 2025 approval information identifies the current MS 1900 as the 2025 Shariah-based quality management system revision.

**Decision:** retain the repository's current `MS 1900:2025` control profile and treat the PDF bibliography entry as an error.

---

# 4. Market-report claim adjudication

## 4.1 Verified/current macro signal retained

Malaysia's 2025 halal exports reached **RM68.52 billion**, up **10.9% year-on-year**, according to current Halal Development Corporation reporting. This is a legitimate macro-context signal.

Official/current source: `https://hdcglobal.com/about-hdc/`

The project does not use this macro figure as proof that a particular China -> GCC SKU will sell.

## 4.2 2030 targets require source/version control

The PDF states a RM70 billion 2030 export target. Current MATRADE material has cited other policy targets, including RM75.2 billion and later 13th Malaysia Plan references to RM80 billion. Targets evolve.

**Repository rule:** store policy targets as dated `POLICY-TARGET` objects; never use them as timeless market facts.

## 4.3 ROI/payback figures are model assumptions, not validated market facts

The market PDF provides example values including:

- fixed initial and recurring compliance budgets;
- assumed revenue lifts;
- payback periods;
- three-year NPVs;
- 30-50% supplier-transition buffers;
- 25-35% incentive-capture assumptions;
- cost ranges for consultants, labour, retrofit, software and testing.

These are useful **scenario parameters**, but they are not sufficiently evidenced to become default project economics.

**Repository rule:** retain the model structure; replace every fixed value with a documented input, quotation, buyer forecast, actual payroll cost, laboratory quote, logistics quote or programme-specific grant approval.

## 4.4 "Mandatory for export" statements are overbroad

The market PDF states or implies blanket certification requirements for broad categories such as cosmetics/pharmaceuticals across Saudi Arabia, UAE, Indonesia or OIC markets.

**Decision:** `REJECTED-AS-GENERAL-RULE`. Every destination is resolved by exact jurisdiction, product category, ingredient composition, halal rule, importer/product registration and certification-body recognition/acceptance.

## 4.5 The export-value model based on automatic MRA savings is rejected

The PDF models re-certification savings as if foreign acceptance were automatic after JAKIM certification. This is not safe for transaction control.

**Repository rule:** destination acceptance is resolved per country and exact product/issuer/scope. Commercial modelling may include avoided certification cost only after the importer/regulator confirms that the Malaysian credential is accepted for that case.

## 4.6 Readiness scores are retained as workflow prompts, not regulatory scores

The 12-question readiness model is useful as an onboarding checklist. Its numeric score bands (`READY`, `PARTIAL`, etc.) are not JAKIM scores and are not treated as certification predictions.

The project therefore converts them into evidence states:

`EVIDENCED / PARTIAL / NOT-EVIDENCED / NOT-APPLICABLE`.

---

# 5. Useful operational material adopted from the PDFs

The following concepts are now explicitly retained as project control patterns, subject to the source-status caveats above.

## 5.1 Internal halal governance pattern

Useful governance fields:

`role -> appointment -> authority -> competence -> meeting -> decision -> action owner -> due date -> evidence -> closure`.

The PDF's proposed committee composition is treated as an implementation template, not as a universal mandatory composition unless the current authority instrument says so.

## 5.2 Document hierarchy

The PDF's five-level document model is useful and is adopted as a repository/data architecture:

1. policy;
2. manual/system description;
3. SOP/procedure;
4. work instruction/form/record;
5. external controlled source.

Every object requires owner, version, approval, effective date, supersession and retention rule.

## 5.3 Traceability and recall architecture

Useful retained pattern:

`raw-material lot -> supplier -> receipt -> batch/formula -> line/shift -> finished lot -> pallet/container -> customer/importer -> recall/withdrawal scope`.

The PDF's specific `24-hour` and `95%` mock-recall targets are **not** promoted as JAKIM requirements unless a controlling primary source is attached. They may be used as internal performance targets if management chooses.

## 5.4 Supplier risk controls

The PDF's supplier-risk concept is adopted using evidence-based tiers:

- `VERY-HIGH`: animal-derived, slaughter-sensitive, gelatin/collagen, high-risk enzyme/media/process-aid;
- `HIGH`: single-source critical ingredient, complex compound ingredient, fermentation route, high regulatory impact;
- `MEDIUM`: formulated ingredient with supplier/certificate/change risk;
- `LOW`: low-risk commodity with complete identity/specification evidence.

Frequency is not hard-coded from the PDF. Audit/verification frequency is set by risk, current authority requirement, incidents, supplier history and certificate/change events.

## 5.5 Economic validation architecture

The market PDF contributes a useful financial model structure:

`initial compliance cost + recurring compliance cost + supplier-transition cost + technology + testing + logistics/regulatory cost + financing/FX + market-activation cost` versus `verified incremental gross contribution`.

The decision engine calculates scenario NPV/payback only from actual project inputs.

## 5.6 Scenario analysis

The PDF's sensitivity model is retained conceptually. Critical variables include:

- revenue/volume actually won because of market access;
- gross margin;
- compliance setup/recurring cost;
- supplier transition;
- destination regulatory cost;
- logistics/freight;
- FX/finance;
- incentive/grant capture actually approved;
- time-to-market;
- certificate/registration renewal cost;
- recall/quality risk.

No assumed probability distribution or revenue-lift percentage is treated as fact.

---

# 6. Source quality policy created by this ingestion

Every imported statement from an external report receives one of these states:

- `PRIMARY-OFFICIAL-VERIFIED`
- `PROJECT-LICENSED-SOURCE-VERIFIED`
- `PRIMARY-COMMERCIAL-CLAIM`
- `SECONDARY-VERIFIED`
- `SECONDARY-ONLY`
- `MODEL-ASSUMPTION`
- `CONFLICTS-WITH-HIGHER-SOURCE`
- `REJECTED-AS-CONTROL`

Higher-ranked sources always override lower-ranked sources for production requirements.

# 7. Final ingestion decision

The two PDFs are valuable **secondary reference documents**, not replacements for the repository's current official/source-backed stack.

They have been used to add governance, traceability, supplier-risk, audit-closure and manufacturer-economics depth. Their outdated catalogue count, incorrect MS 2400 clause architecture, MRA framing, fixed ROI/payback claims, blanket export-mandatory statements and unsupported operational thresholds are explicitly prevented from contaminating production rules.