from dataclasses import asdict
from schema.reliability_input import CaseInput
from governance.reviewer_modes import select_mode, gate_mode_1, gate_mode_2
from governance.evidence_rules import classify_evidence_source
from governance.confidence_model import assign_confidence


class DesignReviewAgent:
    def review(self, case: CaseInput) -> dict:
        mode = select_mode(case)
        missing = gate_mode_1(case) if mode.value == "proposal_prototype" else gate_mode_2(case)

        if missing:
            return {
                "status": "BLOCKED",
                "mode": mode.value,
                "missing_inputs": missing,
                "message": "Blocked by input completeness gates (spec_v1_1)."
            }

        evidence = classify_evidence_source(case)
        confidence = assign_confidence(case, mode, evidence)

        # Minimal “feedback” payload (expand later)
        return {
            "status": "OK",
            "mode": mode.value,
            "evidence_source": evidence.value,
            "confidence": confidence.value,
            "tags": asdict(case.tags) if case.tags else None,
            "recommendation": self._recommend(case),
            "case": asdict(case),
        }

    def _recommend(self, case: CaseInput) -> dict:
        # MVP: rule-driven, no overreach.
        # Always returns: hypothesis/rationale + next action + escalation flag
        tags = case.tags
        rec = {
            "top_hypothesis": None,
            "next_action": None,
            "escalate": False,
            "notes": []
        }

        if tags:
            rec["top_hypothesis"] = (
                f"{tags.load_driver.value} -> {', '.join([r.value for r in tags.structural_response])} "
                f"-> {', '.join([d.value for d in tags.damage_symptom])} @ {tags.location_archetype}"
            )

        # Decision ladder: prefer physical confirmation before CAE
        if case.ec_applied and not case.ec_outcome:
            rec["next_action"] = "Run confirmation drop test on multiple units; record N and fail count; declare EC outcome."
            rec["notes"].append("Confidence cannot upgrade without before/after physical confirmation.")
        elif case.ec_outcome in ("pass", "partial", "fail") and not case.repeatability:
            rec["next_action"] = "Provide repeatability data (N, fail count) to support confidence governance."
        else:
            rec["next_action"] = "Provide missing evidence fields or proceed to next discriminating test per escalation ladder."

        # Escalation triggers (minimal): disagreement/dispersion/safety would be fields later
        # Keep false by default in MVP.
        return rec
