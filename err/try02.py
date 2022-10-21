#!/usr/bin/env python3
"""TLG Learning | CWilliams
   Catching specific errors"""

def main():

    # Start with an infinite loop
    while True:
        try:
            print("Let's divide x by y!")
            x = int(input("What is the integer value of x? "))
            y = int(input("What is the integer value of y? "))
            print("The value of x/y: ", x/y)
        except ZeroDivisionError as zerr:
            print("Handling run-time error:", zerr)

    # General error handling
    # A practical use might be exceptions we haven't designed solutions for yet
        except Exception as err:
            # sys.exc_info returns a 3 tuple with into about the exception handled
            print("We did not anticipate that:", err)

main()