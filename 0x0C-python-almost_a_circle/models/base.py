#!/usr/bin/python3
# models/base.py

class Base:
    # private class attribute to keep track of instances
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor for Base.

        Args:
            id (int): Optional parameter for the instance id.
                      If provided, sets the public instance attribute 'id' to the given value.
                      If not provided, increments __nb_objects and sets 'id' to the new value.

        Attributes:
            id (int): Public instance attribute representing the unique identifier for each instance.
        """
        if id is not None:
            # assign the public instance attribute 'id' with the argument value
            self.id = id
        else:
            # increment __nb_objects and assign the new value to the public instance attribute 'id'
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

# Example usage
if __name__ == "__main__":
    # Creating instances of Base class
    obj1 = Base()
    obj2 = Base()
    obj3 = Base(id=3)
    obj4 = Base()

    # Printing the ids of instances
    print(obj1.id)
    print(obj2.id)
    print(obj3.id)
    print(obj4.id)

