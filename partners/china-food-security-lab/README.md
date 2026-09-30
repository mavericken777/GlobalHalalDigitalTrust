# China laboratory + traceability integration

The current controlling integration profile is:

- [`AHTE_CHINA_LAB_TRACEABILITY_INTEGRATION_PROFILE_2026-09-30.md`](AHTE_CHINA_LAB_TRACEABILITY_INTEGRATION_PROFILE_2026-09-30.md)
- canonical proposal OpenAPI: [`../../master-standards-stack/CHINA_EXECUTION_PACK/api/china-food-security-lab-openapi-extension.yaml`](../../master-standards-stack/CHINA_EXECUTION_PACK/api/china-food-security-lab-openapi-extension.yaml)

The China-side system is treated as a **physical identity + item-level traceability + anti-counterfeit + laboratory evidence production plane** feeding AHTE. The consolidated profile covers one-item-one-code, microdot/QR/VOID physical identity, product/batch binding, unit→box→carton→pallet aggregation, consumer/channel verification, anti-diversion/scan analytics, controlled sampling, laboratory chain of custody, method/QC, signed results, evidence integrity, AI/ML predictive/preemptive assurance, direct JAKIM API connectivity and 24/7 GHSCL + authorised JAKIM Command Center monitoring.

Project authority topology:

`China lab/traceability evidence → AHTE ⇄ DIRECT JAKIM API ⇄ JAKIM → PHC + JAKIM authorised human workflow → authority status → AHTE trust state`

**NOT DETECTED ≠ HALAL.** Laboratory evidence, QR/microdot/VOID identity, AI output and cryptographic hashes are assurance/evidence infrastructure; they do not independently create Halal certification.

Exact laboratory legal entity/site, current accreditation/method scope, contractual role, production API credentials, JAKIM production interface and destination acceptance remain controlled implementation/evidence inputs. Their absence must not remove the target capability: **FULL ARCHITECTURE NOW → REAL CONNECTORS WHEN AVAILABLE → NO REDESIGN REQUIRED.**

The earlier split 26 September profile and 30 September direct-API addendum have been superseded by the consolidated profile and are retired from the active tree; Git history retains their provenance.