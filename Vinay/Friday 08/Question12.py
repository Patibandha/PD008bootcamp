# Question 12
# Level 2
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input
def even_number(numbers):
    answer = []
    for number in range(numbers, 3001):
        string_converter = str(number)
        if (int(string_converter[0] % 2 == 0) and (int(string_converter[1]) % 2 == 0) and (int(string_converter[2]) % 2 == 0) and (int(string_converter[3]) % 2 == 0)):
            answer.append(string_converter)
    print(",".join(answer))


if __name__ == "__main__":
    print(even_number(1000))
