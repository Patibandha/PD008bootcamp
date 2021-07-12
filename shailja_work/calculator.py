def add(num1,num2):
    return num1 + num2


def subtract(num1,num2):
    return num1 - num2


def multiply(num1,num2):
    return num1 * num2


def divide(num1,num2):
    return num1/ num2


def main():
    num1 = float(input("Enter First value: "))
    num2 = float(input("Enter Second value: "))
    print("Enter the operator: ")
    op = input("Enter any value from: + - * / ")

    if op == '+':
        result = add(num1, num2)
    elif op == '-':
        result = subtract(num1, num2)
    elif op == '*':
        result = multiply(num1, num2)
    elif op == '/':
        result = divide(num1, num2)
    else:
        print("Enter numeric value")
    print("result is:", result)


if __name__ == '__main__':
    main()