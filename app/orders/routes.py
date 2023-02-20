from typing import Optional
from datetime import datetime
from fastapi import APIRouter, HTTPException, Response
from app.orders.controller import OrderController
from app.orders.models import OrderStatus


order_router = APIRouter(tags=["orders"], prefix="/api/orders")


@order_router.post("/create-order")
def create_order(user_id: str, shipping_address: str, artwork_id: str, shipping: float):
    order = OrderController.create_order(user_id, shipping_address, artwork_id, shipping)
    return order.as_dict()


@order_router.get("/get-order-by-id/{order_id}")
def get_order_by_id(order_id: str):
    order = OrderController.get_order_by_id(order_id)
    return order


@order_router.get("/get-order-by-artwork-id/{artwork_id}")
def get_order_by_artwork_id(artwork_id: str):
    orders = OrderController.get_order_by_artwork_id(artwork_id)
    return orders


@order_router.get("/get-orders-by-user-or-status")
def get_orders_by_user_or_status(user_id: Optional[str] = None, order_status: Optional[OrderStatus] = None):
    orders = OrderController.get_orders_by_user_or_status(user_id, order_status)
    return orders


@order_router.get("/get-orders-in-date-range")
def get_orders_in_date_range(from_date: str, to_date: str):
    orders = OrderController.get_orders_in_date_range(from_date, to_date)
    return orders


@order_router.get("/artist-summary-report")
def get_artist_summary_report(from_date: datetime, to_date: datetime, artist_id: str):
    report = OrderController.get_artist_summary_report(from_date, to_date, artist_id)
    return {
        artist_id: {
            "number_of_art_sold": report["number_of_art_sold"],
            "total_price_of_art_sold": report["total_price_of_art_sold"],
            "from_date": from_date,
            "to_date": to_date
        }
    }


@order_router.put("/update-order-status/{order_id}")
def update_order_status(order_id: str, status: str):
    try:
        order_status = OrderStatus(status)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid order status '{status}'")
    order = OrderController.update_order_status(order_id, order_status)
    return order


@order_router.delete("/delete-order/{order_id}")
def delete_order(order_id: str):
    OrderController.delete_order(order_id)
    return Response(status_code=204)
