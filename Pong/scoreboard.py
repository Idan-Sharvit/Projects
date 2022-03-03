from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.score = 0
        self.goto(x_cor, y_cor)
        self.hideturtle()
        self.color('white')
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'bold'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'bold'))