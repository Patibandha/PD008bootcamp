# n! = n*(n-1)*(n-2).....*1

# User entering number
number = float(input("Please Enter a number: "))

# Calculation
def factorial(number):
    if number == 1:
        return number
    else:
        return (number*factorial(number-1))

# print statments after calculation
if number < 0:
    print("Number is invalid. Please enter a valid number")
elif number == 0:
    print("0 factorial is 1")
else:
    print("The factorial of ", number, "is", factorial(number))