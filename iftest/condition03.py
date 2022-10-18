#!/usr/bin/env python3
"""TLG Learning | CWilliams
   if condtions 3"""

def main():

    ## Collect input from user
    hostname = input("What value should we set for hostname?")

    ## use the lower method to test if input value matches expected value
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")

    ## Always print out to the user
    print("Existing the script")

main()

