#!/usr/bin/env python3
""" TLG Learning | CWilliams
    Python Project - Adventure Game"""  # python adventure game

import sys


def main():
    """called at runtime"""


# Instructions for the start of the game
WEAPON = False


if __name__ == "__main__":
    while True:
        print("Welcome to the Music Adventure Game!")
        print("As an avid traveler and musician, you have decided to visit\n"
              "the Rock & Roll Hall of Fame.")
        print("However, during your exploration, you find yourself lost.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's start with your name: ")
        name = input()
        print("Good luck, " + name + ".")
        intro_scene()


def intro_scene():
    """define user actions in intro scene"""

    directions = ["left", "right", "forward"]
    print("You are at a crossroads, and you can choose to go down\n"
          "any of the four hallways. Where would you like to go?")

    user_input = ""

    while user_input not in directions:
        print("Options: left/right/backward/forward")

        user_input = input()

        if user_input == "left":
            show_ghost_of_chuck_berry()

        elif user_input == "right":
            show_skeleton_of_ritchie_valens()

        elif user_input == "forward":
            haunted_room()

        elif user_input == "backward":
            print("You find that this door opens into a wall.")

        else:
            print("Please enter a valid option.")


def show_ghost_of_chuck_berry():
    """define user action when encountering shadowy figure"""

    directions = ["right", "backward"]
    print("You see a dark shadowy figure appear in the distance.\n"
          "You are creeped out. Where would you like to go?")

    user_input = ""

    while user_input not in directions:
        print("Options: right/left/backward")

        user_input = input()

        if user_input == "right":
            camera_scene()

        elif user_input == "left":
            print("You find that this door opens into a wall.")

        elif user_input == "backward":
            intro_scene()

        else:
            print("Please enter a valid option.")


def camera_scene():
    """define user action when noticing camera"""

    directions = ["forward", "backward"]
    print("You see a camera that has been dropped on the ground.\n"
          "Someone has been here recently. Where would you like to go?")

    user_input = ""

    while user_input not in directions:
        print("Options: forward/backward")
        user_input = input()

        if user_input == "forward":
            print("You made it! You've found an exit.")

            sys.exit()

        elif user_input == "backward":
            show_ghost_of_chuck_berry()

        else:
            print("Please enter a valid option.")


def haunted_room():
    """define user action when strange voices are heard"""

    directions = ["right", "left", "backward"]
    print("You hear strange voices. You think you have awoken\n"
          "the spirit of Elvis. Where would you like to go?")

    user_input = ""

    while user_input not in directions:
        print("Options: right/left/backward")
        user_input = input()

        if user_input == "right":
            print("Multiple goul-like creatures, with electric guitars,\n"
                  "start emerging as you enter the room. You are killed.")

            sys.exit()

        elif user_input == "left":
            print("You made it! You've found an exit.")

            sys.exit()

        elif user_input == "backward":
            intro_scene()

        else:
            print("Please enter a valid option.")


def show_skeleton_of_ritchie_valens():
    """define user action when encountering skeletons"""

    directions = ["backward", "forward"]

    global WEAPON
    WEAPON = 'knife'

    print("You see a wall of skeletons as you walk into the room.\n"
          "Someone is watching you. Where would you like to go?")

    user_input = ""

    while user_input not in directions:
        print("Options: left/backward/forward")

        user_input = input()

        if user_input == "left":
            print(
                "You find that this door opens into a wall.\n"
                "You open some of the drywall to discover a knife.")

            WEAPON = True

        elif user_input == "backward":
            intro_scene()

        elif user_input == "forward":
            strange_creature()

        else:
            print("Please enter a valid option.")


def strange_creature():
    """define user action when encountering creature"""

    actions = ["fight", "flee"]

    global WEAPON
    WEAPON = 'knife'

    print("A strange goul-like creature resembling John Lennon has appeared.\n"
          "You can either run or fight it. What would you like to do?")

    user_input = ""

    while user_input not in actions:
        print("Options: flee/fight")

        user_input = input()

        if user_input == "fight":
            if WEAPON:
                print(
                    "You kill the goul with the knife you found earlier.\n"
                    "After moving forward, you find one of the exits. Congrats!")

            else:
                print("The goul-like creature has killed you.")

            sys.exit()

        elif user_input == "flee":
            show_skeleton_of_ritchie_valens()

        else:
            print("Please enter a valid option.")


main()
