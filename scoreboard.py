from turtle import Turtle
FONT = ("Helvetica", 30, "bold")
SCOREBOARD_POSITIONS = [(-50, 250), (50, 250), (0, 250)]


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.color("white")
        self.scores = [0, 0]
        self.write_score()
        self.mid_line = Turtle("square")
        self.draw_mid_line()

    def draw_mid_line(self):
        self.mid_line.hideturtle()
        self.mid_line.color("white")
        self.mid_line.penup()
        self.mid_line.setheading(-90)
        self.mid_line.goto(0, 200)
        self.mid_line.shapesize(stretch_len=1.5, stretch_wid=0.5)
        while self.mid_line.ycor() > -290:
            self.mid_line.stamp()
            self.mid_line.forward(60)

    def write_score(self):
        self.scoreboard.clear()
        self.scoreboard.goto(SCOREBOARD_POSITIONS[2])
        self.scoreboard.write(arg="|", align="center", font=FONT)
        for index in range(2):
            self.scoreboard.goto(SCOREBOARD_POSITIONS[index])
            self.scoreboard.write(arg=self.scores[index], align="center", font=FONT)

    def increment_score(self, player_number):
        self.scores[player_number - 1] += 1
