#Saalik Lokhandwala's Story of Soap.
#Ver 0.01

import boxstory
import dishstory

print("Hello World. This is the Story of Soap, an interactive tale told using the most basic Python Code.")
print("Have you met Soap Before? Answer using 'y' or 'n'")
metSoap = input()

if metSoap == ('n' or 'N'):
    print("Soap is an awesome ... bar of soap. Want to know what his adventures are like? Here's how they work.")
    print("One day, Soap was just hanging out in his dark box. What should soap do?")
    soapAction = input()
    print("So Soap decided to " + soapAction)
    print("Well. That's pretty ridiculous isn't it? We need to make sure Soap doesn't do crazy things like " + soapAction +
          ". That's why we should start a real adventure!")
else:
    print("Looks like you didn't say no... so you have met Soap!")

print("Are you ready to go?")
print("You better be! Press ENTER to continue.")
input()

dishstory.dishstart()
boxstory.openingbox()
