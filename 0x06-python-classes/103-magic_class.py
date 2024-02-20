#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by Holberton."""
import math

class MagicClass:
    """Represent a magic class."""

    def __init__(self, radius=0):
        """Initialize a new magic class."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the current area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the current circumference of the circle."""
        return 2 * math.pi * self.__radius

