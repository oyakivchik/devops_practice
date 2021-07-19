import sys

sum  = 0
for i in range(1, len(sys.argv)):
	sum +=int(sys.argv[i])

print("Mean: ", sum / (len(sys.argv) - 1))
