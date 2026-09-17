# 26 — GCC IMPORTER / BUYER ENGAGEMENT PROTOCOL 2026

## ARTIFACT METADATA
| Field | Value |
|---|---|
| Artifact | `26_GCC_IMPORTER_BUYER_ENGAGEMENT_PROTOCOL_2026.md` |
| Target folder | `deliverables/` |
| Control date | 17 September 2026 |
| Freeze boundary | `master-standards-stack/verified-2026-09-17/` |
| Status | Post-freeze pilot operating protocol |
| Commit message | `docs(deliverables): add 26 — GCC importer/buyer engagement protocol [DOCTRINE-CRITICAL]` |

[PILOT: Shipment 001 — importer/buyer engagement]

## 1. PURPOSE
Define the structured engagement protocol for GCC importers and buyers participating in the China → GCC direct corridor pilot. The protocol establishes evidence gates, authority boundaries and commercial qualification requirements.

## 2. SCOPE
Applies to GCC-based importers, distributors and buyers engaging with AHTE pilot manufacturers. Initial destination profiles: Saudi Arabia and UAE; other GCC markets require country-specific authority validation. Non-GCC markets are out of scope.

## 3. AUTHORITY BOUNDARY
- Importer/buyer acceptance does not create Halal certification.
- Destination import, customs, food-control and halal acceptance decisions remain with competent GCC authorities and the authorised importer process.
- No AI output, platform event, laboratory result or partner declaration creates official Halal certification or border release.

## 4. IMPORTER QUALIFICATION CHAIN
`Legal entity registration → applicable food/import trade licence → destination importer/product registration → halal acceptance criteria → product-category familiarity → commercial capability → storage/cold-chain capability where applicable → distribution network → financial capability → AHTE onboarding`

## 5. EVIDENCE GATES
| Gate | Owner | Evidence Required | Status |
|---|---|---|---|
| Importer legal registration | Importer | Trade licence, commercial registration | EXTERNAL-GATE |
| Import eligibility/registration | Importer + destination authority | Applicable importer account/licence and product/item registration | EXTERNAL-GATE |
| Halal acceptance criteria | Destination authority | Current product/certificate/issuer rules | EXTERNAL-GATE |
| Product category fit | Importer | Portfolio, channel and shelf-life capability | EXTERNAL-GATE |
| Commercial terms | Importer + project commercial layer | PO, price, payment terms, Incoterms | EXTERNAL-GATE |
| Logistics capability | Importer + Sinotrans/designated operator | Warehouse, receiving, cold chain where applicable | EXTERNAL-GATE |
| Financial capability | Importer | Credit/bank/commercial evidence as contractually required | EXTERNAL-GATE |

## 6. SAUDI ARABIA PROFILE
Before release for a Saudi transaction, verify at minimum:
- importer eligibility/account and applicable food item/product registration under current SFDA requirements;
- commercial registration/trade activity requirements applicable to the importer;
- product-specific halal certificate/slaughter-certificate requirements;
- Arabic/prepacked-food labelling requirements under current Saudi/GSO rules;
- Saudi Halal Center requirements where applicable;
- ZATCA/customs documentation and release controls.

No requirement is copied across product categories without current authority verification.

## 7. UAE PROFILE
Before release for a UAE transaction, verify at minimum:
- importer/legal entity and emirate-level food/import requirements applicable to the selected entry point;
- MoIAT Halal Products Control / registered halal certification body requirements where applicable;
- applicable UAE/GSO conformity and labelling requirements;
- UAE Customs/ICP and emirate-level customs procedures;
- product/food-authority registration and receiving requirements applicable to the exact SKU.

**Current-source correction:** ESMA is not treated as a current standalone authority. ESMA functions were merged into MoIAT. Federal customs reference uses UAE ICP, with emirate-level customs procedures still transaction-specific.

## 8. ENGAGEMENT SEQUENCE
1. Importer identification and screening.
2. Capability and compliance evidence collection.
3. Destination halal/product acceptance verification.
4. Commercial terms negotiation.
5. Logistics and receiving-process alignment.
6. AHTE onboarding.
7. Shipment 001 SKU/batch selection.
8. PO/order confirmation.
9. Shipment execution/custody tracking.
10. Border release and receiving verification.
11. Post-shipment review and corrective/improvement actions.

## 9. IMPORTER DATA-ROOM MINIMUM
`LegalEntityID; CR/trade licence; authorised signatory; importer/account identifiers; destination registrations; product-registration identifiers; warehouse/receiving sites; cold-chain capability if applicable; insurance/credit evidence as required; halal acceptance criteria; label/artwork approval evidence; buyer category/channel; commercial terms; PO/LOI; compliance contacts; escalation contacts.`

## 10. OPEN GATES
- specific importer identity per shipment;
- exact GCC destination/emirate/port;
- exact SKU/category;
- destination halal acceptance criteria;
- importer/product registration;
- commercial terms/PO;
- logistics route/receiving site;
- live border release/receipt.

## 11. CANONICAL PATH MAPPING
`Authority → destination instrument/requirement → applicability → importer/SKU control → evidence → audit/verification test → authority/customs gate → trust state → operational release`

## 12. AUTHORITY BOUNDARY AFFIRMATION
Importer participation strengthens operational capability but does not transfer or dilute sovereign authority. All external gates remain open until closed with transaction-appropriate evidence.
