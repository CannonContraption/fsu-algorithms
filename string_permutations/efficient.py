#!/usr/bin/python

import sys

args = sys.argv

def uniquesum(strparam):
	sum = 0

	for char in strparam:
		# Take the square of the ASCII value of each character in the string and add it to the sum
		sum += ord(char)**3

	return sum

if (len(args) < 3):
	sys.stderr.write("Invalid Arguments. Enter two strings to compare, no spaces.\n");
	exit(1);

if (len(args[1]) != len(args[2])):
	sys.stderr.write("These strings are not the same length and therefore cannot be permutations.\n");
	exit(2);

if (uniquesum(args[1]) == uniquesum(args[2])):
	print(args[1] + " is a permutation of " + args[2])
else:
	print(args[1] + " is not a permutation of " + args[2])
