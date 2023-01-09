from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shapesize(5, 5, 12)
timmy.color("coral")

def draw_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)

# def draw_dotted_line():
#     for _ in range(10):
#         timmy.forward(10)
#         timmy.penup()
#         timmy.forward(10)
#         timmy.pendown()

# def draw_triangle():
#     for _ in range(3):
#         timmy.forward(100)
#         timmy.right(120)
#
# def draw_pentagon():
#     for _ in range(5):
#         timmy.forward(100)
#         timmy.right(72)
#
# draw_square()
# timmy.pencolor("orange")
# draw_triangle()
# timmy.pencolor("blue")
# draw_pentagon()

def draw_shapes(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)

timmy.colormode(255)

for _ in range(3,11):
    draw_shapes(_)
    #color = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
    timmy.pencolor(41,41,253)

screen = Screen()
screen.exitonclick()