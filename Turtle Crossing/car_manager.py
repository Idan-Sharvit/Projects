from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_AMOUNT_OF_CARS = 70
DISTANCE_BETWEEN_CARS = 50


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.x = 0
        self.car_list = []

    def add_car(self):
        new_car = Turtle(shape='square')
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.penup()
        random_y = random.randint(-250, 250)
        new_car.setposition(300+self.x, random_y)
        self.x += DISTANCE_BETWEEN_CARS
        self.car_list.append(new_car)

    def drive(self):
        for car in self.car_list:
            car.forward(self.speed)

    def accelerate(self):
        self.speed += MOVE_INCREMENT
        for car in self.car_list:
            car.forward(self.speed)

    def check_pos(self):
        for car in self.car_list:
            if car.xcor() < -300:
                self.car_list.remove(car)
