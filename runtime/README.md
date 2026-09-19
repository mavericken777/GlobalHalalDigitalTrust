# Trust gateway + OPA (reference)

```bash
docker compose up -d --build
# Gateway http://localhost:8000/api/v1/health
# OPA     http://localhost:8181/v1/data/halal/compliance

opa test -v runtime/policies/
OPA_URL=http://127.0.0.1:8181/v1/data/halal/compliance pytest -v tests/e2e/test_shipment_pipeline.py
```

Signed documents from `/api/v1/credentials/issue` are **HalalBatchAssertion** objects. They are not JAKIM certificates. Statutory-looking issuer DIDs are rejected.
