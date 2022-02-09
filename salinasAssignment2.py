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
    printNum = n
    for i in range(1,n):
        printNum = printNum * i
    return printNum
# part ii
print(fact(int1)/(fact(int2)*fact(int1-int2)))
# part iii
print(fact(int1)/fact(int1-int2))

print("\nProblem 3:\n")
# Problem 3: Sort List with loop
#            - a list is given, which needs to be sorted
numList = [20, 68, 41, 88, 16, 40, 65, 97, 85]

# This sort function will require multiple helper functions
# helper function: minLoc (minimum location)
def minLoc(list, n1, n2):
    minIndex = n1
    for loc in range(n1+1, len(list)):
        if list[loc] < list[minIndex]:
            minIndex = loc
    return minIndex

# helper function: swap
def swap(list, n1, n2):
    temp = list[n1]
    list[n1] = list[n2]
    list[n2] = temp

# main function: sort - uses the selection sort methodology
def sort(list):
    minIndex = 0
    for loc in range(len(list)-1):
        minIndex = minLoc(list, loc, len(list) - 1)
        swap(list, loc, minIndex)

# print the old list
print("Old list: ",numList)
# sort the list
sort(numList)
#print new list
print("New List: ",numList)


print ("\nProblem 4:\n")
# Problem 4: Even and Odd list from preexisting list
#            - sort the list into odd and even numbers, then
#            - put those sorted numbers into separate lists
# numList from problem 3 will be used here
# create the odd and even lists
oddNums = []
evenNums = []
# loop to sort the list
for i in range(len(numList)):
    if numList[i] % 2 == 0:
        evenNums.append(numList[i])
    else:
        oddNums.append(numList[i])

print("Even list: ",evenNums)
print("Odd list: ",oddNums)

print("\nProblem 5:\n")
# Problem 5: Find prime numbers
#            - print prime numbers between 2 and 50 inclusively
for i in range(2,51):
    for j in range(2,51):
        if i % j == 0:
            break
        print(i)
        break
# cant get it to print 2 for some reason


