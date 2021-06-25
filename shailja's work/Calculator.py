x=float(input("Enter First value: "))
y=float(input("Enter Second value: "))
print("Enter the operator: ");
op=input("Enter any value from: + - * / ")

if op== '+':
    Result=x+y;
elif op== '-':
    Result=x-y;
elif op== '*':
    Result=x*y;
elif op== '/':
    Result=x/y;
else:
    print("Enter numeric value");

print("Result is:", Result);
