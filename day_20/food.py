from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        food = Turtle()
        food.hideturtle()
        food.goto(random.randint(-580, 580), random.randint(-580, 580))
        food.dot(20, "white")
        food.penup()

