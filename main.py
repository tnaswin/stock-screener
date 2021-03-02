import models
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel 
from models import  Stock

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


class StockRequest(BaseModel):
    symbol: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def home(request: Request):
    """
    Display the Homepage
    """
    return templates.TemplateResponse("home.html", {
        'request': request
    })


@app.post("/stock")
def create_stock(stock_request: StockRequest, db: Session = Depends(get_db)):
    """
    Create a stock and store in Database.
    """
    stock = Stock()
    stock.symbol = stock_request.symbol
    db.add(stock)
    db.commit()

    return {
        "code": "Success",
        "message": "Stock Created"
    }