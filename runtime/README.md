# Trust gateway + OPA (reference)

```bash
docker compose up -d --build
# Gateway http://localhost:8000/api/v1/health
# OPA     http://localhost:8181/v1/data/halal/compliance

opa test -v runtime/policies/
OPA_URL=http://127.0.0.1:8181/v1/data/halal/compliance pytest -v tests/e2e/test_shipment_pipeline.py
```

Signed documents from `/api/v1/credentials/issue` are **HalalBatchAssertion** objects. They are not JAKIM certificates. Statutory-looking issuer DIDs are rejected.

`/api/v1/corridor/clearance` is a fixture-only simulation. A new consignment starts at
`COLD_CHAIN_IN_TRANSIT`; later requests must name the recorded demo state. Even when
the simulated FSM reaches `CUSTOMS_RELEASED`, its receipt states `pilot_only=true`,
`authority_authenticated=false`, `operational_release=false`, and
`not_a_customs_clearance=true`. `allowed` and `simulation_passed` refer only to the
fixture policy evaluation. The in-memory ledger and ephemeral signing key are not
an authority record or proof of customs clearance.
