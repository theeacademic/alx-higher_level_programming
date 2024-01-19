#!/usr/bin/python3
# models/rectangle.py

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
        __width (int): Private width of the rectangle.
        __height (int): Private height of the rectangle.
        __x (int): Private x-coordinate of the rectangle.
        __y (int): Private y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor for Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle (default is 0).
            y (int): y-coordinate of the rectangle (default is 0).
            id (int): Optional parameter for the instance id (default is None).

        Attributes:
            __width (int): Private width of the rectangle.
            __height (int): Private height of the rectangle.
            __x (int): Private x-coordinate of the rectangle.
            __y (int): Private y-coordinate of the rectangle.
        """
        # Call the constructor of the Base class with the provided id
        super().__init__(id)

        # Set private attributes with provided values, using the setters
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for width
    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.validate_positive_integer(value, 'width')
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.validate_positive_integer(value, 'height')
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        """Getter for x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x-coordinate."""
        self.validate_non_negative_integer(value, 'x')
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        """Getter for y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y-coordinate."""
        self.validate_non_negative_integer(value, 'y')
        self.__y = value

    def validate_positive_integer(self, value, attribute_name):
        """
        Validate that the given value is a positive integer.

        Args:
            value: The value to be validated.
            attribute_name (str): The name of the attribute for error message.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_non_negative_integer(self, value, attribute_name):
        """
        Validate that the given value is a non-negative integer.

        Args:
            value: The value to be validated.
            attribute_name (str): The name of the attribute for error message.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        elif value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")

