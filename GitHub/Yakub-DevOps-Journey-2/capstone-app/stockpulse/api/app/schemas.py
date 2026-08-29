from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class ItemCreate(BaseModel):
    sku: str = Field(min_length=2, max_length=40)
    name: str = Field(min_length=1, max_length=120)
    category: str = "general"
    unit: str = "pcs"
    quantity: int = Field(default=0, ge=0)
    reorder_level: int = Field(default=5, ge=0)


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    unit: Optional[str] = None
    reorder_level: Optional[int] = Field(default=None, ge=0)


class ItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    sku: str
    name: str
    category: str
    unit: str
    quantity: int
    reorder_level: int
    is_low_stock: bool
    updated_at: datetime


class MovementCreate(BaseModel):
    sku: str
    kind: Literal["in", "out", "adjust"]
    quantity: int = Field(gt=0)
    note: str = ""


class MovementOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    item_id: int
    kind: str
    quantity: int
    note: str
    created_at: datetime


class Summary(BaseModel):
    total_items: int
    total_units: int
    low_stock_count: int
    categories: dict[str, int]
    cached: bool
