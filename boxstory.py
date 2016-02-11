# This is the BoxStory Class - The Storyline which involves a word guessing game.

import random


def boxguessing():
    print("Soap looks around the great dark space. All he has ever known is the cardboard walls that encapsulate him. "
          "Soap wants to see the world. But first, he has to leave his cage. Well, really, he has to leave his box.")
    print("Upon approaching the box, Soap discovers that it has a cardboard lock attached securely to its entrance. "
          "It seems to be inscribed on the cardboard flap: 'You have to guess the secret word in order to unlock me!'")
    print("Soap realized that the only way to leave his humble abode was to scream at the door until he found the "
          "right word.")
    print(separator())
    _guessword1 = random.choice(wordlist)
# Debug Only:
    print(_guessword1)
    _letternum = len(_guessword1)

    for tries in range(5, 0, -1):
        print("The word has " + str(_letternum) + " letters")
        print("What's your guess for the word?")
        ans = input()
        if ans == _guessword1:
            print("You guessed correctly! The word was " + _guessword1 + ".")
            break
        else:
            print("Incorrect. You have " + str(tries-1) + " tries left")
            if tries == 1:
                print("You don't have any tries left. Looks like the door is closed and you'll remain the mustiness for"
                      " now. Goodbye.")
                input()
                quit()
            for i in ans:
                if i in _guessword1:
                    print("The answer contains the letter: " + i)


# Soap wants to figure out whether he wants to see the world or not.
def openingbox():
    print(separator())
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

def separator():
    return "------------------------------------------------------------------------------------------------------"


token = None
wordlist = ['dishes', 'carbon', 'adventure', 'cardboard', 'corny', 'turbulent', 'fastidious', 'fingers']
ansSpot = 0
