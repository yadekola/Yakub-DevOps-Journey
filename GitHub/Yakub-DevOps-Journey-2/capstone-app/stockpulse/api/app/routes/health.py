from fastapi import APIRouter, Depends, Response
from sqlalchemy import func, select, text
from sqlalchemy.orm import Session

from .. import cache, metrics
from ..config import settings
from ..db import get_db
from ..models import Item

router = APIRouter(tags=["ops"])


@router.get("/healthz")
def liveness():
    """LIVENESS: is the process alive? Must NOT touch the database.

    WHY: if this checked the DB, a brief database blip would make Kubernetes restart
    every healthy app pod - turning a small problem into an outage.
    """
    return {"status": "ok", "env": settings.app_env}


@router.get("/readyz")
def readiness(db: Session = Depends(get_db)):
    """READINESS: can this pod serve traffic right now? Checks its dependencies.

    Returns 503 when the database is unreachable, so Kubernetes takes the pod out of the
    Service until it recovers - without restarting it.
    """
    checks = {"database": False, "cache": cache.is_healthy()}
    try:
        db.execute(text("SELECT 1"))
        checks["database"] = True
    except Exception:                      # noqa: BLE001
        pass
    ready = checks["database"]             # cache is optional, database is not
    return Response(
        content=f'{{"ready": {str(ready).lower()}, "checks": {{"database": {str(checks["database"]).lower()}, "cache": {str(checks["cache"]).lower()}}}}}',
        media_type="application/json",
        status_code=200 if ready else 503,
    )


@router.get("/metrics")
def prometheus_metrics(db: Session = Depends(get_db)):
    """Prometheus scrapes this. Plain text, not JSON."""
    total_items = db.scalar(select(func.count()).select_from(Item)) or 0
    total_units = db.scalar(select(func.coalesce(func.sum(Item.quantity), 0))) or 0
    low = db.scalar(
        select(func.count()).select_from(Item).where(Item.quantity <= Item.reorder_level)
    ) or 0
    body = metrics.render({
        "stockpulse_items_total": total_items,
        "stockpulse_units_total": total_units,
        "stockpulse_low_stock_items": low,
        "stockpulse_cache_up": 1 if cache.is_healthy() else 0,
    })
    return Response(content=body, media_type="text/plain; version=0.0.4")
