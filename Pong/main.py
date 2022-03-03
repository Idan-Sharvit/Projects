from screen_properties import screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT_POS = -370
RIGHT_POS = 370

left_paddle = Paddle(LEFT_POS)
right_paddle = Paddle(RIGHT_POS)
ball = Ball()
left_scoreboard = Scoreboard(-200, 250)
right_scoreboard = Scoreboard(200, 250)

screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with upper and lower wall.
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect collision with paddles.
    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    # Detect when paddle missed.
    if ball.xcor() > 380:
        ball.reset_position()
        left_scoreboard.update_score()

    if ball.xcor() < -380:
        ball.reset_position()
        right_scoreboard.update_score()


screen.exitonclick()