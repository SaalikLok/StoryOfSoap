# This is the Dish Story - The storyline where HandSoap wants Soap to choose a new name, something a little less boring.
# Name Generation

import random

name = "Soap"
newname = None
fnamelist = ["Sudsy", "Frothy", "Dood", "Blah", "Stink", "Merp" ]
lnamelist = ["Shampoo", "Man", "Packet", "Bar", "Blah", "McSoap"]

def namegenerator():
    print("You are about to get a new name! The program will present a maximum of five combined first and last names. "
          "Approve of the name by typing 'y' and disapprove of the name, using anything else.")
    for tries in (5, 0, -1):
        newname = random.choice(fnamelist) + " " + random.choice(lnamelist)
        print("Here's a name: " + newname + ".")
        print("You have " + str(tries) + " left, do you like this name? Type 'y' if you do.")
        choice = input()
        if choice == "y":
            name = newname
            print("Awesome! Your new name is: " + name)
            break
        else:
            print("Okay. Let's try again.")

def dishstart():
    print("Soap is sitting in a soap dish. He's basking in the bright bathroom lights, three blazing suns in Soap's "
          "world.")
    print("Suddenly, Soap hear's a sound.")
    input()
    print("HandSoap: 'Hey there Soap. You look so glum. And I think I know why. It's because you hate your name, don't"
          " you? '")
    input()
    print("Handsoap: 'You want a new name, no matter what you say. Let's find one for you.' Press ENTER to continue.")
    input()
    namegenerator()

