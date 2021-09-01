"""Question 13 Level 2

Question: Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, it should be assumed to be a console input"""
from distlib.compat import raw_input


def letters_digits():
    input_value = raw_input()
    digit_value = {"DIGITS":0, "LETTERS":0}
    for i in input_value:
        if i.isdigit():
            digit_value["DIGITS"] += 1
        elif i.isalpha():
            digit_value["LETTERS"] += 1
        else:
            pass
    print("LETTERS", digit_value["LETTERS"])
    print("DIGITS", digit_value["DIGITS"])


if __name__ == '__main__':
    letters_digits()