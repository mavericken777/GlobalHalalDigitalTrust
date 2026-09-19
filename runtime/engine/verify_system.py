from engine import (
    CanonicalCryptoEngine,
    Coordinate3D,
    CutValidation,
    HalalTrustEngine,
    IngestionPayload,
    MadhabScores,
    SlaughterhouseEvent,
    State,
    TelemetryRecord,
    WMSLocationEvent,
)


def base(**kwargs) -> IngestionPayload:
    payload = IngestionPayload(
        consignment_id="FIXTURE-B01",
        state=State.ST07,
        destination_country="ARE",
        slaughterhouse=SlaughterhouseEvent(
            facility_id="FIXTURE-MY-PL-1049",
            slaughterer_credential_active=True,
            cut_validation=CutValidation(
                trachea_cut=True, esophagus_cut=True, carotid_jugular_cut=True
            ),
            mechanical_blade=False,
        ),
        telemetry=TelemetryRecord(
            temp_celsius=-21.5, seal_tamper_detected=False, timestamp="2026-09-20T06:00:00Z"
        ),
        wms=WMSLocationEvent(
            bin_id="RACK-04-A",
            coordinates=Coordinate3D(x=10.0, y=15.0, z=2.0),
            adjacent_non_halal_coordinates=Coordinate3D(x=15.0, y=15.0, z=2.0),
            cross_contamination_detected=False,
        ),
        madhab_scores=MadhabScores(shafii=1.0),
    )
    return payload.model_copy(update=kwargs)


def run_tests() -> None:
    priv, pub = CanonicalCryptoEngine.generate_ed25519_keypair()
    eng = HalalTrustEngine(priv, pub)

    r1 = eng.evaluate_transaction(base())
    assert r1.state == State.ST08.value
    assert r1.hti_score == 0.0
    assert r1.certificate_issued is False

    r2 = eng.evaluate_transaction(base(telemetry=base().telemetry.model_copy(update={"temp_celsius": -14.0})))
    assert r2.state == State.ST11.value
    assert r2.hti_score == 0.0

    close = base().wms.model_copy(
        update={"adjacent_non_halal_coordinates": Coordinate3D(x=12.0, y=15.0, z=2.0)}
    )
    r3 = eng.evaluate_transaction(base(wms=close))
    assert r3.state == State.ST11.value

    r4 = eng.evaluate_transaction(base(madhab_scores=MadhabScores(shafii=0.8), state=State.ST01))
    assert r4.state == State.ST12.value

    r9 = eng.evaluate_transaction(base(state=State.ST08))
    assert r9.state == State.ST09.value
    assert r9.allowed is True
    assert r9.hti_score == 100.0

    print("engine invariants passed (reference FSM)")


if __name__ == "__main__":
    run_tests()
