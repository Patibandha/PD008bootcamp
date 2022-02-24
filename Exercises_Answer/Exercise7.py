"""
Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Example Suppose the following inputs are given to the program: 3,5 Then,
the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

[ [0, 0, 0, 0, 0],[(00), (01), (02), (03), (04)], [0, 1, 2, 3, 4],[(10), (11), (12), (13), (14)]
[0, 2, 4, 6, 8] [(20), (21), (22), (33), (4*4)] ]
for i in range(0,3): i=0,1,2 for j in range(0,5): j=0,1,2,3,4

Hints: Note: In case of input data being supplied to the question,
it should be assumed to be a console input in a comma-separated form.

"""

x = int(input("I: "))
y = int(input("J: "))

arr = [[0 for col in range(y)] for row in range(x)]
for row in range(x):
    for col in range(y):
        arr[row][col] = row*col
print(arr)
