x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))

x = float(x)
y = float(y)

operation = input("Choose your operation from + - * /: ")
if operation == "+":
    r = x + y
elif operation == "-":
    r = x - y
elif operation == "*":
    r = x * y
elif operation == "/":
    r = x / y
else:
    print("Please choose correct operation")

print("Result: ", r)
