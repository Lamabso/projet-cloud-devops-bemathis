import json
from typing import Any, Dict
import yaml


def parse_content(raw: str, file_ext: str) -> Dict[str, Any]:
    """
    Parse raw string content from a JSON or YAML file.
    Returns a dict. Expected format: {"items": [...]} (or YAML equivalent).
    """
    ext = file_ext.lower().strip(".")
    if ext == "json":
        return json.loads(raw)
    if ext in ("yaml", "yml"):
        return yaml.safe_load(raw)
    raise ValueError(f"Unsupported file extension: {file_ext}")
