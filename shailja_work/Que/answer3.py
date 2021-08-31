# Question: With a given integral number n,
# write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included)
# then the program should print the dictionary. Suppose the following input is supplied to the program: 8
# the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple


def dict_num(num):
    num_dictionary = dict()
    for i in range(1, num + 1):
        num_dictionary[i] = i * i
    return num_dictionary


def main():
    num = int(input("Enter a number: "))
    dict_ans = dict_num(num)
    print(dict_ans)


if __name__ == '__main__':
    main()
