from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Courier'
FONT_SIZE = 24
FONT_TYPE = 'bold'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def increase_score(self):
        self.score += 1
        self.score_update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.score_update()

