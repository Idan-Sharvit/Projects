from turtle import Turtle
from screen_properties import screen
import random

EDGE_OF_SCREEN = 280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        self.goto(x=random.randint(-EDGE_OF_SCREEN, EDGE_OF_SCREEN), y=random.randint(-EDGE_OF_SCREEN, EDGE_OF_SCREEN))

    def refresh(self):
        self.__init__()


