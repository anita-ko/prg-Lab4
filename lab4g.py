# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Anita Ko 
# Date: October 14, 2026
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py

# Follow the instructions from readme.md.

#create a list of numbers from 2 to 10
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

#square all numbers using map and lambda
numbers = list(map(lambda x: x ** 2, numbers))
print(numbers)

#filter numbers divisible by 2
divisible_by_2 = list(filter(lambda x: x % 2 == 0, numbers))
print(divisible_by_2)