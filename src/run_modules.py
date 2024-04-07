import module_manager
from modules import top_ten_gainers_stocks

module_manager.load_module(top_ten_gainers_stocks.TopTenGainersStocks())

module_manager.run_modules()