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
timmy.speed(0)
timmy.shapesize(5, 5, 12)
timmy.color("coral")
turtle.colormode(255)
#timmy.hideturtle()

y_coordinate = -500

def go_to_location(y_coordinate):
    timmy.penup()
    timmy.goto(-600, y_coordinate)
    timmy.pendown()

# def rgb_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     timmy.color(r,g,b)

def draw_dots():
    for _ in range(10):
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)

while y_coordinate != 500:
    go_to_location(y_coordinate)
    draw_dots()
    y_coordinate +=100

screen = Screen()
screen.exitonclick()