#!/usr/bin/env python3
"""List objects and methods"""

def main():

    proto = ["ssh", "http", "https"]
    protoa = ["ssh", "http", "https"]
    print(proto)
    proto.append("dns") # this line will add "dns" to the end of our list
    protoa.append("dns") # this line will add "dns" to the end of our list
    print(proto)
    proto2 = [ 22, 80, 443, 53 ] # a list of common ports
    proto3 = [ 143] # list IMAP port
    proto.extend(proto2) # pass proto2 as an argument to the extend method
    print(proto)
    protoa.append(proto2) # pass proto2 as an argument to the extend method
    print(protoa)
    proto.extend(proto3) # pass proto3 as an argument to the extend method
    print(proto)
    protoa.append(proto3) # pass proto3 as an argument to the extend method
    print(protoa)

main()
