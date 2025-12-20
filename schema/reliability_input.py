"""
Schema definition for reliability pipeline input.
Defines the allowed design discussion space.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class ReliabilityInput:
    # test context
    test_type: str                 # e.g. "drop"
    impact_scenario: str           # e.g. "corner_drop"
    system_scope: str              # e.g. "housing_only"

    # geometry / design proxies
    screw_to_edge_distance_mm: float
    material_youngs_modulus_gpa: float

    # optional CAE reference
    fea_result_id: Optional[str] = None
