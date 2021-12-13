from turtle import Turtle
STARTING_POSITIONS_1 = [(-520, 40), (-520, 20), (-520, 0), (-520, -20), (-520, -40)]
STARTING_POSITIONS_2 = [(520, 40), (520, 20), (520, 0), (520, -20), (520, -40)]
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, player_number):
        super().__init__()
        self.hideturtle()
        self.paddle_body = []
        if player_number == 1:
            self.create_paddle(STARTING_POSITIONS_1)
        elif player_number == 2:
            self.create_paddle(STARTING_POSITIONS_2)
            self.is_going_up = True

    def create_paddle(self, starting_positions):
        for position in starting_positions:
            new_paddle = Turtle("square")
            new_paddle.color("white")
            new_paddle.penup()
            new_paddle.goto(position)
            self.paddle_body.append(new_paddle)

    def up(self):
        if self.paddle_body[0].ycor() < 294:
            for component in self.paddle_body:
                component.setheading(UP)
                component.forward(20)

    def down(self):
        if self.paddle_body[-1].ycor() > -294:
            for component in self.paddle_body:
                component.setheading(DOWN)
                component.forward(20)

    def auto_move(self):
        if self.paddle_body[0].ycor() >= 294:
            self.is_going_up = False
        if self.paddle_body[-1].ycor() < -294:
            self.is_going_up = True
        if self.is_going_up:
            self.up()
        else:
            self.down()

    def smart_move(self, target):
        midpoint_index = int(len(self.paddle_body)/2)
        if target.ycor() > self.paddle_body[midpoint_index].ycor():
            self.is_going_up = True
        else:
            self.is_going_up = False
