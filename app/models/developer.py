import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship
from ..db.database import Base

class Developer(Base):
    __tablename__ = 'developers'
    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    level = Column(String(50), nullable=True)

    tickets = relationship("Ticket", back_populates="assignee")
