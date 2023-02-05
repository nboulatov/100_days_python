import time
from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import Cars

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
cars = Cars()

screen.listen()
screen.onkey(player.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.creat_cars()
    cars.move()
    if player.ycor()==260:
        score.increase_level()
        cars.increase_speed()
        player.reset_position()
    for car in cars.all_cars:
        if car.distance(player)<20:
            score.end_game()
            game_is_on = False

screen.exitonclick()