"""Module for order schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, UUID4
from app.users.schemas import UserSchema


class OrderSchema(BaseModel):
    """A schema representing an Order stored in the database"""
    id: UUID4
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
    user_id: str
    shipping_address: str
    artwork_id: str
    shipping: int

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class ArtistSummaryReportSchema(BaseModel):
    """Schema for artist summary report request."""
    from_date: datetime
    to_date: datetime
    artist_id: UUID4

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class ArtistSummaryReportResponseSchema(BaseModel):
    """Schema for the response of an artist summary report."""
    artist_id: str
    number_of_art_sold: int
    total_price_of_art_sold: float
    from_date: datetime
    to_date: datetime

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True
