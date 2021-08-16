# Level 2
# Question£º
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


def uppercase():
    user_sentence = input("Enter the sentence")
    if user_sentence:
        sentence_into_words = user_sentence.upper()
        return sentence_into_words


if __name__ == '__main__':
    print(uppercase())
