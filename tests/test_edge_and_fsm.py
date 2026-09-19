from datetime import datetime, timezone

from runtime_path import load_gateway


def test_seal_roundtrip():
    edge = load_gateway("edge_ingest")
    raw = edge.SmartSealTelemetryParser.encode_frame(
        int(datetime(2026, 9, 20, tzinfo=timezone.utc).timestamp()),
        -21.5,
        True,
        1.2,
        3.14,
        101.68,
    )
    decoded = edge.SmartSealTelemetryParser.decode_frame(raw)
    assert decoded["seal_intact"] is True
    assert abs(decoded["temp_celsius"] + 21.5) < 0.02


def test_fsm_one_hop():
    fsm_mod = load_gateway("fsm")
    fsm = fsm_mod.ConsignmentFSM("COLD_CHAIN_IN_TRANSIT")
    assert fsm.transition_to("BORDER_PORT_INSPECTED") == "BORDER_PORT_INSPECTED"
    try:
        fsm.transition_to("CUSTOMS_RELEASED")
        fsm.transition_to("CUSTOMS_RELEASED")
        raise AssertionError("double hop should fail on second CUSTOMS")
    except fsm_mod.HalalFSMError:
        pass
