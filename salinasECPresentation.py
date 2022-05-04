'''
    List, Set, Tuple, Dictionary
    Ryan Salinas
    5/2/22
'''

#List usage with class objects
studentList = []

class Students():
    def __init__(self, name, grades):
        self.__name = name
        self.__grades = grades

    def get_name(self): return self.__name
    #used for dictionary method

    def get_grades(self): return self.__grades
    #used for dictionary method
    
    def get_obj(self):  #used for list method
        return self.__name, self.__grades

    def add_dict(self,dict1):
        dict1[self.get_name()] = self.get_grades()
    

stu1 = Students("Ryan",[66,84,92,86])
print("Name: \t\t",stu1.get_name())
print("Grades: \t",stu1.get_grades())
print("Student 1: \t",stu1.get_obj())
print("Add Student 1 to studentList...")
studentList.append( stu1.get_obj() )
print("Student List: ",studentList)
#
#stu2 = Students("David",[90,82,94,97])
#print("Add Student 2 to studentList...")
#studentList.append( stu2.get_obj() )
#print("Student List: ",studentList)
#print("Remove last student added...")
#studentList.pop()
#print("Student List: ",studentList)
#
#Dictionary usage
stuDict = {}
# add individual values
stuDict["Trevor"] = [99,99,99,99]
print("\nStudent Dictionary: ",stuDict)
# or add object
stu1.add_dict(stuDict)
print("Student Dictionary: ",stuDict)
del stuDict["Trevor"]
print("Student Dictionary: ",stuDict)

#normal dictionary method
method_dict = dict({1:"Class",2:"on",3:"dictionary"})
#dictionary method with list
list_dict = dict([(1,"Class"),(2,"list"),(3,"into"),(4,"dictionary")])
