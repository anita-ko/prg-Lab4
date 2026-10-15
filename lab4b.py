# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Anita Ko 
# Date: October 14, 2026
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

# TO DO 1: Add the docstring
# @Function definition: find all even numbers in a list
# @param: numbers - a list of integers
# @return: a list containing all even numbers

# TO DO 2: Create the function.
def even_numbers(numbers):
    """return a list of even numbers"""
    even_list = []

    for number in numbers:
        if number %2 == 0:
            even_list.append(number)

    return even_list

# TO DO 3: Call the function.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = even_numbers(numbers)
print(result)