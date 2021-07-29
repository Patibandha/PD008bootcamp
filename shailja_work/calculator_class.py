import string
import logging


class Calculator:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


def main():
    obj_cal = Calculator()
    try:
        num1 = float(input("Enter First value: "))
        num2 = float(input("Enter Second value: "))
        print("Enter the operator: ")
        op = input("Enter any value from: + - * / ")
        result = 0
        if op == '+':
            result = obj_cal.add(num1, num2)
        elif op == '-':
            result = obj_cal.subtract(num1, num2)
        elif op == '*':
            result = obj_cal.multiply(num1, num2)
        elif op == '/':
            result = obj_cal.divide(num1, num2)
        print("result is:", result)

    except ValueError:
        logging.warning("please enter numeric value")


if __name__ == '__main__':
    main()
