def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 // num2


def cal(num1, num2, opr):
    # TODO: add logic to get different operation
    if opr == '1':
        add(num1, num2)
    elif opr == '2':
        subtract(num1, num2)

    elif opr == '3':
        multiply(num1, num2)

    elif opr == '4':
        divide(num1, num2)

    else:
        print("invalid")


# TODO: add main method to take input string for calculator operation
def main():
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    print("Select operation.")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Divide: ")
    opr = int(input(""))
    if opr == ('1', '2', '3', '4'):
        try:
            cal(num1, num2, opr)
            print("Final answer is: ", cal(num1, num2, opr))
        except ValueError:
            print("Number must be between 1-4. Try again: ")
        return main()


if __name__ == '__main__':
    main()
