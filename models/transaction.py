import uuid
import enum


from sqlalchemy import Column, String, Enum, Numeric, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base
from datetime import datetime

class TransactionType(enum.Enum):
    income = "income"
    expense = "expense"

class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    date = Column(DateTime, default=datetime, nullable=False)

    user = relationship("User", back_populates="transactions")