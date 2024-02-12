#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """
    Represents a square shape.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        area(): Calculates and returns the area of the square.
        my_print(): Prints the square using '#' characters.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

