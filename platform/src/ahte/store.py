from __future__ import annotations

from threading import Lock
from typing import Any

from .models import Stored, new_id, now


class MemoryStore:
    def __init__(self) -> None:
        self._lock = Lock()
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
        return self.tables[table].get(rec_id)

    def list(self, table: str) -> list[Stored]:
        return list(self.tables[table].values())

    def trust_for(self, object_id: str) -> Stored | None:
        items = [r for r in self.tables["trust"].values() if r.body.get("object_id") == object_id]
        return items[-1] if items else None


STORE = MemoryStore()
