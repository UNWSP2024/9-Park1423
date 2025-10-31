##
#   -Average numbers-
# 10/31/2025 🎃
# By Parker Jolly
# Reads numbers from a file and returns the average
##

# Initilize varibles to prevent errors
FILEDIRECTORY = "numbers.txt"
file = ""


def sum_numbers_from_file():
    total = 0
    lines = 0

    try:
        # Open file
        file = open(FILEDIRECTORY, "r")

        # For each non-empty line add the line to total and 1 to lines, the total number of lines
        for line in file:
            if line != "":
                lines += 1
                total += int(line)
            else:
                break
            
        # Print the average
        print(f"The average number in the file {FILEDIRECTORY} is {total/lines:.2f}")

    # Handle errors
    except FileNotFoundError:
        print(f"ERR: The file {FILEDIRECTORY} could not be found.")
    except ZeroDivisionError:
        print(f"ERR: The file {FILEDIRECTORY} is empty.")
    except ValueError:
        # Lines here would be the last line read before this crash happened.
        print(f"ERR: Line {lines} in {FILEDIRECTORY} is not a number.")
    except:
        print("ERR: An unkown error occured.")




# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()