import time  # For sleep
import os # to create folders

import util  # Project-related utility functions
import exchange_manager  # Exchange class manager

def write_file_header(file, exchanges):
    file.write("Time (ms),Date&Time")
    for exchange in exchanges:
        file.write(",")
        file.write(exchange)
    file.write(",Min Price,Min Exchange,Max Price,Max Exchange,Average\n")

# Handles all the processes for starting writing to a new file
def start_new_file(filename, exchanges):
        f = open(filename, "w+")
        write_file_header(f, exchanges)
        f.close()

# Creates a folder at the specified path if it doesn't already exist
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Returns true if file exists, else returns false
def file_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False


if __name__ == "__main__":
    log_folder = "./logs/"
    output_file = log_folder + util.get_formatted_date() + "_stats.csv"
    current_day = util.get_current_day()

    # Exchange API related variables
    exchanges = exchange_manager.initialize_exchange_dict()
    ETH_dict = dict()

    # Create logs folder if it doesn't already exist
    create_folder("./logs/")

    # If the file does not exist, create the file and write the header.
    if(not file_exists(output_file)):
        start_new_file(output_file, exchanges)

    while(True):
        # Open a new file every new day start
        if(current_day < util.get_current_day()):
            # Current day is a new day now
            current_day = util.get_current_day()

            # Open the new file
            output_file = log_folder + util.get_formatted_date() + "_stats.csv"
            start_new_file(output_file, exchanges)

        f = open(output_file, "a+")

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
        min_price, min_exchange = util.get_min_ETH_price(ETH_dict)
        max_price, max_exchange = util.get_max_ETH_price(ETH_dict)
        avg_price = util.get_average_ETH_price(ETH_dict)

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
        f.close()
        time.sleep(30)  # sleep for 10 seconds
