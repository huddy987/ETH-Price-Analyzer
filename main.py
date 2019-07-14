import keys  # To access our API keys
import time  # For sleep
import sys  # To include stuff from a folder

from util import *  # utility functions

# Exchange API classes
from exchange_API.binance import Binance_API
from exchange_API.bittrex import Bittrex_API
from exchange_API.OKEx import OKEx_API
from exchange_API.huobi import Huobi_API
from exchange_API.poloniex import Poloniex_API
from exchange_API.bitforex import Bitforex_API
from exchange_API.kucoin import KuCoin_API
from exchange_API.bitfinex import Bitfinex_API
from exchange_API.tradeio import TradeIO_API

debug = True


def initialize_exchange_dict():
    # Handles initializing all exchanges as well as a master exchange dictitonary

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

    KuCoin = KuCoin_API(keys.KUCOIN_ETH_WALLET, keys.KUCOIN_USDT_WALLET,
                        keys.KUCOIN_API_KEY, keys.KUCOIN_SECRET_KEY)

    Bitfinex = Bitfinex_API(keys.BITFINEX_ETH_WALLET, keys.BITFINEX_USDT_WALLET,
                            keys.BITFINEX_API_KEY, keys.BITFINEX_SECRET_KEY)

    TradeIO = TradeIO_API(keys.TRADEIO_ETH_WALLET, keys.TRADEIO_USDT_WALLET,
                          keys.TRADEIO_API_KEY, keys.TRADEIO_SECRET_KEY)

    exchanges = {
        "Binance": Binance,
        "Bittrex": Bittrex,
        "OKEx": OKEx,
        "Huobi": Huobi,
        "Poloniex": Poloniex,
        "Bitforex": Bitforex,
        "KuCoin": KuCoin,
        "Bitfinex": Bitfinex,
        "TradeIO": TradeIO
    }

    return exchanges


if __name__ == "__main__":
    exchanges = initialize_exchange_dict()
    lowest_exchange_name = "Binance"
    highest_exchange_name = "Binance"
    lowest_price = exchanges["Binance"].get_ETH_price()
    highest_price = exchanges["Binance"].get_ETH_price()

    while(True):
        for exchange in exchanges:
            next_price = exchanges[exchange].get_ETH_price()
            if(next_price == -1):
                while(next_price == -1):
                    print("Timeout for 5 minutes. Exchange API limit exceeded!")
                    time.sleep(300)
                    next_price = exchanges[exchange].get_ETH_price()

            # Get the lowest price
            if(next_price < lowest_price):
                lowest_exchange_name = exchange
                lowest_price = exchanges[lowest_exchange_name].get_ETH_price()

            # Get the highest price
            if(next_price > highest_price):
                highest_exchange_name = exchange
                highest_price = exchanges[highest_exchange_name].get_ETH_price()

        average_price = get_average_ETH_price(exchanges)

        if(debug):
            print("DEBUG stats:")
            print("lowest_exchange: " + lowest_exchange_name)
            print("highest_exchange: " + highest_exchange_name)
            print("lowest_price: " + str(lowest_price))
            print("average_price: " + str(average_price))
            print("highest_price: " + str(highest_price))

        # If the highest price is 2% higher than the lowest price, initiate a buy
        if((lowest_price + lowest_price * 0.02) < highest_price):

            # Convert all USDT in the account to ETH
            exchanges[lowest_exchange_name].ETH_bal += exchanges[lowest_exchange_name].USDT_bal / lowest_price
            exchanges[lowest_exchange_name] = 0

            if(debug):
                print("New ETH Bal on " + lowest_exchange_name +
                      ": " + exchanges[lowest_exchange_name].ETH_bal)
                print("New USDT Bal on " + lowest_exchange_name +
                      ": " + exchanges[lowest_exchange_name].USDT_bal)

            # Continually check if we should sell
            while(True):
                lowest_price = exchanges[lowest_exchange_name].get_ETH_price()
                if(lowest_price >= average_price):
                    # Sell condition
                    exchanges[lowest_exchange_name].USDT_bal += exchanges[lowest_exchange].ETH_bal / lowest_price
                    exchanges[lowest_exchange_name] = 0

                    if(debug):
                        print("New ETH Bal on " + lowest_exchange_name +
                              ": " + exchanges[lowest_exchange_name].ETH_bal)
                        print("New USDT Bal on " + lowest_exchange_name +
                              ": " + exchanges[lowest_exchange_name].USDT_bal)
                    break
        else:
            print("Done a cycle, no buy detected. Sleep for 30s")
            time.sleep(30)
