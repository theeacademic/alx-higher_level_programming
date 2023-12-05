#!/usr/bin/python3
# File: 3_print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    # Iterate through the list in reverse order and print each integer
    for i in range(len(my_list) - 1, -1, -1):
        print("{}".format(my_list[i]))

# Uncomment the line below for testing in isolation
# print_reversed_list_integer([1, 2, 3, 4, 5])

