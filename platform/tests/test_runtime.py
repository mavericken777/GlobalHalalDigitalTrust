from fastapi.testclient import TestClient

from ahte.api import app
from ahte.store import STORE

client = TestClient(app)


def setup_function():
    for table in STORE.tables.values():
        table.clear()


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["issues_certificates"] is False


def test_certificate_endpoint_denied():
    assert client.post("/v1/certificates").status_code == 403


def test_ai_cannot_take_d5():
    ev = client.post(
        "/v1/evidence",
        json={"object_id": "sku-1", "evidence_type": "lab", "actor": "tech", "lab_result": "not_detected"},
    )
    assert ev.status_code == 200
    assert ev.json()["body"]["interpretation"] == "NOT_DETECTED_IS_NOT_HALAL"
    asmt = client.post(
        "/v1/assessments",
        json={
            "object_id": "sku-1",
            "evidence_ids": [ev.json()["id"]],
            "finding": "evidence recorded",
            "actor": "auditor",
        },
    )
    denied = client.post(
        "/v1/authority-decisions",
        json={
            "object_id": "sku-1",
            "assessment_id": asmt.json()["id"],
            "actor": "model",
            "actor_type": "ai_advisory",
            "decision": "release",
        },
    )
    assert denied.status_code == 403


def test_human_authority_records_decision_not_certificate():
    ev = client.post(
        "/v1/evidence",
        json={"object_id": "sku-2", "evidence_type": "doc", "actor": "qa"},
    )
    asmt = client.post(
        "/v1/assessments",
        json={
            "object_id": "sku-2",
            "evidence_ids": [ev.json()["id"]],
            "finding": "ok",
            "actor": "auditor",
        },
    )
    dec = client.post(
        "/v1/authority-decisions",
        json={
            "object_id": "sku-2",
            "assessment_id": asmt.json()["id"],
            "actor": "officer",
            "actor_type": "human_authority",
            "decision": "record",
            "emits_certificate": False,
        },
    )
    assert dec.status_code == 200
    assert dec.json()["body"]["certificate_issued"] is False
    ts = client.get("/v1/trust-state/sku-2")
    assert ts.json()["body"]["not_a_certificate"] is True


def test_emit_certificate_flag_denied():
    ev = client.post(
        "/v1/evidence",
        json={"object_id": "sku-3", "evidence_type": "doc", "actor": "qa"},
    )
    asmt = client.post(
        "/v1/assessments",
        json={
            "object_id": "sku-3",
            "evidence_ids": [ev.json()["id"]],
            "finding": "ok",
            "actor": "auditor",
        },
    )
    dec = client.post(
        "/v1/authority-decisions",
        json={
            "object_id": "sku-3",
            "assessment_id": asmt.json()["id"],
            "actor": "officer",
            "actor_type": "human_authority",
            "decision": "certify",
            "emits_certificate": True,
        },
    )
    assert dec.status_code == 403
