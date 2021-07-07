# Define a function factorial
def factorial(f):

    if f < 0:
        msg = "Please Enter Positive number"
        return msg
    elif f == 0 or f == 1:
        return 1
    else:
        fact_number = 1
        while(f > 1):
            fact_number = fact_number * f
            f = f - 1
        return fact_number


def main():
    # Ask user to enter a number
    f = int(input("Enter a number to calulate factorial: "))
    try:
        factorial(f)
    # print the final output
    # print("Factorial of a number is: ", factorial(f))
    except ValueError:
        print("You must choose a number. Please try again")
    return main()

if __name__ == '__main__':
    main()




