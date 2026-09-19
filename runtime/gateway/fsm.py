class HalalFSMError(Exception):
    pass


class ConsignmentFSM:
    VALID_TRANSITIONS = {
        "INIT": ["INGREDIENT_REGISTERED"],
        "INGREDIENT_REGISTERED": ["ANTE_MORTEM_CLEARED", "REJECTED"],
        "ANTE_MORTEM_CLEARED": ["RITUAL_SLAUGHTER_RECORDED", "REJECTED"],
        "RITUAL_SLAUGHTER_RECORDED": ["POST_MORTEM_VERIFIED", "REJECTED"],
        "POST_MORTEM_VERIFIED": ["PROCESSING_SEGREGATED", "QUARANTINED", "REJECTED"],
        "PROCESSING_SEGREGATED": ["PACKAGED_SMART_SEALED", "QUARANTINED"],
        "PACKAGED_SMART_SEALED": ["COLD_CHAIN_IN_TRANSIT", "QUARANTINED"],
        "COLD_CHAIN_IN_TRANSIT": ["BORDER_PORT_INSPECTED", "QUARANTINED"],
        "BORDER_PORT_INSPECTED": ["CUSTOMS_RELEASED", "QUARANTINED"],
        "CUSTOMS_RELEASED": ["RETAIL_DISPENSING_ACTIVE", "QUARANTINED"],
        "RETAIL_DISPENSING_ACTIVE": [],
        "QUARANTINED": ["REJECTED"],
        "REJECTED": [],
    }

    def __init__(self, initial_state: str = "INIT"):
        self.current_state = initial_state

    def transition_to(self, target_state: str) -> str:
        allowed = self.VALID_TRANSITIONS.get(self.current_state, [])
        if target_state not in allowed:
            raise HalalFSMError(
                f"ILLEGAL_TRANSITION: {self.current_state} -> {target_state}"
            )
        self.current_state = target_state
        return self.current_state
