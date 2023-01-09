import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.color("coral")
timmy.speed(0)
timmy.hideturtle()
turtle.colormode(255)

def random_circle():
    turn = 0
    for _ in range(90):
        timmy.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        timmy.circle(100)
        timmy.right(turn)
        turn+=1

random_circle()
screen = Screen()
screen.exitonclick()