import sys
#Пасує аргумент з командного рядку
num = int(sys.argv[1])

for i in range(num):
	i = i + 1
	if(num%i == 0):
		print('The divider is:', i)

print("The number inputed is ",sys.argv[1])


