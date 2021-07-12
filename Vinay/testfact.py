def check_factorial(number):
    if number < 0:
        msg = "Please enter a positive number only"
        return msg
    elif number == 0 or number == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial = factorial * i
        return factorial


def main():
    number = int(input("enter a number"))
    try:
        check_factorial(number)
        print("Your answer is: ", check_factorial(number))
    except ValueError:
        print("Enter a different number")


if __name__ == '__main__':
    main()
