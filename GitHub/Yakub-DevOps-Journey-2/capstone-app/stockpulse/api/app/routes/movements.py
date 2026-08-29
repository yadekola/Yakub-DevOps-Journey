from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import cache
from ..db import get_db
from ..models import Item, Movement
from ..schemas import MovementCreate, MovementOut

router = APIRouter(prefix="/api/movements", tags=["movements"])

SUMMARY_KEY = "stockpulse:summary"


@router.get("", response_model=list[MovementOut])
def list_movements(
    db: Session = Depends(get_db),
    sku: str | None = None,
    limit: int = Query(default=50, le=200),
):
    stmt = select(Movement)
    if sku:
        item = db.scalar(select(Item).where(Item.sku == sku))
        if not item:
            raise HTTPException(status_code=404, detail=f"sku '{sku}' not found")
        stmt = stmt.where(Movement.item_id == item.id)
    stmt = stmt.order_by(Movement.created_at.desc()).limit(limit)
    return db.scalars(stmt).all()


@router.post("", response_model=MovementOut, status_code=201)
def create_movement(payload: MovementCreate, db: Session = Depends(get_db)):
    """Record a stock movement and apply it to the item's quantity.

    This is the only place item.quantity changes, so every change has an audit row.

    The business rule worth defending in an interview: stock cannot go negative. An
    'out' movement larger than the quantity on hand is rejected with 409 and NOTHING is
    written - not the movement, not the quantity change. Both changes happen in one
    transaction or neither does.
    """
    item = db.scalar(select(Item).where(Item.sku == payload.sku))
    if not item:
        raise HTTPException(status_code=404, detail=f"sku '{payload.sku}' not found")

    if payload.kind == "in":
        new_qty = item.quantity + payload.quantity
    elif payload.kind == "out":
        new_qty = item.quantity - payload.quantity
        if new_qty < 0:
            raise HTTPException(
                status_code=409,
                detail=(
                    f"insufficient stock for '{item.sku}': "
                    f"have {item.quantity}, tried to remove {payload.quantity}"
                ),
            )
    else:  # adjust = set an absolute count, e.g. after a physical stock take
        new_qty = payload.quantity

    movement = Movement(
        item_id=item.id, kind=payload.kind, quantity=payload.quantity, note=payload.note
    )
    item.quantity = new_qty
    db.add(movement)
    db.commit()               # one transaction: movement + new quantity, or neither
    db.refresh(movement)
    cache.invalidate(SUMMARY_KEY)
    return movement
