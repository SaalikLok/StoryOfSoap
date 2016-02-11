# This is the BoxStory Class - The Storyline which involves a word guessing game.

import random


def boxguessing():
    print("The box has a cardboard lock tied securely to its entrance. You have to guess the secret word in order "
          "to unlock it!")
    _guessword1 = random.choice(wordlist)
# Debug Only:
    print(_guessword1)
    _letternum = len(_guessword1)

    for tries in range(5, 0, -1):
        print("The word has " + str(_letternum) + " letters")
        print("What's your guess for the word?")
        ans = input()
        if ans == _guessword1:
            print("You guessed correctly! The word was " + _guessword1)
        else:
            print("Incorrect. You have " + str(tries-1) + " left")


# Soap wants to figure out whether he wants to see the world or not.
def openingbox():

    print("Today, Soap feels like breaking out of his shell. Well, he actually feels like breaking out of his box.")
    print("What should he do? 'break' or 'not'?")

    openbox = input()
    try:
        if openbox == "break":
            print("Accept adventure! Let's see what the world has to offer!")
            boxguessing()
        elif openbox == "not":
            print("Looks like the door is closed and you'll remain the mustiness for now. Goodbye.")
            input()
            quit()
    except ValueError:
        print("Try again, you haven't done anything.")


token = None
wordlist = ['dishes', 'carbon', 'adventure', 'cardboard', 'corny', 'turbulent', 'fastidious', 'fingers']
