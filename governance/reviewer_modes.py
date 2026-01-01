from schema.reliability_input import CaseInput
from .taxonomy import LifecycleStage, ReviewerMode


def select_mode(case: CaseInput) -> ReviewerMode:
    if case.lifecycle_stage in (LifecycleStage.PROPOSAL, LifecycleStage.PROTOTYPE):
        return ReviewerMode.MODE_1
    return ReviewerMode.MODE_2


def gate_mode_1(case: CaseInput) -> list[str]:
    missing = []
    if not case.failure_summary:
        missing.append("failure_summary")
    if not case.test_context:
        missing.append("test_context (intended stress scenario)")
    return missing


def gate_mode_2(case: CaseInput) -> list[str]:
    missing = []
    if not case.failure_summary:
        missing.append("failure_summary")
    if not case.test_context:
        missing.append("test_context")
    # Mode 2 must declare evidence for primary driver if claiming direct contact etc.
    if case.contact_evidence is None:
        missing.append("contact_evidence (True/False)")
    if case.tags is None:
        missing.append("failure_tags (driver/response/damage/location/constraint)")
    return missing
