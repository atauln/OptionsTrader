import dataclasses
from datetime import datetime

@dataclasses.dataclass
class ContractData:
    c_id: int
    t_id: int
    expiry: datetime
    strike: float
    type: str

@dataclasses.dataclass
class Transaction:
    t_id: int
    a_id: int
    asset_id: int
    timestamp: datetime
    price_per_asset: float
    quantity: int
    type: str

@dataclasses.dataclass
class Asset:
    asset_id: int
    symbol: str
    type: str

@dataclasses.dataclass
class Account:
    a_id: int
    name: str
    init_balance: float


@dataclasses.dataclass
class Option:
    num_shares: int
    strike: float
    expiry: datetime
    type: str
    ticker: str
    price_per_share: float

@dataclasses.dataclass
class Stock:
    ticker: str
    price_per_share: float
