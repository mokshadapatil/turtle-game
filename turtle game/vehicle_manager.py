from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LEVEL_UP_INCREMENT = 10

class VehicleManager:
    def __init__(self):
        self.all_vehicles = []
        self.vehicle_speed = STARTING_MOVE_DISTANCE

    def create_vehicle(self):
        if random.randint(1, 6) == 1:
            new_vehicle = Turtle("square")
            new_vehicle.shapesize(stretch_wid=1, stretch_len=2)
            new_vehicle.penup()
            new_vehicle.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_vehicle.goto(300, random_y)
            self.all_vehicles.append(new_vehicle)

    def move_vehicles(self):
        for vehicle in self.all_vehicles:
            vehicle.backward(self.vehicle_speed)

    def increase_speed(self):
        self.vehicle_speed += MOVE_INCREMENT

    def reset(self):
        self.all_vehicles = []
        self.vehicle_speed = STARTING_MOVE_DISTANCE