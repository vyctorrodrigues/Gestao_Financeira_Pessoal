from pydantic import BaseModel
import uuid
from enum import Enum
from datetime import datetime

class TransactionType(str, Enum):
    income = 'income'
    expense = 'expense'

class TransactionCreate(BaseModel):
    category_id: uuid.UUID
    amount: float
    type: TransactionType
    date: datetime

class TransactionResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    category_id: uuid.UUID
    amount: float
    type: TransactionType
    date: datetime

    class Config:
        from_attributes = True