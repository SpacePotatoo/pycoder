"""
@Author: Ayuta
Description: a simple turtle code to draw with.
"""
import turtle

wn = turtle.Screen()
wn.title("drawing game")
head = turtle.Turtle()
wn.bgcolor("black")
head.pencolor("blue")
head.pensize(10)
speed = 1

def travel():
    head.forward(speed)
    wn.ontimer(travel, 10)

wn.onkey(lambda: head.left(15), 'Left')
wn.onkey(lambda: head.right(15), 'Right')
wn.onkey(lambda: head.penup(), 'Up')
wn.onkey(lambda: head.pendown(), 'Down')

wn.listen()

travel()

wn.mainloop() 