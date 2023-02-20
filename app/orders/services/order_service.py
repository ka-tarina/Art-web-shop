from datetime import datetime
from typing import List, Optional
from uuid import uuid4

from app.artworks.repository import ArtworkRepository
from app.orders.models import OrderStatus
from app.orders.repository import OrderRepository
from app.orders.exceptions import OrderExceptionCode, OrderNotFoundException, InvalidOrderStatusError
from app.db import SessionLocal


def repository_method_wrapper(func):
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            try:
                repository = OrderRepository(db)
                return func(repository, *args, **kwargs)
            except Exception as e:
                raise e
    return wrapper


class OrderService:
    """A service for handling orders."""
    @staticmethod
    def create_order(user_id: str,
                     shipping_address: str,
                     artwork_id: str,
                     shipping: float):
        """Creates a new order in the database"""
        with SessionLocal() as db:
            try:
                artwork_repository = ArtworkRepository(db)
                order_repository = OrderRepository(db)
                order_date = datetime.now()
                order_status = OrderStatus.PENDING
                artwork = order_repository.get_order_by_artwork_id(artwork_id)
                if not artwork:
                    raise OrderExceptionCode(message=f"Order for artwork already exists.", code=400)
                stock = artwork_repository.get_stock_by_id(artwork_id=artwork_id)
                if stock <= 0:
                    raise InvalidOrderStatusError(f"Artwork with ID {artwork_id} is out of stock.", code=400)
                total_price = artwork.price + shipping
                return order_repository.create_order(user_id=user_id,
                                                     order_date=order_date,
                                                     total_price=total_price,
                                                     shipping_address=shipping_address,
                                                     artwork_id=artwork_id,
                                                     order_status=order_status)
            except Exception as e:
                raise e

    @staticmethod
    @repository_method_wrapper
    def get_order_by_id(repository, order_id: str):
        """Gets an order from the database by its id."""
        order = repository.get_order_by_id(order_id)
        return order.as_dict()

    @staticmethod
    @repository_method_wrapper
    def get_order_by_artwork_id(repository, artwork_id: str):
        """Gets an order from the database by the artwork id."""
        orders = repository.get_order_by_artwork_id(artwork_id)
        return [order.as_dict() for order in orders]

    @staticmethod
    @repository_method_wrapper
    def get_orders_by_user_or_status(repository,
                                     user_id: Optional[str] = None,
                                     order_status: Optional[OrderStatus] = None):
        """Gets a list of orders matching the specified criteria."""
        orders = repository.get_orders_by_user_or_status(user_id, order_status)
        return [order.as_dict() for order in orders]

    @staticmethod
    @repository_method_wrapper
    def get_orders_in_date_range(repository, from_date: datetime, to_date: datetime):
        orders = repository.get_orders_in_date_range(from_date, to_date)
        return [order.as_dict() for order in orders]

    @staticmethod
    @repository_method_wrapper
    def update_order_status(repository, order_id: str, status: OrderStatus):
        """Updates an existing order status."""
        order = repository.update_order_status(order_id, status)
        return order.as_dict()

    @staticmethod
    def get_artist_summary_report(from_date: datetime, to_date: datetime, artist_id: str):
        with SessionLocal() as db:
            try:
                repository = OrderRepository(db)
                orders = repository.get_orders_in_date_range(from_date, to_date)
                artist_orders = [order for order in orders if order.artwork.artist_id == artist_id]

                num_art_sold = len(artist_orders)
                total_price_of_art_sold = sum(order.total_price for order in artist_orders)

                return {
                    artist_id: {
                        "number_of_art_sold": num_art_sold,
                        "total_price_of_art_sold": total_price_of_art_sold,
                        "from_date": from_date,
                        "to_date": to_date
                    }
                }
            except Exception as e:
                raise e

    @staticmethod
    @repository_method_wrapper
    def delete_order(repository, order_id: str):
        """Deletes an order from the database by its id."""
        return repository.delete_order(order_id)
