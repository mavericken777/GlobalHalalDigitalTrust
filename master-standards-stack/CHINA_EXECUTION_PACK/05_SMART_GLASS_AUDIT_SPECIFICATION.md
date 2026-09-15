# 05 — SMART-GLASS AUDIT SPECIFICATION

## Mission

Provide field auditors with a hands-free interface into the AHTE Digital Audit Twin, Evidence Fabric and HCP engine while preserving human observation, evidence provenance and authority workflow.

## Hardware profile

Smart-glass client + authenticated mobile companion + camera + microphone where legally permitted + secure element/TPM + offline encrypted storage + barcode/QR/NFC reader + optional environmental sensors.

## Audit lifecycle

`PREPARE -> AUTHENTICATE -> LOAD SCOPE -> LOAD REQUIREMENTS -> FACILITY NAVIGATION -> ASSET IDENTIFICATION -> OBSERVATION -> EVIDENCE CAPTURE -> HCP TEST -> FINDING/CLEAR -> CAR -> RE-VERIFICATION -> CLOSE`

## Auditor screen modes

1. **Briefing:** site, scope, open findings, special controls.
2. **Requirement mode:** requirement ID, control objective, expected evidence, test method.
3. **Asset mode:** facility/line/equipment/material/batch identification and history.
4. **Observation mode:** spoken/typed note, photo/video, document scan, timestamp, location.
5. **HCP mode:** control test, measurement, witness, pass/fail/exception.
6. **Finding mode:** severity, evidence, owner, containment and due action.
7. **Closeout:** unresolved items, evidence completeness and signatures.

## Evidence binding

Every captured artifact is bound to `audit_id + requirement_id + HCP_id + subject_id + device_id + actor_id + location + time`. The client calculates an evidence digest before synchronisation.

## Offline operation

No connectivity is assumed at a factory. The device creates signed local records with monotonic sequence numbers. Synchronisation performs:

`device authentication -> clock reconciliation -> event hash-chain verification -> duplicate detection -> ordered upload -> server acknowledgement -> local retention policy`.

## AI assist

AI can suggest likely evidence gaps, duplicated observations, contradiction candidates or relevant requirements. Suggestions remain visibly labelled as machine assistance and never overwrite the auditor’s recorded observation.

## Environmental and physical checks

Where the applicable standard/control calls for temperature, cleanliness, zoning, seal condition, equipment status or other measurable observations, the auditor records the measurement source and calibration/verification reference where applicable.

## Sertu workflow support

Where sertu is required, the device provides a controlled checklist, authority/witness capture, material/water evidence, location, operator identity, commencement/completion and verification record. It does not replace the required competent-person/authority determination.

## Evidence quality gates

The capture screen must enforce: subject identified, requirement linked, timestamp valid, operator authenticated, image/document legible, source stated, chain-of-custody present for samples, and exception reason when evidence is absent.

## Security

Device certificate authentication, biometric/local-device policy as approved by the operating organisation, encrypted local storage, remote revocation, secure boot, signed application package and tamper-event reporting.

## Auditor analytics

Dashboard: completion percentage, evidence coverage, HCP test coverage, open findings, repeated findings, change anomalies, unresolved exceptions, elapsed audit time and re-verification readiness.

## Closeout package

A signed audit bundle contains scope, requirement set, observations, evidence digests, findings, corrective actions, signatures, event sequence and final submission state.
