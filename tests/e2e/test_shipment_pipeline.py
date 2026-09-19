import os
import sys

import pytest
from httpx import ASGITransport, AsyncClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../runtime/gateway")))

from app import app  # noqa: E402
from crypto import Ed25519Signer  # noqa: E402


@pytest.mark.asyncio
async def test_full_shipment_pipeline():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        health_res = await client.get("/api/v1/health")
        assert health_res.status_code == 200
        gateway_pubkey = health_res.json()["public_key"]
        assert health_res.json()["issues_statutory_certificates"] is False

        blocked = await client.post(
            "/api/v1/credentials/issue",
            json={
                "subject": {
                    "id": "urn:uuid:batch:blocked",
                    "batchId": "X",
                    "productDescription": "demo",
                    "slaughterDate": "2026-09-20T00:00:00Z",
                    "facilityId": "FIXTURE-MY-PL-1049",
                    "standardCompliance": "MS 1500:2019 (modelled)",
                },
                "issuer_did": "did:web:halal.gov.my:accreditation",
            },
        )
        assert blocked.status_code == 403

        issue_payload = {
            "subject": {
                "id": "urn:uuid:batch:2026-demo-001",
                "batchId": "BATCH-2026-09-A",
                "productDescription": "Frozen demo cuts",
                "slaughterDate": "2026-09-20T00:00:00Z",
                "facilityId": "FIXTURE-MY-PL-1049",
                "standardCompliance": "MS 1500:2019 (modelled, not certified)",
            },
            "issuer_did": "did:web:example.local:ahte-reference",
        }
        cred_res = await client.post("/api/v1/credentials/issue", json=issue_payload)
        assert cred_res.status_code == 200
        vc = cred_res.json()
        unsigned_doc = {
            "@context": vc["@context"],
            "id": vc["id"],
            "type": vc["type"],
            "issuer": vc["issuer"],
            "issuanceDate": vc["issuanceDate"],
            "credentialSubject": vc["credentialSubject"],
        }
        assert Ed25519Signer.verify_signature(unsigned_doc, vc["proof"]["proofValue"], gateway_pubkey)

        compliant_event = {
            "eventType": "ObjectEvent",
            "eventTime": "2026-09-20T04:15:00Z",
            "action": "OBSERVE",
            "bizStep": "urn:epcglobal:cbv:bizstep:transporting",
            "facility_id": "FIXTURE-MY-PL-1049",
            "epcList": ["urn:epc:id:sscc:0000000.0000000000"],
            "telemetry": {
                "temp_celsius": -21.4,
                "seal_intact": True,
                "co_mingled_with_non_halal": False,
            },
        }
        eval_res = await client.post("/api/v1/telemetry/evaluate", json=compliant_event)
        if eval_res.status_code == 503:
            pytest.skip("OPA not reachable from this process")
        assert eval_res.status_code == 200
        eval_data = eval_res.json()
        assert eval_data["allowed"] is True
        receipt = eval_data["notarized_receipt"]
        assert Ed25519Signer.verify_signature(receipt["payload"], receipt["proof"], receipt["gateway_public_key"])

        violation_event = dict(compliant_event)
        violation_event["telemetry"] = {
            "temp_celsius": -10.0,
            "seal_intact": True,
            "co_mingled_with_non_halal": False,
        }
        breach_res = await client.post("/api/v1/telemetry/evaluate", json=violation_event)
        assert breach_res.json()["allowed"] is False
        assert "Cold chain" in breach_res.json()["violation_reason"]

        tamper_event = dict(compliant_event)
        tamper_event["telemetry"] = {
            "temp_celsius": -20.0,
            "seal_intact": False,
            "co_mingled_with_non_halal": False,
        }
        tamper_res = await client.post("/api/v1/telemetry/evaluate", json=tamper_event)
        assert tamper_res.json()["allowed"] is False
        assert "seal" in tamper_res.json()["violation_reason"].lower()
