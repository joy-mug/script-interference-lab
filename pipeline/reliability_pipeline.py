def run_reliability_pipeline():
    return {
        "context": {
            "test_type": "drop",
            "failure_focus": "housing_crack",
            "impact_type": "corner"
        },
        "risk_score": 0.72,
        "risk_level": "High",
        "top_risk_factors": [
            {
                "proxy": "screw_to_edge_dist",
                "direction": "too_small",
                "contribution": 0.31
            },
            {
                "proxy": "youngs_modulus",
                "direction": "too_high_for_geometry",
                "contribution": 0.21
            }
        ]
    }
