import sys
number = int(sys.argv[1])

count_of_dividers = 0
for i in range(1, number + 1, 1):
    if (number % i == 0):
        count_of_dividers += 1

print("Count of dividers:", count_of_dividers)
