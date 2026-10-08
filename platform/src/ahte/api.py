from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from . import __version__, engine
from .demo_scenario import run_demo
from .hitm import HitmDenied
from .models import AssessmentIn, AuthorityDecisionIn, CorridorEventIn, EvidenceIn
from .mock_integrations import MOCK_HUB
from .store import STORE

app = FastAPI(title="AHTE Global Halal Digital Trust Runtime", version=__version__, description="Complete demonstration runtime with replaceable mock integration providers.")

@app.get("/health")
def health():
    return {"ok": True, "runtime": "REFERENCE_WITH_MOCK_INTEGRATIONS", "issues_certificates": False, "canonical_path": engine.CANONICAL,
            "providers": {"jakim": "MOCK", "laboratory": "MOCK", "sinotrans": "MOCK", "port_customs": "MOCK", "gcc": "MOCK", "finance": "MOCK"}}

@app.get("/v1/canonical-path")
def path(): return {"nodes": engine.CANONICAL, "corridor_segments": engine.SEGMENTS}

@app.post("/v1/evidence")
def post_evidence(body: EvidenceIn):
    try: return engine.ingest_evidence(body).model_dump()
    except HitmDenied as e: raise HTTPException(403, e.reason) from e

@app.post("/v1/assessments")
def post_assessment(body: AssessmentIn):
    try: return engine.assess(body).model_dump()
    except HitmDenied as e: raise HTTPException(403, e.reason) from e
    except ValueError as e: raise HTTPException(400, str(e)) from e

@app.post("/v1/authority-decisions")
def post_decision(body: AuthorityDecisionIn):
    try: return engine.authority_decision(body).model_dump()
    except HitmDenied as e: raise HTTPException(403, e.reason) from e
    except ValueError as e: raise HTTPException(400, str(e)) from e

@app.post("/v1/corridor/events")
def post_event(body: CorridorEventIn):
    try: return engine.corridor_event(body).model_dump()
    except (HitmDenied, ValueError) as e: raise HTTPException(400, str(e)) from e

@app.get("/v1/trust-state/{object_id}")
def trust(object_id: str):
    rec = STORE.trust_for(object_id)
    if rec is None: raise HTTPException(404, "no trust state")
    return rec.model_dump()

@app.get("/v1/objects")
def dump(): return {k: [x.model_dump() for x in STORE.list(k)] for k in STORE.tables}

@app.get("/v1/integrations")
def integrations():
    return {"mode": "DEMONSTRATION", "adapters": [
        {"name": "DIRECT_JAKIM_API", "state": "MOCK", "production_boundary": "replace provider without domain or UI rewrite"},
        {"name": "CHINA_LABORATORY", "state": "MOCK", "production_boundary": "sample→custody→method→result→signature"},
        {"name": "SINOTRANS", "state": "MOCK", "production_boundary": "warehouse→logistics→container→seal→custody"},
        {"name": "PORT_CUSTOMS", "state": "MOCK", "production_boundary": "event→inspection→sovereign release"},
        {"name": "GCC_DESTINATION", "state": "MOCK", "production_boundary": "importer→warehouse→distribution→verification"},
        {"name": "SHARIAH_FINANCE", "state": "MOCK", "production_boundary": "trust data→finance/Takaful decision"},
    ]}

@app.post("/v1/demo/run")
def demo_run(payload: dict): return run_demo(payload.get("shipment_id", "shipment-workflow"), payload.get("object_id", "DEMO-PRODUCT-001"))

@app.post("/v1/demo/integrations/jakim")
def demo_jakim(payload: dict): return MOCK_HUB.jakim(payload.get("object_id", "DEMO-OBJECT"), payload.get("action", "status"))

@app.post("/v1/demo/integrations/laboratory")
def demo_lab(payload: dict): return MOCK_HUB.laboratory(payload.get("object_id", "DEMO-OBJECT"), payload.get("result", "NOT_DETECTED"))

@app.post("/v1/demo/integrations/sinotrans")
def demo_sinotrans(payload: dict): return MOCK_HUB.sinotrans(payload.get("shipment_id", "shipment-workflow"), payload.get("status", "IN_TRANSIT"))

@app.post("/v1/demo/integrations/port-customs")
def demo_port(payload: dict): return MOCK_HUB.port_customs(payload.get("shipment_id", "shipment-workflow"), payload.get("port", "ORIGIN_PORT"))

@app.post("/v1/demo/integrations/gcc")
def demo_gcc(payload: dict): return MOCK_HUB.gcc(payload.get("shipment_id", "shipment-workflow"), payload.get("action", "receive"))

@app.post("/v1/demo/integrations/finance")
def demo_finance(payload: dict): return MOCK_HUB.finance(payload.get("object_id", "DEMO-OBJECT"), payload.get("action", "quote"))

@app.get("/v1/demo/integration-events")
def demo_events(): return {"events": MOCK_HUB.events, "count": len(MOCK_HUB.events)}

@app.post("/v1/certificates")
def certificates_blocked():
    return JSONResponse({"error": "Certification authority remains outside AHTE; use the authority workflow."}, status_code=403)
