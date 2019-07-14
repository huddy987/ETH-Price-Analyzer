import requests  # For API requests


# https://docs.kucoin.com/


class KuCoin_API:
    def __init__(self, ETH_wallet, USDT_wallet, public_key, private_key):
        self.__ETH_wallet = ETH_wallet
        self.__USDT_wallet = USDT_wallet
        self.__public_key = public_key
        self.__private_key = private_key
        self.__base_API = "https://api.kucoin.com/"

        self.ETH_bal = 1
        self.USDT_bal = 600

    # Returns the ETH wallet address
    def get_ETH_wallet(self):
        return self.__ETH_wallet

    # Returns the last ETH price in USDT
    # https://huobiapi.github.io/docs/v1/en/#get-the-last-trade
    def get_ETH_price(self):
        ETH_price = requests.get(
            self.__base_API + "api/v1/market/stats?symbol=ETH-USDT")
        ETH_price = ETH_price.json()
        try:
            return float(ETH_price["data"]["last"])
        except:
            return -1
