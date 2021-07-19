numb = int(input("Enter number:"))
count = 0;
print("Result:", end = " ")
for i in range(numb -1, 1, -1):
  if (numb % i ==0):
    count = count + 1
print(count, end = " ")
