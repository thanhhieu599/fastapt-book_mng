from pydantic import BaseModel

class Settings(BaseModel):
    PROJECT_NAME: str = "Book manament API"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./app.db"

settings = Settings()
