import unittest
from datetime import datetime

from src.db.service_layer import *
from src.db.db_utils import *
from src.db.data_access_layer import rebuildTables


class TestServiceLayer(unittest.TestCase):
    
    def test_getAccounts(self):
        rebuildTables()
        accounts = getAccounts()
        self.assertEqual(len(accounts), 0)
        insertAccount(Account(0, 'test', 100.00))
        accounts = getAccounts()
        self.assertEqual(len(accounts), 1)
    
    def test_getAssets(self):
        rebuildTables()
        assets = getAssets()
        self.assertEqual(len(assets), 0)
        insertAsset(Asset(0, 'AAPL', 'stock'))
        assets = getAssets()
        self.assertEqual(len(assets), 1)
    
    def test_getTransactions(self):
        rebuildTables()
        transactions = getTransactions()
        self.assertEqual(len(transactions), 0)
        account = insertAccount(Account(0, 'test', 100.00))
        asset = insertAsset(Asset(0, 'AAPL', 'stock'))
        insertTransaction(Transaction(0, account, asset, datetime.now(), 100.00, 10, 'buy'))
        transactions = getTransactions()
        self.assertEqual(len(transactions), 1)
    
    def test_getContractData(self):
        rebuildTables()
        contract_data = getContractData()
        self.assertEqual(len(contract_data), 0)
        asset = insertAsset(Asset(0, 'AAPL', 'stock'))
        account = insertAccount(Account(0, 'test', 100.00))
        transaction = insertTransaction(Transaction(0, account, asset, datetime.now(), 100.00, 10, 'buy'))
        insertContractData(ContractData(0, transaction, datetime.now(), 100.00, 'call'))
        contract_data = getContractData()
        self.assertEqual(len(contract_data), 1)

    def test_getAccountById(self):
        rebuildTables()
        self.assertIsNone(getAccountById(1))
        account_id = insertAccount(Account(0, 'test', 100.00))
        account = getAccountById(account_id)
        self.assertEqual(account.a_id, account_id)
    
    def test_getAssetById(self):
        rebuildTables()
        self.assertIsNone(getAccountById(1))
        asset_id = insertAsset(Asset(0, 'AAPL', 'stock'))
        asset = getAssetById(asset_id)
        self.assertEqual(asset.asset_id, asset_id)
    
    def test_getTransactionById(self):
        rebuildTables()
        self.assertIsNone(getTransactionById(1))
        account = insertAccount(Account(0, 'test', 100.00))
        asset = insertAsset(Asset(0, 'AAPL', 'stock'))
        transaction_id = insertTransaction(Transaction(0, account, asset, datetime.now(), 100.00, 10, 'buy'))
        transaction = getTransactionById(transaction_id)
        self.assertEqual(transaction.t_id, transaction_id)
    
    def test_getContractDataById(self):
        rebuildTables()
        self.assertIsNone(getContractDataById(1))
        asset = insertAsset(Asset(0, 'AAPL', 'stock'))
        account = insertAccount(Account(0, 'test', 100.00))
        transaction = insertTransaction(Transaction(0, account, asset, datetime.now(), 100.00, 10, 'buy'))
        contract_id = insertContractData(ContractData(0, transaction, datetime.now(), 100.00, 'call'))
        contract_data = getContractDataById(contract_id)
        self.assertEqual(contract_data.c_id, contract_id)
    
    def test_getAssetBySymbol(self):
        rebuildTables()
        self.assertIsNone(getAssetBySymbol('AAPL'))
        asset_id = insertAsset(Asset(0, 'AAPL', 'stock'))
        asset = getAssetBySymbol('AAPL')
        self.assertEqual(asset.asset_id, asset_id)

    def test_getTransactionsByAccountId(self):
        rebuildTables()
        account = insertAccount(Account(0, 'test', 100.00))
        asset = insertAsset(Asset(0, 'AAPL', 'stock'))
        insertTransaction(Transaction(0, account, asset, datetime.now(), 100.00, 10, 'buy'))
        transactions = getTransactionsByAccountId(account)
        self.assertEqual(len(transactions), 1)
    
    def test_getTransactionsByAssetId(self):
        rebuildTables()
        account = insertAccount(Account(0, 'test', 100.00))
        asset = insertAsset(Asset(0, 'AAPL', 'stock'))
        insertTransaction(Transaction(0, account, asset, datetime.now(), 100.00, 10, 'buy'))
        transactions = getTransactionsByAssetId(asset)
        self.assertEqual(len(transactions), 1)

    def test_insertAccount(self):
        rebuildTables()
        account_id = insertAccount(Account(0, 'test', 100.00))
        self.assertEqual(account_id, 1)

    def test_insertAsset(self):
        rebuildTables()
        asset_id = insertAsset(Asset(0, 'AAPL', 'stock'))
        self.assertEqual(asset_id, 1)
    
    def test_insertTransaction(self):
        rebuildTables()
        account = insertAccount(Account(0, 'test', 100.00))
        asset = insertAsset(Asset(0, 'AAPL', 'stock'))
        transaction_id = insertTransaction(Transaction(0, account, asset, datetime.now(), 100.00, 1, 'buy'))
        self.assertEqual(transaction_id, 1)
    
    def test_insertContractData(self):
        rebuildTables()
        account = insertAccount(Account(0, 'test', 100.00))
        asset = insertAsset(Asset(0, 'AAPL', 'stock'))
        transaction = insertTransaction(Transaction(0, account, asset, datetime.now(), 100.00, 10, 'buy'))
        contract_id = insertContractData(ContractData(0, transaction, datetime.now(), 100.00, 'call'))
        self.assertEqual(contract_id, 1)