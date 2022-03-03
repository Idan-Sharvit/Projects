from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for turtle_num in range(len(self.segments) - 1, 0, -1):
            self.segments[turtle_num].goto(self.segments[turtle_num - 1].xcor(), self.segments[turtle_num - 1].ycor())

        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)
