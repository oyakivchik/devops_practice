import sys

numbers = int(sys.argv[1])

quantity = 0
i = 1

while i <= numbers:
 if numbers % i == 0:
  quantity += 1
 i += 1

print("Divisors count: ")
print(quantity)
