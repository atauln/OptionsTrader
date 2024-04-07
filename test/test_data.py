import unittest

from src.data import *

class TestData(unittest.TestCase):
    def test_Account(self):
        account = Account(1, 'test', 100.00)
        self.assertEqual(account.a_id, 1)
        self.assertEqual(account.name, 'test')
        self.assertEqual(account.init_balance, 100.00)
    
    def test_Asset(self):
        asset = Asset(1, 'AAPL', 'stock')
        self.assertEqual(asset.asset_id, 1)
        self.assertEqual(asset.symbol, 'AAPL')
        self.assertEqual(asset.type, 'stock')

