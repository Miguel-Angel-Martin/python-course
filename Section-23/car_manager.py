from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager (Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        radom_chance= random.randint(1,6)
        if radom_chance == 1:
            new_car = Turtle()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.speed(0)
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -300:
                car.goto(300, random.randint(-250, 250))
    def level_up(self):
        self.car_speed += MOVE_INCREMENT