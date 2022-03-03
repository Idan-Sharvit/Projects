from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.setx(x_position)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed('fastest')
        self.score = 0

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
