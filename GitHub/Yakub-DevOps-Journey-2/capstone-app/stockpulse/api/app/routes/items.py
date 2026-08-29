from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .. import cache
from ..db import get_db
from ..models import Item
from ..schemas import ItemCreate, ItemOut, ItemUpdate

router = APIRouter(prefix="/api/items", tags=["items"])

SUMMARY_KEY = "stockpulse:summary"


@router.get("", response_model=list[ItemOut])
def list_items(
    db: Session = Depends(get_db),
    category: str | None = None,
    search: str | None = None,
    limit: int = Query(default=100, le=500),
    offset: int = 0,
):
    stmt = select(Item)
    if category:
        stmt = stmt.where(Item.category == category)
    if search:
        stmt = stmt.where(Item.name.ilike(f"%{search}%"))
    stmt = stmt.order_by(Item.name).limit(limit).offset(offset)
    return db.scalars(stmt).all()


@router.get("/low-stock", response_model=list[ItemOut])
def low_stock(db: Session = Depends(get_db)):
    """Items at or below their reorder level. This is the whole point of the app."""
    stmt = select(Item).where(Item.quantity <= Item.reorder_level).order_by(Item.quantity)
    return db.scalars(stmt).all()


@router.get("/{item_id}", response_model=ItemOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="item not found")
    return item


@router.post("", response_model=ItemOut, status_code=201)
def create_item(payload: ItemCreate, db: Session = Depends(get_db)):
    item = Item(**payload.model_dump())
    db.add(item)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        # 409 not 500: a duplicate SKU is the caller's mistake, not a server fault.
        raise HTTPException(status_code=409, detail=f"sku '{payload.sku}' already exists")
    db.refresh(item)
    cache.invalidate(SUMMARY_KEY)
    return item


@router.patch("/{item_id}", response_model=ItemOut)
def update_item(item_id: int, payload: ItemUpdate, db: Session = Depends(get_db)):
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="item not found")
    # Quantity is deliberately NOT updatable here - stock only changes through a
    # movement, so there is always an audit trail. See routes/movements.py.
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(item, field, value)
    db.commit()
    db.refresh(item)
    cache.invalidate(SUMMARY_KEY)
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="item not found")
    db.delete(item)
    db.commit()
    cache.invalidate(SUMMARY_KEY)
