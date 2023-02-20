from uuid import uuid4
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.users.schemas import UserSchema


class OrderBaseSchema(BaseModel):
    user_id: int
    shipping_address: str


class OrderCreateSchema(OrderBaseSchema):
    artwork_id: uuid4
    total_price: float
    order_date: Optional[datetime] = datetime.utcnow()
    order_status: Optional[str] = "Pending"


class OrderSchema(OrderBaseSchema):
    id: uuid4
    order_date: datetime
    order_status: str
    created_at: datetime
    updated_at: datetime
    user_id: uuid4
    user: Optional[UserSchema]

    class Config:
        orm_mode = True
