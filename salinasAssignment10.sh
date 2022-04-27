#!/bin/bash
<<com
	Assignment 10
	COSC 2348
	Ryan Salinas
	4/24/22
com

#Problem 1
echo Problem 1:
sum1="A10nums.txt"
declare -a num_array
while read line; do
	echo $line
	num_array+=($line)
done < $sum1
echo ${num_array[@]}

function recursive_add () {
	local file=$1
	local n=$2
	global sum=$((file[n]))
	if (( n == 0 )); then
		echo $n
		return
	fi
	$FUNCNAME $file $((n-1)) $((sum+n))
}

recursive_add $sum1 5
