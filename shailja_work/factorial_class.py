from math import factorial


class Fact:

    # Define a function factorial
    def factorial(self, f):
        if f < 0:
            msg = "Please Enter Positive number"
            return msg
        elif f == 0 or f == 1:
            return 1
        else:
            return f * factorial(f - 1)


obj_fac = Fact()


def main():
    f = int(input("Enter a number to calculate factorial: "))
    try:
        ans = obj_fac.factorial(f)
        print("Factorial of a number is: ", ans)
    except ValueError:
        print("You must choose a number. Please try again")


if __name__ == '__main__':
    main()


def obj_fac():
    return None
