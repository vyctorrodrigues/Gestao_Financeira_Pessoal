from pydantic import BaseModel
import uuid
from datetime import date


class GoalCreate(BaseModel):
    name: str
    target_amount : float
    deadline: date

class GoalResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    name: str
    target_amount: float
    deadline: date

    class Config:
        from_attributes = True