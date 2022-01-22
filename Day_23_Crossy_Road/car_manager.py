from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
START_X = 270
START_Y_MIN = -250
START_Y_MAX = 250


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.spawn_rate = 6
        self.move_distance = 5



    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        start_y = random.randint(START_Y_MIN, START_Y_MAX)
        new_car.goto(START_X, start_y)
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def next_level(self):
        #self.spawn_rate -= 1
        self.move_distance += 5

