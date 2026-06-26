from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.category import Category
from schemas.category import CategoryCreate, CategoryResponse
import uuid

router = APIRouter(prefix="/category", tags=["Category"])

@router.post("/{user_id}", response_model=CategoryResponse)

def read_category(user_id: uuid.UUID, category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(
        id=uuid.uuid4(),
        user_id=user_id,
        name=category.name,
        type=category.type
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.get("/{user_id}", response_model=list[CategoryResponse])
def get_categories(user_id: uuid.UUID, db: Session = Depends(get_db)):
    return db.query(Category).filter(Category.id == uuid.uuid4()).all()
