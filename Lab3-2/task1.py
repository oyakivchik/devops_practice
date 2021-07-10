numb = int(input("Enter an integer: "))
count = 0
for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        count += 1
print("Number of divisors:", count)