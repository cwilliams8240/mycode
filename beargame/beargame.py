#!/usr/bin/env python3
"""TLG Learning | CWilliams
   The Bear Game"""

def main():
    """ Code at runetime """
    print("Hey! Ready to play? First, tell me a little about yourself.")

    name = input("First, what's your name?")
    print("Great to meet you, {0}!".format(name))

    age = int(input("Next, how old are you? "))

    # Calculate how old?!?
    if age >= 27:
        print("OMG! {0}, you're old as dirt.".format(name))
    elif age <= 25:
        print("You're a youngin. {0}.".format(name))
    else:
        print("Enter a number silly")
   
    print("Okay, let's set the stage. You're walking through a dense forest \n" "when suddenly you happen upon a bear.")

    bearChoice = input("What do you do? run, cry or fight? ")

    if bearChoice == "run":
        print("Smart choice. That bear would have ripped you apart. You win the game!")
    elif bearChoice == "cry":
        print("Well, that doesn't help...You're dead!")
    elif bearChoice == "fight":
        print("Well, that was dumb...You're dead!")
    else:
        print("I don't think that was an option. I'll let you try again.")

main()

