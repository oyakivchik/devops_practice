def mediana(enter_list):
    enter_list.sort()
    return enter_list[1]

list_num = [int(input()) for i in range(3)]
print("\n Median: ", mediana(list_num))
