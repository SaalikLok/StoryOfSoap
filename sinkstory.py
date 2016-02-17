# This is the Sink Story, where soap must answer riddles so that the hand will take him away from corrosive water.
import random


def sinkriddles(r):
    if r == 1:
        print("What building has the most stories?")
        ans1 = input()
        if ans1 == "library":
            print("Correct! You escape the corrosive water and go back to hanging out in the bathroom.")
            input()
            quit()
        else:
            print("Sorry, the correct answer is: the LIBRARY. See you next time!")
            input()
            quit()
    if r == 2:
        print("Railroad crossings are without cars. Can you spell that without any r's?")
        ans2 = input()
        if ans2 == "that":
            print("Correct! You escape the corrosive water and go back to hanging out in the bathroom!")
            input()
            quit()
        else:
            print("Sorry, the correct answer is: THAT. See you next time!")
            input()
            quit()
    if r == 3:
        print("What am I?")
        ans3 = input()
        if ans3 == "question":
            print("Correct! You escape the corrosive water and go back to hanging out in the bathroom.")
            input()
            quit()
        else:
            print("Sorry, the correct answer is: a QUESTION. See you next time!")
            input()
            quit()
    if r == 4:
        print("What cheese isn't yours?")
        ans4 = input()
        if ans4 == "nacho":
            print("Correct! You escape the corrosive water and go back to hanging out in the bathroom.")
            input()
            quit()
        else:
            print("Sorry, the correct answer is: NACHO. Get it, not-cho cheese? See you next time!")
            input()
            quit()
    if r == 5:
        print("What's brown and sticky?")
        ans5 = input()
        if ans5 == "stick":
            print("Correct! You escape the corrosive water and go back to hanging out in the bathroom.")
            input()
            quit()
        else:
            print("Sorry, the correct answer is: a STICK! See you next time!")
            input()
            quit()


def sinkstart():
    print("Soap finds himself being grabbed by two greedy, sweaty hands. The hands move him to the center of the "
          "'sink', some mysterious device that humans use. To soap, it's an overrated bowl. As the water pours onto "
          "him, Soap realizes that it is slowly ripping away at him.")
    input()
    print("Answering the riddle will fix him. Answer all riddles in lowercase letters and in one word.")
    r = random.randint(1, 5)
    sinkriddles(r)
