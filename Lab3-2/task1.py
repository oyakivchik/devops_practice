#!/usr/bin/python

while True:
   try:
     number=int(input("Enter a Number: "))
     if (number < 1):
       raise ValueError();
     break;
     
   except ValueError:
     print("Invalid input")

divisors = []

for i in range (1, number+1):
   if number % i == 0:
     divisors.append(i)

print("Number ", number, " has ", len(divisors), " divisors")
print(divisors)
