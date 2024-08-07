from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import SMA
from surmount.logging import log
from surmount.data import Asset

class TradingStrategy(Strategy):
    def __init__(self):
        # Defining a set of tickers traditionally considered more resilient during recessions
        self.resilient_tickers = ["PG", "JNJ", "KO", "PFE", "WMT", "XLU"]
        # Note: PG - Procter & Gamble, JNJ - Johnson & Johnson, KO - Coca Cola, PFE - Pfizer, WMT - Walmart, XLU - Utilities ETF

    @property
    def assets(self):
        # We're interested in the assets defined as resilient
        return self.resilient_tickers

    @property
    def interval(self):
        # Using a daily interval for assessment
        return "1day"

    def run(self, data):
        # Initialize an empty dictionary to store our target allocations
        allocation_dict = {}

        for ticker in self.resilient_tickers:
            # For simplicity, we equally distribute our investment across the chosen assets
            # A more sophisticated approach could use indicators like SMA, RSI, etc., to dynamically adjust allocations
            allocation_dict[ticker] = 1 / len(self.resilient_tickers)

        return TargetAllocation(allocation_dict)