import requests  # For API requests


# https://github.com/huobiapi


class Huobi_API:
    def __init__(self, ETH_wallet, USDT_wallet, public_key, private_key):
        self.__ETH_wallet = ETH_wallet
        self.__USDT_wallet = USDT_wallet
        self.__public_key = public_key
        self.__private_key = private_key
        self.__base_API = "https://api.huobi.pro/"

        self.ETH_bal = 1
        self.USDT_bal = 600

    # Returns the ETH wallet address
    def get_ETH_wallet(self):
        return self.__ETH_wallet

    # Returns the last ETH price in USDT
    # https://huobiapi.github.io/docs/spot/v1/en/#get-the-last-trade
    def get_ETH_price(self):
        try:
            ETH_price = requests.get(
                self.__base_API + "market/trade?symbol=ethusdt")
            ETH_price = ETH_price.json()
            return float(ETH_price["tick"]["data"][0]["price"])
        except:
            return -1

    # Returns the ETH bid in USDT
    def get_ETH_bid(self):
        try:
            ETH_price = requests.get(
                self.__base_API + "market/detail/merged?symbol=ethusdt")
            ETH_price = ETH_price.json()
            return float(ETH_price["tick"]["bid"][0])   # bid 1 is amount
        except:
            return -1

    # Returns the ETH ask in USDT
    def get_ETH_ask(self):
        try:
            ETH_price = requests.get(
                self.__base_API + "market/detail/merged?symbol=ethusdt")
            ETH_price = ETH_price.json()
            return float(ETH_price["tick"]["ask"][0]) # ask 1 is amount
        except:
            return -1
