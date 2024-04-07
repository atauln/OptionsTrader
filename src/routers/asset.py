from data import *
from fastapi import APIRouter, HTTPException
from db import application_layer, service_layer
from routers.router_utils import *
from finance import stocks, options

router = APIRouter(prefix="/assets")

# this class is for pulling asset data from market upstream
# TODO: implement this class, once we have a market data source

@router.get("/stock/{ticker}")
async def get_stock(ticker: str):
    stock = stocks.get_stock_data(ticker)
    if stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock