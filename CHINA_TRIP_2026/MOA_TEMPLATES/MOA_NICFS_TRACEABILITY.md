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

Guobanfa citations and Hengqin demonstration language describe **China food-safety / anti-counterfeit policy**. They do not confer Malaysian or destination certification or regulatory powers. JSM and GSO provide standards functions; they are not interchangeable with shipment-release authorities. A scanned H5 badge is not SPHM.

## 5. IP and namespace

Each Party keeps pre-existing IP. Platform keeps its code namespace. GHSC keeps AmanahGraph object IDs. Joint schema changes need written approval.

## 6. Security

No production keys in email. Staging first. Either Party may suspend a feed on a written security notice.

## 7. Commercials

Platform licence / per-code fees in Annex C only. No exclusivity unless Annex C is signed — and English/Chinese must match.

## 8. Term / character / law

Two years. Non-binding except Schedule D.

## Annexes

- Annex A — field dictionary (Platform field → GHSC field)
- Annex B — interface (endpoint / file layout)
- Annex C — fees

## Signatures

For Platform
Name: __________  Title: __________  Date: __________  Chop:

For GHSC
Name: __________  Title: __________  Date: __________  Chop:


Version: 1.1 · Control date: 2026-09-27 · Artifact: `CHINA_TRIP_2026/MOA_TEMPLATES/MOA_NICFS_TRACEABILITY.md`.
Supersedes the 2026-09-26 working draft where inconsistent.
Commit: `fix(mission): reconcile signing and readiness controls [EVIDENCE-UPDATE]`.
[PROPOSAL: trip preparation — path point: Control / Evidence / Authority Gate]

**DRAFT FOR REVIEW — NOT SIGNING READY.** Schedule D below controls legal-character conflicts. The [signing matrix](../SIGNING_MATRIX.md) preserves the intended parties and scope.

<!-- COMMON_TERMS_START -->
## Schedule D — common protective terms (proposed)

D1. **Legal character and precedence.** The cooperation, service, procurement, volume, price and exclusivity proposals are non-binding unless a separate executed schedule expressly makes identified obligations binding. Schedule D is intended to bind only when this instrument is validly executed by every named Party. It controls any inconsistent legal-character, publicity, confidentiality, notice or dispute wording elsewhere in this draft. Existing executed agreements remain unchanged unless an express written amendment is signed by every affected party. No partnership, agency, power to bind another Party, certification mandate or joint and several liability is created.

D2. **Confidential information.** Each recipient shall use non-public commercial, technical, customer, sample and operational information disclosed in connection with this instrument only to evaluate or perform the stated cooperation. It shall protect that information with reasonable care, restrict access to personnel and professional advisers who need it and owe equivalent confidentiality duties, and not disclose it externally without the discloser's written consent. Exceptions apply to information demonstrably public without breach, already lawfully held, independently developed or lawfully received without restriction. Legally compelled disclosure shall be limited to what is required, with advance notice where lawful. On request or termination, return or securely delete information, except required legal records and inaccessible routine backups, which remain protected. These obligations survive termination for three years; trade secrets remain protected while legally qualifying as such. This duration is a proposed commercial term, not a statement of mandatory law.

D3. **Publicity and marks.** No Party may publish another Party's name, logo, endorsement, customer identity or jointly branded announcement without prior written approval of the exact wording and artwork, except a legally required disclosure. No government mark, halal certificate, recognition or exclusivity may be represented as granted by this instrument. Accurate confidential evidence attribution does not permit promotional use.

D4. **Data, IP and security.** Each Party retains its existing IP; no implied licence or ownership transfer arises. Only information necessary for the agreed purpose may be shared. Before transferring personal data or restricted cross-border data, the Parties shall record purpose, lawful basis, applicable jurisdictions, controller/processor roles, authorised recipients, safeguards, retention and deletion in Annex B. Roles follow the actual processing and applicable law, not an assumed label. No production credentials may be placed in public repositories or messages. Notify affected Parties without undue delay after discovering a security incident; restrict affected access and cooperate on containment and legally required notifications. A feed may be suspended for a documented security or compliance risk. New IP, licences, development charges and service liability require a separately executed schedule.

D5. **Notices and term.** Complete a notices table for EVERY named Party before execution: exact legal name | registered address | authorised contact | email. Notices must be in writing to that email with acknowledgement or tracked delivery to that address; messaging-app discussions alone do not amend the instrument. The stated term starts on the last valid signature. Any Party may terminate on 30 days' written notice, without cancelling separate purchase orders or service agreements. Confidentiality, accrued rights, IP protections and dispute terms survive as applicable.

D6. **Law and disputes — proposed for counterparty review.** Hong Kong SAR law governs the binding provisions. The Parties shall first seek resolution through authorised representatives for 30 days after written notice, then submit disputes to the exclusive jurisdiction of the courts of Hong Kong SAR; urgent interim relief may be sought from a competent court. Any alternative law or arbitration arrangement must replace this clause expressly in the final agreed version; do not leave competing checkboxes. This is a drafting proposal, not an opinion on enforceability in any jurisdiction.

D7. **Execution and language.** Record each Party's full registered name, registration number, address, authorised signer's name/title, mandate reference, actual signature date and seal requirements. Do not backdate or fill an existing executed original unilaterally; use a jointly signed confirmation or amendment. The final bilingual instrument must identify its controlling language and resolve every discrepancy before signature. Amendments require all affected Parties' signatures. Attach and initial Annexes A/B; identify Annex C as separately executed or expressly not agreed. A blank identity, mandate, controlling language or required annex blocks signature.
<!-- COMMON_TERMS_END -->
