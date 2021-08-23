# Question 11
# Level 2
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# 4 number seperated with commas.
# if they are check if they are divisble of 5
# print it out

def check_divide(number):
    value = []
    numbers = number.split(',')
    for item in numbers:
        answer = int (item, 2)
        if not answer % 5:
            value.append(item)
    print(','.join(value))


def main():
    number = input("Enter 4 numbers if need to add more use comma: ")
    print(check_divide(number))


if __name__ == "__main__":
    main()


