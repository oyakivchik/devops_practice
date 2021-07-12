import sys

def mediana(enter_tupl):
   return sum(x**2 for x in enter_tupl)   

tupl = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
print(mediana(list(tupl)))
