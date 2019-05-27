import keys  # To access our API keys
import time  # For sleep
import sys  # To include stuff from a folder

from wallet import Wallet  # Wallet class
from util import current_time_ms  # Utility functions

# Exchange API includes
from exchange_API.binance import Binance_API
from exchange_API.bittrex import Bittrex_API
from exchange_API.OKEx import OKEx_API
from exchange_API.huobi import Huobi_API
from exchange_API.poloniex import Poloniex_API
from exchange_API.bitforex import Bitforex_API


def main():
    wallet = Wallet(0, 10)

    Binance = Binance_API(keys.BINANCE_ETH_WALLET, keys.BINANCE_USDT_WALLET,
                          keys.BINANCE_API_KEY, keys.BINANCE_SECRET_KEY)

    Bittrex = Bittrex_API(keys.BITTREX_ETH_WALLET, keys.BITTREX_USDT_WALLET,
                          keys.BITTREX_API_KEY, keys.BITTREX_SECRET_KEY)

    OKEx = OKEx_API(keys.OKEX_ETH_WALLET, keys.OKEX_USDT_WALLET,
                    keys.OKEX_API_KEY, keys.OKEX_SECRET_KEY)

    Huobi = Huobi_API(keys.HUOBI_ETH_WALLET, keys.HUOBI_USDT_WALLET,
                      keys.HUOBI_API_KEY, keys.HUOBI_SECRET_KEY)

    Poloniex = Poloniex_API(keys.POLONIEX_ETH_WALLET, keys.POLONIEX_USDT_WALLET,
                            keys.POLONIEX_API_KEY, keys.POLONIEX_SECRET_KEY)

    Bitforex = Bitforex_API(keys.BITFOREX_ETH_WALLET, keys.BITFOREX_USDT_WALLET,
                            keys.BITFOREX_API_KEY, keys.BITFOREX_SECRET_KEY)

    print(Binance.get_ETH_price())
    print(Bittrex.get_ETH_price())
    print(OKEx.get_ETH_price())
    print(Huobi.get_ETH_price())
    print(Poloniex.get_ETH_price())
    print(Bitforex.get_ETH_price())


main()
