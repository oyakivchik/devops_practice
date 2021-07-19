import sys

num=int(sys.argv[1])
counter=0
i=1

while i<= num:
	if num % i == 0:
		counter+=1
	i+=1
print(counter)
