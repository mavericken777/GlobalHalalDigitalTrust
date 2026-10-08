# National Food Safety (Hengqin) Innovation Center — laboratory evidence integration

**Named institution:** National Food Safety (Hengqin) Innovation Center under Chinese Academy of Agricultural Sciences, China.

The current controlling records are:

- [AHTE China laboratory + traceability integration profile](AHTE_CHINA_LAB_TRACEABILITY_INTEGRATION_PROFILE_2026-09-30.md)
- [Proposal OpenAPI for laboratory evidence](../../master-standards-stack/CHINA_EXECUTION_PACK/api/china-food-security-lab-openapi-extension.yaml)

The named laboratory institution contributes to the scientific-evidence workflow: controlled sampling, sample identity, chain of custody, method/QC, technical review, authorised signatory and signed report. The physical identity / item-level traceability / anti-counterfeit interface is a separate integration component unless an authoritative instrument confirms that it is operated by the same contracting entity.

The integration profile covers product/batch binding, unit→box→carton→pallet aggregation, consumer/channel verification, anti-diversion/scan analytics, evidence integrity, AHTE event ingestion, direct JAKIM API authority workflow and the GHSCL + authorised JAKIM Command Center.

Project authority topology:

`China laboratory evidence → AHTE ⇄ DIRECT JAKIM API ⇄ JAKIM → authorised human workflow → authority status → AHTE trust state`

**NOT_DETECTED ≠ HALAL.** Laboratory evidence, QR/microdot/VOID identity, AI output and cryptographic hashes are assurance/evidence infrastructure; they do not independently create Halal certification.

The contracting legal entity, registered site, current accreditation/method scope, contractual role, production API credentials, JAKIM production interface and destination acceptance remain controlled implementation/evidence inputs. Their absence must not remove the target capability: **FULL ARCHITECTURE NOW → REAL CONNECTORS WHEN AVAILABLE → NO REDESIGN REQUIRED.**
