print("Welcome to calculation process")
#add formula
def add(x, y):
    return x + y

#subratct formula
def subtract (x,y):
    return x-y
#multiply formula
def multiply (x,y):
    return x*y
#divison
def divide (x,y):
    return x//y
#Option Selection
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Divison \n")

while True:
    choice= input("")

#check the option
    if choice in ('1','2','3','4'):
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        if choice =='1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice =='2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice =='3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice =='4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print ("invalid choice")