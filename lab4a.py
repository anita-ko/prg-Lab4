# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Anita Ko 
# Date: October 14, 2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py

# TO DO 1: Add the docstring
# @Function definition: check if a number is even
# @param: number - an integer to check
# @return: true if even, flase if odd

# TO DO 2: define the function with name `is_even`.
def is_even(numbers):
    """check if number is even"""
    result = False

    for number in numbers:
        if number & 2 == 0:
            result = True
            break

    return result

# TO DO 3: Call the function `is_even`.
numbers = [1, 2, 3, 4, 5, 6]

result = is_even(numbers)
print(result)