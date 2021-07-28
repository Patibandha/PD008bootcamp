class Calculator:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 // value2


def main_method():
    calculation = Calculator()
    try:
        value1 = float(input("Enter yours 1st number"))
        value2 = float(input("Enter yours 2nd number"))
        print(" + for add")
        print(" - for subtract")
        print(" * for multiply")
        print("  // for divide")
        options_are = input("choose: ")
        if options_are == '+':
            print(calculation.add(value1, value2))
        elif options_are == '-':
            print(calculation.subtract(value1, value2))
        elif options_are == '*':
            print(calculation.multiply(value1, value2))
        elif options_are == '//':
            print(calculation.divide(value1, value2))
        else:
            print("Choose the correction option")
    except ValueError:
        print("Enter valid input")


if __name__ == '__main__':
    main_method()
