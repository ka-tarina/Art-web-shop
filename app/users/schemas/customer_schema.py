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
        orm_mode = True


class CustomerSchemaIn(BaseModel):
    """A schema representing a Customer creation request"""
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class CustomerSchemaOut(BaseModel):
    """A schema representing a base of Customer."""
    username: str
    email: str
    status: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.CUSTOMER

    class Config:
        orm_mode = True


class UpdateCustomerSchema(BaseModel):
    customer_id: str
    status: Optional[UserStatus]
    email: Optional[EmailStr]

    class Config:
        orm_mode = True
