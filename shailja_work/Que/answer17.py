"""Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following: D 100 W 200

D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500

Hints: In case of input data being supplied to the question, it should be assumed to be a console input."""
from distlib.compat import raw_input


def bank_function():
    final_amount = 0
    while True:
        d_w = raw_input()
        value = d_w.split(" ")
        print(value)
        transaction = value[0]
        if transaction == "E":
            break
        else:
            amount = int(value[1])
            if transaction == "D":
                final_amount += amount
            elif transaction == "W":
                final_amount -= amount
            else:
                pass
    print(final_amount)
        # operation = value[0]
        # final_amount = int(value[1])
        # if operation == "D":
        #     amount += final_amount
        # if operation == "W":
        #     amount -= final_amount
        # else:
        #     pass
        # return amount


if __name__ == '__main__':
    bank_function()