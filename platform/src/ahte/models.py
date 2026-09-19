from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


def now() -> datetime:
    return datetime.now(timezone.utc)


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:16]}"


class ActorType(str, Enum):
    human = "human"
    human_authority = "human_authority"
    system = "system"
    ai_advisory = "ai_advisory"


class DecisionClass(str, Enum):
    D0 = "D0"  # evidence intake
    D1 = "D1"  # assessment
    D2 = "D2"  # hitm case open
    D3 = "D3"  # hold / exception
    D4 = "D4"  # re-verification
    D5 = "D5"  # authority decision record (not a certificate)
    D6 = "D6"  # operational release recommendation only


class TrustState(str, Enum):
    pending = "PENDING"
    evidence_complete = "EVIDENCE_COMPLETE"
    assessed = "ASSESSED"
    hold = "HOLD"
    disputed = "DISPUTED"
    verified = "VERIFIED"  # internal model only
    expired = "EXPIRED"
    revoked = "REVOKED"
    recalled = "RECALLED"


class EvidenceIn(BaseModel):
    object_id: str
    evidence_type: str
    source_system: str = "manual"
    payload: dict[str, Any] = Field(default_factory=dict)
    actor: str
    actor_type: ActorType = ActorType.human
    lab_result: str | None = None


class AssessmentIn(BaseModel):
    object_id: str
    evidence_ids: list[str]
    finding: str
    actor: str
    actor_type: ActorType = ActorType.human
    ai_confidence: float | None = None


class AuthorityDecisionIn(BaseModel):
    object_id: str
    assessment_id: str
    actor: str
    actor_type: ActorType
    decision: str
    emits_certificate: bool = False
    source_instrument: str | None = None


class CorridorEventIn(BaseModel):
    shipment_id: str
    segment: str
    bizstep: str
    actor: str
    notes: str | None = None


class Stored(BaseModel):
    id: str
    created_at: datetime
    body: dict[str, Any]
