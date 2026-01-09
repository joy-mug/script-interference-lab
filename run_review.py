import json
from governance.taxonomy import (
    LifecycleStage, LoadDriver, StructuralResponse, DamageSymptom, ConstraintState
)
from schema.reliability_input import CaseInput, FailureTags
from pipeline.reliability_pipeline import ReliabilityPipeline


def load_case(path: str) -> CaseInput:
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    tags = None
    if raw.get("tags"):
        t = raw["tags"]
        tags = FailureTags(
            load_driver=LoadDriver(t["load_driver"]),
            structural_response=[StructuralResponse(x) for x in t["structural_response"]],
            damage_symptom=[DamageSymptom(x) for x in t["damage_symptom"]],
            location_archetype=t["location_archetype"],
            constraint_state=ConstraintState(t["constraint_state"]),
        )

    return CaseInput(
        case_id=raw["case_id"],
        lifecycle_stage=LifecycleStage(raw["lifecycle_stage"]),
        failure_summary=raw["failure_summary"],
        test_context=raw["test_context"],
        repeatability=raw.get("repeatability"),
        design_state=raw.get("design_state"),
        contact_evidence=raw.get("contact_evidence"),
        ec_applied=raw.get("ec_applied"),
        ec_description=raw.get("ec_description"),
        ec_outcome=raw.get("ec_outcome"),
        tags=tags,
    )


if __name__ == "__main__":
    case = load_case("data/case_002.json")
    pipe = ReliabilityPipeline(data_dir="data")
    result = pipe.run(case)
    print(json.dumps(result, indent=2, ensure_ascii=False))
