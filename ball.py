from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.ball_list = []
        self.direction = True
        self.create_ball()
        self.ball = self.ball_list[0]
        self.shoot()
        self.collision_count = 0
        # self.ball.setheading(0)
        # self.ball.goto(0,0)

    def create_ball(self):
        new_ball = Turtle("square")
        new_ball.color("white")
        new_ball.penup()
        self.ball_list.append(new_ball)

    def shoot(self):
        is_flat = True
        while is_flat:
            if self.direction:
                self.ball.setheading(random.randint(-45, 45))
            else:
                self.ball.setheading(random.randint(135, 225))
            if self.ball.heading() != 0 and self.ball.heading() != 180:
                is_flat = False
        self.ball.goto(x=0, y=random.randint(-284, 284))

        self.collision_count = 0
        heading = self.ball.heading()
        self.ball.tiltangle(-heading)
        self.direction = not self.direction

    def move(self):
        self.ball.forward(20)

    def is_collide(self, paddle):
        for segment in paddle:
            if self.ball.distance(segment) <= 20:
                self.collision_count += 1
                return True
        return False

    def hit_wall(self):
        return self.ball.ycor() > 294 or self.ball.ycor() < -294

    def reflect(self):
        if self.hit_wall():
            new_heading = 360 - self.ball.heading()
        else:
            new_heading = 180 - self.ball.heading()

        while new_heading >= 360:
            new_heading -= 360
        while new_heading < 0:
            new_heading += 360

        self.ball.setheading(new_heading)
        self.ball.tiltangle(-new_heading)

    def is_ball_out(self):
        if self.ball.xcor() > 540:
            return 1
        elif self.ball.xcor() < -540:
            return 2
        else:
            return False
