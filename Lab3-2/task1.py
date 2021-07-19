import sys
num = int(sys.argv[1])

print("Divisors of this num :")

for i in range(num):
	i+=1
	if(num%i==0):
		print(i)
