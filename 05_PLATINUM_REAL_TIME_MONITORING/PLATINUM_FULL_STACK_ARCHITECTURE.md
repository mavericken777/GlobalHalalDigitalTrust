# Platinum Tier — Full-Stack Real-Time Halal/Tayyib Monitoring Architecture

## Definition

**Platinum = full-stack real-time monitoring and evidence orchestration across product identity, manufacturing/site conditions, custody, logistics and destination receiving.**

Platinum does not itself determine Halal certification. Halal status is established by the competent authority and applicable certification framework. Platinum provides continuous Tayyib/product-integrity, custody, environmental and exception evidence that supports assurance, auditability and transaction trust.

## Stack

```text
PRODUCT / BATCH IDENTITY
        |
        +-- QR / NFC / serialized identifier
        +-- batch/lot linkage
        +-- seal ID
        |
SOURCE & SCIENTIFIC EVIDENCE
        |
        +-- raw-material provenance references
        +-- laboratory test result references
        +-- Halal certificate/reference
        |
SITE / FACTORY EDGE
        |
        +-- temperature
        +-- humidity
        +-- door/open-close
        +-- tamper/seal status
        +-- power status
        +-- optional product-specific sensors
        |
IOT / GATEWAY
        |
        +-- device identity
        +-- BLE / LoRaWAN / cellular / other approved connectivity
        +-- buffering / store-and-forward
        +-- time synchronisation
        |
REAL-TIME TRUST PLATFORM
        |
        +-- event ingestion
        +-- rules engine
        +-- geofencing
        +-- anomaly detection
        +-- alerting
        +-- evidence hash
        +-- chain-of-custody graph
        |
SINOTRANS / LOGISTICS EVENTS
        |
        +-- booking
        +-- pickup/loading
        +-- vehicle/container
        +-- transfer
        +-- port/border
        +-- warehouse
        +-- delivery
        |
DESTINATION / GCC
        |
        +-- receiving
        +-- condition check
        +-- exception disposition
        +-- importer confirmation
        |
DIGITAL PRODUCT PASSPORT / TRUST RECORD
```

## Sensor profile

Select sensors based on the commodity risk profile rather than installing every sensor on every shipment.

### Core controls

- device identity and secure provisioning;
- GPS/geolocation where appropriate;
- temperature;
- humidity;
- door/open-close;
- tamper/seal status;
- shock/vibration where appropriate;
- power/battery state;
- timestamp/time synchronisation.

### Optional controls

- light exposure;
- CO2/air-quality indicators for selected cargo;
- pressure;
- water ingress;
- cold-chain probes;
- freezer/refrigeration status;
- other product-specific variables.

## Data integrity controls

Every telemetry/event record should be:
- attributable to a device, person or system;
- timestamped;
- bound to the relevant shipment/site/SKU/batch;
- integrity protected;
- retained or referenced according to the evidence policy;
- auditable;
- subject to access control.

Do not place unnecessary raw data into a global database. Use sovereign storage plus selective disclosure and cryptographic references where practical.

## Trust event model

Example event types:

`MANUFACTURING_RELEASED`
`LAB_RESULT_LINKED`
`HALAL_STATUS_REFERENCED`
`SHIPMENT_CREATED`
`PICKUP_CONFIRMED`
`SEAL_APPLIED`
`LOADED`
`IN_TRANSIT`
`GEOFENCE_ENTERED`
`TEMPERATURE_EXCEPTION`
`TAMPER_ALERT`
`HANDOVER_COMPLETED`
`WAREHOUSE_RECEIVED`
`DISPATCHED`
`DELIVERED`
`DESTINATION_ACCEPTED`
`EXCEPTION_CLOSED`

## Alert classes

### Critical
Potential loss of integrity, tamper evidence, major environmental excursion, unauthorised custody event, identity mismatch.

### High
Route deviation, repeated environmental excursion, unexpected handling point, missing expected event.

### Medium
Connectivity loss, battery degradation, incomplete event payload, delayed data.

### Low
Routine maintenance, calibration due, non-critical metadata discrepancy.

AI may prioritise, correlate and recommend actions. AI must not silently alter a certification or legal status.

## Integration with China Trust / laboratory workflow

The target flow is:

`Manufacturer origin evidence -> approved laboratory workflow -> test result -> evidence reference -> Halal/Tayyib compliance workflow -> digital trust record -> shipment/batch identity -> Platinum monitoring -> logistics -> GCC verification`

Laboratory reports remain under the laboratory's lawful control. The trust layer stores authorised references, provenance metadata and integrity evidence rather than pretending to become the laboratory or certification authority.

## Integration with Sinotrans

Preferred architecture:

`Sinotrans/Y2T/MIS/EDI/IoT -> secure adapter/API -> event normalizer -> Halal/Tayyib trust event -> evidence store`

The pilot should avoid replacement of existing Sinotrans systems.

## Device lifecycle

`Procure -> register -> provision identity -> install -> test -> calibrate -> activate -> monitor -> maintain -> recalibrate -> retire`

Calibration and maintenance records must themselves be evidence objects.

## Cybersecurity baseline

- unique device identity;
- credential/key protection;
- encrypted communications;
- role-based access;
- least privilege;
- signed firmware where supported;
- secure API authentication;
- audit logging;
- vulnerability/patch management;
- incident response;
- backup and recovery;
- segregation of operational and evidence stores.

## Commercial model

Separate one-time and recurring costs:

`hardware + installation + calibration + gateway + connectivity + platform + integration + support + replacement/maintenance`

For CODA discussion, build a transparent support model that shows manufacturer cost before and after any eligible support mechanism. Do not assume subsidy eligibility or amount without written programme confirmation.

## Platinum acceptance test

A Platinum deployment is not complete until the team can demonstrate:

1. product/SKU/batch identity is linked;
2. device identity is linked;
3. telemetry is received;
4. event timestamps are reliable;
5. at least one controlled exception is generated;
6. an alert reaches an authorised role;
7. custody events are recorded;
8. evidence integrity can be verified;
9. a human corrective-action workflow is completed;
10. an audit/verification report can be generated;
11. the destination party can verify the authorised view.
