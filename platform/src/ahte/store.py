from __future__ import annotations

from threading import RLock
from typing import Any

from .models import Stored, new_id, now


class MemoryStore:
    def __init__(self) -> None:
        self._lock = RLock()
        self.tables: dict[str, dict[str, Stored]] = {
            "evidence": {},
            "assessments": {},
            "hitm": {},
            "decisions": {},
            "trust": {},
            "events": {},
        }

    def put(self, table: str, body: dict[str, Any], prefix: str) -> Stored:
        rec = Stored(id=new_id(prefix), created_at=now(), body=body)
        with self._lock:
            self.tables[table][rec.id] = rec
        return rec

    def get(self, table: str, rec_id: str) -> Stored | None:
        with self._lock:
            return self.tables[table].get(rec_id)

    def list(self, table: str) -> list[Stored]:
        with self._lock:
            return list(self.tables[table].values())

    def trust_for(self, object_id: str) -> Stored | None:
        with self._lock:
            items = [r for r in self.tables["trust"].values() if r.body.get("object_id") == object_id]
            return items[-1] if items else None

    def put_trust(self, body: dict[str, Any]) -> Stored:
        """Check and append a trust state under one lock, so stale writes cannot clear a restriction."""
        with self._lock:
            current = self.trust_for(body["object_id"])
            restricted = {"HOLD", "REVOKED", "RECALLED", "EXPIRED", "DISPUTED"}
            if current and current.body["state"] in restricted:
                proposed = body["state"]
                # A recorded restriction cannot be cleared by more evidence or an
                # unauthenticated decision. HOLD may escalate to a terminal state.
                if current.body["state"] != "HOLD" or proposed not in {"REVOKED", "RECALLED", "EXPIRED"}:
                    body = {**body, "state": current.body["state"]}
            return self.put("trust", body, "ts")


STORE = MemoryStore()
