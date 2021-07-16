#!/usr/bin/python


import sys

Input=int(sys.argv[1])

n=0
i=1
print("Devisors: ")
while i <= Input:
 if Input % i == 0:
  n+=1
  print(i)
 i+=1
print("Count of devisors: ")
print(n)

