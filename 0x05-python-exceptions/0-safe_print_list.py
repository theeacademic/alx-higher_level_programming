#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            nb_print += 1
    except IndexError:
        pass
    finally:
        print()
        print("nb_print:", nb_print)
        return nb_print

# Test cases
my_list1 = [1, 2]
safe_print_list(my_list1, 5)

