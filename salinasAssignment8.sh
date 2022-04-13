#!/bin/bash
<<com
	Assignment 8
	Ryan Salinas
	COSC 2348.001
	4/7/22
com
#Problem 1
echo Problem 1:
x=1
# Using while loop
while [ $x -le 15 ]
do
	echo -n $((x++))" "
done
echo
x=0
# Using until loop
until [ $x -eq 15 ]
do
	echo -n $((++x))" "
done
echo
# Using for loop
for num in $( seq 15)
do
	echo -n $num" "
done

#Problem 2
echo -e '\n\nProblem 2:'
sum=0
first=20
# Using while loop
while [ $first -le 40 ]
do	
	sum=$(expr $sum + $first)
	((first=first+1))
done
echo Sum: $sum
sum=0
first=20
# Using until loop
until [ $first -eq 41 ]
do
	sum=$(expr $sum + $first)
	((first=first+1))
done
echo Sum: $sum
sum=0
# Using for loop
for first in $( seq 20 40)
do
       sum=$(expr $sum + $first)
       ((first=first+1))
done
echo Sum: $sum

#Problem 4
echo -e "\nProblem 4:"
echo -n "Enter a city: "
read input
city=${input,,}
case "$city" in
	#case 1
	"corpus") echo "Texas A&M University Corpus Christi"
	;;
	#case 2
	"kingsville") echo "Texas A&M University Kingsville"
	;;
	#case 3
	"commerce") echo "Texas A&M University Commerce"
	;;
*) echo "Texas A&M University"
esac
