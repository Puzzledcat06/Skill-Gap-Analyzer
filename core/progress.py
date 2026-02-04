import json
from pathlib import Path
from datetime import datetime

PROGRESS_FILE = Path("storage/progress.json")

def load_progress() -> dict:
    if not PROGRESS_FILE.exists():
        return {}
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_progress(user_id: str, role_id: str, results: list):
    data = load_progress()
    if user_id not in data:
        data[user_id] = []

    data[user_id].append({
        "role_id": role_id,
        "timestamp": datetime.utcnow().isoformat(),
        "results": results
    })

    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
