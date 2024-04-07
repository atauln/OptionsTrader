from data import *
from db.service_layer import *
from datetime import datetime, timedelta

def calculateAccountBalance(a_id: int, timestamp: datetime = None) -> int:
    if timestamp is None:
        timestamp = datetime.now()
    account = getAccountById(a_id)
    transactions = getTransactionsByAccountId(a_id)
    if transactions is None:
        return account.init_balance
    balance = account.init_balance
    for transaction in [t for t in transactions if t.timestamp < timestamp + timedelta(days=1)]:
        if transaction.type == "buy":
            balance -= transaction.price_per_asset * transaction.quantity
        else:
            balance += transaction.price_per_asset * transaction.quantity
    return balance

def purchaseOptionsContract(a_id: int, ticker: str, price_per_contract: float, quantity: int, expiration: datetime, type: str, timestamp: datetime = None) -> int:
    if timestamp is None:
        timestamp = datetime.now()
    asset = getAssetBySymbol(ticker)
    transaction = insertTransaction(Transaction(0, a_id, asset.asset_id, timestamp, price_per_contract, quantity, "buy"))
    return insertContractData(ContractData(0, transaction, expiration, price_per_contract / 100, type))

def purchaseStock(a_id: int, ticker: str, price_per_stock: float, quantity: int, timestamp: datetime = None) -> int:
    if timestamp is None:
        timestamp = datetime.now()
    asset = getAssetBySymbol(ticker)
    transaction = insertTransaction(Transaction(0, a_id, asset.asset_id, timestamp, price_per_stock, quantity, "buy"))
    return transaction

def sellStock(a_id: int, ticker: str, price_per_stock: float, quantity: int, timestamp: datetime = None) -> int:
    if timestamp is None:
        timestamp = datetime.now()
    asset = getAssetBySymbol(ticker)
    transaction = insertTransaction(Transaction(0, a_id, asset.asset_id, timestamp, price_per_stock, quantity, "sell"))
    return transaction

def getCurrentAssets(a_id: int, timestamp: datetime = None) -> dict[str, int]:
    if timestamp is None:
        timestamp = datetime.now()
    transactions = getTransactionsByAccountId(a_id)
    assets = {}
    for transaction in transactions:
        asset = getAssetById(transaction.asset_id)
        if transaction.type == "buy":
            if asset.symbol in assets:
                assets[asset.symbol][0] += transaction.quantity
            else:
                assets[asset.symbol] = [transaction.quantity, transaction.price_per_asset]
        else:
            if asset.symbol in assets:
                assets[asset.symbol][0] -= transaction.quantity
            else:
                assets[asset.symbol] = [-transaction.quantity, transaction.price_per_asset]
    return assets
