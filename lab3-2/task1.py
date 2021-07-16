#!/usr/bin/python

import sys

inputNumber=int(sys.argv[1])

count=0
i=1
print("Devisors: ")
while i <= inputNumber:
 if inputNumber % i == 0:
  count+=1
  print(i)
 i+=1
print("Count of devisors: ")
print(count)


