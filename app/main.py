from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endponts import author,category,book

app = FastAPI(
    title="book management api",
    description="simple api to manage book, author, category and book covers",
    version="1.0.0"
)

app.include_router(author.router,prefix="/author", tags=["Author"])
app.include_router(category.router,prefix="/category", tags=["Category"])
app.include_router(book.router,prefix="/book", tags=["Book"])

@app.get("/") #127.0.0.1:8000/
def read_roof():
    return {"message":"hello world"}
