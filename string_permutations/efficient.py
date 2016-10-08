#!/usr/bin/python

import sys

args = sys.argv

def uniquesum(strparam):
	sum = 0

	for char in strparam:
		# Take the square of the ASCII value of each character in the string and add it to the sum
		sum += pow(ord(char), 2)

	return sum

if (len(args) < 3):
	raise ValueError("Bad arguments.")

if (uniquesum(args[1]) == uniquesum(args[2])):
	print(args[1] + " is a permutation of " + args[2])
else:
	print(args[1] + " is not a permutation of " + args[2])
