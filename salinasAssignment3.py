'''
    Assignment 3
    Ryan Salinas
    COSC 2348.001
    2/15/22
'''
# import pandas library to format output of Problem 2/3
import pandas as pd
# import random for student class
import random

print("Problem 1:\n")
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

print("\nProblem 2+3:\n")
# Problem 2&3: Employee Class
#            - create an employee class with attributes and functions
#            - 3 employees will be created with database naming conventions
class Employee():
    def __init__(self, F_NAME, L_NAME, ID, DEPT, J_TITLE):
        self._F_NAME = F_NAME
        self._L_NAME = L_NAME
        self._ID = ID
        self._DEPT = DEPT
        self._J_TITLE = J_TITLE
# Problem 3: add full name and email attributes
        self._FULLNAME = self._F_NAME + " " + self._L_NAME
        self._EMAIL = self._F_NAME.lower() + "." + self._L_NAME.lower() + "@company.com"
        



    def show_data(self):
        return [self._F_NAME,
                self._L_NAME,
                self._ID,
                self._DEPT,
                self._J_TITLE,
                self._FULLNAME,
                self._EMAIL]

# input employee data
smeyers = Employee("Susan","Meyers",47899,"Accounting","Vice President")
mjones = Employee("Mark","Jones",39119,"IT","Programmer")
jrogers = Employee("Joy","Rogers",81774,"Manufacturing","Engineer")
#format employee data for table output
data = [smeyers.show_data(),mjones.show_data(),jrogers.show_data()]
table = pd.DataFrame(data, columns = ["Name","","ID Number","Department",
                                      "Job Title","Full Name","Email"])
print(table)

print("\nProblem 4:\n")
# Problem 4: Student Database
#            - a program to sort students based on total grade and average grade

class Student():
    def __init__(self,intlist):
        self._C1 = intlist[0]
        self._C2 = intlist[1]
        self._C3 = intlist[2]
        self._C4 = intlist[3]
        self._C5 = intlist[4]
        self._C6 = intlist[5]

    def get_percentage(self):
        sum = (self._C1 + self._C2 + self._C3 +
               self._C4 + self._C5 + self._C6)
        percent = "{:.2f}".format(sum/600)
        return percent

# random number generator
randlist = random.sample(range(70,100),6)
print(randlist)
for i in range(25):
    randlist = random.sample(range(70,100),6)
    print(("student%d: ",randlist).format(i))
    student{i} = Student(randlist)

