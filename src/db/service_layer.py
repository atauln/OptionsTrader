from db import data_access_layer
from data import *

def getAccounts() -> list:
    accounts = []
    for account in data_access_layer.getAccounts():
        accounts.append(Account(*account))
    return accounts

def getAssets() -> list:
    assets = []
    for asset in data_access_layer.getAssets():
        assets.append(Asset(*asset))
    return assets

def getTransactions() -> list:
    transactions = []
    for transaction in data_access_layer.getTransactions():
        transactions.append(Transaction(*transaction))
    return transactions

def getContractData() -> list:
    contract_data = []
    for data in data_access_layer.getContractData():
        contract_data.append(ContractData(*data))
    return contract_data



def getAccountById(account_id: int) -> Account | None:
    account_info = data_access_layer.getAccountById(account_id)
    if account_info:
        return Account(*account_info)
    else:
        return None
    
def getAccountByName(name: str) -> Account | None:
    account_info = data_access_layer.getAccountByName(name)
    if account_info:
        return Account(*account_info)
    else:
        return None

def getAssetById(asset_id: int) -> Asset | None:
    asset_info = data_access_layer.getAssetById(asset_id)
    if asset_info:
        return Asset(*asset_info)
    else:
        return None

def getTransactionById(t_id: int) -> Transaction | None:
    transaction_info = data_access_layer.getTransactionById(t_id)
    if transaction_info:
        return Transaction(*transaction_info)
    else:
        return None

def getContractDataById(c_id: int) -> ContractData | None:
    contract_data_info = data_access_layer.getContractDataById(c_id)
    if contract_data_info:
        return ContractData(*contract_data_info)
    else:
        return None

def getAssetBySymbol(symbol: str) -> Asset | None:
    asset_info = data_access_layer.getAssetBySymbol(symbol)
    if asset_info:
        return Asset(*asset_info)
    else:
        return None

def getTransactionsByAccountId(account_id: int) -> list[Transaction]:
    transactions = []
    for transaction in data_access_layer.getTransactionsByAccountId(account_id):
        transactions.append(Transaction(*transaction))
    return transactions

def getTransactionsByAssetId(asset_id: int) -> list[Transaction]:
    transactions = []
    for transaction in data_access_layer.getTransactionsByAssetId(asset_id):
        transactions.append(Transaction(*transaction))
    return transactions



def insertAccount(account: Account) -> int:
    return data_access_layer.insertAccount(account.name, account.init_balance)

def insertAsset(asset: Asset) -> int:
    return data_access_layer.insertAsset(asset.symbol, asset.type)

def insertTransaction(transaction: Transaction) -> int:
    return data_access_layer.insertTransaction(transaction.a_id, transaction.asset_id, transaction.timestamp, transaction.price_per_asset, transaction.quantity, transaction.type)

def insertContractData(contract_data: ContractData) -> int:
    return data_access_layer.insertContractData(contract_data.t_id, contract_data.strike, contract_data.expiry, contract_data.type)


def deleteAccount(account_id: int) -> None:
    data_access_layer.deleteAccount(account_id)

def deleteAsset(asset_id: int) -> None:
    data_access_layer.deleteAsset(asset_id)

def deleteTransaction(t_id: int) -> None:
    data_access_layer.deleteTransaction(t_id)

def deleteContractData(c_id: int) -> None:
    data_access_layer.deleteContractData(c_id)
