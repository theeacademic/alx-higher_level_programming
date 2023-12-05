#!/usr/bin/python3
# File: 2_replace_in_list.py

def replace_in_list(my_list, idx, new_element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Modify the list by replacing the element at the specified index
    my_list[idx] = new_element
    return my_list

