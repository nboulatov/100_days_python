import random
import turtle
from turtle import Turtle, Screen
import colorgram

# colors = colorgram.extract('image.jpg', 10)
# collection = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     collection.append(new_color)

color_list = [(251, 251, 251), (229, 223, 225), (210, 2, 35), (198, 181, 3), (223, 1, 1), (231, 248, 242), (250, 215, 0), (243, 246, 249), (224, 157, 74), (201, 87, 19)]


timmy = Turtle()
timmy.width(4)
#timmy.speed(10)
timmy.shapesize(5, 5, 12)
timmy.color("coral")
# timmy.hideturtle()
timmy.penup()
timmy.goto(-600, -500)
timmy.pendown()
turtle.colormode(255)

def draw_dots():

    for _ in range(5):
        timmy.dot(20, turtle.pencolor())
        timmy.penup()
        timmy.forward(50)

draw_dots()
screen = Screen()
screen.exitonclick()