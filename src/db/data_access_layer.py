from db.db_utils import *

def rebuildTables():
    exec_sql_file('../db_base/initdb.sql')


# GET ALL

def getAccounts():
    return exec_get_all("SELECT * FROM Account")

def getAssets():
    return exec_get_all("SELECT * FROM Asset")

def getTransactions():
    return exec_get_all("SELECT * FROM Transaction")

def getContractData():
    return exec_get_all("SELECT * FROM ContractData")


# GET BY

def getAccountById(account_id):
    return exec_get_one("SELECT * FROM Account WHERE account_id = %s", (account_id,))

def getAccountByName(name):
    return exec_get_one("SELECT * FROM Account WHERE name = %s", (name,))

def getAssetById(asset_id):
    return exec_get_one("SELECT * FROM Asset WHERE asset_id = %s", (asset_id,))

def getTransactionById(t_id):
    return exec_get_one("SELECT * FROM Transaction WHERE t_id = %s", (t_id,))

def getContractDataById(contract_id):
    return exec_get_one("SELECT * FROM ContractData WHERE c_id = %s", (contract_id,))

def getTransactionsByAccountId(account_id):
    return exec_get_all("SELECT * FROM Transaction WHERE a_id = %s", (account_id,))

def getTransactionsByAssetId(asset_id):
    return exec_get_all("SELECT * FROM Transaction WHERE asset_id = %s", (asset_id,))

def getAssetBySymbol(symbol):
    return exec_get_one("SELECT * FROM Asset WHERE symbol = %s", (symbol,))


# INSERT

def insertAccount(name, init_balance):
    return exec_insert_returning("INSERT INTO Account(name, init_balance) VALUES (%(name)s, %(init_balance)s) RETURNING account_id", {'name': name, 'init_balance': init_balance})

def insertAsset(symbol, type):
    return exec_insert_returning("INSERT INTO Asset(symbol, type) VALUES (%(symbol)s, %(type)s) RETURNING asset_id", {'symbol': symbol, 'type': type})

def insertTransaction(a_id, asset_id, timestamp, price_per_asset, quantity, type):
    return exec_insert_returning("INSERT INTO Transaction(a_id, asset_id, timestamp, price_per_asset, quantity, type) VALUES (%(a_id)s, %(asset_id)s, %(timestamp)s, %(price_per_asset)s, %(quantity)s, %(type)s) RETURNING t_id", {'a_id': a_id, 'asset_id': asset_id, 'timestamp': timestamp, 'price_per_asset': price_per_asset, 'quantity': quantity, 'type': type})

def insertContractData(t_id, strike, expiry, type):
    return exec_insert_returning("INSERT INTO ContractData(t_id, strike, expiry, type) VALUES (%(t_id)s, %(strike)s, %(expiry)s, %(type)s) RETURNING c_id", {'t_id': t_id, 'strike': strike, 'expiry': expiry, 'type': type})


# DELETE

def deleteAccount(account_id):
    exec_commit("DELETE FROM Account WHERE account_id = %s", (account_id,))

def deleteAsset(asset_id):
    exec_commit("DELETE FROM Asset WHERE asset_id = %s", (asset_id,))

def deleteTransaction(t_id):
    exec_commit("DELETE FROM Transaction WHERE t_id = %s", (t_id,))

def deleteContractData(c_id):
    exec_commit("DELETE FROM ContractData WHERE c_id = %s", (c_id,))
