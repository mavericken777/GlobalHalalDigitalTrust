# AHTE reference runtime

Runnable **reference implementation** of the adopted specification.

This is not a substitute for JAKIM, GCC authorities, laboratory accreditation, customs systems, or executed partner networks.

## Run

```bash
cd platform
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
uvicorn ahte.api:app --app-dir src --host 127.0.0.1 --port 8080
```

Or: `docker compose up --build`

## What it does

- Stores evidence, assessments, HITM cases, authority decisions, trust states, corridor events
- Enforces HITM default-deny in-process (and ships the `.rego` draft)
- Refuses to mint Halal certificates or set `trust_state=CERTIFIED`
- Treats `not_detected` lab results as evidence only
- Marks corridor events as pilot-only; does not instantiate Shipment 001
- Binds evidence and assessments to their object; negative decisions cannot become VERIFIED
- Keeps self-asserted approvals PENDING because caller identity is not authenticated
- Preserves restrictive trust states until an authenticated re-verification workflow exists

## What it does not do

- Talk to live JAKIM/MYeHALAL, GCC single windows, Sinotrans, or lab LIMS
- Deploy OPA/SPIRE/SCITT/EPCIS in production
- Close TRANSACTION-GATE or SOURCE-LOCKED items

## Reference limits

MemoryStore is volatile and resets on restart. No production authentication, persistence or immutable audit log is implemented. Compose binds to localhost only. Use synthetic data; do not expose it publicly. See [mission demo runbook](../docs/OCTOBER_2026_DEMO_RUNBOOK.md).
