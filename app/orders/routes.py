"""
API for order management. It includes routes for
creating, deleting and updating orders.
"""
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Response
from app.orders.controller import OrderController
from app.orders.models import OrderStatus
from app.orders.schemas import (
    OrderSchema,
    OrderSchemaIn,
    ArtistSummaryReportSchema,
    ArtistSummaryReportResponseSchema
)

order_router = APIRouter(tags=["orders"], prefix="/api/orders")


@order_router.post("/create-order", response_model=OrderSchema)
def create_order(order: OrderSchemaIn):
    """Creates a new order."""
    new_order = OrderController.create_order(order.user_id,
                                             order.shipping_address,
                                             order.artwork_id,
                                             order.total_price)
    return new_order


@order_router.get("/get-order-by-id/{order_id}", response_model=OrderSchema)
def get_order_by_id(order_id: str):
    """Retrieves an order by id."""
    order = OrderController.get_order_by_id(order_id)
    return order


@order_router.get("/get-order-by-artwork-id/{artwork_id}", response_model=OrderSchema)
def get_order_by_artwork_id(artwork_id: str):
    """Retrieves orders by artwork ID."""
    orders = OrderController.get_order_by_artwork_id(artwork_id)
    return orders


@order_router.get("/get-orders-by-user-or-status", response_model=list[OrderSchema])
def get_orders_by_user_or_status(user_id: Optional[str] = None, order_status: Optional[OrderStatus] = None):
    """Retrieves orders by user ID or status."""
    orders = OrderController.get_orders_by_user_or_status(user_id, order_status)
    return orders


@order_router.get("/get-orders-in-date-range", response_model=list[OrderSchema])
def get_orders_in_date_range(from_date: str, to_date: str):
    """Retrieves orders within a specified date range."""
    orders = OrderController.get_orders_in_date_range(from_date, to_date)
    return orders


@order_router.get("/artist-summary-report", response_model=List[ArtistSummaryReportResponseSchema])
def get_artist_summary_report(artist_summary_report: ArtistSummaryReportSchema):
    """
    Retrieves a summary report of the number of art sold and
    total price of art sold by an artist within a specified date range.
    """
    report = OrderController.get_artist_summary_report(
        artist_summary_report.from_date,
        artist_summary_report.to_date,
        artist_summary_report.artist_id,
    )
    return [
        ArtistSummaryReportResponseSchema(
            artist_id=artist_summary_report.artist_id,
            number_of_art_sold=report["number_of_art_sold"],
            total_price_of_art_sold=report["total_price_of_art_sold"],
            from_date=artist_summary_report.from_date,
            to_date=artist_summary_report.to_date,
        )
    ]


@order_router.put("/update-order-status/{order_id}", response_model=OrderSchema)
def update_order_status(order_id: str, status: str):
    """Updates the status of an order."""
    try:
        order_status = OrderStatus(status)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid order status '{status}'")
    order = OrderController.update_order_status(order_id, order_status)
    return order


@order_router.delete("/delete-order/{order_id}")
def delete_order(order_id: str):
    """Deletes an order by ID."""
    OrderController.delete_order(order_id)
    return Response(status_code=204)
