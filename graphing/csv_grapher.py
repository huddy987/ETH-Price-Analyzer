import sys # For argv

# For plotting
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime # For datetime.datetime for time on the x axis

# Number of exchanges currently in the csv logger
exchange_number = 9

# Returns filename if specified otherwise prints the usage and closes
def parse_args():
    try:
        return str(sys.argv[1])
    except IndexError:
        print("Usage: python csv_grapher.py <path-to-file>")
        sys.exit()

# Generates a list of data from the csv file. Row is the row number you
# want to generate data from.
def generate_data(filename, row):
    file = open(filename, "r+")

    data = list()

    # Skip the header
    file.readline()

    while(True):
        # Read a line and return if we have hit EOF
        line = file.readline()
        if(line == ""):
            return data

        line = line.split(",")
        data.append(float(line[row]))

# Converts epoch to a timestamp usable by pyplot
def convert_epoch(timestamps):
    return_array = list()
    for timestamp in timestamps:
        return_array.append(timestamp/1000)
    return md.epoch2num(return_array)

# Gets the exchange names from the header
def get_exchange_names(filename):
    file = open(filename, "r+")
    exchanges = list()

    # Read the header
    line = file.readline()
    line = line.split(",")

    for i in range(exchange_number):
        name_cell = line[i+2] # Exchanges start at cell 3
        name_cell = name_cell.split()
        exchanges.append(name_cell[0])

    return exchanges


# Plots the data
def plot(x, y_array, exchange_names):
    fig, ax1 = plt.subplots()

    # Date/time formatting
    date_fmt = '%d-%m-%y %H:%M:%S'
    date_formatter = md.DateFormatter(date_fmt)
    ax1.xaxis.set_major_formatter(date_formatter)
    ax1.xaxis_date()

    # Axis labels
    ax1.set_xlabel("Time (UTC)")
    ax1.set_ylabel("Price (USD)")

    # Print all of the y data
    for i,y in enumerate(y_array):
        ax1.plot(x, y, label=exchange_names[i])

    # Set all of the colors
    colors = ["Red", "Green", "Blue", "Pink", "Purple", "Orange", "Brown", "Grey", "Yellow", "Black"]
    for i,j in enumerate(ax1.lines):
        j.set_color(colors[i])

    plt.legend(loc='lower left')

    plt.show()


if __name__ == "__main__":
    # Get the filename from sys.argv
    filename = parse_args()

    # Get the time data
    date_time = generate_data(filename, 0)

    # Convert epoch timestamps to proper format for pyplot
    date_time = convert_epoch(date_time)

    # Get the price data
    price_array = list()
    for i in range(exchange_number):
        price_array.append(generate_data(filename, (i + 2))) # Start at the 3rd cell

    # Get exchange names in the same order as the prices
    exchange_names = get_exchange_names(filename)

    # Plot the data
    plot(date_time, price_array, exchange_names)
