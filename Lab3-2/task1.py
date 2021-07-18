
numbers = int(input())

count = 0
i=1

while i<= int(numbers):
	if numbers % i == 0 :
		count += 1
	i+= 1
print("Count is :")
print(count)
