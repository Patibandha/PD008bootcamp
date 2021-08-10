# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
import logging
import logging


number = int(input("Enter a number: "))


def factorial(number):
    if number == 1:
        return number
    else:
        return (number * factorial(number - 1))


if number < 0:
    logging.warning('Number is invalid. Please enter a valid number')
elif number == 0:
    logging.warning('0 factorial is 1')
else:
    print("The factorial of ", number, "is", factorial(number))
