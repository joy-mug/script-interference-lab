from schema.reliability_input import CaseInput
from .taxonomy import ConfidenceLevel, ReviewerMode, EvidenceSource
from typing import Tuple, List

def assign_confidence(
    case: CaseInput,
    mode: ReviewerMode,
    evidence: EvidenceSource
) -> tuple[ConfidenceLevel, list[str]]:

    # Mode 1 is always hypothesis by governance.
    if mode == ReviewerMode.MODE_1:
        return ConfidenceLevel.L0, []

    # Mode 2 starts at Supported unless explicitly validated.
    # L2 requires: before/after test confirmation + repeatability info.
    has_repeatability = bool(case.repeatability and ("n=" in case.repeatability.lower() or "fail" in case.repeatability.lower()))
    has_ec_outcome = bool(case.ec_outcome and case.ec_outcome.lower() in ("pass", "fail", "partial"))
    has_before_after = bool(case.ec_applied is True and has_ec_outcome)

    # Track why L2 is blocked (internal, non-behavioral)
    l2_block_reasons = []

    if not has_before_after:
        l2_block_reasons.append("missing_ec_before_after_confirmation")

    if not has_repeatability:
        l2_block_reasons.append("missing_repeatability_evidence")

    if has_before_after and has_repeatability:
        # Still conservative: L2 implies validated outcome
        return ConfidenceLevel.L2, []

    return ConfidenceLevel.L1, l2_block_reasons
