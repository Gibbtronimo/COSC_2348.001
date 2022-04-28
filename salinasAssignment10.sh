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
i=0

while read line; do
	a[i]=$line
	let i+=1
done < $sum1

echo array: ${a[@]}
sum=0

function recursive_sum () {
	index=$1
	sum=$2

	if [ ${#a[@]} -lt 1 ]; then
		return 0
	else
		temp1=${a[$index]}
		let sum=sum+temp1
		unset a[index]
		let temp2=index+1
		recursive_sum $temp2 $sum
	fi

}

recursive_sum 0 $sum
totalSum=$?
echo The final sum: 
echo "$sum"

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
