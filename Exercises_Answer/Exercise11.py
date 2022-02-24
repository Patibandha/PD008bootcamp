"""
Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and
then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
items = []
number = [x for x in raw_input().split(',')]
for j in number:
    x = int(j,2)
    if not x%5:
        items.append(j)
print(','.join(items))