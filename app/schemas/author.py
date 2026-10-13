from pydantic import  BaseModel

class AuthorBase(BaseModel):
    """common field"""
    name: str
    bio: str | None = None

class AuthorCreate(AuthorBase):
    """shema for creating category"""
    pass

class AuthorUpdate(AuthorBase):
    name: str | None = None
    bio: str | None = None

class AuthorInDBase(AuthorBase):
    id: int

    class config:
        orm_mode = True #pydantic read from SQLAchemy model

class Author(AuthorBase):
    """schema for returning to client"""
    pass


