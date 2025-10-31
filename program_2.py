# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

##
#   -Random Number File Writer-
# 10/31/2025 🎃
# By Parker Jolly
# Writes random numbers to a file
##
from random import *

FILEDIRECTORY = "numbers.txt"


def main():
    try:
        # Open file and get number of numbers to generate
        file = open(FILEDIRECTORY,"w")
        numOfNums = int(input("Enter the number of random numbers to generate: "))

        # Create random numbers
        for i in range(numOfNums):
            file.write(str(randint(1,500)))
            
            # Don't add a newline to the last line
            if i != numOfNums-1:
                file.write("\n")
        
        print("File created successfully.")

    #Handle errors
    except TypeError:
        print(f"ERR: Your input must be a valid integer, such as 1, 200, or -5")
    except:
        print("ERR: An unkown error occured.")




if __name__ == "__main__":
    main()