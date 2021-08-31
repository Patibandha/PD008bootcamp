# Question 7 Level 2

# Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 Then,
# the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


def twodim_array(row, col):
    final_array = []
    for x in range(0, row):
        nested_list = []
        for y in range(0, col):
            nested_list.append(x*y)
        final_array.append(nested_list)
    return final_array


def main():
    input_string = input("enter a value for [x,y]: ")
    dimensions = [int(x) for x in input_string.split(',')]
    row = dimensions[0]
    col = dimensions[1]
    final_out = twodim_array(row, col)
    print(final_out)


if __name__ == '__main__':
    main()
