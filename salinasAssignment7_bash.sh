#!/bin/bash
# Uses bash shell
echo Problem 1:
echo This is Assignment 7

var_name="Ryan"
class_1="Intro to Database Systems"
class_2="Cyber Defense II"
class_3="Intro to Scripting"
class_4="Technical and Professional Writing"
class_5="Digital Forensics"
echo
echo Problem 2:
echo $var_name
echo $class_1
echo $class_2
echo $class_3
echo $class_4
echo $class_5
echo
echo Problem 3:
echo My name is $1
echo Class 1: $2
echo Class 2: $3
echo Class 3: $4
echo Class 4: $5
echo Class 5: $6
echo
echo Problem 4:
echo Current process number: $$
echo All arguments passed: $*
echo
echo Problem 5:
grades=($(shuf -i 0-100 -n 1))
if [[ $grades -le 100 && $grades -ge 90 ]]
then
	echo Your grade of $grades is an A
elif [[ $grades -lt 90 && $grades -ge 80 ]]
then
	echo Your grade of $grades is a B
elif [[ $grades -lt 80 && $grades -ge 70 ]]
then
	echo Your grade of $grades is a C
elif [[ $grades -lt 70 && $grades -ge 60 ]]
then
	echo Your grade of $grades is a D
elif [[ $grades -lt 60 ]]
then
	echo Your grade of $grades is an F
else
	echo $grades is outside of bounds
fi
echo
echo Problem 6:
x=7
y=3
z=49
a=27
b=73
echo $z + $b = $((z+b))
echo $a - $y = $((a-y))
echo $x x $a = $((x*a))
echo $z / $x = $((z/x))
echo $b % $y = $((b%y))
echo $x ^ $y = $((x**y))
echo $((z++)) + 1 = $z
echo $((a--)) - 1 = $a
echo
echo Problem 7:
echo -n "Enter your basic salary with no commas or spaces: "
read salary
echo $salary
if [[ $salary -le 10000 ]]
then
	hra=$(echo "scale=2; $salary * 0.2" | bc)
	da=$(echo "scale=2; $salary * 0.8" | bc)
	echo HRA: $hra
	echo DA: $da
	echo -n "Gross Salary: "
	echo "scale=2; $salary + $hra + $da" | bc
elif [[ $salary -ge 10001 && $salary -le 20000 ]]
then	
	hra=$(echo "scale=2; $salary * 0.25" | bc)
	da=$(echo "scale=2; $salary * 0.9" | bc)	
	echo HRA: $hra
	echo DA: $da
	echo -n "Gross Salary: "
	echo "sclae=2; $salary + $hra + $da" | bc
elif [[ $salary -ge 20001 ]]
then
	hra=$(echo "scale=2; $salary * 0.3" | bc)
	da=$(echo "scale=2; $salary * 0.95" | bc)
	echo HRA: $hra
	echo DA: $da
	echo -n "Gross Salary: "
	echo "scale=2; $salary + $hra + $da" | bc
else
	echo Basic Salary is out of range
fi
