from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(2, 2)
        self.setheading(90)
        self.reset_position()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)