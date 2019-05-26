import requests  # For API requests


# https://bittrex.github.io/api/v1-1


class Bittrex_API:
    def __init__(self, ETH_wallet, USDT_wallet, public_key, private_key):
        self.__ETH_wallet = ETH_wallet
        self.__USDT_wallet = USDT_wallet
        self.__public_key = public_key
        self.__private_key = private_key
        self.__base_API = "https://api.bittrex.com/api/v1.1/"

    # Returns the ETH wallet address
    def get_ETH_wallet(self):
        return self.__ETH_wallet

    # Returns the last ETH price in USDT
    def get_ETH_price(self):
        ETH_price = requests.get(
            self.__base_API + "public/getticker?market=USDT-ETH")
        ETH_price = ETH_price.json()
        return ETH_price["result"]["Last"]
