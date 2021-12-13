from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1080, height=608)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(n=0)

paddle_1 = Paddle(player_number=1)
paddle_2 = Paddle(player_number=2)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=paddle_1.up, key="Up")
screen.onkeypress(fun=paddle_1.down, key="Down")
# screen.onkeypress(fun=paddle_2.up, key="Up")
# screen.onkeypress(fun=paddle_2.down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05 * 0.5 ** ball.collision_count)

    ball.move()
    # paddle_2.smart_move(ball.ball)
    paddle_2.auto_move()

    if ball.is_ball_out():
        scoreboard.increment_score(ball.is_ball_out())
        scoreboard.write_score()
        if scoreboard.scores[0] == 10 or scoreboard.scores[1] == 10:
            game_is_on = False
        ball.shoot()
    elif ball.is_collide(paddle_1.paddle_body) or ball.is_collide(paddle_2.paddle_body) or ball.hit_wall():
        ball.reflect()

screen.exitonclick()
