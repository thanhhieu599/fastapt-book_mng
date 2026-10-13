from sqlalchemy import  Column, Integer, String, Text
from sqlalchemy.orm import  relationship
from app.db.base import Base

#xây dựng class author
class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),nullable=False,unique=True,index=True)
    bio = Column(Text,nullable=True)

    #relationship with book
    books = relationship("Book", back_populates="author")