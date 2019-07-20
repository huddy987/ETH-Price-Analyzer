import time  # For sleep

import util  # Project-related utility functions
import exchange_manager  # Exchange class manager
import threading

def min_thread_call():
    global min_price, min_exchange, exchanges, ETH_dict
    min_price, min_exchange = util.get_min_ETH_price(ETH_dict)


def max_thread_call():
    global max_price, max_exchange, exchanges, ETH_dict
    max_price, max_exchange = util.get_max_ETH_price(ETH_dict)


def avg_thread_call():
    global avg_price, exchanges, ETH_dict
    avg_price = util.get_average_ETH_price(ETH_dict)

def write_file_header(file, exchanges):
    file.write("Time (ms),Date&Time")
    for exchange in exchanges:
        file.write(",")
        file.write(exchange)
    file.write(",Min Price,Min Exchange,Max Price,Max Exchange,Average\n")


if __name__ == "__main__":
    min_price = 0
    min_exchange = ""
    max_price = 0
    max_exchange = ""
    avg_price = 0
    output_file = util.get_formatted_date() + "_stats.csv"
    current_day = util.get_current_day()

    # Exchange API related variables
    exchanges = exchange_manager.initialize_exchange_dict()
    ETH_dict = dict()

    f = open(output_file, "w+")

    # Write out the file header
    write_file_header(f, exchanges)

    while(True):

        # Open a new file every new day start
        if(current_day < util.get_current_day()):
            # Current day is a new day now
            current_day = util.get_current_day()

            # Close the old file
            f.close()

            print("test")

            # Open the new file
            output_file = util.get_formatted_date() + "_stats.csv"
            f = open(output_file, "w+")

            # Write out the file header
            write_file_header(f, exchanges)

        # API calls
        ETH_dict = util.get_ETH_dict(exchanges)

        # Write prices to file
        f.write(str(util.get_current_time_ms()))
        f.write(",")
        f.write(util.get_current_date_time())
        for exchange in ETH_dict:
            f.write(",")
            f.write(str(ETH_dict[exchange]))
        f.write(",")

        # Calculate statistics
        min_thread = threading.Thread(
            target=min_thread_call, args=())
        max_thread = threading.Thread(
            target=max_thread_call, args=())
        avg_thread = threading.Thread(
            target=avg_thread_call, args=())

        # Threading operations
        min_thread.start()
        max_thread.start()
        avg_thread.start()

        min_thread.join()
        max_thread.join()
        avg_thread.join()


        # Write calculated statistics to the file
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

        # Sleep for a while
        print("Done an entry, sleep for 30s")
        time.sleep(30)  # sleep for 10 seconds
