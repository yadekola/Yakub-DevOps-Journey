from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .. import cache
from ..db import get_db
from ..models import Item
from ..schemas import Summary

router = APIRouter(prefix="/api", tags=["summary"])

SUMMARY_KEY = "stockpulse:summary"


@router.get("/summary", response_model=Summary)
def summary(db: Session = Depends(get_db)):
    """Dashboard totals. Cached in Redis because the frontend polls this every few seconds.

    The `cached` field in the response is there on purpose: open the dashboard, watch it
    flip between true and false, and you can SEE the cache working. When you kill Redis in
    the capstone demo it stays false forever and the app keeps serving. That is the
    difference between a degraded system and a broken one.
    """
    hit = cache.get(SUMMARY_KEY)
    if hit:
        hit["cached"] = True
        return hit

    total_items = db.scalar(select(func.count()).select_from(Item)) or 0
    total_units = db.scalar(select(func.coalesce(func.sum(Item.quantity), 0))) or 0
    low = db.scalar(
        select(func.count()).select_from(Item).where(Item.quantity <= Item.reorder_level)
    ) or 0
    rows = db.execute(
        select(Item.category, func.count()).group_by(Item.category)
    ).all()

    payload = {
        "total_items": total_items,
        "total_units": int(total_units),
        "low_stock_count": low,
        "categories": {c: n for c, n in rows},
        "cached": False,
    }
    cache.setex(SUMMARY_KEY, payload)
    return payload
