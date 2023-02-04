from turtle import Turtle
SCORE_POSITION = [(-40,0),(40,0)]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100,0)
        self.write(self.score_left,align="center",font=("Ariel",80,"normal"))
        self.goto(100,0)
        self.write(self.score_right,align="center",font=("Ariel",80,"normal"))

    def increase_score_left(self):
        self.score_left+=1
        self.clear()
        self.update_scoreboard()

    def increase_score_right(self):
        self.score_right+=1
        self.clear()
        self.update_scoreboard()

    def end_game(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Game over. {self.score_left} - {self.score_right}", False, align="center", font=("Ariel",40,"normal"))