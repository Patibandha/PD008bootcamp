# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

import math


def method(number):
    output_value = []
    for i in number:
        result = round(math.sqrt(2 * 50 * int(i) / 30))
        output_value.append(result)
    return output_value


if __name__ == "__main__":
    print(method([100, 150, 180]))
