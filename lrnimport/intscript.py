#!/usr/bin/env python3
"""TLG Learning | CWilliams
   Scripting commands with Python"""

def main():
    from subprocess import call
    call(["ip", "link", "show", "up"])
    print("This program will check your interfaces.")

    interface = input("Enter an interface, like, ens3: ")
    call(["ip", "addr", "show", "dev", interface])

main()
