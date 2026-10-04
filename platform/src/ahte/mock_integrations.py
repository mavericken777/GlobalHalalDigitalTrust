from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4


def _id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:12]}"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class MockIntegrationHub:
    """Replaceable demonstration providers for the full China→GCC journey.

    These providers simulate connectivity and return clearly marked synthetic
    data. They preserve the production adapter boundary so a real connector can
    replace each provider without changing the domain workflow or UI.
    """

    def __init__(self) -> None:
        self.events: list[dict] = []

    def _event(self, system: str, action: str, payload: dict) -> dict:
        event = {
            "event_id": _id("mockevt"),
            "system": system,
            "action": action,
            "provider_state": "MOCK",
            "synthetic": True,
            "timestamp": _now(),
            "payload": payload,
        }
        self.events.append(event)
        return event

    def jakim(self, object_id: str, action: str = "status") -> dict:
        return self._event("DIRECT_JAKIM_API_ADAPTER", action, {
            "object_id": object_id,
            "authority": "JAKIM",
            "connection": "MOCK",
            "authority_decision": "DEMONSTRATION_ONLY",
            "requires_authorised_human_decision": True,
        })

    def laboratory(self, object_id: str, result: str = "NOT_DETECTED") -> dict:
        return self._event("CHINA_LABORATORY_ADAPTER", "sample_result", {
            "object_id": object_id,
            "sample_id": _id("sample"),
            "result": result,
            "interpretation": "NOT_DETECTED_IS_NOT_HALAL" if result == "NOT_DETECTED" else None,
            "chain_of_custody": "SIMULATED",
            "signed_result": "SIMULATED",
        })

    def sinotrans(self, shipment_id: str, status: str = "IN_TRANSIT") -> dict:
        return self._event("SINOTRANS_ADAPTER", "logistics_event", {
            "shipment_id": shipment_id,
            "status": status,
            "warehouse": "MOCK_SINOTRANS_WAREHOUSE",
            "container": f"MOCK-{shipment_id[-8:]}",
            "seal": f"SEAL-{shipment_id[-8:]}",
            "custody": "SIMULATED",
        })

    def port_customs(self, shipment_id: str, port: str = "ORIGIN_PORT") -> dict:
        return self._event("PORT_CUSTOMS_ADAPTER", "border_event", {
            "shipment_id": shipment_id,
            "port": port,
            "customs_state": "SIMULATED",
            "sovereign_release": False,
            "release_requires_authority": True,
        })

    def gcc(self, shipment_id: str, action: str = "receive") -> dict:
        return self._event("GCC_DESTINATION_ADAPTER", action, {
            "shipment_id": shipment_id,
            "destination": "GCC",
            "receiving_state": "SIMULATED",
            "verification": "AVAILABLE_FOR_DEMO",
        })

    def finance(self, object_id: str, action: str = "quote") -> dict:
        return self._event("SHARIAH_FINANCE_API_ADAPTER", action, {
            "object_id": object_id,
            "financing_state": "SIMULATED",
            "takaful_state": "SIMULATED",
            "approval": "NOT_GRANTED",
            "independent_financial_and_shariah_decision_required": True,
        })


MOCK_HUB = MockIntegrationHub()
