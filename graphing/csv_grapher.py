import sys # For argv

# For plotting
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime # For datetime.datetime for time on the x axis

# Number of exchanges currently in the csv logger
exchange_number = 9

# Desired timezone offset from UTC (ms) currently set to MST
timezone_offset = 21600000

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
        # This is a bit of a hack, but subtract off the ms so we can convert
        # the timezone from UTC to MST
        return_array.append((timestamp - timezone_offset)/1000)
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
    # We will store our list of lines in this list
    lines = list()
    # We will use this line dict to map thte lines to the legends
    linedict = dict()

    # Initialize the figure and the plot
    fig = plt.figure(figsize=(16,9))
    ax1 = fig.add_subplot(111)

    fig.canvas.set_window_title('Ethereum Price Graph :D')

    # Date/time formatting
    date_fmt = '%d-%m-%y %H:%M:%S'
    date_formatter = md.DateFormatter(date_fmt)
    ax1.xaxis.set_major_formatter(date_formatter)
    ax1.xaxis_date()

    # Axis labels and titles
    ax1.set_xlabel("Time (MST)")
    ax1.set_ylabel("Price (USD)")
    ax1.set_title("Ethereum Price Vs. Time")

    colors = ["Red", "Green", "Magenta", "Navy", "Purple", "Orange", "Brown", "Grey", "Yellow", "Black"]
    # Print all of the y data
    for i,y in enumerate(y_array):
        lines.append(ax1.plot(x, y, color=colors[i], label=exchange_names[i]))

    # Show the legend
    legend = plt.legend(loc='lower left')

    # Map the lines to the appropriate legend
    for legline, origline in zip(legend.get_lines(), lines):
        legline.set_picker(5)  # 5 pts tolerance
        linedict[legline] = origline

    # Bind the onpick event to allow series to be shown/hidden
    fig.canvas.mpl_connect("pick_event", lambda event: onpick(event, linedict, fig))

    plt.show()

# Allows hiding/showing series when the appropriate legend title is selected
# From https://matplotlib.org/examples/event_handling/legend_picking.html
def onpick(event, linedict, fig):
    # on the pick event, find the orig line corresponding to the
    # legend proxy line, and toggle the visibility
    legline = event.artist
    origline = linedict[legline]

    # For each point in the series, toggle the visibility
    for point in origline:
        vis = not point.get_visible()
        point.set_visible(vis)

    # Change the alpha on the line in the legend so we can see what lines
    # have been toggled
    if vis:
        legline.set_alpha(1.0)
    else:
        legline.set_alpha(0.2)
    fig.canvas.draw()

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
