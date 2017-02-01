import sys
if(len(sys.argv)!=3):
	print("Invalid args.")
	exit(1)
if(list(sys.argv[1]).sort() == list(sys.argv[2]).sort()):
	print("Is permutation")
else:
	print("Isn't")
