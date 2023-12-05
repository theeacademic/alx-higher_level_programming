#!/usr/bin/python3
# File: 1-element_at.py

def element_at(my_list, idx):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return None
    
    # Return the element at the specified index
    return my_list[idx]

