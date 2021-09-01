"""Question 14 Level 2

Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

Hints: In case of input data being supplied to the question, it should be assumed to be a console input."""
from distlib.compat import raw_input


def upper_lower():
    input_value = raw_input()
    digit_value = {"UPPER CASE":0, "LOWER CASE":0}
    for i in input_value:
        if i.isupper():
            digit_value["UPPER CASE"] += 1
        elif i.islower():
            digit_value["LOWER CASE"] += 1
        else:
            pass
    print("UPPER CASE", digit_value["UPPER CASE"])
    print("LOWER CASE", digit_value["LOWER CASE"])


if __name__ == '__main__':
    upper_lower()