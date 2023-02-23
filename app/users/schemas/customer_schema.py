"""Module for customer schemas."""
from pydantic import UUID4, BaseModel, EmailStr
from pydantic.schema import Optional
from app.users.enums import UserRole, UserStatus


class CustomerSchema(BaseModel):
    """A schema representing a Customer."""
    id: UUID4
    username: str
    email: str
    password: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.CUSTOMER

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class CustomerSchemaIn(BaseModel):
    """A schema representing a Customer creation request"""
    username: str
    email: EmailStr
    password: str

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class CustomerSchemaOut(BaseModel):
    """A schema representing a base of Customer."""
    username: str
    email: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.CUSTOMER

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class UpdateCustomerStatusSchema(BaseModel):
    """Schema for updating Customer status."""
    customer_id: str
    status: UserStatus

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True


class UpdateCustomerEmailSchema(BaseModel):
    """Schema for updating Customer email."""
    customer_id: str
    email: EmailStr

    class Config:
        """Configuration options for the Pydantic BaseModel."""
        orm_mode = True
