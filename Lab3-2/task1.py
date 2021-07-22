import sys
number=int(sys.argv [1])
out = 0
for i in range(number -1, 1, -1):
	if (number % i == 0):
		out = out+1
print (out+2)

