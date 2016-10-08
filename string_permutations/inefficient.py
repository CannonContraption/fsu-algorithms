#!/usr/bin/python

import sys

args = sys.argv

isPerm = True

if (len(args) < 3):
	raise ValueError("Bad arguments.")

if (len(args[1]) != len(args[2])):
	print(args[1] + " is not a permutation of " + args[2])
	quit()

for char in args[1]:
	if (char not in args[2]):
		isPerm = False
		break

if isPerm:
	print(args[1] + " is a permutation of " + args[2])
else:
	print(args[1] + " is not a permutation of " + args[2])
