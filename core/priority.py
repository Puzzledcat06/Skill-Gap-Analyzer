def calculate_priority(importance_weight: int, skill_score: float) -> float:
    """
    Higher importance + lower score => higher priority
    Max skill_score = 2.0
    """
    priority = importance_weight * (2.0 - skill_score)
    return round(priority, 2)

def classify_skill(skill_score: float) -> str:
    if skill_score >= 1.5:
        return "strength"
    elif skill_score >= 1.0:
        return "needs_improvement"
    return "gap"
