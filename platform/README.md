# AHTE reference runtime

Runnable **reference implementation** of the adopted project specification.


This is not a substitute for JAKIM, MAIN/JAIN, GCC authorities, laboratory accreditation, customs systems, or executed partner networks.

## Run

```bash
cd platform
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
uvicorn ahte.api:app --app-dir src --host 127.0.0.1 --port 8080
```

Or: `docker compose up --build`

## Decision-class binding

The reference PEP follows `00_EXECUTIVE_COMMAND/hitm-decision-class-registry.json`:

- D0 — encoded operational ingest
- D1 — encoded control execution
- D2 — machine assessment; creates assessment objects only
- D3 — finding / CAPA classification; human accountability
- D4 — trust-fracture HOLD; automatic release prohibited
- certification review — competent-certification review reserved; human authority only
- certification determination — sovereign / legal reserved; no executable action in this runtime

High AI confidence never bypasses authorised certification decision workflow. Undefined policy results deny.

## What it does

- Stores evidence, assessments, HITM cases, asserted authority decisions, trust states and corridor events
- Enforces HITM default-deny in-process and via a Rego policy fixture
- Refuses to mint Halal certificates or set `trust_state=CERTIFIED`
- Treats `not_detected` lab results as evidence only
- Separates demonstration events from authenticated operating events
- Binds evidence and assessments to their object; negative decisions cannot become VERIFIED
- Keeps self-asserted approvals PENDING because caller identity is not authenticated
- Preserves restrictive trust states until an authenticated re-verification workflow exists

## What it does not do

- Talk to live JAKIM/MYeHALAL, GCC single windows, Sinotrans, or lab LIMS
- Deploy OPA/SPIRE/SCITT/EPCIS in production
- Execute certification determination sovereign/legal decisions
- Connect and validate the configured authority, logistics, laboratory and destination interfaces

## Reference limits

MemoryStore is volatile and resets on restart. This reference runtime has no production authentication, persistence or immutable audit log. Compose binds to localhost only. Use synthetic data and keep it on a trusted local environment.
