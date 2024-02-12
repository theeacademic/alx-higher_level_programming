#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """
    Represents a square shape.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

