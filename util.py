# General utility functions

import time  # For current_time_ms
import datetime # For datetime.datetime.now()


def get_current_time_ms():
    return int(round(time.time() * 1000))

def get_current_date_time():
    return str(datetime.datetime.now())

def get_formatted_date():
    currentDT = datetime.datetime.now()
    return str(currentDT.year) + "-" + str(currentDT.month) + "-" + str(currentDT.day)

def get_current_day():
    currentDT = datetime.datetime.now()
    return currentDT.day    # Leave as int so we can do comparisons

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


def get_ETH_dict(exchanges):
    # Create a dictionary where the keys are the exchange names and the values are the ETH prices
    ETH_dict = dict()
    for exchange in exchanges:
        ETH_dict[exchange] = exchanges[exchange].get_ETH_price()

        if(ETH_dict[exchange] == -1):   # Constantly retry exchanges returning null values
            while(ETH_dict[exchange] == -1):
                ETH_dict[exchange] = exchanges[exchange].get_ETH_price()
                print("Timeout for 5 minutes. Exchange API returned -1. (" + exchange + ")")
                time.sleep(300)

    return ETH_dict


def get_average_ETH_price(ETH_dict):
    # Returns the average eth price across all exchanges
    sum = 0
    for exchange in ETH_dict:
        sum += ETH_dict[exchange]

    return sum / len(ETH_dict)


def get_min_ETH_price(ETH_dict):
    # Default to Binance as lowest (will be overridden)
    lowest_exchange_name = "Binance"
    lowest_price = ETH_dict["Binance"]

    for exchange in ETH_dict:
        next_price = ETH_dict[exchange]

        # Get the lowest price
        if(next_price < lowest_price):
            lowest_exchange_name = exchange
            lowest_price = next_price

    return lowest_price, lowest_exchange_name


def get_max_ETH_price(ETH_dict):
    # Default to Binance as highest (will be overridden)
    highest_exchange_name = "Binance"
    highest_price = ETH_dict["Binance"]

    for exchange in ETH_dict:
        next_price = ETH_dict[exchange]

        # Get the highest price
        if(next_price > highest_price):
            highest_exchange_name = exchange
            highest_price = next_price

    return highest_price, highest_exchange_name
