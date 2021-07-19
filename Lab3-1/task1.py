n = int(input())
count = 0
i=1
while i<= int(n):
	if n % i == 0 :
		count += 1
	i+= 1
print("Count is : "+ str(count))