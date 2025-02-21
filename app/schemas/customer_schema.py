
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from .product_schema import ProductSchema

class CustomerSchema(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr] 
    address: Optional[str]

    class Config:
        orm_mode = True


class CustomerWithProductsSchema(CustomerSchema):
    products: List[ProductSchema] = []
    