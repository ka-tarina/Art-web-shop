from typing import List, Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    email: str
    password: str
    status: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    is_verified: Optional[bool]


class Customer(CustomerBase):
    id: str

    class Config:
        orm_mode = True


class CustomerInDB(Customer):
    password: str


class CustomerCollection(BaseModel):
    customers: List[Customer]
