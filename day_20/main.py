from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

#how to make separate file with class screen?
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_snake()
        score.increase_score()

    if snake.head.xcor()>280 \
        or snake.head.xcor()<-280 \
        or snake.head.ycor()>280 \
        or snake.head.ycor()<-280:
        score.reset()
        snake.reset()

    for _ in snake.segments[1:]:
        if snake.head.distance(_) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()