#!/usr/bin/python3
"""Defines an integer addition function."""
def add_integer(a, b=98):
    """
    Function to add two numbers after ensuring they are integers.

    Parameters:
    a (int, float): The first parameter.
    b (int, float): The second parameter. Default is 98.

    Returns:
    int: The return value. a and b casted to integers and added together.

    Raises:
    TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

