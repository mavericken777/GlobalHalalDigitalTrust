package halal.compliance

import rego.v1

default allow := false
default violation_reason := ""

allow if {
	input.eventType == "ObjectEvent"
	valid_action
	valid_temperature
	certified_facility
	seal_intact
	not cross_contaminated
}

valid_action if {
	input.action == "OBSERVE"
}

valid_temperature if {
	input.telemetry.temp_celsius >= -25.0
	input.telemetry.temp_celsius <= -18.0
}

certified_facility if {
	facility := data.accredited_facilities[input.facility_id]
	facility.status == "ACTIVE"
}

seal_intact if {
	input.telemetry.seal_intact == true
}

cross_contaminated if {
	input.telemetry.co_mingled_with_non_halal == true
}

violation_reason := "Cold chain threshold breached: outside -25C to -18C" if {
	not valid_temperature
}

violation_reason := "Facility not recognized or accreditation revoked" if {
	not certified_facility
}

violation_reason := "Smart seal compromised during transit" if {
	not seal_intact
}

violation_reason := "Co-mingled with non-halal consignment" if {
	cross_contaminated
}
