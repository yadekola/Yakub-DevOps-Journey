"""Seed the database with realistic sample data.

Run:  python -m app.seed
Idempotent: existing SKUs are skipped, so it is safe to run repeatedly - which matters
when it runs as a Kubernetes init container or a Job.
"""
from sqlalchemy import select

from .db import Base, SessionLocal, engine
from .models import Item, Movement

SAMPLE = [
    ("BEV-001", "Bottled Water 75cl", "beverages", "crate", 40, 10),
    ("BEV-002", "Malt Drink 33cl", "beverages", "crate", 12, 8),
    ("BEV-003", "Orange Juice 1L", "beverages", "pcs", 6, 6),
    ("STA-001", "A4 Paper Ream", "stationery", "ream", 25, 5),
    ("STA-002", "Blue Biro", "stationery", "box", 3, 5),
    ("STA-003", "Stapler", "stationery", "pcs", 14, 4),
    ("CLN-001", "Bleach 1L", "cleaning", "pcs", 18, 6),
    ("CLN-002", "Hand Soap 500ml", "cleaning", "pcs", 2, 5),
    ("ELE-001", "LED Bulb 12W", "electrical", "pcs", 55, 15),
    ("ELE-002", "Extension Cable 3m", "electrical", "pcs", 4, 5),
    ("ELE-003", "AA Batteries", "electrical", "pack", 30, 10),
    ("FOO-001", "Rice 5kg", "food", "bag", 22, 8),
]


def run():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    created = skipped = 0
    try:
        for sku, name, category, unit, qty, reorder in SAMPLE:
            if db.scalar(select(Item).where(Item.sku == sku)):
                skipped += 1
                continue
            item = Item(
                sku=sku, name=name, category=category, unit=unit,
                quantity=qty, reorder_level=reorder,
            )
            db.add(item)
            db.flush()
            db.add(Movement(
                item_id=item.id, kind="in", quantity=qty, note="opening stock",
            ))
            created += 1
        db.commit()
        print(f"seed complete: {created} created, {skipped} already present")
    finally:
        db.close()


if __name__ == "__main__":
    run()
