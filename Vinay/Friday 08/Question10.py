# Level 2
# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.


def checking_sentence(check):
    read = check.split(' ')
    values = []
    for i in read:
        if(check.count(i) >= 1 and (i not in values)):
            values.append(i)
    print(' '.join(values))


def main():
    check = input("Enter the sentence: ")
    print(checking_sentence(check))

if __name__ == '__main__':
    main()
