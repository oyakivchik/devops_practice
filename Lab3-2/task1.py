#!/usr/bin/python

import sys

input=int(sys.argv[1])

count=0
i=1
print("Devisors: ")
while i <= input:
 if input % i == 0:
  count+=1
  print(i)
 i+=1
print("Count of devisors: ")
print(count)


