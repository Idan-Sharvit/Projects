from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setposition(position)
        self.hideturtle()
        self.level = 0

    def write_level(self):
        self.write(f'Level: {self.level}', font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', font=FONT)

    def failed(self):
        self.clear()
        self.write(f'You lost!\nYour score is: {self.level}', align='center', font=FONT)
