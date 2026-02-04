RECOMMENDATIONS = {
    "Python Programming": [
        "Revise Python basics (lists, dicts, functions).",
        "Practice pandas and NumPy for data manipulation.",
        "Solve small data cleaning tasks."
    ],
    "Feature Engineering": [
        "Learn encoding techniques (target, frequency, one-hot).",
        "Practice feature scaling and transformation.",
        "Work on feature selection using correlation and importance."
    ],
    "Model Training": [
        "Practice training baseline models (logistic regression, trees).",
        "Understand bias-variance tradeoff.",
        "Experiment with hyperparameter tuning."
    ],
    "Model Evaluation": [
        "Study evaluation metrics for imbalanced datasets.",
        "Practice cross-validation on real-world datasets.",
        "Analyze confusion matrix and ROC-AUC."
    ],
    "Model Deployment": [
        "Learn basics of REST APIs (FastAPI/Flask).",
        "Containerize a simple model using Docker.",
        "Explore basic CI/CD for ML pipelines."
    ],
    "SQL": [
        "Practice GROUP BY, JOINs, and window functions.",
        "Solve SQL interview-style problems."
    ],
    "Exploratory Data Analysis (EDA)": [
        "Practice identifying patterns and anomalies in datasets.",
        "Learn how to communicate insights using visualizations."
    ]
}

def get_recommendations(skill_name: str):
    return RECOMMENDATIONS.get(
        skill_name,
        ["Revise fundamentals and practice with real-world datasets."]
    )
