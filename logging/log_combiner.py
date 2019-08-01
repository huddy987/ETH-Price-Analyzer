import sys # For argv
import os # For chdir
import glob # To find csv files in directory

# Returns filename if specified otherwise prints the usage and closes
def parse_args():
    try:
        return str(sys.argv[1])
    except IndexError:
        print("Usage: python log_combiner.py <log-directory>")
        sys.exit()

def add_to_combined_csv(filename, combined_filename, is_first_file):
    input_file = open(filename, "r+")
    output_file = open(combined_filename, "a+")

    # Skip the header
    if(not is_first_file):
        input_file.readline()

    while(True):
        line = input_file.readline()

        if(line == ""):
            input_file.close()
            output_file.close()
            return

        output_file.write(line)



if __name__ == "__main__":
    directory = parse_args()
    combined_filename = "combined.csv"

    # Enter the directory specified
    os.chdir(directory)

    print("Starting...")
    is_first_file = True # Used for determining if we should write the header

    # Delete the combined file if it already exists in the directory
    if(os.path.isfile("./" + combined_filename)):
        userin = input("Combined CSV already exists! Continuing will delete it. [Y] to continue.")

        # Only continue if the user is ok with it
        if(userin == "Y" or userin == "y"):
            os.remove("./" + combined_filename)
        else:
            print("Aborting.")
            sys.exit(1)

    for filename in glob.glob("*.csv"):
        # Skip adding itself if the combined filename already exists
        if(filename == combined_filename):
            continue

        # Add all the files in the directory to the combined csv
        add_to_combined_csv(filename, combined_filename, is_first_file)

        # This is for writing the header, disable the flag after the first file
        if(is_first_file == True):
            is_first_file = False

        print("Completed adding " + filename)

    print("Done!")
