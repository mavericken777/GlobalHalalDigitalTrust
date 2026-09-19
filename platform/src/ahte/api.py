from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from . import __version__, engine
from .hitm import HitmDenied
from .models import AssessmentIn, AuthorityDecisionIn, CorridorEventIn, EvidenceIn
from .store import STORE

app = FastAPI(
    title="AHTE reference runtime",
    version=__version__,
    description="Specification runtime. Does not issue Halal certificates.",
)


@app.get("/health")
def health():
    return {
        "ok": True,
        "runtime": "REFERENCE",
        "issues_certificates": False,
        "canonical_path": engine.CANONICAL,
    }


@app.get("/v1/canonical-path")
def path():
    return {"nodes": engine.CANONICAL, "corridor_segments": engine.SEGMENTS}


@app.post("/v1/evidence")
def post_evidence(body: EvidenceIn):
    try:
        rec = engine.ingest_evidence(body)
    except HitmDenied as e:
        raise HTTPException(403, e.reason) from e
    return rec.model_dump()


@app.post("/v1/assessments")
def post_assessment(body: AssessmentIn):
    try:
        rec = engine.assess(body)
    except HitmDenied as e:
        raise HTTPException(403, e.reason) from e
    except ValueError as e:
        raise HTTPException(400, str(e)) from e
    return rec.model_dump()


@app.post("/v1/authority-decisions")
def post_decision(body: AuthorityDecisionIn):
    try:
        rec = engine.authority_decision(body)
    except HitmDenied as e:
        raise HTTPException(403, e.reason) from e
    except ValueError as e:
        raise HTTPException(400, str(e)) from e
    return rec.model_dump()


@app.post("/v1/corridor/events")
def post_event(body: CorridorEventIn):
    try:
        rec = engine.corridor_event(body)
    except (HitmDenied, ValueError) as e:
        raise HTTPException(400, str(e)) from e
    return rec.model_dump()


@app.get("/v1/trust-state/{object_id}")
def trust(object_id: str):
    rec = STORE.trust_for(object_id)
    if rec is None:
        raise HTTPException(404, "no trust state")
    return rec.model_dump()


@app.get("/v1/objects")
def dump():
    return {k: [x.model_dump() for x in STORE.list(k)] for k in STORE.tables}


@app.post("/v1/certificates")
def certificates_blocked():
    return JSONResponse({"error": "AHTE does not issue Halal certificates"}, status_code=403)
