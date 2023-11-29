#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Print the desired output
print("Last digit of", number, "is", last_digit, "and is", end=" ")

if number < 0:
    last_digit *= -1  # Make it negative if the original number was negative

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
