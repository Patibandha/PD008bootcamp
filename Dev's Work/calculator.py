class Operation(val1, val2):
    def add(self, val1, val2):
        return val1 + val2
    def subtract(self, val1, val2):
        return val1 - val2
    def multiply(self, val1, val2):
        return val1 * val2
    def divide(self, val1, val2):
        return val1 // val2

calculate = Operation(val1, val2)

def main_method():
    print("Enter an operation from +, - , /, *")
    operator = input("enter here:")
    val1 = input("Enter your 1st number:")
    val2 = input("Enter your 2nd number:")
    if operator == '+':
        print(calculate.add(val1, val2))
    elif operator == '-':
        print(calculate.subtract(val1, val2))
    elif operator == '/':
        print(calculate.divide(val2, val1))
    elif operator == '*':
        print(calculate.multiply(val2, val1))
    else:
        print("Choose the correct option")
if __name__ == '__main__':
    main_method()
