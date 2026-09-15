# 02 — CHINA ↔ MALAYSIA ↔ GCC RULE-PRECEDENCE ENGINE

## 1. Purpose

The engine resolves which requirement applies to a specific entity, product, process, shipment, location and event. It prevents contradictory instructions from being collapsed into one generic compliance rule.

## 2. Rule classes

`R0 Shariah/Fatwa/authoritative religious determination`

`R1 Mandatory law/regulation/competent-authority decision in the applicable jurisdiction`

`R2 Official certification/protocol/circular/technical authority instrument`

`R3 Malaysian Standard / destination technical standard / recognised conformity rule`

`R4 Contractual corridor requirement approved by programme governance`

`R5 Internal SOP / operational control`

`R6 Advisory or optimisation logic`

A lower-number class cannot be used to nullify a higher-number authoritative requirement. Jurisdictional applicability is evaluated before precedence.

## 3. Applicability dimensions

Every rule carries:

- `jurisdiction`: CHN | MYS | GCC-SAUDI | GCC-UAE | GCC-OTHER | INTERNATIONAL
- `authority_type`
- `instrument_id`
- `effective_from`, `effective_to`
- `object_type`: organisation, facility, material, product, process, lot, shipment, container, warehouse, retail, person, data
- `activity`: manufacture, test, pack, store, transport, export, import, release, sale, recall
- `origin`, `transit`, `destination`
- `market_scope`
- `product_scope`
- `exceptions`

## 4. Resolution algorithm

1. Identify the controlled object.
2. Determine physical location and transaction location.
3. Determine origin, transit and destination jurisdictions.
4. Identify the market/authority decision being sought.
5. Retrieve active rules whose scope matches the object and activity.
6. Partition rules into jurisdictional sets.
7. Apply mandatory legal/authority rules for the jurisdiction in which the activity occurs.
8. Apply destination import/market-entry requirements to the destination transaction.
9. Apply Malaysian/JAKIM requirements where Malaysia certification, Malaysian authority activity, Malaysian-issued evidence or a Malaysia-governed assurance step is involved.
10. Apply China requirements for China-located manufacture, data handling, export and factory operations.
11. Apply contractual corridor rules only where they do not conflict with mandatory requirements.
12. Resolve conflicts by: specific-over-general, current-over-superseded, explicit-product-scope-over-generic, destination-admission-over-private-release, authority-issued-over-internal.
13. Produce `APPLIES`, `APPLIES_WITH_ADDITIONAL_CONTROL`, `NOT_APPLICABLE`, or `ESCALATE_TO_AUTHORITY`.
14. Store the resolution as an immutable rule-decision object attached to the affected event.

## 5. Example — China factory / GCC destination

**Factory production in China:** China law/regulation + applicable local industrial/product controls + agreed halal controls + applicable Malaysian/JAKIM evidence workflow.

**Shipment export from China:** China customs/export requirements + shipment identity/seal/custody controls.

**GCC import:** destination GCC authority/import requirements + customs/food/product controls + authenticated shipment and halal evidence presented according to destination rules.

**Retail in GCC:** destination market rules + importer/retailer controls + AHTE trust view + any approved customer contractual requirements.

## 6. Conflict handling

### Case A — internal SOP stricter than law
The stricter internal SOP may remain active if it is lawful and commercially accepted.

### Case B — destination requirement conflicts with origin operating practice
Destination admission controls win for the import transaction. The shipment remains blocked until the destination requirement is satisfied or the authority issues a determination.

### Case C — Malaysian evidence requested for a China-origin product
The engine records the Malaysian evidence pathway separately from China manufacture controls. It does not rewrite the Chinese manufacturing requirement.

### Case D — standard edition changes
The rule engine freezes the edition that governed the event. Future events use the new active edition when effective.

## 7. Data object

```json
{
  "rule_decision_id": "RD-CHN-MYS-GCC-000001",
  "controlled_object": "SHIPMENT-001",
  "activity": "IMPORT_RELEASE",
  "jurisdictions": ["CHN","MYS","GCC"],
  "rules_evaluated": ["R1","R2","R3","R4"],
  "decision": "APPLIES_WITH_ADDITIONAL_CONTROL",
  "controls": ["identity","seal","document","evidence","inspection"],
  "authority_route": "GCC_COMPETENT_AUTHORITY",
  "effective_at": "event-time",
  "evidence_refs": [],
  "decision_hash": "sha256:..."
}
```

## 8. Governance

The rule catalogue, authority registry and supersession table are controlled repositories. Any change to precedence logic requires regression tests against China factory, Malaysia assurance and GCC border scenarios.

## 9. Engine outputs

The engine returns: `RULE_SET`, `MANDATORY_CONTROLS`, `EVIDENCE_SET`, `AUTHORITY_GATE`, `DATA_HANDLING_POLICY`, `PHYSICAL_RELEASE_CONDITION`, and `EXCEPTION_ROUTE`.
