# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Anita Ko 
# Date: October 14, 2026
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

# Follow the instructions from readme.md.

#function to add two numbers
def sum(num1, num2):
    """return the sum of two numbers"""
    return num1 + num2

#main function
def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = sum(num1, num2)
    print("The sum is:", result)


#call the main function
if __name__ == "__main__":
    main()