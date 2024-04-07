import unittest
from datetime import datetime, timedelta

from src.db.application_layer import *
from src.db.db_utils import *
from src.db.data_access_layer import rebuildTables


class TestApplicationLayer(unittest.TestCase):
    def test_calculateAccountBalance(self):
        rebuildTables()
        account = insertAccount(Account(0, 'test', 1000.00))
        asset = insertAsset(Asset(0, 'AAPL', 'stock'))
        insertTransaction(Transaction(0, account, asset, datetime.now() - timedelta(days=14), 100.00, 10, 'buy'))
        balance = calculateAccountBalance(account)
        self.assertEqual(balance, 0.00)
        insertTransaction(Transaction(0, account, asset, datetime.now() - timedelta(days=7), 200.00, 10, 'sell'))
        balance = calculateAccountBalance(account)
        self.assertEqual(balance, 2000.00)
        insertTransaction(Transaction(0, account, asset, datetime.now(), 100.00, 10, 'buy'))
        balance = calculateAccountBalance(account)
        self.assertEqual(balance, 1000.00)
        balance = calculateAccountBalance(account, datetime.now() - timedelta(days=6))
        self.assertEqual(balance, 2000.00)
        balance = calculateAccountBalance(account, datetime.now() - timedelta(days=7))
        self.assertEqual(balance, 2000.00)
        balance = calculateAccountBalance(account, datetime.now() - timedelta(days=8))
        self.assertEqual(balance, 0.00)
    
    def test_purchaseOptionsContract(self):
        rebuildTables()
        account = insertAccount(Account(0, 'test', 1000.00))
        asset = insertAsset(Asset(0, 'AAPL', 'stock'))
        purchaseOptionsContract(account, getAssetById(asset).symbol, 100.00, 10, datetime.now() + timedelta(days=30), 'call')
        self.assertEqual(len(getContractData()), 1)