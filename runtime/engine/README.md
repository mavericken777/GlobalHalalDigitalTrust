# Consignment FSM engine (reference)

```bash
cd runtime/engine
python verify_system.py
uvicorn engine:app --port 8001
```

- 12 states; advance one hop per successful evaluation.
- Quarantine / reject per table; HTI is 0 unless the hop lands on ST-09/ST-10.
- Facility IDs must use `FIXTURE-` prefix.
- Madhab numbers are **inputs**, not a fiqh engine.
- Health will not claim JAKIM anchoring.
