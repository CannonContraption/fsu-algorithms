#!/usr/bin/env python3
import sys

def showhelp():
	print("Checkversionnumber Script")
	print()
	print("checkversionnumber.py ((-h|--help)|{First version} {Second version})")
	print()
	print("Checks the first argument (as a dot-separated version number) against the second")
	print("   (same format). Reports which one is newer and exits.");
	print()
	print("-h   --help            Displays this message.")
	print("     {First version}   First version number. Example: 0.1.3")
	print("     {Second version}  Second version number. Example: 0.1.9")
	print()
	print("Created Jan '17 by Jim Read. Licence: GPL v2")
	print()

if len(sys.argv) < 2:
	showhelp()
	sys.stderr.write("\033[1;31mNo arguments.\033[m\nExiting now.\n");
	sys.exit(1);
elif len(sys.argv) < 3:
	if(sys.argv[1] == '--help'):
		showhelp();
		sys.exit(0)
	if(sys.argv[1] == '-h'):
		showhelp()
		sys.exit(0)
	sys.stderr.write("\033[1;31mComparing a version number to itself is pointless.\033[m\nExiting now.\n");
	sys.exit(2);
elif len(sys.argv) == 3:
	if(sys.argv[1] == '--help'):
		showhelp();
		sys.exit(0)
	if(sys.argv[1] == '-h'):
		showhelp()
		sys.exit(0)
	splitversion1 = sys.argv[1].split('.');
	splitversion2 = sys.argv[2].split('.');
	if(len(splitversion1) != len(splitversion2)):
		sys.stderr.write("\033[1;31mThese version numbering schemes don't match\033[m\nPlease try a different set, where there is an equal number of sub-versions.\n");
	for i in range(0,len(splitversion1)):
		sv1 = int(splitversion1[i])
		sv2 = int(splitversion2[i])
		if(sv1 < sv2):
			print("Second is newer.");
			sys.exit(0)
		elif (sv1 == sv2):
			pass
		elif (sv1 > sv2):
			print("First is newer.");
			sys.exit(0);
	print("These are the same.")
else:
	if(sys.argv[1] == '--help'):
		showhelp();
		sys.exit(0)
	elif(sys.argv[1] == '-h'):
		showhelp()
		sys.exit(0)
	else:
		sys.stderr.write("\033[1;31mInvalid arguments.\033[m\nExiting now.\n")
