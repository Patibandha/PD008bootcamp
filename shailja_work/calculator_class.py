class Calculator:

    def add(self,num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


obj_cal = Calculator()


def main():
    num1 = float(input("Enter First value: "))
    num2 = float(input("Enter Second value: "))
    print("Enter the operator: ")
    op = input("Enter any value from: + - * / ")

    if op == '+':
        result = obj_cal.add(num1, num2)
    elif op == '-':
        result = obj_cal.subtract(num1, num2)
    elif op == '*':
        result = obj_cal.multiply(num1, num2)
    elif op == '/':
        result = obj_cal.divide(num1, num2)
    else:
        print("Enter numeric value")
    print("result is:", result)


if __name__ == '__main__':
    main()
