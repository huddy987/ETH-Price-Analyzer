# Stores crypto balances
class Wallet:
    def __init__(self, ETH_balance, USDT_balance):
        self.__ETH_balance = ETH_balance
        self.__USDT_balance = USDT_balance

    def get_ETH_balance(self):
        return self.__ETH_balance

    def get_USDT_balance(self):
        return self.__USDT_balance

    # Just add negative values if we want to decrease
    def add_ETH_balance(self, price_change):
        self.__ETH_balance += price_change
        assert self.__ETH_balance > 0, "ETH balance less then 0"

    # Just add negative values if we want to decrease
    def add_USDT_balance(self, price_change):
        self.__USDT_balance += price_change
        assert self.__USDT_balance > 0, "USDT balance less then 0"
