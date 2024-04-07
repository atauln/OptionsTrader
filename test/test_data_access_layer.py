import unittest
from datetime import datetime, timedelta

from src.db.data_access_layer import *
from src.db.db_utils import *

class TestDataAccessLayer(unittest.TestCase):
    def test_rebuildTables(self):
        rebuildTables()
        sql = """
        SELECT *
        FROM pg_catalog.pg_tables
        WHERE schemaname != 'pg_catalog' AND 
            schemaname != 'information_schema';
        """
        tables = exec_get_all(sql)
        self.assertEqual(len(tables), 4)

    def test_getAccounts(self):
        rebuildTables()
        accounts = getAccounts()
        self.assertEqual(len(accounts), 0)

    def test_getAssets(self):
        rebuildTables()
        assets = getAssets()
        self.assertEqual(len(assets), 0)

    def test_getTransactions(self):
        rebuildTables()
        transactions = getTransactions()
        self.assertEqual(len(transactions), 0)
    
    def test_getContractData(self):
        rebuildTables()
        contract_data = getContractData()
        self.assertEqual(len(contract_data), 0)

    def test_getAccountById(self):
        rebuildTables()
        account = getAccountById(1)
        self.assertEqual(account, None)

    def test_getAssetById(self):
        rebuildTables()
        asset = getAssetById(1)
        self.assertEqual(asset, None)

    def test_getTransactionById(self):
        rebuildTables()
        transaction = getTransactionById(1)
        self.assertEqual(transaction, None)
    
    def test_getContractDataById(self):
        rebuildTables()
        contract_data = getContractDataById(1)
        self.assertEqual(contract_data, None)

    def test_getTransactionsByAccountId(self):
        rebuildTables()
        transactions = getTransactionsByAccountId(1)
        self.assertEqual(len(transactions), 0)
    
    def test_getTransactionsByAssetId(self):
        rebuildTables()
        transactions = getTransactionsByAssetId(1)
        self.assertEqual(len(transactions), 0)
    
    def test_getAssetBySymbol(self):
        rebuildTables()
        asset = getAssetBySymbol('AAPL')
        self.assertEqual(asset, None)
    
    def test_insertAccount(self):
        rebuildTables()
        account_id = insertAccount('test', 100.00)
        self.assertEqual(account_id, 1)

    def test_insertAsset(self):
        rebuildTables()
        asset_id = insertAsset('AAPL', 'stock')
        self.assertEqual(asset_id, 1)
    
    def test_insertTransaction(self):
        rebuildTables()
        account_id = insertAccount('test', 100.00)
        asset_id = insertAsset('AAPL', 'stock')
        transaction_id = insertTransaction(account_id, asset_id, datetime.now(), 100.00, 1, 'buy')
        self.assertEqual(transaction_id, 1)
    
    def test_insertContractData(self):
        rebuildTables()
        account_id = insertAccount('test', 100.00)
        asset_id = insertAsset('AAPL', 'option')
        transaction_id = insertTransaction(account_id, asset_id, datetime.now(), 100.00, 1, 'buy')
        contract_data_id = insertContractData(transaction_id, 1.00, datetime.now() + timedelta(days=30), 'call')
        self.assertEqual(contract_data_id, 1)