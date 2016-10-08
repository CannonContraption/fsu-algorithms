#!/usr/bin/python

import sys

args = sys.argv

if (len(args) < 3):
	raise ValueError("Bad arguments.")

if (len(args[1]) != len(args[2])):
	print(args[1] + " is not a permutation of " + args[2])
	exit

for char in args[1]:
	for compchar in args[2]:
		if (char != compchar):
			print(args[1] + " is not a permutation of " + args[2])
			exit

print(args[1] + " is a permutation of " + args[2])
