import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
users_bet = screen.textinput(title="Place your bets!", prompt="Which color do you think will win?")
colors = ["red","orange","yellow","green","blue","purple"]

contestants = []

def position():
    y_coordinate = -90
    for _ in range(6):
        new_turtle = Turtle("turtle")
        new_turtle.shapesize(2, 2, 2)
        new_turtle.color(colors[_])
        contestants.append(new_turtle)
        new_turtle.penup()
        new_turtle.goto(x=-240,y=y_coordinate)
        y_coordinate +=30

position()

racing = True
while racing:
    for _ in range(6):
        if contestants[_].xcor() >230:
            winner = contestants[_].pencolor()
            racing = False
            if winner == users_bet:
                print(f"You've won! {winner} has won the race!")
            else:
                print(f"You've lost! {winner} has won the race!")
        contestants[_].forward(random.randint(0,10))



screen.exitonclick()