from dataclasses import dataclass
from typing import Optional, List
from governance.taxonomy import (
    LifecycleStage, LoadDriver, StructuralResponse, DamageSymptom, ConstraintState
)


@dataclass
class FailureTags:
    load_driver: LoadDriver
    structural_response: List[StructuralResponse]
    damage_symptom: List[DamageSymptom]
    location_archetype: str
    constraint_state: ConstraintState


@dataclass
class CaseInput:
    case_id: str
    lifecycle_stage: LifecycleStage
    failure_summary: str
    test_context: str

    # Optional but powerful
    repeatability: Optional[str] = None          # e.g. "N=10, fail=3"
    design_state: Optional[str] = None           # narrative
    contact_evidence: Optional[bool] = None      # witness marks or not

    # EC tracking for confidence governance
    ec_applied: Optional[bool] = None
    ec_description: Optional[str] = None
    ec_outcome: Optional[str] = None             # "pass" | "fail" | "partial" | None

    tags: Optional[FailureTags] = None
