import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

LEVEL_POS = (-280, 260)
FAILED_POS = (0, 0)

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

turtle = Player()
level_scoreboard = Scoreboard(LEVEL_POS)
level_scoreboard.write_level()
cars = CarManager()

screen.listen()
screen.onkey(turtle.move, 'Up')

counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if counter % 6 == 0:
        cars.add_car()
    cars.drive()

    # Detect collision with car.
    for car in cars.car_list:
        x_plus = car.xcor() + 5
        x_minus = car.xcor() - 5
        if turtle.distance(x_plus, car.ycor()) < 20 or turtle.distance(x_minus, car.ycor()) < 20:
            game_is_on = False
            failed_scoreboard = Scoreboard(FAILED_POS)
            level_scoreboard.clear()
            failed_scoreboard.failed()

    # Detect successful road-crossing.
    if turtle.finished():
        level_scoreboard.update_level()
        turtle.restart_pos()
        cars.accelerate()


screen.exitonclick()