from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class TelemetryPayload(BaseModel):
    temp_celsius: float
    seal_intact: bool
    co_mingled_with_non_halal: bool


class EPCISObjectEvent(BaseModel):
    eventType: str = Field(default="ObjectEvent")
    eventTime: str
    action: str = Field(default="OBSERVE")
    bizStep: str
    facility_id: str
    epcList: List[str]
    telemetry: TelemetryPayload


class CredentialSubject(BaseModel):
    id: str
    batchId: str
    productDescription: str
    slaughterDate: str
    facilityId: str
    standardCompliance: str


class IssueCredentialRequest(BaseModel):
    subject: CredentialSubject
    issuer_did: str


class ProofModel(BaseModel):
    type: str = "Ed25519Signature2020"
    created: str
    verificationMethod: str
    proofPurpose: str = "assertionMethod"
    proofValue: str


class VerifiableCredential(BaseModel):
    context: List[str] = Field(
        default=["https://www.w3.org/2018/credentials/v1", "https://example.local/ahte/v1"],
        alias="@context",
    )
    id: str
    type: List[str] = ["VerifiableCredential", "HalalBatchAssertion"]
    issuer: str
    issuanceDate: str
    credentialSubject: CredentialSubject
    proof: Optional[ProofModel] = None
    disclaimer: str = "Technical assertion only. Not a statutory Halal certificate."

    model_config = {"populate_by_name": True}


class IngestionEvaluationResponse(BaseModel):
    status: str
    allowed: bool
    violation_reason: str
    epcis_hash: str
    notarized_receipt: Dict[str, Any]
