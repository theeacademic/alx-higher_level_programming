#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# YOUR CODE HERE
if number < 0:
    print(f"The number {number} is negative")
elif number == 0:
    print(f"The number {number} is zero")
else:
    print(f"The number {number} is positive")
