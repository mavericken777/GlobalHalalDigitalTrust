# Standards alignment (reference engine)

| Domain | Referenced standard | Code | Limit |
|---|---|---|---|
| Supply-chain events | GS1 EPCIS 2.0 shaped payload | `runtime/gateway/models.py` | Shape only; not a certified EPCIS repository |
| Halal food model | MS 1500 / SMIIC 1 themes | `runtime/policies/halal_gate.rego` | Policy paraphrase; licensed clauses not reproduced |
| Digital assertions | W3C VC-like signed JSON | `runtime/gateway/crypto.py` | Project assertion, not a statutory certificate |
| Cold-chain demo bound | Demo -25 to -18 C | `valid_temperature` | Fixture bound, not a universal Codex rule |
| Facility registry | `runtime/policies/data.json` | Fixture IDs only | **Not a JAKIM / BPJPH / SFDA / DAFF list** |

## Statutory disclaimer

This engine evaluates demo telemetry against demo policy. Physical certification, ritual compliance, and corridor release remain with accredited competent authorities. Facility keys prefixed `FIXTURE-` are simulated.
