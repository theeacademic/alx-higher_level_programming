#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

# Test cases
result1 = safe_print_integer(89)
result2 = safe_print_integer(-89)
result3 = safe_print_integer("School is not an integer")

# Output exactly as requested
print(result1)
print(result2)
print(result3)

