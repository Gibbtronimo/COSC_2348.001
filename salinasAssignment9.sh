#!/bin/bash
<<com
	Assignment 9
	Ryan Salinas
	COSC 2348.001
	4/14/22
com

#Problem 1
echo -e "Problem 1:\n"
declare -a num_array
for num in $(seq 1 20)
do
	num_array+=($RANDOM)
done

echo "Array in original order"
echo ${num_array[*]}

# Performing Bubble sort
for ((i = 0; i<20; i++))
do

    for((j = 0; j<20-i-1; j++))
    do

        if [ ${num_array[j]} -gt ${num_array[$((j+1))]} ]
        then
            # swap
            temp=${num_array[j]}
            num_array[$j]=${num_array[$((j+1))]}
            num_array[$((j+1))]=$temp
        fi
    done
done

echo "Array in sorted order"
echo ${num_array[*]}
