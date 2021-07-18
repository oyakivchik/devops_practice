import sys

number=int(sys.argv[1])

counter=0
i=1
print("Devisors: ", end ="")
while i <= number:
 if number % i == 0:
  counter+=1
  print(i, end=" ")
 i+=1
print()
print("Number of devisors: ")
print(counter)