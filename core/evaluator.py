from typing import List

SCORE_MAP = {
    "none": 0,
    "partial": 1,
    "complete": 2
}

def score_checkpoint(level: str) -> int:
    return SCORE_MAP.get(level, 0)

def evaluate_subskill(checkpoint_scores: List[int]) -> float:
    if not checkpoint_scores:
        return 0.0
    return sum(checkpoint_scores) / len(checkpoint_scores)

def evaluate_skill(subskill_scores: List[float]) -> float:
    if not subskill_scores:
        return 0.0
    return sum(subskill_scores) / len(subskill_scores)
