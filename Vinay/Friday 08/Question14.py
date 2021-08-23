# Question 14
# Level 2
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def characters(upper_lower):
    upper_lower = list(upper_lower)
    upper, lower = 0, 0
    for i in upper_lower:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1
        else:
            pass
    print("UPPER CASE ", upper)
    print("LOWER CASE ", lower)


def main():
    upper_lower= input("Enter the sentence to check Upper case and Lower case: ")
    print(characters(upper_lower))


if __name__ == "__main__":
    main()

