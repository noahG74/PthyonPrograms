"""
Author: Noah Gonzales
Date: 2/10/2022
"""

#Question 1

class Car():
    def __init__(self, yearModel, make, speed):
		self.yearModel = yearModel
		self.make = make
        self.speed = 0
    def accelerate (speed):
        speed += 5
    def break (speed):
        speed -= 5
    def get_Speed (speed):
        return speed


if name == '__main__':
    car = car(2021, "Chevy Colorado")
    for temp in range(0,5):
        car.accelerate()
        car.get_speed()
    for temp in range(0,5):
        car.break()
        car.get_speed()
