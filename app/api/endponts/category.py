from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app import models
from app.schemas.category import Category, CategoryCreate, CategoryUpdate

router = APIRouter()

@router.get("/", response_model=List[Category])
def list_category(
        skip: int = 0,
        limit: int = 100,
        db: Session =  Depends(get_db)
):
    """Get list categories, paginate sample use skip/limit"""
    categories = db.query(models.category).offset(skip).limit(limit).all()
    return categories

@router.get("/{cate_id}",response_model=Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    """Get category detail according id"""
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if  not category:
        raise  HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    return category

@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(
        category_in: CategoryCreate,
        db: Session = Depends(get_db)
):
   existing = db.query(models.Category).filter(models.Category.name == category_in).filter()
   if existing:
       raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST,
           detail="category with this name already exist",
       )

   category = models.Category(name = category_in, description = category_in.description)
   db.add(category)
   db.commit()
   db.refresh(category)

   return category

@router.put("/{cate_id}", response_model=Category)
def update_category(
        category_id:int,
        category_up: CategoryUpdate,
        db: Session = Depends(get_db)
):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="category not found",
        )

    if category_up.name is not  None and category_up.name != category.name:
        existing= db.query(models.Category).filter(models.Category.name==category_up.name).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="another category with this name already exists"
            )
        category.name = category_up.name

    if category_up.description is not None:
        category.description = category_up.description

    db.add(category)
    db.commit()
    db.refresh(category)
    return category

@router.delete("/{cate_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
        category_id:int,
        db:Session = Depends(get_db)
):
    categoty = db.query(models.Category).filter(models.Category.id == category_id).first()

    if not categoty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="category not found",
        )
    db.delete(categoty)
    db.commit()