numb = int(input("Введіть ціле число: "))
count_of_dividers = 0
for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        count_of_dividers += 1
print("Кількість дільників:", count_of_dividers)
