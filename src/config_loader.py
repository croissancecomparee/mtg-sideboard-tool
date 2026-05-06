import json
from pathlib import Path

def load_formats_config():
    config_path = Path("config/formats.json")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)