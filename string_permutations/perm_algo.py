#!/usr/bin/python

import sys

def uniquesum(strparam):
	sum = 0

	for char in strparam:
		# Take the square of the ASCII value of each character in the string and add it to the sum
		sum += pow(ord(char), 2)

	return sum

if (len(sys.argv) < 3):
	raise ValueError("Bad arguments.")

if (uniquesum(sys.argv[1]) == uniquesum(sys.argv[2])):
	print(sys.argv[1] + " is a permutation of " + sys.argv[2])
else:
	print(sys.argv[1] + " is not a permutation of " + sys.argv[2])
