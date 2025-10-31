##
#   -Item Counter-
# 10/31/2025 🎃
# By Parker Jolly
# Counts non-empty lines in a file.
##

def count_file_lines():
    # Create variables
    num_of_names = 0
    FILEPATH = "names.txt"
    file = ""

    # Run in a try to catch errors
    try:
        # Try to open file
        file = open(FILEPATH,"r")

        # If a line is not empty, assume its a name and add to the accumulator
        for line in file:
            if line != "":
                num_of_names += 1
            else:
                break

        print(f"There are {num_of_names} names in the file names.txt.")

    # Error messages
    except FileNotFoundError:
        print(f"The file {FILEPATH} could not be found")
    except:
        print("An unkown error occured")
    finally:
        # To avoid an error, only close the file if it was a file
        if file != "":
            file.close()


if __name__ == '__main__':
    count_file_lines()