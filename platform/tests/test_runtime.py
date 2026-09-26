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


def make_assessment(object_id="sku-a"):
    ev = client.post("/v1/evidence", json={"object_id": object_id, "evidence_type": "doc", "actor": "qa"})
    return client.post("/v1/assessments", json={"object_id": object_id, "evidence_ids": [ev.json()["id"]], "finding": "ok", "actor": "auditor"}).json()["id"]


def record_decision(assessment_id, decision, object_id="sku-a"):
    return client.post("/v1/authority-decisions", json={"object_id": object_id, "assessment_id": assessment_id, "actor": "asserted-officer", "actor_type": "human_authority", "decision": decision})


def test_cross_object_evidence_rejected():
    ev = client.post("/v1/evidence", json={"object_id": "sku-a", "evidence_type": "doc", "actor": "qa"})
    r = client.post("/v1/assessments", json={"object_id": "sku-b", "evidence_ids": [ev.json()["id"]], "finding": "ok", "actor": "auditor"})
    assert r.status_code == 400
    assert client.get("/v1/trust-state/sku-b").status_code == 404


def test_empty_assessment_rejected():
    r = client.post("/v1/assessments", json={"object_id": "sku-a", "evidence_ids": [], "finding": "ok", "actor": "auditor"})
    assert r.status_code == 400


def test_cross_object_decision_rejected():
    assert record_decision(make_assessment(), "approve", "sku-b").status_code == 400


def test_self_asserted_authority_cannot_verify():
    assert record_decision(make_assessment(), "approve").status_code == 200
    state = client.get("/v1/trust-state/sku-a").json()["body"]
    assert state["state"] == "PENDING"
    assert state["authority_authenticated"] is False


def test_negative_decision_does_not_verify_or_clear_hold():
    aid = make_assessment()
    assert record_decision(aid, "reject").status_code == 200
    assert client.get("/v1/trust-state/sku-a").json()["body"]["state"] == "HOLD"
    assert record_decision(aid, "approve").status_code == 200
    assert client.get("/v1/trust-state/sku-a").json()["body"]["state"] == "HOLD"


def test_unknown_decision_rejected():
    assert record_decision(make_assessment(), "anything").status_code == 400


def test_new_evidence_and_assessment_do_not_clear_restriction():
    record_decision(make_assessment(), "revoke")
    make_assessment()
    assert client.get("/v1/trust-state/sku-a").json()["body"]["state"] == "REVOKED"
