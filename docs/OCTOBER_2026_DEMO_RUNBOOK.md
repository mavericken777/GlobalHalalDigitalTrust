# October mission — offline reference demo runbook

- Artifact: `OCTOBER_2026_DEMO_RUNBOOK.md`; folder: `docs/`; v1.0; 2026-09-26.
- Commit: `fix(mission): reconcile October itinerary and reference safeguards [EVIDENCE-UPDATE]`
- Status: demonstration only; no authority integration, production release or certification.

Use `platform/` as the single mission demonstration. The legacy `runtime/` OPA stack, escrow and circuit are engineering references, not a required public demonstration path.

## Prepare before travel

1. Download the reviewed Git commit and Python dependencies on the presentation laptop before departure. Use a dedicated virtual environment; record commit and test results.
2. Run `python tools/validate_repository.py` from repository root and `python -m pytest -q` from `platform/` after installing `platform/requirements.txt`.
3. Start `uvicorn ahte.api:app --app-dir src --host 127.0.0.1 --port 8080` from `platform/`.
4. Open `http://127.0.0.1:8080/docs`; disconnect the laptop from the network and repeat the demonstration. Keep a local copy of this pack and screenshots as fallback.
5. Use synthetic object IDs (`DEMO-OCT-001`), people and documents only. Do not load partner data or connect external authority services.

## Five-minute demonstration

- `/health`: show `REFERENCE` and `issues_certificates=false`.
- `/v1/evidence`: record a synthetic lab result `not_detected`; show its interpretation `NOT_DETECTED_IS_NOT_HALAL`.
- `/v1/assessments`: use the returned evidence ID and the same object ID; explain object binding.
- `/v1/authority-decisions`: an AI advisory actor is refused; an asserted human-authority `approve` remains `PENDING`. Caller-supplied identity is not authentication.
- A `reject` decision puts the object on `HOLD`; subsequent evidence cannot automatically clear it.
- `/v1/certificates`: show the explicit refusal to issue certificates.

Example evidence input:

```json
{"object_id":"DEMO-OCT-001","evidence_type":"lab","source_system":"synthetic-demo","actor":"demo-technician","lab_result":"not_detected"}
```

## Known limits and stop conditions

The store is **in-memory**: restart loses records. There is no authenticated authority channel, persistent audit log, tenant isolation, production key management or live partner adapter. Restricted states need an implemented, authenticated re-verification workflow before production; this demo deliberately cannot clear them by asserted approval. Do not expose the app to the Internet or port-forward it.

If tests fail or the offline path does not work, use the static architecture and gate walkthrough. Do not switch to an untested public endpoint during the ceremony. Never present a simulated customs state as actual clearance, a reference signature as an authority signature, or the escrow/circuit as audited or deployed.

## Rehearsal sign-off (external gate)

Proposed technical lead records: laptop/OS; commit; dependency-install success; offline test result; date; presenter; backup laptop/materials; AV and interpreter check. Proposed deadline: **8 October**, repeat short check **11 October evening**. No rehearsal completion is claimed by this document.
