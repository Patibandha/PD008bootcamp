# Question 7
# Level 2
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


def math_logic(row, column):
    two_array = []
    for i in range(0, row):
        row_list = []
        for j in range(0, column):
            row_list.append(i * j)
        two_array.append(row_list)
    print(two_array)


def main():
    row, column = int(input("Enter two numbers")), int(input("Enter second number"))
    print(math_logic(row, column))


if __name__ == "__main__":
    main()

