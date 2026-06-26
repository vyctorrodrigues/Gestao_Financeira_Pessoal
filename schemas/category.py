from pydantic import BaseModel
import uuid
from enum import Enum

class CategoryType(str, Enum):
    income = 'income'
    expense = 'expense'

class CategoryCreate(BaseModel):
    name: str
    type: CategoryType

class CategoryResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    name: str
    type: CategoryType

    class Config:
        from_attributes = True