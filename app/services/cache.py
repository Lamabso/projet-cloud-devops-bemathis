from cachetools import TTLCache
from typing import Any, Optional


class MemoryTTLCache:
    def __init__(self, ttl_seconds: int = 60, maxsize: int = 128):
        self._cache = TTLCache(maxsize=maxsize, ttl=ttl_seconds)

    def get(self, key: str) -> Optional[Any]:
        return self._cache.get(key)

    def set(self, key: str, value: Any) -> None:
        self._cache[key] = value
