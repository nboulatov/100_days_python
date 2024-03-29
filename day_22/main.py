import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle) <50 and ball.xcor()>320 \
            or ball.distance(l_paddle) <50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_position()
        score.increase_score_left()
    elif ball.xcor()<-380:
        ball.reset_position()
        score.increase_score_right()
    if score.score_left == 1 or score.score_right ==1:
        score.end_game()
        game_is_on = False

screen.exitonclick()