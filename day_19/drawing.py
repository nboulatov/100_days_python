from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(100)

def turn_left():
    heading = timmy.heading() + 20
    timmy.setheading(heading)

def turn_right():
    heading = timmy.heading() - 20
    timmy.setheading(heading)

def move_backward():
    timmy.backward(100)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.goto(0,0)
    timmy.pendown()

screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='a',fun=turn_left)
screen.onkey(key='d',fun=turn_right)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='c',fun=clear)

screen.exitonclick()