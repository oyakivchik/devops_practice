import sys

num = int(sys.argv[1])
print("dividers:")
for i in range(2, num-1):
    if num % i == 0:
        print(i)

