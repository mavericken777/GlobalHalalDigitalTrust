# IQ300 Sertu + Slaughter/Stunning Protocol Linkage

**Control date:** 17 September 2026  
**Purpose:** prevent cross-standard ambiguity by separating prescribed sertu controls, slaughter controls, stunning controls, laboratory evidence and authority decisions.

## 1. Sertu is a prescribed control, not a generic sanitation event

The AHTE event model treats sertu as a distinct governed lifecycle triggered by applicable `najs mughallazah` contamination or other competent-authority determination. Ordinary cleaning/sanitation records do not close a sertu-required event.

Canonical flow:

`CONTAMINATION / DOUBT -> IDENTIFY AFFECTED OBJECTS -> IMMEDIATE HOLD/ISOLATION -> CLASSIFY EVENT -> CONFIRM APPLICABLE SERTU SOURCE/RULE -> AUTHORISE PROCEDURE -> EXECUTE -> CAPTURE EVIDENCE -> COMPETENT VERIFICATION WHERE REQUIRED -> EFFECTIVENESS/COMPLETENESS CHECK -> RELEASE OR CONTINUE HOLD`.

## 2. Cross-standard sertu linkage

| Instrument | Sertu linkage in controlled source | IQ300 use |
|---|---|---|
| MPPHM 2020 | Procedure 58 / certification operating control | authority/certification procedure, escalation, evidence and release conditions |
| MHMS 2020 | HAS includes sertu as a management-system element | organisation must maintain controlled procedure, competence, records and review |
| MS 1500:2019 | Annex A sertu | food premises/equipment/process asset cleansing control |
| MS 2400-1:2019 | Annex D sertu; Clause 7 includes sertu control | transport vehicle/container/equipment/site event |
| MS 2400-2:2019 | sertu annex/control in warehousing standard | warehouse zone/equipment/material-handling asset event |
| MS 2400-3:2019 | sertu control/annex in retail standard | retail premise/equipment/utensil/display/preparation asset event |
| MS 2424:2019 | Annex A washing/sertu | pharmaceutical manufacturing/storage/equipment contamination event |
| MS 2634:2019 | Annex A sertu | cosmetics manufacturing/handling asset event |
| MS 2636:2019 | Annex A sertu | medical-device manufacturing/handling asset event |
| MS 2738:2023 | consumable-goods contamination/cleanliness control profile; exact annex detail remains source-locked in this snapshot | invoke current licensed text/authority instruction before claiming a numbered sertu annex |

## 3. Sertu event object

Minimum fields:

`SertuEventID; TriggerEventID; asset/site/vehicle/container/equipment/utensil/zone; product/batch exposure; contamination classification; source instrument + edition + clause/annex; authority/jurisdiction; opened_at; initiator; immediate containment; procedure version; approved materials; executor; competent supervisor/verifier where applicable; start/end timestamps; photographic/document evidence refs; affected-lot disposition; effectiveness/completeness decision; release authority; release timestamp; recurrence/root-cause link; NCR/CAR link`.

## 4. Sertu decision rules

1. A negative PCR/qPCR result does not cancel a prescribed sertu requirement.
2. A generic sanitation cycle is not relabelled as sertu after the fact.
3. A sertu event cannot close while affected product/assets remain unidentified.
4. Release requires the verification required by the governing rule/authority.
5. Cross-jurisdiction operations apply the controlling local/destination rule in addition to the source-country control profile; one jurisdiction's sertu record is not automatically a legal release in another jurisdiction.
6. AI may detect a trigger or evidence gap but cannot determine a religious/legal exception or override a competent authority.

## 5. Slaughter/stunning source precedence

The project shall not hard-code superseded MS 1500:2009 slaughter/stunning values as if they were current clauses of MS 1500:2019.

Controlled precedence:

`Current applicable law/fatwa -> current JAKIM/DVS Malaysian Protocol for Halal Meat and Poultry Production -> current MPPHM 2020 annex/guidance (including the stunning parameter guideline) -> MS 1500:2019 food requirements -> facility SOP/validated equipment settings -> batch/animal-line evidence`.

Where a destination jurisdiction imposes additional rules:

`Malaysia/JAKIM alignment profile + DESTINATION HALAL/FOOD/ANIMAL-WELFARE/IMPORT REQUIREMENTS -> stricter/applicable operational rule as determined by authorised compliance owner`.

## 6. Historical fatwa context versus production rule

JAKIM's published historical fatwa material records Malaysian positions on stunning methods, including prohibitions/restrictions on captive-bolt methods and conditional permissibility of specified electrical/waterbath and other methods where the animal is not killed by stunning and Shariah conditions are satisfied.

**Production rule:** historical fatwa summaries provide lineage and interpretive context; they do not replace the current Malaysian Protocol, MPPHM annex parameters, current fatwa/circulars or the settings approved for the specific species/equipment/facility.

No numerical stunning setting is stored as a production rule in this package unless it is verified against the current authoritative protocol/annex applicable to the transaction.

## 7. Slaughter/stunning HCP model

| HCP | Required control | Evidence | Failure state |
|---|---|---|---|
| Animal/species identity | permitted species and traceable lot | animal/lot/source records | HOLD |
| Animal condition | eligibility/welfare/health requirements | pre-slaughter inspection/status | HOLD |
| Slaughterer | competent/authorised Muslim slaughterer under applicable rule | identity/credential/shift record | LINE-HOLD |
| Equipment | approved maintained equipment and settings | equipment ID/calibration/maintenance | LINE-HOLD |
| Stunning method | method permitted by current authority profile | protocol/rule link; equipment configuration | LINE-HOLD |
| Stunning parameter | setting within currently approved/validated range | controller log/setting/verification | HOLD |
| Viability after stunning | animal not killed by stunning where rule requires | observation/test/line record | REJECT/HOLD |
| Slaughter act | required cut/action performed in accordance with Shariah/protocol | witness/line evidence | REJECT |
| Invocation/operational religious requirement | controlled according to applicable protocol | operator/process evidence | NCR/HOLD |
| Bleeding/death confirmation | process meets current protocol before downstream step | line monitoring | HOLD |
| Mechanical line exception control | manual intervention/reject route defined | exception log | HOLD |
| Segregation | halal line/carcass/product integrity preserved | tags/lot/zone/custody | QUARANTINE |
| Processing | post-slaughter process maintains identity/integrity | batch/process trace | QUARANTINE |
| Certification | recognised/competent halal evidence for exact facility/product/consignment as required | credential/consignment cert | RELEASE-BLOCK |

## 8. Protocol-linked data model

`SpeciesProfile -> MethodProfile -> ProtocolVersion -> EquipmentModel -> ApprovedSettingProfile -> FacilityValidation -> OperatorCompetence -> LineEvent -> Animal/LotOutcome -> Carcass/ProductBatch -> Certificate/Consignment -> Shipment`.

Settings are configuration data with effective dates, approving source and equipment/species scope. They are never embedded as timeless constants in software.

## 9. China -> GCC implications

For the project's direct China -> GCC corridor:

- JAKIM/MS alignment can be used as a high-integrity control architecture and as part of the project's trust framework.
- It does **not** by itself establish Saudi, UAE or other GCC import/halal acceptance.
- Saudi Arabia currently requires halal slaughter certification for meat, poultry and their products and applies SFDA importer/item registration and border-control requirements.
- UAE Halal product recognition is tied to the UAE Halal Products Control System, applicable UAE/GSO standards and registered halal certification bodies where required.
- Shipment 001 cannot use a generic manufacturer `Halal` logo as proof. The exact issuer, facility, product/SKU, validity, destination-recognition status and consignment requirements must be verified.

## 10. Digital enforcement

Critical events:

`E-CONTAMINATION-DETECTED; E-ASSET-HOLD; E-SERTU-OPEN; E-SERTU-PROCEDURE-VERIFIED; E-SERTU-EVIDENCE; E-SERTU-CLOSE; E-ASSET-RELEASE; E-STUN-PROFILE-LOAD; E-STUN-SETTING; E-STUN-EXCEPTION; E-SLAUGHTER-WITNESS; E-LINE-HOLD; E-BATCH-REJECT; E-AUTHORITY-VERIFY`.

Any unauthorised change to a stunning profile, sertu procedure or governing source creates `REGULATORY/PROCESS CONFIGURATION EXCEPTION` and blocks automatic release until re-authorised.