from datetime import datetime, timedelta
from data import Stock
from polygon import RESTClient
from dotenv import load_dotenv
from polygon.rest.models import TickerSnapshot
import os

load_dotenv()

client = RESTClient(api_key=os.getenv("POLYGON_API_KEY"))

def get_stock_data(ticker: str, data_date: datetime = None) -> TickerSnapshot:
    if data_date is None:
        data_date = datetime.now()
    return client.get_snapshot_ticker("stocks", ticker)

def get_stock_returns(stock: Stock, quantity: int, data_date: datetime = None) -> float:
    if data_date is None:
        data_date = datetime.now()
    # TODO calculate stock returns
    pass

def get_top_gainers(data_date: datetime = None) -> list[TickerSnapshot]:
    if data_date is None:
        data_date = datetime.now()
    return client.get_snapshot_direction("stocks", "gainers")

def get_client() -> RESTClient:
    return client
