from schema.reliability_input import CaseInput
from .taxonomy import EvidenceSource


def classify_evidence_source(case: CaseInput) -> EvidenceSource:
    # MVP: treat physical witness marks / photos as reality evidence.
    # Simulation trend evidence is only used when explicitly supplied later.
    if case.contact_evidence is True or case.lifecycle_stage.value in ("evt", "dvt", "pvt"):
        return EvidenceSource.REALITY
    return EvidenceSource.REALITY
