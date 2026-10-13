from pydantic import  BaseModel

class CategoryBase(BaseModel):
    """common field"""
    name: str
    description: str | None = None

class CategoryCreate(CategoryBase):
    """shema for creating category"""
    pass

class CategoryUpdate(BaseModel):
    name: str | None = None
    description: str | None = None

class CategoryInDBase(CategoryBase):
    id: int

    class config:
        orm_mode = True #pydantic read from SQLAchemy model

class Category(CategoryInDBase):
    """schema for returning to client"""
    pass


