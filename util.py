import time  # For current_time_ms

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


def current_time_ms():
    return int(round(time.time() * 1000))


def get_total_ETH(exchanges):
    # Returns the total ETH balance across all accounts
    # exchanges is the master exchanges dictionary
    sum = 0
    for exchange in exchanges:
        sum += exchanges[exchange].ETH_bal

    return sum


def get_total_USDT(exchanges):
    # Returns the total USDT balance across all accounts
    # exchanges is the master exchanges dictionary
    sum = 0
    for exchange in exchanges:
        sum += exchanges[exchange].USDT_bal

    return sum


def get_average_ETH_price(exchanges):
    # Returns the average eth price across all exchanges
    sum = 0
    for exchange in exchanges:
        sum += exchanges[exchange].get_ETH_price()

    return sum / len(exchanges)
