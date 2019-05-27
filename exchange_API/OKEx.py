import requests  # For API requests


# https://www.okex.com/docs/en/#README


class OKEx_API:
    def __init__(self, ETH_wallet, USDT_wallet, public_key, private_key):
        self.__ETH_wallet = ETH_wallet
        self.__USDT_wallet = USDT_wallet
        self.__public_key = public_key
        self.__private_key = private_key
        self.__base_API = "https://www.okex.com/api/"

    # Returns the ETH wallet address
    def get_ETH_wallet(self):
        return self.__ETH_wallet

    # Returns the last ETH price in USDT
    # https://www.okex.com/docs/en/#spot-all
    def get_ETH_price(self):
        ETH_price = requests.get(
            self.__base_API + "spot/v3/instruments/ETH-USDT/ticker")
        ETH_price = ETH_price.json()
        return ETH_price["last"]
