from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.users.schemas import UserSchema


class OrderBaseSchema(BaseModel):
    user_id: int
    total_price: float
    shipping_address: str


class OrderCreateSchema(OrderBaseSchema):
    order_date: Optional[datetime] = datetime.utcnow()
    order_status: Optional[str] = "Pending"


class OrderSchema(OrderBaseSchema):
    id: str
    order_date: datetime
    order_status: str
    created_at: datetime
    updated_at: datetime
    user: Optional[UserSchema]

    class Config:
        orm_mode = True
