"""
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even,
otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.

Solution def checkValue(n): if n%2 == 0: print "It is an even number" else: print "It is an odd number"

checkValue(7)
"""
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even number".format(num))
else:
   print("{0} is Odd number".format(num))