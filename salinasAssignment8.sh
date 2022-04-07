#!/bin/bash

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
echo
#Problem 2
echo
echo Problem 2:
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
