# MEMORANDUM OF AGREEMENT — TRACEABILITY PLATFORM INTEGRATION (TEMPLATE)

**Status:** TEMPLATE — not executed  
**Ref:** MOA-NICFS-TRACE-2026-DRAFT-01

Between

**GLOBAL HALAL SUPPLY CHAIN LIMITED** (HK, No. 79801544) (“GHSC”)

and

**[LEGAL NAME OF PLATFORM OPERATOR]** (“Platform”)  
Product name on deck: one-item-one-code / micro-dot / VOID / H5  
Code namespace owner: ______________

---

## 1. Purpose

Define how a **China-origin physical identity layer** (item or lot code) can sit **beside** a GHSC lot ID so a later auditor can see both, without treating the China platform as a Halal authority.

## 2. In scope

2.1 Mapping table: Platform item/lot code ↔ GHSC lot ID ↔ SSCC.  
2.2 Event types Platform will export: commission, bind, ship, exception, unbind.  
2.3 Export channel that is not WeChat-only (file, SFTP, or API — tick in Annex B).  
2.4 Rules for damaged-label unbind / replace so the tree does not silently fork.

## 3. Out of scope

Laboratory methods (lab MoA). Warehouse operation. Consumer insurance products unless Annex C says the policy is assignable to the importer.

## 4. Authority firewall

Guobanfa citations and Hengqin demonstration language describe **China food-safety / anti-counterfeit policy**. They do not move JAKIM, JSM, SFDA or GSO competence. A scanned H5 badge is not SPHM.

## 5. IP and namespace

Each Party keeps pre-existing IP. Platform keeps its code namespace. GHSC keeps AmanahGraph object IDs. Joint schema changes need written approval.

## 6. Security

No production keys in email. Staging first. Either Party may suspend a feed on a written security notice.

## 7. Commercials

Platform licence / per-code fees in Annex C only. No exclusivity unless Annex C is signed — and English/Chinese must match.

## 8. Term / character / law

Two years. Binding: confidentiality, IP, security, publicity, HK law.

## Annexes

- Annex A — field dictionary (Platform field → GHSC field)  
- Annex B — interface (endpoint / file layout)  
- Annex C — fees

## Signatures

For Platform  
Name: __________  Title: __________  Date: __________  Chop:

For GHSC  
Name: __________  Title: __________  Date: __________  Chop:
