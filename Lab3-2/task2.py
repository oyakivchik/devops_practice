#!/usr/bin/python

while True:
   try:
      print("Input numbers (separated bt space): ")
      array = [ int(num) for num in input().split()]
      break;
   except ValueError:
      print("Invalid input")

def Average(arr):
   return sum(arr) / len(arr)

print ("Average is ", round(Average(array), 2))
