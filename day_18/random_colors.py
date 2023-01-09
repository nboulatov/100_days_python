import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.color("coral")
timmy.width(4)
timmy.speed(10)
timmy.hideturtle()
turtle.colormode(255)
direction = [0,90,180,270]

def random_walk():
    for _ in range(100):
        timmy.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        timmy.forward(20)
        timmy.setheading(random.choice(direction))


random_walk()
screen = Screen()
screen.exitonclick()