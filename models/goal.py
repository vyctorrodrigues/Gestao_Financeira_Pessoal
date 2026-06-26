import uuid
from sqlalchemy import Column, String, Numeric,Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class Goal(Base):
    __tablename__ = "goals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    target_amount = Column(Numeric(10,2), nullable=False)
    deadline = Column(Date, nullable=False)