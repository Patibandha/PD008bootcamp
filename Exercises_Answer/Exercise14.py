"""
Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program: Hello world! Then,
the output should be: UPPER CASE 1 LOWER CASE 9

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
s = raw_input("Enter line: ")

u=l=0
for a in s:
    if a.isupper():
        u=u+1
    elif a.islower():
        l=l+1
    else:
        pass

print "Upper Case:", u
print "Lower Case:", l


