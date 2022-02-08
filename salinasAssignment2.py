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

print("\nProblem 2:\n")
# Problem 2: Factorial inputs
#            - take two integer inputs and print two
#              different calculations
# part i
int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))
# creating a factorial function to call on repeatedly
def fact(n):
    if (n==0):
        return 1
    else:
        return n*fact(n-1)
# part ii
print(fact(int1)/(fact(int2)*fact(int1-int2)))
# part iii
print(fact(int1)/fact(int1-int2))

