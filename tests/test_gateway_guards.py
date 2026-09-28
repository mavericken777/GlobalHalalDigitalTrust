"""Reference gateway must not sign under caller-selected identities."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "runtime/gateway"))
from tests.runtime_path import load_gateway
from fastapi.testclient import TestClient


def test_non_demo_issuer_is_denied():
    app = load_gateway("app")
    client = TestClient(app.app)
    subject = {"id": "demo", "batchId": "demo", "productDescription": "demo", "slaughterDate": "2026-10-01", "facilityId": "FIXTURE-DEMO", "standardCompliance": "demo only"}
    for issuer in ["did:web:sfda.gov.sa", "did:web:unrelated.example", "did:web:halal.gov.my"]:
        assert client.post("/api/v1/credentials/issue", json={"issuer_did": issuer, "subject": subject}).status_code == 403


def test_caller_cannot_seed_a_customs_released_demo_receipt():
    app = load_gateway("app")
    client = TestClient(app.app)
    event = {
        "consignment_id": "fixture-guard-new",
        "current_state": "BORDER_PORT_INSPECTED",
        "facility_id": "FIXTURE-DEMO",
        "destination_country": "AE",
        "temp_celsius": 2.0,
        "seal_tamper_detected": False,
        "coordinates": {"x": 0, "y": 0, "z": 0},
    }
    assert client.post("/api/v1/corridor/clearance", json=event).status_code == 400


def test_caller_cannot_override_recorded_demo_state():
    app = load_gateway("app")
    client = TestClient(app.app)
    app.LEDGER_DB["fixture-guard-existing"] = {"current_state": "QUARANTINED", "history": []}
    event = {
        "consignment_id": "fixture-guard-existing",
        "current_state": "BORDER_PORT_INSPECTED",
        "facility_id": "FIXTURE-DEMO",
        "destination_country": "AE",
        "temp_celsius": 2.0,
        "seal_tamper_detected": False,
        "coordinates": {"x": 0, "y": 0, "z": 0},
    }
    assert client.post("/api/v1/corridor/clearance", json=event).status_code == 409


def test_simulated_customs_state_cannot_claim_operational_release(monkeypatch):
    app = load_gateway("app")
    client = TestClient(app.app)

    class PolicyResponse:
        status_code = 200

        def json(self):
            return {"result": {"allow": True, "hti_score": 1.0, "reasons": []}}

    class PolicyClient:
        def __init__(self, **kwargs):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            pass

        async def post(self, *args, **kwargs):
            return PolicyResponse()

    monkeypatch.setattr(app.httpx, "AsyncClient", PolicyClient)
    event = {
        "consignment_id": "fixture-guard-sequence",
        "facility_id": "FIXTURE-DEMO",
        "destination_country": "AE",
        "temp_celsius": 2.0,
        "seal_tamper_detected": False,
        "coordinates": {"x": 0, "y": 0, "z": 0},
    }
    first = client.post("/api/v1/corridor/clearance", json=event)
    assert first.status_code == 200
    assert first.json()["receipt"]["state"] == "BORDER_PORT_INSPECTED"
    second = client.post("/api/v1/corridor/clearance", json={**event, "current_state": "BORDER_PORT_INSPECTED"})
    assert second.status_code == 200
    receipt = second.json()["receipt"]
    assert receipt["state"] == "CUSTOMS_RELEASED"
    assert receipt["pilot_only"] is True
    assert receipt["authority_authenticated"] is False
    assert receipt["operational_release"] is False
    assert receipt["not_a_customs_clearance"] is True
