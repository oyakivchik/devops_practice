n = int(input("Write integer number: "))
dividers = 0
for i in range(n - 1, 1, -1):
    if (n % i == 0):
        dividers += 1
print("Count of dividers: ", dividers)
