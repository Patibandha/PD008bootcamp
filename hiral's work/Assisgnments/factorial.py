# function to calculate factorial
def factorial(n):
    # first checking the number is 0 or 1,
    # it is then, return   1
    # otherwise calculate factorial for given number
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * factorial(n-1))


# getting user input for factorial
num = float(input("enter your number"))
print("you entered", num)
print("Factorial is:", factorial(num))