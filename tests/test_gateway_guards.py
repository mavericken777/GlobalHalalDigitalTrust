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
