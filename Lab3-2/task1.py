#!/usr/bin/python

number=int(input("Input a Number: "))


counter = 0

for i in range (1, number+1):
   if number % i == 0:
     counter += 1

print("Number ", number, " has ", counter, " divisors")
