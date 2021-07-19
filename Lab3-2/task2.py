import sys

def avg(number):
    sum = 0
    for i in number:
        sum = sum + i           
    avg = sum / len(number)
    return avg

arguments = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]

print(avg(arguments))
