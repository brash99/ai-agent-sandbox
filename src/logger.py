import json
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def save_response(data: dict, prefix: str = "run") -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = LOG_DIR / f"{prefix}_{timestamp}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return str(path)
