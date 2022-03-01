"""
Question: Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following: D 100 W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500

Hints: In case of input data being supplied to the question, it should be assumed to be a console input..
"""
tot = 0
n = (raw_input())
i = 0
while(i < n):
    x = input()
    values = x.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        tot += amount
    elif operation == "W":
        tot -= amount
    else:
        pass
    i += 1
print("total=", tot)

