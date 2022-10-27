#!/usr/bin/env python3
""" TLG Learning | CWilliams
    Music Adventure Game Project """    # What is it

weapon = False

def main():
    # Instructions for the start of the game
    if __name__ == "__main__":
        while True:
            print("Welcome to the Music Adventure Game!")
            print("As an avid traveler and musician, you have decided to visit the Rock & Roll Hall of Fame.")
            print("However, during your exploration, you find yourself lost.")
            print("You can choose to walk in multiple directions to find a way out.")
            print("Let's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    introScene()
    
    # gives instructions on how to navigate
    def introScene():
        directions = ["left","right","forward"]
        print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
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

    def showGhostofChuckBerry():
        directions = ["right","backward"]
        print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
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

    def cameraScene():
        directions = ["forward","backward"]
        print("You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to go?")
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

    def hauntedRoom():
        directions = ["right","left","backward"]
        print("You hear strange voices. You think you have awoken the spirit of Elvis. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      print("Multiple goul-like creatures, with electric guitars, start emerging as you enter the room. You are killed.")
      quit()
    elif userInput == "left":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option.")

    def showSkeletonofRitchieValens():
        directions = ["backward","forward"]
    global false
    print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/backward/forward")
    userInput = input()
    if userInput == "left":
      print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
      weapon = True
    elif userInput == "backward":
      introScene()
    elif userInput == "forward":
      strangeCreature()
    else:
      print("Please enter a valid option.")

    def strangeCreature():
        actions = ["fight","flee"]
    global false 
    print("A strange goul-like creature resembling John Lennon has appeared. You can either run or fight it. What would you like to do?")
    userInput = ""
    while userInput not in actions:
        print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
      if weapon:
        print("You kill the goul with the knife you found earlier. After moving forward, you find one of the exits. Congrats!")
      else:
        print("The goul-like creature has killed you.")
      quit()
    elif userInput == "flee":
      showGhostofRitchieValens()
    else:
      print("Please enter a valid option.")

main()

