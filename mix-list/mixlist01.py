#!/usr/bin/env python3
"""TLG Learning | CWilliams
   Playing with lists"""

def main():

    my_list = [ "192.168.0.5", 5060, "UP" ]
    # display only the IP addresses to the screen.
    iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]
    wordbank= ["indentation", "spaces"] 
    tlgstudents= ["Aaron", "Andy", "Asif",
            "Brent", "Cedric", "Chris",
            "Cory", "Ebrima", "Franco",
            "Greg", "Hoon", "Joey",
            "Jordan", "JC", "LB",
            "Mabel", "Shon", "Pat", "Zach"]
    wordbank.append(4)
    num= input("Pick a student number!")
    num= int(input("Pick a student number!"))
    choice= int(input("Pick a student number!"))
    student_name= tlgstudents[choice]
    
    print("The first item in the list (IP): " + my_list[0] )
    print("The second item in the list (port): " + str(my_list[1]) )
    print("The last item in the list (state): " + my_list[2] )
    print("IP addresses:", iplist[3], ", and", iplist[4])
    print(<student_name> always uses <4> <spaces> to indent.)

main()
