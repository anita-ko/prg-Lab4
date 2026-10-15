# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Anita Ko 
# Date: October 14, 2026
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# Follow the instructions from readme.md.


#function to perform calculations
def compute(num1, num2, operation="+"):
    """Perform a calculation using two numbers."""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

#main function
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    result = compute(num1, num2, operation)
    print("The result is:", result)

    #test positional and default parameters
    print(compute(13, 45, "*"))
    print(compute(13, 45, "/"))
    print(compute(13, 45, "-"))
    print(compute(13, 45, "+"))
    print(compute(13, 45))


#call the main function
if __name__ == "__main__":
    main()
