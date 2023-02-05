from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-150,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level {self.level}", align="center",font= ("Arial",24,"normal"))

    def increase_level(self):
        self.level+=1
        self.clear()
        self.update_scoreboard()

    def end_game(self):
        self.clear()
        self.home()
        self.write(f"GAME OVER \n Highest Level reached {self.level}", align="center", font=("Arial", 24, "normal"))