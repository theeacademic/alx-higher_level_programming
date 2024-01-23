#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Extracting command line arguments and converting them to integers
    args_as_integers = [int(arg) for arg in argv[1:]]
    
    # Calculating the sum of the integers
    result = sum(args_as_integers)

    # Printing the result
    print(result)

