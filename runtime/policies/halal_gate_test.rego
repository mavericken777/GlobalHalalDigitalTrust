package halal.compliance_test

import rego.v1
import data.halal.compliance

test_compliant_event_allowed if {
	mock_event := {
		"eventType": "ObjectEvent",
		"action": "OBSERVE",
		"facility_id": "FIXTURE-MY-PL-1049",
		"telemetry": {
			"temp_celsius": -20.5,
			"seal_intact": true,
			"co_mingled_with_non_halal": false,
		},
	}
	compliance.allow with input as mock_event with data.accredited_facilities as data.accredited_facilities
}

test_temperature_breach_denied if {
	mock_event := {
		"eventType": "ObjectEvent",
		"action": "OBSERVE",
		"facility_id": "FIXTURE-MY-PL-1049",
		"telemetry": {
			"temp_celsius": -12.0,
			"seal_intact": true,
			"co_mingled_with_non_halal": false,
		},
	}
	not compliance.allow with input as mock_event
	compliance.violation_reason == "Cold chain threshold breached: outside -25C to -18C" with input as mock_event
}

test_unaccredited_facility_denied if {
	mock_event := {
		"eventType": "ObjectEvent",
		"action": "OBSERVE",
		"facility_id": "UNKNOWN-ABATTOIR-999",
		"telemetry": {
			"temp_celsius": -21.0,
			"seal_intact": true,
			"co_mingled_with_non_halal": false,
		},
	}
	not compliance.allow with input as mock_event
	compliance.violation_reason == "Facility not recognized or accreditation revoked" with input as mock_event
}

test_tampered_seal_denied if {
	mock_event := {
		"eventType": "ObjectEvent",
		"action": "OBSERVE",
		"facility_id": "FIXTURE-MY-PL-1049",
		"telemetry": {
			"temp_celsius": -20.0,
			"seal_intact": false,
			"co_mingled_with_non_halal": false,
		},
	}
	not compliance.allow with input as mock_event
	compliance.violation_reason == "Smart seal compromised during transit" with input as mock_event
}
