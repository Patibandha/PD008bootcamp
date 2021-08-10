# Question: With a given integral number n,
# write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included)
# then the program should print the dictionary. Suppose the following input is supplied to the program: 8
# the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple


num = int(input("Enter a number: "))
num_dictonary = dict()

for i in range(1, num + 1):
    num_dictonary[i] = i * i

print(num_dictonary)
