package halal.platinum

import rego.v1

default allow := false
default hti_score := 0.0
default quarantine_required := false

# Caller-supplied madhab_scores are assertions, not computed fiqh.
allow if {
	not quarantine_required
	shafii_baseline_satisfied
	destination_weight_gate
	facility_in_fixture_registry
	slaughter_fields_present
	cold_chain_maintained
	spatial_segregation_valid
}

shafii_baseline_satisfied if {
	input.madhab_scores.shafii >= 1.0
}

destination_weight_gate if {
	dest := input.logistics.destination_country
	weights := data.corridor_weights[dest]
	computed_score := (weights.shafii * input.madhab_scores.shafii) + (weights.hanafi * input.madhab_scores.hanafi) + (weights.maliki * input.madhab_scores.maliki) + (weights.hanbali * input.madhab_scores.hanbali)
	computed_score >= 1.0
}

facility_in_fixture_registry if {
	facility := data.accredited_registry[input.slaughterhouse.facility_id]
	facility.status == "ACTIVE"
	facility.not_jakim_listing == true
}

slaughter_fields_present if {
	input.slaughterhouse.slaughterer_credential_active == true
	input.slaughterhouse.cut_validation.trachea_cut == true
	input.slaughterhouse.cut_validation.esophagus_cut == true
	input.slaughterhouse.cut_validation.carotid_jugular_cut == true
	input.slaughterhouse.mechanical_blade == false
}

cold_chain_maintained if {
	input.telemetry.temp_celsius >= -25.0
	input.telemetry.temp_celsius <= -18.0
	input.telemetry.seal_tamper_detected == false
}

spatial_segregation_valid if {
	input.wms.cross_contamination_detected == false
	input.wms.segregation_distance_meters >= 3.0
}

quarantine_required if {
	input.telemetry.seal_tamper_detected == true
}

quarantine_required if {
	input.telemetry.temp_celsius > -18.0
}

quarantine_required if {
	input.wms.cross_contamination_detected == true
}

hti_score := calculated_hti if {
	allow
	s_halal := 1.0
	s_science := input.hti_metrics.science_score
	s_process := input.hti_metrics.process_score
	s_trace := input.hti_metrics.traceability_score
	s_esg := input.hti_metrics.esg_score
	calculated_hti := (s_halal * 40.0) + (s_science * 20.0) + (s_process * 15.0) + (s_trace * 15.0) + (s_esg * 10.0)
}

reasons contains "CRITICAL: Physical smart seal compromised" if {
	input.telemetry.seal_tamper_detected == true
}

reasons contains "CRITICAL: Cold chain threshold breached" if {
	input.telemetry.temp_celsius > -18.0
}

reasons contains "VIOLATION: Spatial segregation breached in WMS" if {
	input.wms.segregation_distance_meters < 3.0
}
