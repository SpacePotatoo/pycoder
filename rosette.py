"""
@Author: Ayuta
Description: a simple turtle code to draw a rosette
"""

import turtle 
 
wn = turtle.Screen()        
alex = turtle.Turtle()
wn.bgcolor("black")
alex.pencolor("blue")
speed=100 



for y in range(1,19):
    for z in range(1,361):
        alex.forward(1)
        alex.left(1)  
    alex.right(20)

    
