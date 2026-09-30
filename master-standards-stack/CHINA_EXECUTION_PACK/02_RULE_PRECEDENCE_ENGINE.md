# 02 — China ↔ Malaysia ↔ GCC Rule-Precedence Engine

## 1. Purpose

The rule-precedence engine determines which obligations apply to a product, facility, shipment, data flow or operational event when multiple jurisdictions, authorities, standards and contracts are involved.

It is a **resolution engine**, not a replacement for legal or competent-authority interpretation.

## 2. Rule layers

| Priority | Rule layer | Typical examples | Engine treatment |
|---|---|---|---|
| P0 | Sovereign law / constitutionally valid mandatory law | China laws, GCC national law, customs law, data law | Non-overridable for activity inside jurisdiction |
| P1 | Mandatory implementing regulation / compulsory technical requirement | Mandatory Chinese standards, GCC technical regulations, customs requirements | Non-overridable within scope |
| P2 | Competent-authority orders / official certification instruments | JAKIM/JAIN instruments, SFDA/MoIAT authority requirements, port directives | Authority-scoped; explicit effective date |
| P3 | Applicable voluntary/sector standards adopted by mandate | Malaysian MS standards, Chinese recommended standards, GSO/UAE/Saudi standards | Applied when scope/contract/certification programme makes them applicable |
| P4 | Contract / commercial specification | Buyer specification, logistics SLA, importer requirement | Adds obligations; cannot cancel P0–P2 |
| P5 | AHTE control policy | Internal risk control, evidence retention, trust threshold | Operationalises higher-level requirements |
| P6 | Optimisation / AI recommendation | Suggested test, additional sampling, route anomaly | Advisory unless accepted through workflow |

## 3. Jurisdiction rule

A rule is first filtered by:

`ACTIVITY_LOCATION + DATA_LOCATION + PRODUCT_DESTINATION + ACTOR_JURISDICTION + CONTRACT_SCOPE`

Examples:

- A factory data rule may be governed by China requirements because the processing occurs in China.
- A Saudi import documentation requirement applies when the shipment is destined for Saudi Arabia and falls within its commodity/import scope.
- A UAE Halal National Mark workflow applies where the product/service/production system seeks that UAE conformity mark.
- A Malaysian Halal standard becomes an AHTE assurance requirement where the project scope adopts it and where its use is applicable to the product/process.

## 4. Resolution algorithm

```text
INPUT: transaction/object/event
        ↓
IDENTIFY JURISDICTIONS
        ↓
LOAD ACTIVE RULE SETS
        ↓
FILTER BY SCOPE
        ↓
FILTER BY EFFECTIVE DATE
        ↓
CLASSIFY RULE TYPE
        ↓
APPLY PRECEDENCE
        ↓
DETECT CONFLICTS
        ↓
IF COMPATIBLE → COMPOSE
IF ADDITIVE     → APPLY ALL
IF CONFLICTING  → ESCALATE TO RULE OWNER
        ↓
CREATE ResolvedRequirementSet
        ↓
BIND CONTROL / HCP / EVIDENCE / AUTHORITY GATE
```

## 5. Compatibility logic

### Compatible
Two rules can both be executed without contradiction.

**Action:** compose both into the control set.

### Additive
A lower-priority rule adds a stricter control without violating a higher-priority rule.

**Action:** apply the stricter compatible requirement and preserve both provenance records.

### Conflicting
Two active rules require mutually inconsistent actions.

**Action:** do not silently choose. Create `RULE-CONFLICT` with:

- Rule IDs.
- Jurisdictions.
- Source hierarchy.
- Effective dates.
- Contradiction description.
- Object scope.
- Responsible rule owners.
- Interim containment.
- Required authority/legal resolution.

## 6. Malaysia integration

Malaysia requirements should be represented as a first-class source family alongside China and GCC requirements. For halal-specific controls, the source lineage includes:

`MS 1500:2019; MS 2400-1/-2/-3:2019; MS 2424:2019; MS 2634:2019; MS 2636:2019; MS 2738:2023; MS 2803:2025; MS 2809:2025; MS 2810:2025; MS 2393:2023; MS 2627:2017; MS 2627-2:2025; MS 1900:2025; MS 2691:2021; MS 2610:2015 supporting context`, plus applicable JAKIM/JAIN governance instruments, MPPHM/MHMS, protocols, circulars, fatwa and regulatory requirements already represented in the AHTE knowledge layer.

## 7. GCC destination rule packs

### Saudi Arabia
The destination rule pack must evaluate:

- importer registration;
- product registration where required;
- Saudi technical regulations/standards applicable to the product;
- certificate of origin;
- halal documentation where required;
- slaughter documentation for meat/poultry where required;
- destination customs requirements;
- warehouse/market-release requirements.

SFDA states that imported food must meet KSA requirements and that a halal certificate may be required depending on the product; its current halal-centre workflow includes eligibility review, audit and decision-committee issuance. citeturn848971search1turn848971search0

### UAE
The destination rule pack must evaluate:

- applicable product conformity requirements;
- Halal National Mark conditions where sought/applicable;
- registered/accepted halal certification-body interfaces;
- conformity documentation;
- customs/import requirements;
- destination storage and market-release controls.

MoIAT describes a digital application, document submission, field assessment and digital licence process for national conformity marks, including the Halal National Mark; it also maintains a registration route for halal certification bodies. citeturn848971search2turn848971search12

## 8. Data rule precedence

For data crossing the China border, apply a separate data rule engine:

```text
DATA CLASSIFICATION
  ↓
PERSONAL INFORMATION?
  ↓
IMPORTANT DATA?
  ↓
CRITICAL-INFRASTRUCTURE CONTEXT?
  ↓
DATA-CROSS-BORDER MECHANISM
  ↓
TRANSFER PURPOSE / NECESSITY
  ↓
RECIPIENT / CONTRACT / SECURITY CONTROLS
  ↓
APPROVAL / FILING / ASSESSMENT AS APPLICABLE
  ↓
ALLOW / RESTRICT / RETAIN DOMESTICALLY
```

The 2024 CAC provisions state that certain international trade, cross-border transport and multinational manufacturing data transfers can be exempt from specified data-export procedures when they contain neither personal information nor important data. Personal-information exports remain subject to applicable mechanisms and assessments. citeturn164534search0turn164534search1

## 9. Rule object

```json
{
  "RuleID": "RULE-CN-CUSTOMS-001",
  "Jurisdiction": "CN",
  "Authority": "GACC_OR_APPLICABLE_LOCAL_AUTHORITY",
  "SourceType": "LAW|REGULATION|MANDATORY_STANDARD|AUTHORITY_INSTRUMENT|STANDARD|CONTRACT|AHTE_POLICY",
  "SourceReference": "...",
  "Version": "...",
  "EffectiveFrom": "...",
  "EffectiveTo": null,
  "Scope": {"commodity":[],"activity":[],"destination":[],"dataClass":[]},
  "Priority": "P0",
  "Requirement": "...",
  "ControlBindings": [],
  "EvidenceBindings": [],
  "AuthorityGate": null,
  "ConflictRoute": "..."
}
```

## 10. Resolved requirement object

```json
{
  "ResolvedRequirementSetID": "RRS-SHP001-0001",
  "ObjectID": "SHIP-001",
  "ApplicableRules": ["..."],
  "SupersededRules": [],
  "Conflicts": [],
  "Controls": ["..."],
  "HCPs": ["..."],
  "EvidenceRequirements": ["..."],
  "AuthorityGates": ["..."],
  "DecisionOwner": "...",
  "EffectiveAt": "..."
}
```

## 11. Prohibited engine behaviour

- Never overwrite a higher-priority mandatory rule with a lower-priority project rule.
- Never infer destination admission from origin compliance alone.
- Never infer halal status from a laboratory result alone.
- Never infer authority approval from a generated QR/NFC/RFID identifier.
- Never silently downgrade a requirement because a factory system cannot implement it.
- Never export data merely because another system requests it; first resolve data-classification and transfer rules.

## 12. Decision trace

Every resolved rule set must be explainable through:

`Object → Rule candidates → Scope filters → Precedence → Compatibility → Conflict handling → Final requirements → Control bindings → Authority gate`.

This decision trace becomes evidence for audits of the AHTE rules engine itself.
