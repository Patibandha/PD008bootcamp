"""
Question: Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program: hello world! 123 Then, the output should be:
LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
s = raw_input("Enter line: ")

d=l=0
for a in s:
    if a.isdigit():
        d=d+1
    elif a.isalpha():
        l=l+1
    else:
        pass

print "Letters:", l
print "Digit:", d



