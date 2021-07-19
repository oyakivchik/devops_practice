def arithmetic_mean():
    count = 1
    average = 0
    while count <= 3:
        numbers = input(f"Введіть {count} число: ")
        average += float(numbers)
        count += 1
    return average / 3


print("Середнє арефметичне =", arithmetic_mean())
