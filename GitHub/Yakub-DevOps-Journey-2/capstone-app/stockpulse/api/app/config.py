"""Configuration comes from the environment. Nothing is hard-coded.

WHY: the same image must run on your laptop, in CI, and on Kubernetes without being
rebuilt. The only thing that changes between them is the environment.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # SQLite by default so tests and local dev need no services running.
    # docker-compose and Kubernetes override this with a Postgres URL.
    database_url: str = "sqlite:///./stockpulse.db"

    # Optional. If Redis is unreachable the app still works, just without caching.
    # A cache should never be a hard dependency for a read path.
    redis_url: str = ""

    app_env: str = "development"
    cache_ttl_seconds: int = 30

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
