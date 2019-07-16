# General utility functions

import time  # For current_time_ms


def get_current_time_ms():
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


def get_min_ETH_price(exchanges):
    # Default to Binance as lowest (will be overridden)
    lowest_exchange_name = "Binance"
    lowest_price = exchanges["Binance"].get_ETH_price()

    for exchange in exchanges:
        next_price = exchanges[exchange].get_ETH_price()
        if(next_price == -1):
            while(next_price == -1):
                print("Timeout for 5 minutes. Exchange API limit exceeded!")
                print(exchange)
                time.sleep(300)
                next_price = exchanges[exchange].get_ETH_price()

        # Get the lowest price
        if(next_price < lowest_price):
            lowest_exchange_name = exchange
            lowest_price = exchanges[lowest_exchange_name].get_ETH_price()

    return lowest_price, lowest_exchange_name


def get_max_ETH_price(exchanges):
    # Default to Binance as highest (will be overridden)
    highest_exchange_name = "Binance"
    highest_price = exchanges["Binance"].get_ETH_price()

    for exchange in exchanges:
        next_price = exchanges[exchange].get_ETH_price()
        if(next_price == -1):
            while(next_price == -1):
                print("Timeout for 5 minutes. Exchange API limit exceeded!")
                print(exchange)
                time.sleep(300)
                next_price = exchanges[exchange].get_ETH_price()

        # Get the highest price
        if(next_price > highest_price):
            highest_exchange_name = exchange
            highest_price = exchanges[highest_exchange_name].get_ETH_price()

    return highest_price, highest_exchange_name
