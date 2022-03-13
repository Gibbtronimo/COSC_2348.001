'''
    Assignment 6
    Ryan Salinas
    COSC 2348.001
    3/6/22
'''
import re

#Function to read in files for Problem 2
#Had to define it up here so it wouldn't be categorized as member function of Student()
def readFiles(p1,p2,p3):
    try:
        f1 = open(p1,'r')
        f2 = open(p2,'r')
        f3 = open(p3,'r')
        print("Files opened successfully")
    except FileNotFoundError:
        print("File path of one or more inputs is not valid")

    f1.close()
    f2.close()
    f3.close()


#-------------------------------------------------------------------------------------------------
# Problem 1: Students.txt
#            - read in students.txt and A3 to create new students file
#-------------------------------------------------------------------------------------------------
#Create Student class for problem 1
class Student():
    def __init__(self,fname,lname,email,courses):
        firstname = fname
        lastname = lname
        email = email
        all_courses = courses

def addStudent(stuObject, stuList):
    #Skip first line of the 
    next(stuObject)
    for line in stuObject:
        split = re.split('\s',line)
        try:
            f = split[0]
            l = split[1]
            e = split[2]
            c = []
            c_split = re.split(',',split[3])
            for n in c_split:
                c.append(n)
            stuList.append(Student(f,l,e,c))
            print(f,'added to list')
        except IndexError:
            continue



if __name__ == "__main__":
    print("Problem 1:\n")
    #Read in students text file
    students = open('students.txt','r')
    #List of student objects
    stuClass = []

    addStudent(students,stuClass)
    for stu in stuClass:
        print(stu)

    students.close()

    print("Problem 2:\n")
    readFiles('f1.txt','f2.txt','f3.txt')
