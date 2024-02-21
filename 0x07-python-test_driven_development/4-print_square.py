#!/usr/bin/python3
"""Defines a square-printing function."""
def print_square(size):
    """
    Function to print a square with the character #.

    Parameters:
    size (int): The size length of the square.

    Raises:
    TypeError: If size is not an integer or if size is a float and is less than 0.
    ValueError: If size is less than 0.

    >>> print_square(3)
    ###
    ###
    ###
    >>> print_square(0)
    <BLANKLINE>
    >>> print_square(4.0)
    ####
    ####
    ####
    ####
    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0
    >>> print_square(4.5)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer
    >>> print_square("4")
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer
    """

    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

