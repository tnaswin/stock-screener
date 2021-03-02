import models
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    """
    Display the Homepage
    """
    return templates.TemplateResponse("home.html", {
        'request': request
    })


@app.post("/stock")
def create_stock():
    """
    Create a stock and store in Database.
    """
    return {
        "code": "Success",
        "message": "Stock Created"
    }