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
