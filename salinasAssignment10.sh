#!/bin/bash
<<com
	Assignment 10
	COSC 2348
	Ryan Salinas
	4/24/22
com

#Problem 1
echo Problem 1:
#sum1="A10nums.txt"
#declare -a num_array
#while read line; do
#	echo $line
#	num_array+=($line)
#done < $sum1
#echo ${num_array[@]}
#
#function recursive_add () {
#	local file=$1
#	local n=$2
#	global sum=$((file[n]))
#	if (( n == 0 )); then
#		echo $n
#		return
#	fi
#	$FUNCNAME $file $((n-1)) $((sum+n))
#}
#
#recursive_add $sum1 5

#Problem 2
echo -e "\nProblem 2:\n"

function fibonacci () {
	n=$1
	if [ $n -le 1 ]; then
		return $n
	else
		return $(( fibonacci ( n - 1 ) + fibonacci ( n - 2 ) ))
	fi
}

read -p "Enter a number >= 2: " num
fibonacci $num
