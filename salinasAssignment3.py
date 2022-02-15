'''
    Assignment 3
    Ryan Salinas
    COSC 2348.001
    2/15/22
'''

print("Problem 1:")
# Problem 1: Car Class
#            - create a car class with attributes and functions
class Car():
    def __init__(self, year, make):
        self._year_model = year
        self._make = make
        self._speed = 0

    def accelerate(self):
        self._speed += 5

    def brake(self):
        self._speed -= 5

    def get_speed(self):
        return self._speed

myTruck = Car("Ford", "2018 F150")
for i in range(5):
    myTruck.accelerate()
    print(myTruck.get_speed())
for i in range(5):
    myTruck.brake()
    print(myTruck.get_speed())


