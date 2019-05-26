import keys  # To access our API keys
import time  # For sleep
import sys  # To include stuff from a folder

from wallet import Wallet  # Wallet class
from util import current_time_ms  # Utility functions

# Exchange API includes
from exchange_API.binance import Binance_API
from exchange_API.bittrex import Bittrex_API


def main():
    wallet = Wallet(0, 10)

    Binance = Binance_API(keys.BINANCE_ETH_WALLET, keys.BINANCE_USDT_WALLET,
                          keys.BINANCE_API_KEY, keys.BINANCE_SECRET_KEY)

    Bittrex = Bittrex_API(keys.BITTREX_ETH_WALLET, keys.BITTREX_USDT_WALLET,
                          keys.BITTREX_API_KEY, keys.BITTREX_SECRET_KEY)
    print(Binance.get_ETH_price())
    print(Bittrex.get_ETH_price())
    print(current_time_ms())


main()
