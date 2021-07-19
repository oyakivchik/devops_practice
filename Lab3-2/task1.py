import sys

def sum_divisor(number):
    counter = 0
    for i in range(number - 1, 1, -1):
        if (number % i == 0):
            counter+=1
    return counter

argument = int(sys.argv[1])
            
print(sum_divisor(argument))
