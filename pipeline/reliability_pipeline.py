import json
from pathlib import Path
from agents.design_review_agent import DesignReviewAgent

class ReliabilityPipeline:
    def __init__(self, data_dir: str = "data"):
        self.agent = DesignReviewAgent()
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.reviews_path = self.data_dir / "reviews.jsonl"

    def run(self, case_obj) -> dict:
        result = self.agent.review(case_obj)
        self._append_jsonl(self.reviews_path, result)
        return result

    def _append_jsonl(self, path: Path, obj: dict) -> None:
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")
