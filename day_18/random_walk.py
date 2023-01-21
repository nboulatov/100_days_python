from turtle import Turtle, Screen
import random

timmy = Turtle()
#timmy.shapesize(5, 5, 12)
timmy.color("coral")
timmy.width(4)
timmy.speed(10)
timmy.hideturtle()

colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen"]
direction = ["right","left"]

def random_walk():
    for _ in range(100):
        timmy.color(random.choice(colors))
        timmy.forward(20)
        which_way = random.choice(direction)
        if which_way == 'right':
            timmy.right(90)
        else:
            timmy.left(90)

random_walk()
screen = Screen()
screen.exitonclick()