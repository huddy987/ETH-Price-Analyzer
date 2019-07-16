import keys  # To access our API keys

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
