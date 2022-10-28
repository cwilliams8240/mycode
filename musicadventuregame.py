#!/usr/bin/env python3
""" TLG Learning | CWilliams
    Music Adventure Game """

weapon = False    # weapon for later in game

"""called at runtime"""


def strangeCreature():    # prompts user to an action against the creature

    actions = ["fight", "flee"]

    global weapon

    print("A strange goul-like creature that resembles John Lennon/n"
          "has appeared. You can either run or fight it. What would/n"
          "you like to do?")

    userInput = ""

    while userInput not in actions:  # create a while loop for choices

        print("Options: flee/fight")

        userInput = input()    # prompts user to flee or fight

        if userInput == "fight":

            if weapon:

                print("You kill the goul with the knife you found earlier./n"
                      "After moving forward, you find one of the exits. Congats!")

        else:

            print("The goul-like creature has killed you.")

            quit()

        if userInput == "flee":

            showSkeletonofRitchieValens()

        else:

            print("Please enter a valid option.")


def showSkeletonofRitchieValens():  # prompts user to an action

    directions = ["backward", "forward"]

    global weapon

    print("You see a wall of skeletons as you walk into the room.\n"
          "Someone is watching you. Where would you like to go?")

    userInput = ""

    while userInput not in directions:

        print("Options: left/backward/forward")

        userInput = input()

        if userInput == "left":

            print("You find that this door opens into a wall.\n"
                  "You open some of the drywall to discover a knife.")

            weapon = True  # user obtains weapon

        elif userInput == "backward":

            introScene()

        elif userInput == "forward":

            strangeCreature()

        else:

            print("Please enter a valid option.")


def hauntedRoom():  # defines room with the Ghost of Elvis

    directions = ["right", "left", "backward"]

    print("You hear a strange voice. You think you have awoken\n"
          "the ghost of Elvis. Where would you like to go?")

    userInput = ""

    while userInput not in directions:

        print("Options: right/left/backward")

        userInput = input()

        if userInput == "right":

            print("Multiple goul-like creatures start emerging\n"
                  "as you enter the room. You are killed.")

            quit()

        elif userInput == "left":

            print("You made it! You've found an exit.")

            quit()

        elif userInput == "backward":

            introScene()

        else:

            print("Please enter a valid option.")


def cameraScene():

    directions = ["forward", "backward"]

    print("You see a camera that has been dropped on the ground.\n"
          "Someone has been here recently. Where would you like to go?")

    userInput = ""

    while userInput not in directions:

        print("Options: forward/backward")

        userInput = input()

        if userInput == "forward":

            print("You made it! You've found an exit.")

            quit()

        elif userInput == "backward":

            showGhostofChuckBerry()

        else:

            print("Please enter a valid option.")


def showGhostofChuckBerry():

    directions = ["right", "backward"]

    print("You see a dark shadowy figure appear in the distance.\n"
          "You are creeped out. Where would you like to go?")

    userInput = ""

    while userInput not in directions:

        print("Options: right/left/backward")

        userInput = input()

        if userInput == "right":

            cameraScene()

        elif userInput == "left":

            print("You find that this door opens into a wall.")

        elif userInput == "backward":

            introScene()

        else:

            print("Please enter a valid option.")


def introScene():

    directions = ["left", "right", "forward"]

    print("You are at a crossroads, and you can choose to go down\n"
          "any of the four hallways. Where would you like to go?")

    userInput = ""

    while userInput not in directions:

        print("Options: left/right/backward/forward")

        userInput = input()

        if userInput == "left":

            showGhostofChuckBerry()

        elif userInput == "right":

            showSkeletonofRitchieValens()

        elif userInput == "forward":

            hauntedRoom()

        elif userInput == "backward":

            print("You find that this door opens into a wall.")

        else:

            print("Please enter a valid option.")


if __name__ == "__main__":

    while True:

        print("Welcome to the Rock & Roll Hall of Fame Adventure Game!")

        print(
            "As an avid traveller, you have decided to visit the Rock & Roll Hall of Fame.")

        print("However, during your exploration, you find yourself lost.")

        print("You can choose to walk in multiple directions to find a way out.")

        print("Let's start with your name: ")

        name = input()

        print("Good luck, " + name + ".")

        introScene()
