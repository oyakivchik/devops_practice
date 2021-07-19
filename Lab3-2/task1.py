numb = int(input("Input number "))
divider = int(0)
print("result:", end = " ")
for i in range(numb , 0, -1):
    if (numb % i == 0):
       divider += 1
print(divider)