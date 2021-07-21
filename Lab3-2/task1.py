#!/usr/bin/python

import sys

Input = int (sys.argv[1])
count=0
i=1

while i<=Input:
	if Input %i==0:
		count+=1
		print(i)
		i+=1

print ("Count is :")
print (count)

