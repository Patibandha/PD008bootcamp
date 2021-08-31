# Question 2: Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
#
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

def factorial(f):
    if f == 0 or f == 1:
        return 1
    else:
        return f * factorial(f - 1)


def main():
    f = int(input("Enter a number to calulate factorial: "))
    try:
        factorial(f)
        print("Factorial of a number is: ", factorial(f))
    except ValueError:
        print("You must choose a number. Please try again")


if __name__ == '__main__':
    main()
