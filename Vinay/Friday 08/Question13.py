# Level 2
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def letter_digit(argument):
    argument = list(argument)
    number, letter = 0, 0
    for i in argument:
        if i.isalpha():
            letter = letter + 1
        if i.isdigit():
            number = number + 1
        else:
            pass
    print("Letters are:", letter)
    print("Numbers are:", number)


def main():
    argument = input("Please enter the sentence")
    print(letter_digit(argument))


if __name__ == "__main__":
    main()

