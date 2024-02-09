#!/usr/bin/python3
class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square (private attribute).

    Methods:
        None

    Usage:
        my_square = Square(3)
        print(type(my_square))  # Output: <class '1-square.Square'>
        print(vars(my_square))  # Output: {'_Square__size': 3}
        print(my_square.size)   # Output: AttributeError: 'Square' object has no attribute 'size'
        print(my_square.__size) # Output: AttributeError: 'Square' object has no attribute '__size'
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.

        Note:
            The size is a private attribute.
        """
        self.__size = size

if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))  # Output: <class '1-square.Square'>
    print(vars(my_square))  # Output: {'_Square__size': 3}

    # Attempt to access the private attribute directly
    try:
        print(my_square.size)   # Output: AttributeError: 'Square' object has no attribute 'size'
        print(my_square.__size) # Output: AttributeError: 'Square' object has no attribute '__size'
    except AttributeError as e:
        print(e)

