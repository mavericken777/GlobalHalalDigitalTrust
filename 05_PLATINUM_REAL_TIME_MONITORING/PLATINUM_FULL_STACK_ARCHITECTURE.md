# Platinum Tier — Full-Stack End-to-End Real-Time Halal/Tayyib Monitoring Architecture

## Artifact metadata

- Artifact: `05_PLATINUM_REAL_TIME_MONITORING/PLATINUM_FULL_STACK_ARCHITECTURE.md`
- Revision: `v2.0.0`
- Control date: `2026-09-30`
- Classification: post-freeze architecture artifact
- Freeze impact: none; `master-standards-stack/verified-2026-09-17/` remains immutable
- Authority effect: none
- Status: `[PROPOSAL]` where this revision records project-design assertions not yet backed by repository-native authority/technical instruments
- Supersession: this revision supersedes the earlier contents of this file where inconsistent

[PROPOSAL: closes end-to-end monitoring architecture gap — path point: Evidence → Audit Test → Authority Gate → Trust State → Operational Release]

## 1. Definition

**Platinum = complete end-to-end, real-time monitoring and evidence orchestration from verified raw-material origin through laboratory evidence, manufacturing, packaging, warehousing, transport, export, international transit, GCC import/receiving and downstream distribution, with every material evidence object integrity-anchored by an immutable cryptographic hash.**

AHTE provides continuous standards / evidence / trust intelligence across that chain.

Platinum does **not** itself determine Halal certification. Halal certification and other formal authority decisions remain with the competent authority under the applicable certification framework. AI, laboratory results, QR/NFC, blockchain/DLT, evidence hashes and platform trust states are decision-support and assurance mechanisms; none independently creates official Halal certification.

Core principle:

> **Verified provenance + authenticated evidence + chain of custody + immutable integrity anchoring + continuous monitoring + human/authority decision.**

A cryptographic hash proves integrity of the hashed object after creation; it does not by itself prove the truth, lawful authority or correctness of the underlying assertion.

## 2. Operating model

```text
MALAYSIAN HALAL ECOSYSTEM
        |
        +-- Perak Halal Corporation (PHC)
        |      Perak State Government GLC — halal industry local and global
        |
        +-- Global Halal Supply Chain Limited (Hong Kong)
               International operating + digital-infrastructure vehicle
                         |
                         v
                        AHTE
         Standards / Evidence / Trust Intelligence
                         |
       +-----------------+-----------------+
       |                 |                 |
 Manufacturers       Laboratories      Logistics / custody
 / producers             |                 |
       +-----------------+-----------------+
                         |
                 Continuous evidence
                         |
                 Immutable hash layer
                         |
                 Real-time monitoring
                         |
                    AI assistance
                         |
                 Authority interface
                         |
                 Human / authority gate
                         |
              China origin -> GCC destination
```

PHC, GHSCL, AHTE and the competent authority are separate roles. Corporate ownership, digital infrastructure, evidence generation and certification authority must not be collapsed into one function.

## 3. Complete source-to-destination chain

```text
CERTIFIED / VERIFIED RAW-MATERIAL ORIGIN
        |
        +-- source identity
        +-- supplier / producer identity
        +-- facility / farm / origin identity where applicable
        +-- raw-material identity
        +-- lot / batch identity
        +-- origin documentation / certification reference
        +-- timestamp + provenance
        |
        v
SAMPLE + CHAIN OF CUSTODY
        |
        +-- sample ID bound to source lot/batch
        +-- collector identity
        +-- collection time/location
        +-- seal / tamper record
        +-- transfer / receipt events
        |
        v
AUTHORIZED / QUALIFIED LABORATORY WORKFLOW
        |
        +-- lab identity
        +-- accession / sample receipt
        +-- test method
        +-- accreditation / authorization scope reference
        +-- result
        +-- analyst / system identity
        +-- signature / provenance
        +-- immutable evidence hash
        |
        v
RAW-MATERIAL RELEASE / HOLD / ESCALATION
        |
        v
MANUFACTURING / PROCESSING
        |
        +-- approved supplier / ingredient linkage
        +-- formula / BOM / input identity
        +-- production batch
        +-- facility / line / equipment
        +-- cleaning / segregation evidence
        +-- HCP / SCCP evidence where applicable
        +-- operator / timestamp / event provenance
        +-- exceptions / CAPA
        |
        v
PACKAGING / PRODUCT IDENTITY
        |
        +-- SKU / batch / lot
        +-- serialized ID / QR / NFC where used
        +-- packaging material evidence where applicable
        |
        v
WAREHOUSE
        |
        +-- receiving
        +-- segregation / storage controls
        +-- environmental telemetry where applicable
        +-- custody handover
        |
        v
TRANSPORT / LOGISTICS
        |
        +-- booking / pickup
        +-- vehicle / container identity
        +-- seal identity
        +-- route / geofence events
        +-- environmental telemetry where applicable
        +-- custody handovers
        |
        v
EXPORT / PORT / BORDER
        |
        +-- export documentation
        +-- container / seal status
        +-- customs / port event references
        |
        v
INTERNATIONAL TRANSIT
        |
        +-- custody
        +-- route
        +-- tamper / seal
        +-- telemetry / exceptions
        |
        v
GCC IMPORT / RECEIVING
        |
        +-- destination authority/importer requirements
        +-- receiving identity / timestamp
        +-- seal / condition check
        +-- exception disposition
        +-- importer confirmation
        |
        v
GCC DISTRIBUTION / RETAIL / AUTHORIZED CONSUMER VIEW
        |
        v
CURRENT TRUST STATE + DIGITAL PRODUCT PASSPORT / TRUST RECORD
```

## 4. Standards and requirements scope

AHTE must not be hard-coded around MS 2400 alone.

The applicability layer must map the **complete applicable Malaysian halal standards and operative certification instruments**, together with relevant authority requirements and destination-market requirements, into controls and evidence requirements.

Canonical path:

`Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release`

The standards/requirements engine and the trust engine are distinct:

- **Standards/requirements engine:** determines what requirement applies and what control/evidence is required.
- **Trust engine:** evaluates the current evidentiary state of the entity, product, batch, shipment, facility or transaction.

## 5. Evidence object integrity

Every material evidence object should be attributable, bound and integrity protected.

Minimum logical fields:

```json
{
  "evidence_id": "EV-...",
  "entity_id": "ENTITY-...",
  "shipment_id": "SHIPMENT-...",
  "batch_id": "BATCH-...",
  "material_id": "MATERIAL-...",
  "event_type": "...",
  "issuer": "...",
  "issuer_role": "...",
  "source_system": "...",
  "timestamp": "ISO-8601",
  "standard_or_requirement_reference": "...",
  "control_reference": "...",
  "payload_reference": "...",
  "content_hash": "...",
  "digital_signature_or_authentication_reference": "...",
  "verification_status": "...",
  "trust_state": "..."
}
```

The production implementation must use schemas registered under the repository schema registry; this example is architectural, not a replacement schema.

Integrity controls:

- authenticated evidence issuer;
- stable entity / product / batch / shipment binding;
- reliable timestamping;
- digital signature or equivalent authenticated provenance where available;
- cryptographic content hash;
- append-only / tamper-evident audit history;
- controlled correction and supersession rather than silent overwrite;
- role-based access and selective disclosure;
- sovereign storage / data-locality controls where required;
- independent verification of hash/signature at audit and destination review.

## 6. Laboratory-native evidence integration

The preferred laboratory architecture is API/system-native, not manual PDF upload as the primary control:

```text
AHTE sample ID
      -> sample collection + seal
      -> chain of custody
      -> laboratory receipt / accession
      -> laboratory method execution
      -> result generated
      -> authenticated laboratory evidence
      -> immutable hash
      -> AHTE evidence ingestion/reference
      -> trust-state update
```

Laboratory evidence remains within the laboratory's lawful competence and scope. `NOT DETECTED != HALAL` remains mandatory.

### Project-design assertion requiring external proof

The target architecture specifies a **China government laboratory endorsed/accepted by JAKIM for the intended workflow and scope**.

[SOURCE-LOCKED: JAKIM endorsement/acceptance of the China government laboratory — required: official JAKIM instrument or other competent-authority evidence identifying the laboratory and permitted scope]

[OPEN GATE: laboratory identity + endorsement + accreditation/method scope — owner: JAKIM / laboratory / applicable China authority — blocking: Evidence]

Until that instrument is repository-native, do not convert this target-state design into a verified authority claim.

## 7. JAKIM / competent-authority system connectivity

The target-state design specifies direct authority-system connectivity so authorised evidence/status can be visible in near-real-time or real-time according to the actual interface contract.

Preferred pattern:

```text
JAKIM / COMPETENT AUTHORITY
           ^  |
           |  v
       DIRECT JAKIM API
           ^  |
           |  v
          AHTE
           |
   origin / lab / factory /
 warehouse / logistics / GCC
```

The internal Direct JAKIM API adapter isolates authority connectivity from ordinary commercial applications. It is an implementation boundary, not an external intermediary or separate authority. The controlling topology is **AHTE ⇄ Direct JAKIM API ⇄ JAKIM**. The adapter must enforce:

- strong service authentication;
- role and scope authorization;
- schema validation;
- read/write separation;
- signed/traceable requests where supported;
- rate / availability controls;
- event synchronization / idempotency;
- audit logging;
- error and retry policy;
- revocation / credential rotation;
- data-minimization and selective disclosure;
- retention and sovereignty rules;
- human approval gates for authority-affecting actions.

### Project-design assertion requiring external proof

The project design specifies **JAKIM API integration for direct authority-system connectivity and real-time end-to-end monitoring**.

[SOURCE-LOCKED: JAKIM API integration — required: API specification, endpoint documentation, integration agreement and/or credentials-scope instrument]

[OPEN GATE: JAKIM API scope — owner: JAKIM / authorised integration owner — blocking: Authority Gate]

Required technical facts before production classification:

`read/write scope → endpoints → schemas → authentication → authorization → event/webhook model → latency → authority actions → error semantics → audit logs → retention → revocation → availability/SLA`

## 8. Event-driven real-time monitoring

Every relevant material change should produce an attributable event rather than wait for an audit-document collection cycle.

Representative event types:

`ORIGIN_VERIFIED`
`RAW_MATERIAL_LOT_CREATED`
`ORIGIN_CERTIFICATE_LINKED`
`SAMPLE_COLLECTED`
`SAMPLE_SEALED`
`LAB_RECEIVED`
`LAB_RESULT_LINKED`
`RAW_MATERIAL_RELEASED`
`RAW_MATERIAL_HELD`
`SUPPLIER_CHANGED`
`INGREDIENT_CHANGED`
`MANUFACTURING_STARTED`
`MANUFACTURING_RELEASED`
`HCP_EXCEPTION`
`SCCP_EXCEPTION`
`CAPA_OPENED`
`CAPA_REVERIFIED`
`PACKAGED`
`WAREHOUSE_RECEIVED`
`SHIPMENT_CREATED`
`PICKUP_CONFIRMED`
`SEAL_APPLIED`
`LOADED`
`IN_TRANSIT`
`GEOFENCE_ENTERED`
`ROUTE_DEVIATION`
`TEMPERATURE_EXCEPTION`
`TAMPER_ALERT`
`HANDOVER_COMPLETED`
`EXPORT_RELEASE_REFERENCED`
`PORT_RECEIVED`
`DISPATCHED`
`GCC_ARRIVAL`
`DESTINATION_RECEIVED`
`DESTINATION_ACCEPTED`
`EXCEPTION_CLOSED`
`AUTHORITY_STATUS_UPDATED`

## 9. Trust graph

The primary architecture is a linked provenance/trust graph rather than an isolated document repository.

```text
RAW MATERIAL
  |-- produced/provided by --> SUPPLIER / ORIGIN
  |-- sampled as -----------> SAMPLE
  |-- tested by ------------> LABORATORY
  |-- consumed in ----------> PRODUCTION BATCH

PRODUCTION BATCH
  |-- produced at ----------> FACILITY
  |-- governed by ----------> CONTROLS / HCP / SCCP
  |-- packaged as ----------> PRODUCT LOT / SKU

PRODUCT LOT / SHIPMENT
  |-- stored at ------------> WAREHOUSE
  |-- transported by -------> LOGISTICS PROVIDER
  |-- exported through -----> PORT / BORDER
  |-- received by ----------> GCC IMPORTER / DESTINATION
```

Every node and edge that carries a material trust claim should resolve to attributable evidence and an integrity reference.

## 10. AI role

AI may continuously:

- map evidence to applicable requirements and controls;
- detect missing or stale evidence;
- identify supplier, ingredient or origin changes;
- detect sample/batch mismatches;
- correlate laboratory anomalies;
- detect custody gaps, route deviation and seal/tamper events;
- detect environmental excursions where relevant;
- prioritize HCP/SCCP exceptions;
- identify unresolved CAPA;
- identify certification/status expiry or inconsistencies;
- generate human-review queues and audit preparation views.

AI may recommend or escalate. AI must not silently issue, alter, revoke or replace an official Halal certification or other formal authority decision.

Suggested operational states are decision-support only:

- `GREEN` — no detected exception under current evidence;
- `AMBER` — human review required;
- `RED` — potential material breach / high-priority escalation;
- `BLOCKED` — operational release prevented by configured control pending authorised review.

These platform states are not official Halal certification statuses unless an applicable authority instrument expressly defines them as such.

## 11. Immutable hash / DLT role

Blockchain/DLT, where used, is an **integrity-anchoring mechanism**, not a certification authority.

```text
Original evidence
      -> authenticated evidence record
      -> timestamp + issuer + entity/batch/shipment binding
      -> cryptographic hash
      -> optional DLT / append-only anchor
      -> later integrity verification
```

Do not place unnecessary raw confidential evidence on-chain. Prefer hashes, signed references and selective disclosure while authoritative source data remains in the appropriate sovereign/controlled repository.

## 12. Logistics and Sinotrans integration

Preferred architecture:

`Sinotrans/Y2T/MIS/EDI/IoT -> secure adapter/API -> event normalizer -> Halal/Tayyib trust event -> evidence store / trust graph`

The platform should integrate with rather than unnecessarily replace existing logistics systems.

Relevant evidence includes booking, pickup, vehicle/container identity, seal, route, transfer, warehouse, port/border, environmental telemetry where applicable, delivery and custody handover.

## 13. Destination / GCC

The primary destination ecosystem is GCC.

Destination release and acceptance remain subject to the competent destination authority/importer requirements for the specific product, shipment and market.

The authorised destination view should enable verification of, as permitted:

- product / batch / shipment identity;
- origin provenance;
- relevant laboratory evidence reference;
- certification / authority-status reference;
- supply-chain custody history;
- material exceptions and their disposition;
- evidence integrity / hash verification;
- current platform trust state;
- destination-specific documents and approvals.

## 14. Transparency model

"Complete transparency" means **complete attributable provenance and auditability for authorised roles**, not unrestricted disclosure of all raw data to every participant.

Use role-based, purpose-limited views:

- manufacturer: own product, supplier, facility and corrective-action evidence;
- laboratory: sample, method, result and chain-of-custody scope;
- logistics operator: shipment, custody and transport scope;
- PHC / authorised assurance role: evidence and audit scope granted by instrument;
- competent authority: authority-level scope under the actual integration mandate;
- GCC authority/importer: destination verification scope;
- consumer/public: reduced verified product/trust view only.

## 15. Sensor / edge profile

Select sensors based on commodity and shipment risk; do not install every sensor on every movement.

Core / commonly applicable controls:

- device identity and secure provisioning;
- GPS/geolocation where appropriate;
- temperature where relevant;
- humidity where relevant;
- door/open-close;
- tamper/seal status;
- power/battery state;
- timestamp/time synchronization.

Optional product-specific controls:

- shock/vibration;
- light exposure;
- CO2/air-quality indicators;
- pressure;
- water ingress;
- cold-chain probes;
- freezer/refrigeration status;
- other validated product-specific variables.

Calibration and maintenance records are themselves evidence objects.

## 16. Cybersecurity baseline

- unique device/service identity;
- credential and key protection;
- encrypted communications;
- least privilege and role-based access;
- secure API authentication and authorization;
- signed firmware where supported;
- audit logging;
- vulnerability and patch management;
- incident response;
- backup and recovery;
- segregation of operational, authority-interface and evidence stores;
- cryptographic-agility plan;
- signing-key rotation/revocation;
- tamper-evident evidence history;
- data-sovereignty / cross-border-transfer controls.

## 17. shipment workflow pilot mapping

[PILOT: shipment workflow]

The pilot should instantiate the architecture only when transaction-native evidence exists.

Target evidence accumulation:

1. product identity;
2. manufacturer / facility identity;
3. raw-material identity and origin provenance;
4. supplier approval references;
5. sample and chain-of-custody evidence;
6. laboratory evidence;
7. manufacturing / HCP / SCCP evidence as applicable;
8. packaging / batch / lot identity;
9. warehouse evidence;
10. vehicle/container/seal identity;
11. logistics and telemetry events;
12. export / port evidence;
13. authority-linked status where actually available;
14. GCC destination requirements / receiving evidence;
15. exceptions, findings and CAPA;
16. re-verification evidence;
17. current trust state;
18. complete hash / signature manifest.

Do not mark a shipment workflow event as occurred until transaction-native proof exists.

## 18. Platinum acceptance test

A Platinum deployment is not complete until the team can demonstrate, for the relevant scope:

1. raw-material source/lot identity is linked;
2. sample identity is bound to the raw-material lot/batch;
3. sample chain of custody is auditable;
4. laboratory evidence is attributable and scope-bound;
5. product/SKU/batch identity is linked;
6. applicable standards/requirements map to controls;
7. device/system/person identities are linked to events;
8. event timestamps are reliable;
9. evidence hashes can be independently reverified;
10. controlled correction/supersession does not destroy history;
11. at least one controlled exception is generated and routed;
12. an alert reaches an authorised role;
13. custody events are recorded end-to-end;
14. a human corrective-action workflow is completed;
15. re-verification is recorded;
16. an audit/verification report can be generated;
17. the authority-interface path can be demonstrated within the actual approved API scope;
18. the GCC destination party can verify its authorised view;
19. the system proves role-based transparency rather than unrestricted disclosure;
20. no AI/platform/hash/DLT event is represented as official certification without competent-authority basis.

## 19. Open gates created/retained by this revision

[SOURCE-LOCKED: JAKIM API integration — required: API specification / endpoint documentation / integration agreement / credentials-scope instrument]

[SOURCE-LOCKED: JAKIM endorsement/acceptance of China government laboratory — required: official JAKIM or competent-authority instrument identifying laboratory and scope]

[OPEN GATE: JAKIM API scope — owner: JAKIM / authorised integration owner — blocking: Authority Gate]

[OPEN GATE: laboratory identity + endorsement + accreditation/method scope — owner: JAKIM / laboratory / applicable China authority — blocking: Evidence]

These gates do not negate the target architecture. They prevent project-design assertions from being silently converted into verified authority facts before the supporting instruments are repository-native.
