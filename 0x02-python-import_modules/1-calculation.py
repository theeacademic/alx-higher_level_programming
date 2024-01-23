#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
    result_add = add(a, b)
    result_subtract = sub(a, b)
    result_multiply = mul(a, b)
    result_divide = div(a, b)

    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_subtract))
    print("{} * {} = {}".format(a, b, result_multiply))
    print("{} / {} = {}".format(a, b, result_divide))


