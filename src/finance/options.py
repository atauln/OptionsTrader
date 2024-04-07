from datetime import datetime, timedelta
from data import Option
import requests
from polygon import RESTClient
from dotenv import load_dotenv
import os

load_dotenv()

api_root_path = "https://api.marketdata.app/v1/options"
client = RESTClient(api_key=os.getenv("POLYGON_API_KEY"))

def get_options_data(ticker: str, strike_price: float, expiry: datetime, option_type: str, data_date: datetime = None) -> Option:
    if data_date is None:
        data_date = datetime.now()
    # TODO get options data from API
    pass

def get_exercise_returns(option: Option, quantity: int, data_date: datetime = None) -> float:
    if data_date is None:
        data_date = datetime.now()
    # TODO calculate exercise returns
    pass

def get_contract_sell_returns(option: Option, quantity: int, data_date: datetime = None) -> float:
    if data_date is None:
        data_date = datetime.now()
    # TODO calculate contract sell returns
    pass

def get_occ_format(option: Option) -> str:
    url = f"{api_root_path}/lookup/{option.ticker}%20{option.expiry.strftime('%d/%m/%Y')}%20{option.strike}%20{option.type}"
    response = requests.request("GET", url)
    return response.json()['optionSymbol']
