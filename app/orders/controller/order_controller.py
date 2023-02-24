"""Module for order controller."""
from datetime import datetime
from uuid import uuid4

from fastapi import HTTPException, Response
from app.orders.exceptions import OrderExceptionCode, OrderNotFoundException, InvalidOrderStatusError
from app.orders.models import OrderStatus
from app.orders.services import OrderService


class OrderController:
    """A controller for handling requests related to orders."""
    @staticmethod
    def create_order(user_id: str, shipping_address: str, artwork_id: str, shipping: float):
        """Creates a new order in the database."""
        try:
            OrderService.create_order(user_id, shipping_address, artwork_id, shipping)
        except OrderExceptionCode as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except InvalidOrderStatusError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def get_all_orders():
        """Gets all artworks from the database."""
        orders = OrderService.get_all_orders()
        return orders

    @staticmethod
    def get_order_by_id(order_id: str):
        """Gets an order from the database by its id."""
        try:
            order = OrderService.get_order_by_id(order_id)
            return order
        except OrderNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))

    @staticmethod
    def get_order_by_artwork_id(artwork_id: str):
        """Gets an order from the database by the artwork id."""
        try:
            orders = OrderService.get_order_by_artwork_id(artwork_id)
            return orders
        except ValueError:
            OrderNotFoundException(code=404, message=f"Order with artwork ID {artwork_id} not found.")

    @staticmethod
    def get_orders_by_user_or_status(user_id: str = None, order_status: OrderStatus = None):
        """Gets a list of orders matching the specified criteria."""
        orders = OrderService.get_orders_by_user_or_status(user_id, order_status)
        return orders

    @staticmethod
    def get_orders_in_date_range(from_date: str, to_date: str):
        """Gets a list of orders created in the specified date range."""
        orders = OrderService.get_orders_in_date_range(from_date, to_date)
        return orders

    @staticmethod
    def get_artist_summary_report(from_date: datetime, to_date: datetime, artist_id: uuid4):
        """Returns a summary report of an artist's sales for a given period."""
        try:
            report = OrderService.get_artist_summary_report(from_date, to_date, artist_id)
            return {
                artist_id: {
                    "number_of_art_sold": report["number_of_art_sold"],
                    "total_price_of_art_sold": report["total_price_of_art_sold"],
                    "from_date": from_date,
                    "to_date": to_date
                }
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_order_status(order_id: str, status: str):
        """Updates an existing order status."""
        try:
            order_status = OrderStatus(status)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid order status '{status}'")
        try:
            order = OrderService.update_order_status(order_id, order_status)
            return order
        except OrderNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))

    @staticmethod
    def delete_order(order_id: str):
        """Deletes an order from the database by its id."""
        try:
            OrderService.delete_order(order_id)
            return Response(status_code=204)
        except OrderNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
