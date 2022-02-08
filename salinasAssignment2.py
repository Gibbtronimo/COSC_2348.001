'''
    Assignment 2
    Ryan Salinas
    COSC 2348.001
    2/8/22
'''

print("Problem 1:")
# Problem 1: Pattern Printing
#            - print out a series of asterisks using a loop
# part i
num = 6
for a in range(num):
    print(a*"*")
# part ii
for b in reversed(range(num)):
    print(b*" " + (num-b)*"*")

