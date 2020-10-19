"""
@Author: Ayuta
Description: a text based game
"""
def gold_room():
    print("This room is full of gold. How much do you take?")
    
    choice=input(">> ")
    if "0" in choice or "1" in choice:
        how_much=int(choice)
    else:dead("man, learn to type a number")
    