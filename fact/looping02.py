#!/usr/bin/env python3
"""TLG Learning | CWilliams
   For - Using a file's lines a s aource for the for-loop"""

def main():

    # open file in a read mode
    dnsfile = open("dnsservers.txt", "r")

    # create list of lines
    dnslist = dnsfile.readlines()

    # loop over lines
    for svr in dnslist:
        # printand end without a newline
        print(svr, end="")  # the line we read ALREADY contains a \n (newline)

    # close the file (we created the list of lines)
    dnsfile.close() # best practice to close your file

main()
