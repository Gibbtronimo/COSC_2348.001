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
for num in $(seq 1 20); do
	num_array+=($RANDOM)
done

echo "Array in original order"
echo ${num_array[*]}

# Performing Bubble sort
for ((i = 0; i<20; i++)); do
    for((j = 0; j<20-i-1; j++)); do
        if [ ${num_array[j]} -gt ${num_array[$((j+1))]} ]; then
            # swap
            temp=${num_array[j]}
            num_array[$j]=${num_array[$((j+1))]}
            num_array[$((j+1))]=$temp
        fi
    done
done

echo "Array in sorted order: least to greatest"
echo ${num_array[*]}

#Problem 2
echo -e "\nProblem 2:\n"
declare -a arr2
for num in $(seq 1 20); do
	arr2+=($RANDOM)
done

echo "Array in original order"
echo ${arr2[*]}

# Performing Bubble sort
for ((i = 0; i<20; i++)); do
    for((j = 0; j<20-i-1; j++)); do
        if [ ${arr2[j]} -lt ${arr2[$((j+1))]} ]; then
            # swap
            temp=${arr2[j]}
            arr2[$j]=${arr2[$((j+1))]}
            arr2[$((j+1))]=$temp
        fi
    done
done

echo "Array in sorted order: greatest to least"
echo ${arr2[*]}

#Problem 3
echo -e "\nProblem 3:\n"
declare -a arr3
for num in $(seq 1 50); do
	arr3+=($num)
done
echo ${arr3[*]}

#Problem 4
# defining the function to find prime numbers in an array
#function find_primes {
#	i=2
#	f=0
#	if [ $# -eq 1 ]; then
#		local -n list=$1
#		for num in ${list[*]}; do
#			if test $num -eq 1 || test $num -eq 2; then
#				break
#
#			fi
#
#			while test $i -le 'expr $num / 2'; do
#				if test 'expr $num % $i' -eq 0; then
#					$f=1
#				fi
#				$i='expr $i + 1'
#			done
#			if test $f -eq 1; then
#				continue
#			else
#				echo -n $num" "
#			fi
#		done
#	else
#		echo This function only takes one argument - an array of numbers
#	fi
#
#}
# calling the function and passing arr3 as an argument
#echo
#find_primes arr3

#Problem 5
echo -e "\nProblem 5:\n"
declare -a even_arr
declare -a odd_arr
even_sum=0
odd_sum=0
for num in $(seq 1 50); do
	if test $((num%2)) -eq 0; then
		even_arr+=($num)
		even_sum=$((even_sum + num))
	else
		odd_arr+=($num)
		odd_sum=$((odd_sum + num))
	fi
done
echo Even array:
echo ${even_arr[*]}
echo Even sum: $even_sum
echo Odd array:
echo ${odd_arr[*]}
echo Odd sum: $odd_sum
