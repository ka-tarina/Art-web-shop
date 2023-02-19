from datetime import datetime
from typing import Optional
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.orders.models import Order
from app.orders.models.order_enum import OrderStatus


class OrderRepository:
    """A repository for CRUD operations on orders."""
    def __init__(self, db: Session):
        self.db = db

    def create_order(self,
                     user_id: str,
                     order_date: datetime,
                     total_price: float,
                     shipping_address: str,
                     artwork_id: str,
                     order_status: OrderStatus = OrderStatus.PENDING):
        """Creates a new order in the database"""
        try:
            order = Order(user_id=user_id,
                          order_date=order_date,
                          total_price=total_price,
                          shipping_address=shipping_address,
                          artwork_id=artwork_id,
                          order_status=order_status)
            self.db.add(order)
            self.db.commit()
            return order
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def get_order_by_id(self, order_id: str):
        """Gets an order from the database by its id."""
        try:
            return self.db.query(Order).filter(Order.id == order_id).first()
        except Exception as e:
            raise e

    def get_order_by_artwork_id(self, artwork_id: str):
        """Gets an order from the database by the artwork id."""
        try:
            order = self.db.query(Order).filter_by(artwork_id=artwork_id).all()
            if not order:
                raise ValueError(f"Order with artwork ID {artwork_id} not found.")
            return order
        except Exception as e:
            raise e

    def get_orders_by_user_or_status(self, user_id: Optional[str] = None, order_status: Optional[OrderStatus] = None):
        """Gets a list of orders matching the specified criteria."""
        try:
            query = self.db.query(Order)
            if user_id:
                query = query.filter(Order.user_id == user_id)
            if order_status:
                query = query.filter(Order.order_status == order_status)
            return query.all()
        except Exception as e:
            raise e

    def get_orders_in_date_range(self, from_date: datetime, to_date: datetime):
        try:
            return self.db.query(Order).filter(Order.order_date >= from_date, Order.order_date <= to_date).all()
        except Exception as e:
            raise e

    def update_order_status(self, order_id: str, status: OrderStatus):
        """Updates an existing order status."""
        try:
            order = self.get_order_by_id(order_id)
            if not order:
                raise ValueError(f"Order with ID {order_id} not found.")
            order.order_status = status
            self.db.commit()
            return order
        except IntegrityError as e:
            raise e

    def delete_order(self, order_id: str):
        """Deletes an order from the database by its id."""
        try:
            order = self.get_order_by_id(order_id)
            if not order:
                raise ValueError(f"Order with ID {order_id} not found.")
            self.db.delete(order)
            self.db.commit()
            return True
        except Exception as e:
            raise e
