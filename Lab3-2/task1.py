#!/usr/bin/python

import sys

number=int(sys.argv[1])

count=0
i=1

print("Devisors: ")
while i <= number:
 if number % i == 0:
  count+=1
  print(i)
 i+=1
print("Count of devisors: ")
print(count)


