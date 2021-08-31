##----------------------------------------# Question 9 Level 2
#Question£º Write a program that accepts sequence of lines as input and
#prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
# Hello world Practice makes perfect Then,
# the output should be: HELLO WORLD PRACTICE MAKES PERFECT

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


def line_sequence():
    lines = []
    input_line = input("Enter a line: ")
    if input_line:
        lines.append(input_line.upper())
        for sentence in lines:
            print(sentence)


if __name__ == '__main__':
    line_sequence()