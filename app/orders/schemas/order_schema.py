"""Module for order schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, UUID4
from app.users.schemas import UserSchema


class OrderSchema(BaseModel):
    """A schema representing an Order stored in the database"""
    id: uuid4
    order_date: datetime
    order_status: str
    created_at: datetime
    updated_at: datetime
    user_id: UUID4
    user: Optional[UserSchema]

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class OrderSchemaIn(BaseModel):
    """Model for representing incoming Order data."""
    user_id: uuid4
    shipping_address: str
    artwork_id: UUID4
    total_price: float

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class DateRangeSchema(BaseModel):
    from_date: datetime
    to_date: datetime

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class ArtistSummaryReportSchema(BaseModel):
    from_date: datetime
    to_date: datetime
    artist_id: UUID4

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class ArtistSummaryReportResponseSchema(BaseModel):
    artist_id: str
    number_of_art_sold: int
    total_price_of_art_sold: float
    from_date: datetime
    to_date: datetime

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True

