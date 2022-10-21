#!/usr/bin/python3
"""TLG Learning | CWilliams
   Review of try and except logic"""

def main():

    # Start with an infinite loop
    while True:
        try:
            print("Enter a file name: ")
            name = input
            with open(name, "w") as myfile:
                myfile.write("No problems with that file name.")
            break

        except:
            print("Error with that file name! Try again...")

main()
