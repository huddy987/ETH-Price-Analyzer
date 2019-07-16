import time  # For sleep

import util  # Project-related utility functions
import exchange_manager  # Exchange class manager
import threading

min_price = 0
min_exchange = ""
max_price = 0
max_exchange = ""
avg_price = 0

exchanges = exchange_manager.initialize_exchange_dict()


def min_thread_call():
    global min_price, min_exchange, exchanges
    min_price, min_exchange = util.get_min_ETH_price(exchanges)


def max_thread_call():
    global max_price, max_exchange, exchanges
    max_price, max_exchange = util.get_max_ETH_price(exchanges)


def avg_thread_call():
    global avg_price, exchanges
    avg_price = util.get_average_ETH_price(exchanges)


if __name__ == "__main__":

    f = open("exchange_stats.csv", "w+")

    # Write out the file header
    f.write("Time")
    for exchange in exchanges:
        f.write(",")
        f.write(exchange)
    f.write(",Min Price,Min Exchange,Max Price, Max Exchange,Average\n")

    while(True):
        f.write(str(util.get_current_time_ms()))
        for exchange in exchanges:
            f.write(",")
            f.write(str(exchanges[exchange].get_ETH_price()))
        f.write(",")

        min_thread = threading.Thread(
            target=min_thread_call, args=())
        max_thread = threading.Thread(
            target=max_thread_call, args=())
        avg_thread = threading.Thread(
            target=avg_thread_call, args=())

        min_thread.start()
        max_thread.start()
        avg_thread.start()

        min_thread.join()
        max_thread.join()
        avg_thread.join()

        f.write(str(min_price))
        f.write(",")
        f.write(min_exchange)
        f.write(",")
        f.write(str(max_price))
        f.write(",")
        f.write(max_exchange)
        f.write(",")
        f.write(str(avg_price))
        f.write("\n")
        print("Done an entry, sleep for 30s")
        time.sleep(30)  # sleep for 10 seconds
