from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.goal import Goal
from schemas.goal import GoalCreate, GoalResponse
import uuid


router = APIRouter(prefix="/goals", tags=["Goals"])

@router.post("/{user_id}", response_model=GoalResponse)
def create_goal(user_id: uuid.UUID, goal: GoalCreate, db: Session = Depends(get_db)):
    new_goal = Goal(
        id=uuid.uuid4(),
        user_id=user_id,
        name=goal.name,
        target_amount=goal.target_amount,
        deadline=goal.deadline
    )

    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return new_goal

@router.get("/{user_id}", response_model=list[GoalResponse])
def get_goal(user_id: uuid.UUID, db: Session = Depends(get_db)):
    return db.query(Goal).filter(Goal.id == user_id).all()