print("input number: ")
num = int(input())
print("dividers:")
for i in range(2, num-1):
    if num % i == 0:
        print(i)

