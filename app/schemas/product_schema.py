
from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    name: str
    price: str

    class Config:
        orm_mode = True
