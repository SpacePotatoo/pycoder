"""
@Author: Ayuta
Description: a text based game
"""

import sys

yes_no = ["yes", "no", "y", "n"]
directions_1 = ["left", "right", "forward", "backward", "l", "r", "f", "b"]
directions_2 = ["left", "right", "into the forest", "l", "r", "i"]
choice = ["run", "fight", "r", "f"]


name = input("What is your name, adventurer?\n>>")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 

response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n>>")
    
    if response == "yes" or response == "y" :
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no" or response == "n":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        sys.exit()
    else: 
        print("I didn't understand that.\n")

    
response = ""    
while response not in directions_1:
    print("To your left, you see a bear.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n>>")
    
    if response == "left" or response == "l":
        print("The bear rips you to shreds. Farewell, " + name + ".")
        sys.exit()
    elif response == "right" or response == "r":
        print("You head deeper into the forest.\n")
    elif response == "forward" or response == "f":
        print("You hear rumbling. Seconds later a boulder comes rolling downhill, needless to say, you die. Farewell, " + name + ".")
        sys.exit()
    elif response == "backward" or response == "b":
        print("You leave the forest. Goodbye, " + name + ".")
        sys.exit()
    else:
        print("I didn't understand that.\n")


response1 = ""            
while response1 not in directions_2:
    print("After trekking through the forest for a while, you see that the dirt path you had been following so far has split up.\n")
    response1 = input("which path do you choose?\nleft/right/into the forest\n>>")
    
    if response1 == "into the forest" or response == "i":
        print("as you stray from the path and enter the forest, you slip on some mud and crack your head on a nearby rock. Farewell, "+ name + ".")
        sys.exit()
    elif response1 == "left" or response1 == "l":
        print("You take the left path and walk on.\n")
    elif response1 == "right" or response1 == "r":
        print("You take the right path and walk on.\n")
    else:
        print("i didn't understand that.\n")
        
if response1 == "left" or response1 == "l":
    response = ""
    while response not in choice:
        print("After following the left path for a while you suddenly see a pack of wolves in front of you. They have now noticed you.")
        response = input("What do you do?\nfight/run\n>>")
        
        if response == "fight" or response == "f":
            print("You were no match for those wolves and quickly became their lunch. Farewell, " + name + ".")
            
        elif response == "run" or response == "r":
            print("The wolfs quickly caught up to you and devoured you. Farewell adventurer.")
 
        
sys.exit()
