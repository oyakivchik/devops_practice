import sys

number = int(sys.argv[1])
print("Divisors of " , number , "is: ")
for i in range(number):
	i += 1
	if(number % i == 0):
		print(i)
 