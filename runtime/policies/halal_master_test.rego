package halal.platinum_test

import rego.v1
import data.halal.platinum

test_nominal_clearance if {
	input_data := {
		"slaughterhouse": {
			"facility_id": "FIXTURE-MY-PL-1049",
			"slaughterer_credential_active": true,
			"cut_validation": {"trachea_cut": true, "esophagus_cut": true, "carotid_jugular_cut": true},
			"mechanical_blade": false,
		},
		"telemetry": {"temp_celsius": -20.0, "seal_tamper_detected": false},
		"wms": {"cross_contamination_detected": false, "segregation_distance_meters": 5.0},
		"logistics": {"destination_country": "MYS"},
		"madhab_scores": {"shafii": 1.0, "hanafi": 1.0, "maliki": 1.0, "hanbali": 1.0},
		"hti_metrics": {"science_score": 1.0, "process_score": 1.0, "traceability_score": 1.0, "esg_score": 1.0},
	}
	platinum.allow with input as input_data
	platinum.hti_score == 100.0 with input as input_data
}

test_shafii_violation if {
	input_data := {
		"slaughterhouse": {
			"facility_id": "FIXTURE-MY-PL-1049",
			"slaughterer_credential_active": true,
			"cut_validation": {"trachea_cut": true, "esophagus_cut": true, "carotid_jugular_cut": true},
			"mechanical_blade": false,
		},
		"telemetry": {"temp_celsius": -20.0, "seal_tamper_detected": false},
		"wms": {"cross_contamination_detected": false, "segregation_distance_meters": 5.0},
		"logistics": {"destination_country": "MYS"},
		"madhab_scores": {"shafii": 0.8, "hanafi": 1.0, "maliki": 1.0, "hanbali": 1.0},
		"hti_metrics": {"science_score": 1.0, "process_score": 1.0, "traceability_score": 1.0, "esg_score": 1.0},
	}
	not platinum.allow with input as input_data
	platinum.hti_score == 0.0 with input as input_data
}

test_cold_chain_quarantine if {
	input_data := {
		"slaughterhouse": {
			"facility_id": "FIXTURE-MY-PL-1049",
			"slaughterer_credential_active": true,
			"cut_validation": {"trachea_cut": true, "esophagus_cut": true, "carotid_jugular_cut": true},
			"mechanical_blade": false,
		},
		"telemetry": {"temp_celsius": -14.0, "seal_tamper_detected": false},
		"wms": {"cross_contamination_detected": false, "segregation_distance_meters": 5.0},
		"logistics": {"destination_country": "MYS"},
		"madhab_scores": {"shafii": 1.0, "hanafi": 1.0, "maliki": 1.0, "hanbali": 1.0},
		"hti_metrics": {"science_score": 1.0, "process_score": 1.0, "traceability_score": 1.0, "esg_score": 1.0},
	}
	platinum.quarantine_required with input as input_data
	not platinum.allow with input as input_data
}
