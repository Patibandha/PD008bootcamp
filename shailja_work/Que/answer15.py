#Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a. Suppose the following input is supplied to the program: 9 Then, the output should be: 11106
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


def output_function(compute_value):
    ans = 0
    if compute_value == 0:
        return ans
    else:
        ans = compute_value + int(str(compute_value) + str(compute_value)) + int(str(compute_value) + str(compute_value) + str(compute_value)) \
              + int(str(compute_value) + str(compute_value) + str(compute_value) + str(compute_value))
        return ans


if __name__ == '__main__':
    print(output_function(9))