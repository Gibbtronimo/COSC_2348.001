"""
	Assignment 1
	Ryan Salinas
	COSC 2348.001
	1/27/22
"""

print("Problem 1:\n")
# Problem 1: Personal Information
#	    - print out personal information to console
print("Name:    Ryan Salinas")
print("Address: 1109 Nancy Dr, Corpus Christi")
print("         Texas, 78412")

print("\nProblem 2:\n")
# Problem 2: Land Calculation
#	    - calculates acres from square feet
sqFeet = float(input("Enter the sqare footage to convert to acres: "))
acres = float(sqFeet/43560)
print("You have approximately {:.2f} acres." .format(acres))

print("\nProblem 3:\n")
# Problem 3: Car Distance
#	     - calculates distance traveled at certain speed and time
carSpeed = 70
print("The car will travel {:d} miles in 6 hours" .format(carSpeed*6))
print("The car will travel {:d} miles in 10 hours" .format(carSpeed*10))
print("The car will travel {:d} miles in 15 hours" .format(carSpeed*15))

print("\nProblem 4:\n")
# Problem 4: Age Classifier
#	     - classifies a person by age
personAge = int(input("Enter your age: "))
if personAge >= 0 and personAge <= 1:
	print("You are an infant")
elif personAge > 1 and personAge < 13:
	print("You are a child")
elif personAge >= 13 and personAge < 20:
	print("You are a teenager")
else:
	print("You are an adult")

print("\nProblem 5:\n")
# Problem 5: Change Counting Game
#	     - User enters amount of coins, returns if it adds up to a dollar or not
quarters = int(input("Enter the amount of quarters: "))
dimes = int(input("Enter the amount of dimes: "))
nickels = int(input("Enter the amount of nickels: "))
pennies = int(input("Enter the amount of pennies: "))
totalVal = (quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01)

if totalVal == 1.0:
	print("Congratulations! You won the game!")
elif totalVal < 1.0:
	print("Your total came out to less than a dollar at {:.2f}" .format(totalVal))
else:
	print("Your total came out to more than a dollar at {:.2f}" .format(totalVal))

print("\nProblem 6:\n")
# Problem 6: February Leap Year
#	     - user enters a year and the program will return how many days of February are in the year
#	     - The program will also say if it is a leap year or not
year = int(input("Enter a year: "))
if year % 100 == 0:
	if year % 400 == 0:
		print("Leap year")
	else:
		print("Not leap year")
else:
	if year % 4 == 0:
		print("Leap year")
	else:
		print("Not leap year")
