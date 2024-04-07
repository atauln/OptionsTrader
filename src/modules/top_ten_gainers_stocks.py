# This module gets the highest gainers in the market today and buys put options on them 1 point down from the current price.

from data import *
from db import application_layer
from finance import stocks
from modules.base_module import BaseModule
import logging

# set logging level to print out anything with info
logging.basicConfig(level=logging.INFO)

class TopTenGainersStocks(BaseModule):
    allocation_per_trade = 500
    limit_sell_percent = 0.95
    profit_percent = 1.1

    def __init__(self):
        self.name = "Top Ten Gainers, Buy Stocks"
        self.description = "Buys stocks the top ten gainers of the day"
        self.account = Account(None, "top_ten_gainers_stocks", 10000)

    def run(self):
        if super().run() == 1:
            return
        
        # TODO sell old assets that are currently below the limit sell percent or above the profit percent
        assets = application_layer.getCurrentAssets(self.account.a_id)
        for asset in assets:
            stock = stocks.get_stock_data(asset)
            if stock.day.close is not None:
                if stock.day.close < 1.0:
                    continue
            else:
                continue
            stock_price = stock.day.close
            if stock_price < assets[asset][1] * self.limit_sell_percent:
                logging.info(f"Selling {assets[asset][0]} shares of {asset} at {stock_price}")
                application_layer.sellStock(self.account.a_id, asset, stock_price, -assets[asset][0])
            elif stock_price > assets[asset][1] * self.profit_percent:
                logging.info(f"Selling {assets[asset][0]} shares of {asset} at {stock_price}")
                application_layer.sellStock(self.account.a_id, asset, stock_price, -assets[asset][0])



        if application_layer.calculateAccountBalance(self.account.a_id) < self.allocation_per_trade:
            logging.error("Insufficient funds")
            return 1
        
        gainers = stocks.get_client().get_snapshot_direction("stocks", "gainers")
        assets_bought: list[int] = []
        account_balance_start = application_layer.calculateAccountBalance(self.account.a_id)
        logging.info(f"Account balance start: ${account_balance_start}")
        for gainer in gainers:
            stock = stocks.get_stock_data(gainer.ticker)
            if stock.day.close is not None:
                if stock.day.close < 1.0:
                    continue
            else:
                continue
            stock_price = stock.day.close
            asset: Asset = application_layer.getAssetBySymbol(gainer.ticker)
            if asset is None:
                asset = Asset(0, gainer.ticker, "stock")
                asset.asset_id = application_layer.insertAsset(asset)
            quantity = self.allocation_per_trade // stock_price
            if quantity == 0:
                continue
            logging.info(f"Buying {quantity} shares of {gainer.ticker} at {stock_price}")
            application_layer.purchaseStock(self.account.a_id, gainer.ticker, stock_price, quantity)
            assets_bought.append(asset.symbol)

        account_balance_end = application_layer.calculateAccountBalance(self.account.a_id)
        logging.info(f"Account balance change: ${account_balance_end - account_balance_start} [{account_balance_start} -> {account_balance_end}]")
        logging.info(f"Options bought: {assets_bought}")
