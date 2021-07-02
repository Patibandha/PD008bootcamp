x = float(input("Enter First value: "))
y=float(input("Enter Second value: "))
print("Enter the operator: ")
op=input("Enter any value from: + - * / ")

if op== '+':
    result=x+y
elif op== '-':
    result=x-y
elif op== '*':
    result=x*y
elif op== '/':
    result=x/y
else:
    print("Enter numeric value")

print("result is:", result)
