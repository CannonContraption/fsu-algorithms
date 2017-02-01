import math
import sys

for letter in range(ord('a'), ord('z')):
	for lettertwo in range(ord('A'), ord('Z')):
		letconv = (letter**2)+(lettertwo**2)
		for i in range(0,int(letconv/2)):
			conv1 = letconv-i
			if(math.sqrt(conv1)%2==0):
				conv2 = letconv-(letconv-i)
				if(math.sqrt(conv2)%2==0):
					if int(math.sqrt(conv1))<128:
						if int(math.sqrt(conv2))<128:
							if(conv1 != letter):
								if(conv1 != lettertwo):
									if(conv2 != letter):
										if(conv2 != lettertwo):
											sys.stdout.write(str(chr(letter)));
											sys.stdout.write("	");
											sys.stdout.write(str(chr(lettertwo)));
											sys.stdout.write("	");
											sys.stdout.write(str(chr(int(math.sqrt(conv1)))))
											sys.stdout.write("	")
											sys.stdout.write(str(chr(int(math.sqrt(conv2)))))
											print()
