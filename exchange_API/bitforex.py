import requests  # For API requests


# https://github.com/bitforexapi


class Bitforex_API:
    def __init__(self, ETH_wallet, USDT_wallet, public_key, private_key):
        self.__ETH_wallet = ETH_wallet
        self.__USDT_wallet = USDT_wallet
        self.__public_key = public_key
        self.__private_key = private_key
        self.__base_API = "https://api.bitforex.com/api/"

    # Returns the ETH wallet address
    def get_ETH_wallet(self):
        return self.__ETH_wallet

    # Returns the last ETH price in USDT
    def get_ETH_price(self):
        ETH_price = requests.get(
            self.__base_API + "v1/market/ticker?symbol=coin-usdt-eth")
        ETH_price = ETH_price.json()
        return ETH_price["data"]["last"]