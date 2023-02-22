"""Module defines enumeration class for OrderStatus."""
from enum import Enum


class OrderStatus(str, Enum):
    """Defines the possible status values for an order."""
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
