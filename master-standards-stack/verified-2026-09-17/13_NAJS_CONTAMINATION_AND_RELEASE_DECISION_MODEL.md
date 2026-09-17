# IQ300 Najs, Contamination and Release Decision Model

**Control date:** 17 September 2026  
**Source basis:** user-supplied `compliance_manual.pdf`, reconciled with the canonical JAKIM/MS source hierarchy, MS 1500/MS 2393 terminology layers, MHMS/MPPHM controls and the existing sertu module.  
**Authority boundary:** this is an operational decision-support model. It does not replace current fatwa, JAKIM/JAIN/MAIN determination or licensed normative text.

## 1. Purpose

The uploaded compliance manual contains useful cross-cutting material on `najs`, contamination, sertu and halal eligibility. This module converts that material into a controlled event/decision architecture without promoting disputed secondary wording as authority text.

Canonical path:

`Trigger -> substance/source identity -> affected object/scope -> contamination classification -> source rule -> immediate containment -> required cleansing/disposition -> evidence -> re-verification -> authority gate -> release/reject`.

## 2. Controlled terminology

AHTE maintains current terminology objects for the three commonly used najs classes:

- `MUGHALLAZAH` - severe category, including pig/dog-origin contamination under the applicable Malaysian Shariah/halal framework;
- `MUTAWASSITAH` - intermediate/general impurity category where the applicable rule requires removal/cleansing but not the mughallazah sertu procedure;
- `MUKHAFFAFAH` - light category under the applicable definition/rule.

Exact definitions, examples and treatment conditions are sourced from the current authoritative terminology/halal instrument. The uploaded PDF is `SECONDARY-REFERENCE`; it does not override licensed MS 2393/MS 1500 or competent-authority interpretation.

## 3. Contamination event object

Minimum fields:

`EventID; date/time; organisation; site; zone; asset/equipment/vehicle/container; product/batch/lot; material/substance; source/supplier; suspected species/origin; contact mechanism; physical state; quantity/extent; discovery method; reporter; evidence IDs; photographs/video; sample IDs; affected downstream objects; source instrument/version; preliminary class; competent reviewer; decision; disposition; NCR/CAR; release authority`.

## 4. Immediate containment rule

Any credible halal-integrity contamination/doubt event opens a controlled state:

`NORMAL -> HOLD -> SCOPE-IDENTIFIED -> CLASSIFIED -> CONTROL-EXECUTED -> RE-VERIFIED -> RELEASED / REJECTED / QUARANTINED / RECALLED`.

No automatic release occurs while:

- the contaminant/source is unidentified;
- affected lots/assets are unknown;
- the applicable cleansing/disposition rule is unresolved;
- required sertu/cleaning has not been completed;
- required authority review is pending;
- traceability cannot prove the blast radius.

## 5. Decision dimensions

The classification engine tests:

1. substance/material identity;
2. species/origin where relevant;
3. halal/haram/najs status under the current rule;
4. direct contact vs proximity/no contact;
5. wet/dry/contact-transfer conditions where legally relevant;
6. food-contact/process-contact status;
7. product/material exposure;
8. shared-equipment/line history;
9. downstream distribution exposure;
10. current source rule and authority interpretation.

Where facts are insufficient the state is `DOUBT / SYUBHAH-REVIEW`, not `HALAL`.

## 6. Halal eligibility control family

The uploaded manual presents a multi-condition halal eligibility test. IQ300 represents this as control families rather than freezing a secondary-source numeric checklist:

- ingredient/material permissibility;
- absence/control of najs contamination;
- animal species and slaughter provenance where applicable;
- processing-aid/enzyme/media provenance;
- equipment/utensil/process integrity;
- segregation from non-halal/najs exposure;
- safety/wholesomeness/legal compliance where applicable;
- packaging/storage/transport/display integrity;
- competent-authority certification/claim conditions.

The exact legal/normative formulation is loaded from the governing current source profile.

## 7. Cleaning versus sertu

`CLEANING` and `SERTU` are separate controlled procedures.

- ordinary sanitation cannot close a mughallazah-triggered sertu event;
- a completed sertu record cannot be inferred from a generic cleaning log;
- laboratory `not detected` evidence does not retroactively erase a prescribed cleansing requirement;
- the affected scope, execution evidence and verification must be linked before release.

The detailed sertu lifecycle remains canonical in `04_SERTU_STUNNING_PROTOCOL_LINKAGE.md`.

## 8. Product and sector overlays

### Food - MS 1500

Apply material, equipment, processing, hygiene, storage/transport/display and sertu controls to the exact batch/process/asset scope.

### Transportation / Warehousing / Retail - MS 2400

Contamination can propagate across vehicle/container, loading equipment, warehouse zone, pallet/MHE, display/preparation equipment or custody handover. The 613 source-backed MS 2400 requirement objects remain controlling for numbered clauses.

### Pharmaceuticals - MS 2424

Assessment extends to API/excipient/process-aid/media/solvent/equipment/QC/packaging provenance and contamination controls.

### Cosmetics - MS 2634

Assessment extends to INCI/material source, animal-derived inputs, alcohol/fermentation route, applicators/brushes, shared equipment and packaging/contact materials.

### Consumable goods / animal-derived materials - MS 2738 / MS 2803

Species/source/provenance and downstream product/material exposure must remain traceable.

## 9. Evidence hierarchy

Preferred evidence order:

`authority/current normative source -> certificate/issuer record -> supplier/material specification -> process/batch/asset record -> physical observation -> sample/lab evidence -> secondary reference`.

Analytical evidence can support identity/contamination questions but cannot independently create halal certification status.

## 10. Digital events

Recommended events:

- `E-HALAL-INTEGRITY-DOUBT`
- `E-CONTAMINATION-SUSPECTED`
- `E-CONTAMINATION-CONFIRMED`
- `E-AFFECTED-SCOPE-IDENTIFIED`
- `E-ASSET-HOLD`
- `E-BATCH-QUARANTINE`
- `E-SERTU-REQUIRED`
- `E-CLEANING-REQUIRED`
- `E-SAMPLE-COLLECTED`
- `E-LAB-RESULT`
- `E-CAR-OPEN`
- `E-REVERIFICATION`
- `E-AUTHORITY-REVIEW`
- `E-ASSET-RELEASE`
- `E-BATCH-REJECT`
- `E-RECALL-OPEN`

## 11. Audit tests

Auditor verifies:

- incident trigger and timestamp;
- containment speed and affected scope;
- source/version used for classification;
- material/species/source evidence;
- traceability forward/backward;
- cleansing/sertu procedure and competence;
- execution records and witnesses;
- laboratory chain of custody if used;
- NCR/CAR/root cause;
- re-verification;
- release/reject authority.

## 12. Completion state

This module closes the cross-cutting `najs -> contamination -> cleansing/sertu -> re-verification -> release` gap exposed by the uploaded compliance manual while preserving source hierarchy and authority boundaries.
