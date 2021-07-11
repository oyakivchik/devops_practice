import sys

def mediana(enter_list):
    sorted_tuple = tuple(sorted(enter_list))
    return sorted_tuple[1]

tupl = sys.argv[1], sys.argv[2], sys.argv[3]
print(mediana(tupl))
