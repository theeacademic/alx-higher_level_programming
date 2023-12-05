#!/usr/bin/env python3
# File: 5_no_c.py

def no_c(my_string):
    # Create a new string without characters 'c' and 'C'
    new_string = ''
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string

