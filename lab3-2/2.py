from sys import argv

def average(number1, number2, number3):
    return print((number1 + number2 + number3) / 3)

task2,number1, number2, number3 = argv
average(float(number1), float(number2), float(number3))
