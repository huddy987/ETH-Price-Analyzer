import time  # For sleep
import os # to create folders

import util  # Project-related utility functions
import exchange_API.exchange_manager as exchange_manager  # Exchange class manager

debug = True

# Writes the file header
def write_file_header(file, exchanges):
    file.write("Time (ms),Date&Time")
    for exchange in exchanges:
        file.write(",")
        file.write(exchange)
        file.write(" Price(USD)")
    file.write(",Min Price(USD),Min Exchange,Max Price(USD),Max Exchange,Average Price(USD),Biggest Spread(%)")
    for exchange in exchanges:
        file.write(",")
        file.write(exchange)
        file.write(" Bid(USD)")
    for exchange in exchanges:
        file.write(",")
        file.write(exchange)
        file.write(" Ask(USD)")
    file.write("\n")

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

# Print out the values for a given dict
def print_values(file, dict):
    for key in dict:
        f.write(",")
        f.write(str(dict[key]))

if __name__ == "__main__":
    log_folder = "./logs/"
    output_file = log_folder + util.get_formatted_date() + "_stats.csv"
    current_day = util.get_current_day()

    # Exchange API related variables
    exchanges = exchange_manager.initialize_exchange_dict()

    # Create logs folder if it doesn't already exist
    create_folder(log_folder)

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
        ETH_price_dict = exchange_manager.get_ETH_price_dict(exchanges)
        ETH_bid_dict = exchange_manager.get_ETH_bid_dict(exchanges)
        ETH_ask_dict = exchange_manager.get_ETH_ask_dict(exchanges)

        # Write the time to the file
        f.write(str(util.get_current_time_ms()))
        f.write(",")
        f.write(util.get_current_date_time())

        # Write prices to file
        print_values(f, ETH_price_dict)
        f.write(",")

        # Calculate statistics
        min_price, min_exchange = util.get_min_ETH_price(ETH_price_dict)
        max_price, max_exchange = util.get_max_ETH_price(ETH_price_dict)
        avg_price = util.get_average_ETH_price(ETH_price_dict)
        biggest_percent_spread = util.get_biggest_percent_spread(min_price, max_price)

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
        f.write(",")
        f.write(str(biggest_percent_spread))

        # Print the bids and asks to the csv file
        print_values(f, ETH_bid_dict)
        print_values(f, ETH_ask_dict)

        f.write("\n")

        # Sleep for a while
        f.close()
        if(debug):
            # Sleep 60s or else I go over rate limit (2 devices running the script at once)
            print("Debugging...sleep for 60s")
            time.sleep(60)
        else:
            print("Done an entry, sleep for 30s")
            time.sleep(30)
