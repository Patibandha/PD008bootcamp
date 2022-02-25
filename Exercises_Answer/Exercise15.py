"""
Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
value = input("Enter Number: ")

n1 = int("%s" % value)
n2 = int("%s%s" % (value,value))
n3 = int("%s%s%s" % (value,value,value))
n4 = int("%s%s%s%s" % (value,value,value,value))

total = n1 + n2 + n3 + n4
print(total)




