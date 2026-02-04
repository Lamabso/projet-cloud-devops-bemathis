from typing import Any, Dict, Tuple

from app.services.blob_client import LocalContentClient
from app.services.cache import MemoryTTLCache
from app.services.parser import parse_content


class ContentService:
    def __init__(self, client: LocalContentClient, cache: MemoryTTLCache):
        self.client = client
        self.cache = cache

    def get_items(self, filename: str) -> Dict[str, Any]:
        cached = self.cache.get(filename)
        if cached is not None:
            return cached

        raw = self.client.read_text(filename)
        ext = filename.split(".")[-1]
        parsed = parse_content(raw, ext)

        # Normalize response to always have {"items": [...]}
        if "items" not in parsed or not isinstance(parsed["items"], list):
            parsed = {"items": parsed.get("items", []) if isinstance(parsed, dict) else []}

        self.cache.set(filename, parsed)
        return parsed
