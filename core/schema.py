import json
from pathlib import Path

DATA_DIR = Path("data")

def load_role_schema(role_id: str) -> dict:
    path = DATA_DIR / f"{role_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"Role schema not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
