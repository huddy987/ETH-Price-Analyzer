import requests  # For API requests


# https://docs.bitfinex.com/docs


class Bitfinex_API:
    def __init__(self, ETH_wallet, USDT_wallet, public_key, private_key):
        self.__ETH_wallet = ETH_wallet
        self.__USDT_wallet = USDT_wallet
        self.__public_key = public_key
        self.__private_key = private_key
        self.__base_API = "https://api-pub.bitfinex.com/"
        self.__base_API_auth = "https://api.bitfinex.com/"

        self.ETH_bal = 1
        self.USDT_bal = 600

    # Returns the ETH wallet address
    def get_ETH_wallet(self):
        return self.__ETH_wallet

    # Returns the last ETH price in USDT
    def get_ETH_price(self):
        ETH_price = requests.get(
            self.__base_API_auth + "v1/pubticker/ethusd")
        ETH_price = ETH_price.json()
        try:
            return float(ETH_price["last_price"])
        except:
            return -1

    # Returns the ETH bid in USDT
    def get_ETH_bid(self):
        ETH_price = requests.get(
            self.__base_API_auth + "v1/pubticker/ethusd")
        ETH_price = ETH_price.json()
        try:
            return float(ETH_price["bid"])
        except:
            return -1

    # Returns the ETH ask in USDT
    def get_ETH_ask(self):
        ETH_price = requests.get(
            self.__base_API_auth + "v1/pubticker/ethusd")
        ETH_price = ETH_price.json()
        try:
            return float(ETH_price["ask"])
        except:
            return -1
