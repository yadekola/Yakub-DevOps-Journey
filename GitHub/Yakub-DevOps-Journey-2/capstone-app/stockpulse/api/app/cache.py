"""Redis cache wrapper that degrades gracefully.

WHY this matters for DevOps: if Redis goes down and the whole API returns 500, you have
built a system where a cache outage is a total outage. Every method here swallows the
connection error and falls back to "no cache". The app gets slower, not broken.

You will demonstrate exactly this in the capstone: kill the Redis pod, show the app still
serving, show the cache_hits metric flatline in Grafana.
"""
import json
import logging

from .config import settings

log = logging.getLogger("stockpulse.cache")

_client = None


def get_client():
    global _client
    if not settings.redis_url:
        return None
    if _client is None:
        try:
            import redis

            _client = redis.Redis.from_url(
                settings.redis_url, socket_connect_timeout=1, socket_timeout=1
            )
            _client.ping()
        except Exception as exc:          # noqa: BLE001 - any failure means "no cache"
            log.warning("cache unavailable, continuing without it: %s", exc)
            _client = None
    return _client


def get(key: str):
    c = get_client()
    if not c:
        return None
    try:
        raw = c.get(key)
        return json.loads(raw) if raw else None
    except Exception as exc:              # noqa: BLE001
        log.warning("cache read failed: %s", exc)
        return None


def setex(key: str, value, ttl: int | None = None) -> bool:
    c = get_client()
    if not c:
        return False
    try:
        c.setex(key, ttl or settings.cache_ttl_seconds, json.dumps(value))
        return True
    except Exception as exc:              # noqa: BLE001
        log.warning("cache write failed: %s", exc)
        return False


def invalidate(*keys: str) -> None:
    """Called on every write. A cache you never invalidate is a bug generator."""
    c = get_client()
    if not c:
        return
    try:
        c.delete(*keys)
    except Exception as exc:              # noqa: BLE001
        log.warning("cache invalidate failed: %s", exc)


def is_healthy() -> bool:
    c = get_client()
    if not c:
        return False
    try:
        return bool(c.ping())
    except Exception:                     # noqa: BLE001
        return False
