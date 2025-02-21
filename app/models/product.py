import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship
from ..db.database import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    price = Column(String(20), nullable=False)  # Fixed typo from 'prince' to 'price'

    owner_id = Column(CHAR(36), ForeignKey("customers.id"), nullable=False)
    owner = relationship("Customer", back_populates="products")