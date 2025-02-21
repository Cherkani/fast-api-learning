import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship
from ..db.database import Base

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    status = Column(String(50), nullable=False, default="open")  # open, in_progress, closed

    assignee_id = Column(CHAR(36), ForeignKey("developers.id"), nullable=False)
    assignee = relationship("Developer", back_populates="tickets")
