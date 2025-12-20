
print("RUN_REVIEW.PY IS EXECUTING")
from agents.design_review_agent import DesignReviewAgent
from pipeline.reliability_pipeline import run_reliability_pipeline
from pipeline.schema import ReliabilityInput


def main():
    # 1. 準備 pipeline 的輸入資料
    input_data = ReliabilityInput(
        test_type="drop",
        impact_scenario="corner_drop",
        system_scope="housing_only",
        screw_to_edge_distance_mm=2.1,
        material_youngs_modulus_gpa=70.0,
    )

    # 2. 執行 reliability pipeline
    pipeline_output = run_reliability_pipeline(input_data)

    # 3. 讓 agent 做 review
    agent = DesignReviewAgent()
    review_notes = agent.review(pipeline_output)

    # 4. 印出結果
    print("=== Pipeline Output ===")
    print(pipeline_output)

    print("\n=== Design Review Agent Output ===")
    print(review_notes)


if __name__ == "__main__":
    main()
