from sys import argv

def number_of_divisors(number):
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    return print(counter)

task1, number = argv
number_of_divisors(int(number))
