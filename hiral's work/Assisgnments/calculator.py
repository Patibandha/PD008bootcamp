
# Basic calculator
# functions for basic operation +, -, *, /
def addition(add1,add2):
    print("This is your addition")
    return add1 + add2
def subtraction(sub1, sub2):
    print("This is your subtraction")
    return sub1 - sub2
def multiplication(mul1, mul2):
    print("This is your multiplication")
    return mul1 * mul2
def division(div1,div2):
    print("This is your division")
    return div1 / div2

#function to get user choice of operation
def mainMenu():
    print("Please choose which operation you would like to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice of operation number: "))
    return choice

#function to get user input for two numbers for operation
def calculation():
    ch = mainMenu()
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    if ch == 1:
        result = addition(num1,num2)
    if ch == 2:
        result = subtraction(num1,num2)
    if ch == 3:
        result = multiplication(num1,num2)
    if ch == 4:
        result = division(num1,num2)
    print("Result is", result)

calculation()
# Basic calculator

# functions for basic operation +, -, *, /
def addition(add1,add2):
    print("This is your addition")
    return add1 + add2
def subtraction(sub1, sub2):
    print("This is your subtraction")
    return sub1 - sub2
def multiplication(mul1, mul2):
    print("This is your multiplication")
    return mul1 * mul2
def division(div1,div2):
    print("This is your division")
    return div1 / div2

#function to get user choice of operation
def mainMenu():
    print("Please choose which operation you would like to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice of operation number: "))
    return choice

#function to get user input for two numbers for operation
def calculation():
    ch = mainMenu()
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    if ch == 1:
        result = addition(num1,num2)
    if ch == 2:
        result = subtraction(num1,num2)
    if ch == 3:
        result = multiplication(num1,num2)
    if ch == 4:
        result = division(num1,num2)
    print("Result is", result)

calculation()
>>>>>>> 6b0339e8187f1258e9c21c91080cde419a9b43e3
