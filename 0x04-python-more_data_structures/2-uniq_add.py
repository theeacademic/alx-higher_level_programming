#!/usr/bin/python3

# Importing is not needed in this case, you can define the function directly
# uniq_add = __import__('2-uniq_add').uniq_add

def uniq_add(my_list=[]):
    # Use a set to store unique integers and sum them up
    unique_sum = sum(set(my_list))
    
    return unique_sum

if __name__ == "__main__":
    # Test the function with the provided list
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)

    # Print the result
    print("Result: {:d}".format(result))

