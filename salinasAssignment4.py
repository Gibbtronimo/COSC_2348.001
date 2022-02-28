'''
    Assignment 4
    Ryan Salinas
    COSC 2348.001
    2/22/22
'''
import random
# Problem 1: Employee Management System
#            - store employee objects in a dictionary

#Global variables for menu
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#Same employee class from A3 P2
class Employee():
    def __init__(self,NAME,ID,DEPT,TITLE):
        self.NAME = NAME
        self.ID = ID
        self.DEPT = DEPT
        self.TITLE = TITLE

    #returns a list for pandas table output
    def show_data(self):
        return [self.NAME,self.ID,
                self.DEPT,self.TITLE]
    
    #Setters for the change function
    def set_name(self,name):
        self.NAME = name

    def set_dept(self,dept):
        self.DEPT = dept

    def set_title(self,title):
        self.TITLE = title

    def createEmp(dict_name):
        emp_id = str(input("Enter employee ID: "))
        emp_name = str(input("Enter employee name: "))
        emp_dept = str(input("Enter employee department: "))
        emp_title = str(input("Enter employee job title: "))
        dict_name[emp_id] = Employee(emp_name,emp_id,emp_dept,emp_title)

# Menu function
def Menu():
    print("\nEmployee Management System:")
    print("-------------------------------------")
    print("1: Look up employee")
    print("2: Add new employee")
    print("3: Change attribute")
    print("4: Delete employee")
    print("5: Quit program")
    print()

    choice = int(input("Enter your choice: "))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))

    return choice

# Function to look up employees
def look_up(dictionary):
    id = input("Enter an ID: ")
    #print in pandas list function
    if dictionary:
        try:
            print(dictionary.get(id))
        except:
            print("This employee id is not registered\n")
    else:
        print("The dictionary is empty\n")

# Function to add a new employee
def add(dictionary):
    emp_name = input("Enter a name: ")
    emp_id = input("Enter an id: ")
    dept = input("Enter a department: ")
    title = input("Enter a title: ")

    if emp_id not in dictionary:
        dictionary[emp_id] = Employee(emp_name,emp_id,dept,title)
    else:
        print("That entry already exists!\n")

# Function to change an employee attribute
def change(dictionary):
    emp_id = input("Enter an id: ")
    try:
        print("1: name\n2: department\n3: job title")
        choice = input("Select an attribute to change: ")
        if choice == '1':
            name = input("New name: ")
            dictionary[emp_id].set_name(name)
        elif choice == '2':
            dept = input("New department: ")
            dictionary[emp_id].set_dept(dept)
        elif choice == '3':
            title = input("New title: ")
            dictionary[emp_id].set_title(title)
    except:
        print("That employee does not exist!\n")

# Function to delete an employee from the library
def delete(dictionary):
    emp_id = input("Enter an id: ")
    if emp_id in dictionary:
        del dictionary[emp_id]
    else:
        print("That employee does not exist!\n")

# Problem 2: Number Analysis List
#            - takes list of 20 numbers and performs calculations on the list
def numAnalysis(numList):
    print("Enter 20 numbers into a list one by one")
    for i in range(0,20):
        num = float(input("Enter a number: "))
        numList.append(num)

    lowest = numList[0]
    highest = numList[0]
    total = 0
    for i in range(0,20):
        if numList[i] < lowest:
            lowest = numList[i]
        elif numList[i] > highest:
            highest = numList[i]
        total += numList[i]
    print("\nLowest number in the list: ",lowest)
    print("Highest number in the list: ",highest)
    print("Total of numbers in the list: ",total)
    print("Average of the list: ",(total/len(numList)))

# Problem 3: Square number dictionary
#            - program to create a dictionary and print the contents
def dictScript():
    n = int(input("Enter a number n: "))
    numDict = dict()
    num = random.randint(1,n)
    numDict[num] = num*num
    print(numDict)

if __name__ == "__main__":
    print("\nProblem 1:")
    employees = dict()

    menu_choice = 0

    while menu_choice != QUIT:
        menu_choice = Menu()

        if menu_choice == LOOK_UP:
            look_up(employees)
        elif menu_choice == ADD:
            add(employees)
        elif menu_choice == CHANGE:
            change(employees)
        elif menu_choice == DELETE:
            delete(employees)

    print("\nProblem 2:\n")
    numberList = []

    numAnalysis(numberList)

    print("\nProblem 3:\n")
    dictScript()
    
