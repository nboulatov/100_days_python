from turtle import Screen
from snake import Snake
from food import Food
import time

#how to make separate file with class screen?
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()


screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    food = Food()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()
