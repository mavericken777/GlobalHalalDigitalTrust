# Sinotrans Integration Data Mapping

## Objective

Provide a minimum viable data contract for integrating Sinotrans logistics events with the GHDTE trust layer.

| Sinotrans/legacy concept | GHDTE canonical object | Required fields | Evidence action |
|---|---|---|---|
| Customer/order | Shipment | shipment_id, customer_ref, origin, destination | hash order reference |
| Booking | Shipment event | booking_ref, carrier, mode, timestamp | signed event |
| Container | Container identity | container_id, seal_id | identity + hash |
| Pickup | Logistics event | location, actor, time | attestation |
| Loading | Logistics event | location, unit, sequence | hash + optional media ref |
| Port handoff | Custody event | location, party, timestamp | signature |
| Customs document | Document reference | doc_id, type, authority, status | hash source document |
| Temperature telemetry | Telemetry reference | sensor, time, reading, unit | hash/attest sampled data |
| Warehouse receipt | Warehouse event | location, batch, quantity, condition | signed event |
| Dispatch | Logistics event | destination, batch, quantity | signed event |
| Proof of delivery | Delivery evidence | receiver, time, shipment | signature + hash |

## Integration pattern

`Source system -> adapter -> schema validation -> policy check -> event normalization -> trust event -> evidence hash -> sovereign evidence store`

## Minimum payload principle

Only the fields required to perform an authorized trust function should leave the source jurisdiction. For example, a public consumer verification event should not expose a commercial contract, supplier price, employee identity or unrelated customer data.

## Offline handling

Where connectivity is unavailable, events can be queued locally, signed, timestamped and synchronized when the secure connection returns. The synchronization process must preserve event order and prevent replay attacks.

## Exception mapping

Exceptions are first-class events. Do not overwrite a previous event to hide a discrepancy. Create a new corrective event linked to the original event.
