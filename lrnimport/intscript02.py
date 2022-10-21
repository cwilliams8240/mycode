#!/usr/bin/env python3
"""TLG Learning | CWilliams
   Scripting Commands with Python"""

def main():
    import subprocess  ## <------ changed
    subprocess.call(["ip", "link", "show", "up"])
    print("This program will check your interfaces.")
    interface = input("Enter an interface, like, ens3: ")
    subprocess.call(["ip", "addr", "show", "dev", interface])  ## <---- changed
    subprocess.call(["ip", "route", "show", "dev", interface]) ## <---- changed

main()
