#!/bin/bash

#Problem 1
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
for num in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
	echo -n $num" "
done	
