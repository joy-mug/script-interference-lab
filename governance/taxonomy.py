from enum import Enum


class LifecycleStage(str, Enum):
    PROPOSAL = "proposal"
    PROTOTYPE = "prototype"
    EVT = "evt"
    DVT = "dvt"
    PVT = "pvt"


class ReviewerMode(str, Enum):
    MODE_1 = "proposal_prototype"
    MODE_2 = "evt_dvt_pvt_failure_review"


class EvidenceSource(str, Enum):
    REALITY = "reality_based"
    SIM_TREND = "simulation_trend_based"


class ConfidenceLevel(str, Enum):
    L0 = "hypothesis"
    L1 = "supported"
    L2 = "validated"
    L3 = "robust"


class LoadDriver(str, Enum):
    IMPACT_SHOCK = "impact_shock"
    INERTIAL_MASS = "inertial_mass_effect"
    QUASI_STATIC = "quasi_static_load"
    CYCLIC_FATIGUE = "cyclic_fatigue"
    THERMAL_ENV = "thermal_environmental"


class StructuralResponse(str, Enum):
    LOCAL_BENDING = "local_bending"
    GLOBAL_BENDING = "global_bending"
    STRESS_CONCENTRATION = "stress_concentration"
    CONSTRAINT_INSTABILITY = "constraint_instability"
    LOAD_PATH_REDIRECTION = "load_path_redirection"
    CONTACT_AMPLIFICATION = "contact_amplification"


class DamageSymptom(str, Enum):
    CRACK_FRACTURE = "crack_fracture"
    STRESS_WHITENING = "stress_whitening"
    PERM_DEFORMATION = "permanent_deformation"
    CREEP_RELAX = "creep_relaxation"
    COSMETIC_DEFECT = "cosmetic_defect"


class ConstraintState(str, Enum):
    RIGID = "rigidly_constrained"
    SEMI = "semi_constrained"
    FLOATING = "floating"
    VARIABLE = "constraint_unstable_variable"
