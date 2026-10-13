from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime,func
from sqlalchemy.orm import relationship
from app.db.base import Base



class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    published_year = Column(Integer, nullable=False)

    author_id = Column(Integer,ForeignKey("authors.id",onupdate="RESTRICT"),nullable=False)
    category_id = Column(Integer,ForeignKey("categories.id",onupdate="RESTRICT"),nullable=False)

    cover_image = Column(String(255), nullable=True)

    create_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, onupdate=func.now())

    # relationship with author, category
    author = relationship("Author", back_populates="books")
    category  = relationship("Category", back_populates="books")

