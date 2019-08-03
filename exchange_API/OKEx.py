import requests  # For API requests

# https://www.okex.com/docs/en/#README


class OKEx_API:
    def __init__(self, ETH_wallet, USDT_wallet, public_key, private_key):
        self.__ETH_wallet = ETH_wallet
        self.__USDT_wallet = USDT_wallet
        self.__public_key = public_key
        self.__private_key = private_key
        self.__base_API = "https://www.okex.com/api/"

        self.ETH_bal = 1
        self.USDT_bal = 600

    # Returns the ETH wallet address
    def get_ETH_wallet(self):
        return self.__ETH_wallet

    # Returns the last ETH price in USDT
    # https://www.okex.com/docs/en/#spot-all
    def get_ETH_price(self):
        try:
            ETH_price = requests.get(
                self.__base_API + "spot/v3/instruments/ETH-USDT/ticker")
            ETH_price = ETH_price.json()
            return float(ETH_price["last"])
        except:
            return -1

    # Returns the ETH bid in USDT
    def get_ETH_bid(self):
        try:
            ETH_price = requests.get(
                self.__base_API + "spot/v3/instruments/ETH-USDT/ticker")
            ETH_price = ETH_price.json()
            return float(ETH_price["best_bid"])
        except:
            return -1

    # Returns the ETH ask in USDT
    def get_ETH_ask(self):
        try:
            ETH_price = requests.get(
                self.__base_API + "spot/v3/instruments/ETH-USDT/ticker")
            ETH_price = ETH_price.json()
            return float(ETH_price["best_ask"])
        except:
            return -1
