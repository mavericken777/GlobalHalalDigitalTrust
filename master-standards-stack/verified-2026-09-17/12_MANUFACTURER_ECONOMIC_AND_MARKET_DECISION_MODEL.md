# IQ300 Manufacturer Economic, Readiness and Market-Decision Model

**Control date:** 17 September 2026  
**Source basis:** user-supplied `market_validation.pdf`, reconciled with current official/public sources and the existing China -> GCC qualification dossier.

## 1. Purpose

The uploaded market report contains useful financial and operational decision structures but also mixes factual data, consultant estimates, scenario assumptions and broad market claims. This module keeps the structure and removes false precision.

The model answers:

1. Is the manufacturer operationally ready for halal certification/assurance work?
2. What does compliance actually cost for this site/SKU/scheme?
3. What market access or buyer value is evidenced rather than assumed?
4. What is the risk-adjusted commercial return?
5. What must be true before Shipment 001 can proceed?

---

# 2. Current macro context retained

## 2.1 Malaysia halal exports

Current HDC reporting states that Malaysia's halal exports reached **RM68.52 billion in 2025**, up **10.9% year-on-year**, representing about **4.3% of national exports**.

Source: `https://hdcglobal.com/about-hdc/`

This supports the proposition that halal is a material trade sector. It does not prove demand for a particular product or manufacturer.

## 2.2 Current foreign-body recognition context

JAKIM's current Malaysia Halal Council Secretariat profile states **78 recognised Foreign Halal Certification Bodies from 45 countries**.

Source: `https://www.islam.gov.my/en/sekretariat-majlis-halal-malaysia/profil?tmpl=component`

This replaces the uploaded report's `76 MRA partners` abstraction. FHCB recognition is not treated as blanket import approval or automatic foreign acceptance of a Malaysian certificate.

## 2.3 Approval-time context

JAKIM has publicly discussed a move from 30 to 23 working days as an efficiency target/study under ISPHM 2.0. The project does not use `23 days` as a guaranteed certification lead time.

Source: `https://www.islam.gov.my/ms/kenyataan-media/3917-kenyataan-media-ketua-pengarah-jabatan-kemajuan-islam-malaysia-berkenaan-pelaksanaan-inisiatif-segera-pensijilan-halal-malaysia-2-0`

---

# 3. Readiness model - evidence state, not arbitrary score

The uploaded report uses a 12-question numeric readiness score. IQ300 converts it into an evidence matrix.

| Readiness domain | Evidence required | State |
|---|---|---|
| operational history / current records | actual dated operational records required by current authority profile | `EVIDENCED/PARTIAL/NOT-EVIDENCED` |
| halal governance role | appointment + competence + authority | state |
| halal policy | approved/current/communicated | state |
| internal halal governance | applicable structure, terms, meetings/actions | state |
| raw-material control | complete material/supplier register and evidence | state |
| process/equipment segregation | site/process evidence | state |
| facilities/personnel requirements | scheme-specific site compliance | state |
| cleaning/sanitation/sertu readiness | approved procedures and records | state |
| HCP/risk control | risk/HCP register + monitoring | state |
| traceability/withdrawal | tested genealogy and exercise evidence | state |
| internal verification | current audit/NCR/CAR/re-verification | state |
| controlled records | version/retention/retrieval | state |

No fixed `READY at 10/12` rule is used. Readiness is a gate decision based on critical missing evidence and scheme-specific requirements.

---

# 4. Manufacturer cost stack

The uploaded report usefully identifies cost classes. IQ300 converts these into quote-backed budget objects.

## 4.1 Direct certification/regulatory costs

Fields:

`application/processing fee; scheme/scope fee; audit/inspection cost; laboratory/sampling cost; certificate/reissue/amendment cost; destination product-registration cost; destination halal/certification cost if applicable; translation/legalisation/document cost`.

**Rule:** populate only from current authority fee schedules, invoices or quotations. Do not use the uploaded PDF's generic fee table as a production budget.

## 4.2 Internal implementation costs

- Halal Executive / responsible-person staffing;
- governance/IHC time;
- training;
- system/manual/SOP development;
- document/evidence management;
- internal audit and corrective action;
- traceability/recall exercises;
- laboratory testing;
- calibration/monitoring equipment;
- facility/equipment segregation or retrofit;
- cleaning/sertu capability;
- supplier transition and qualification;
- label/artwork changes;
- IT/API/evidence integration.

## 4.3 China -> GCC market-entry costs

- China inland logistics;
- export documentation/handling;
- ocean/air freight;
- cargo insurance;
- destination port/terminal;
- customs broker/clearance;
- duty/tax;
- importer fees;
- product registration;
- Arabic/local label work;
- halal-document/certification cost where applicable;
- laboratory/inspection cost;
- warehousing/distribution;
- marketplace/retailer fees;
- promotion/launch allowance;
- returns/write-off;
- financing/FX.

## 4.4 Supplier-transition cost

The uploaded report correctly highlights supplier transition as a hidden cost. The project budgets it bottom-up:

`Supplier count -> high-risk materials -> missing evidence -> alternative sourcing -> sample/qualification -> audit/test -> reformulation/validation -> obsolete-stock disposition -> new MOQ/price -> document/change-control effort`.

No universal `30-50% buffer` is assumed. A contingency may be added only as a management planning parameter.

---

# 5. Commercial-value model

Certification is not treated as creating revenue automatically.

## 5.1 Evidence classes for commercial value

### E1 - market existence

Evidence that the product category is sold in the target market.

### E2 - buyer interest

Importer/distributor/retailer requests samples, catalogue, quotation or compliance documents.

### E3 - buyer validation

Buyer confirms pack, price band, registration path and commercial fit.

### E4 - commercial commitment

LOI, trial order, PO, distribution agreement or other documented commitment.

### E5 - realised value

Actual orders, revenue, gross margin and repeat purchase.

Only E4/E5 can support committed revenue forecasts. E1-E3 are pipeline evidence.

---

# 6. NPV and payback model

The uploaded report's NPV framework is retained but all values are variable.

## 6.1 Cash-flow structure

For period `t`:

`Incremental gross contribution_t = verified incremental revenue_t x gross margin_t`

`Net cash flow_t = incremental gross contribution_t - compliance cost_t - market-entry cost_t - financing/FX cost_t - incremental operating cost_t`

`NPV = sum(Net cash flow_t / (1 + discount rate)^t)`

`Payback = first period cumulative discounted/un-discounted cash flow turns positive`, depending on the project's selected policy.

## 6.2 Revenue attribution rule

Incremental revenue is counted as halal/certification-enabled only when a causal basis exists, such as:

- buyer explicitly required the credential;
- market entry was previously blocked without the credential;
- tender/specification required it;
- a new channel accepted the product because the compliance package was completed;
- controlled A/B/channel data supports the lift.

Generic percentage uplifts from the uploaded report are `MODEL-ASSUMPTION` only.

---

# 7. Scenario analysis

The uploaded report's scenario methodology is retained with project-specific inputs.

## 7.1 Core scenarios

- `NO-MARKET-LIFT`: certification is achieved but no incremental orders are won;
- `BASE-PIPELINE`: only evidenced buyer pipeline converts at conservative probability;
- `BUYER-CONFIRMED`: commercial terms/volume are documented;
- `DELAY`: certification/registration/logistics take longer than plan;
- `COST-OVERRUN`: supplier/retrofit/testing costs exceed budget;
- `REGULATORY-CHANGE`: destination or standards requirement changes;
- `SUPPLY-DISRUPTION`: critical supplier or logistics failure;
- `UPSIDE`: additional buyer/channel orders won after successful pilot.

Probabilities are management inputs, not report-derived facts.

## 7.2 Sensitivity variables

Rank sensitivity by actual model effect across:

- buyer volume;
- selling price;
- gross margin;
- compliance setup cost;
- recurring compliance cost;
- supplier transition;
- freight/logistics;
- FX;
- registration/certification lead time;
- working capital;
- incentive/grant approval;
- returns/write-off;
- repeat-order rate.

---

# 8. Funding and incentives due-diligence model

The uploaded report lists HRD Corp, MATRADE, MIDA, Islamic financing and technology grants. These are retained only as **candidate funding channels**.

For each programme store:

`ProgrammeID -> issuing body -> official current URL -> eligible company/activity -> eligible cost -> maximum support -> pre-approval requirement -> application window -> evidence -> claim timing -> approval state -> amount actually approved`.

No fixed claim percentage or grant ceiling from the uploaded PDF is used without current programme verification.

Potential bodies to monitor:

- HRD Corp;
- MATRADE;
- MIDA;
- HDC and current halal-industry programmes;
- Islamic banks/financiers;
- relevant state economic/halal programmes;
- technology/digitalisation grants that match the actual applicant.

---

# 9. Supplier and partner commercial-risk register

## 9.1 Supplier risks

- halal certificate expiry/status change;
- undisclosed formulation/source/sub-supplier change;
- high-risk material substitution;
- capacity/MOQ shift;
- quality or lab failure;
- shipment-document inconsistency;
- legal-entity/site mismatch;
- fraud/counterfeit evidence.

## 9.2 Logistics risks

- wrong container/vehicle condition;
- mixed-load/segregation breach;
- seal discrepancy;
- temperature/condition excursion;
- custody gap;
- unqualified subcontractor;
- destination hold or missing document.

## 9.3 Commercial risks

- no buyer after certification;
- buyer price below landed-cost threshold;
- importer margin makes shelf price uncompetitive;
- registration delay;
- product label/claim rejection;
- insufficient remaining shelf life;
- payment/credit risk;
- concentration in a single buyer/distributor.

Each risk stores `likelihood`, `impact`, `evidence`, `owner`, `mitigation`, `trigger`, `residual risk` and `review date`.

---

# 10. China -> GCC Shipment 001 commercial gate

Shipment 001 shall not be selected on generic category popularity or modelled ROI. The chosen SKU must simultaneously satisfy:

1. legal/factory identity verified;
2. exact SKU/formula evidence complete;
3. current halal certificate/issuer/scope verified as applicable;
4. destination country regulatory path confirmed;
5. importer/customer confirmed;
6. label/artwork acceptable;
7. full landed-cost model complete;
8. buyer price/margin/volume documented;
9. MOQ and production lead time acceptable;
10. batch traceability demonstrated;
11. logistics route qualified;
12. documentary/port requirements complete;
13. commercial downside remains acceptable under sensitivity analysis.

---

# 11. Manufacturer decision record

Each candidate/SKU gets a decision memo with no opaque ranking:

`Evidence status -> unresolved compliance gaps -> buyer evidence -> landed economics -> cash requirement -> time-to-market -> sensitivity -> critical risks -> next gate -> accountable decision owner`.

Possible operational states:

`DISCOVERED -> EVIDENCE-REQUESTED -> TECHNICALLY-QUALIFIED -> REGULATORY-QUALIFIED -> BUYER-VALIDATED -> ECONOMICS-VALIDATED -> PILOT-APPROVED -> SHIPMENT-001-ELIGIBLE`.

---

# 12. What was deliberately not imported from the PDF as fact

- universal 8-15% or other revenue-lift assumptions;
- fixed 6-18 month payback claims;
- fixed consultant/salary/retrofit/software cost bands;
- automatic MRA-driven re-certification savings;
- blanket mandatory-certification claims for whole countries/industries;
- fixed readiness-score bands as certification predictions;
- fixed incentive capture rates;
- fixed scenario probabilities;
- market-demand labels such as `GREEN/AMBER` as an investment verdict.

These remain optional scenario inputs only when management explicitly adopts and documents them.

# 13. Completion state

This module closes the commercial-analysis gap between the repository's compliance/manufacturer qualification system and a financeable Shipment 001 decision. It converts the useful framework in the uploaded market report into a source-controlled economic model that requires real quotations, buyer evidence and regulatory facts before a transaction is approved.