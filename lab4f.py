# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Anita Ko 
# Date: October 14, 2026
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

# Follow the instructions from readme.md.

#function to get initials from names
def get_initials(*args):
    """Return the first letter of each name."""
    initials = []

    for name in args:
        initials.append(name[0])

    return initials


#main function
def main():
    names = get_initials("Alice", "Bob", "Charlie", "David")
    print(names)


#call the main function
if __name__ == "__main__":
    main()
