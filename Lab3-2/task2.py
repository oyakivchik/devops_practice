#!/usr/bin/python

array = [ int(num) for num in input().split()]

def Average(arr):
   return sum(arr) / len(arr)

print ("Average is ", round(Average(array), 2))
