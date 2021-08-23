# Level 2
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# Hints:
# In case of input data being supplied to the question,…
def digits(values):
    number1 = int("%s" % values)
    number2 = int("%s%s" % (values, values))
    number3 = int("%s%s%s" % (values, values, values))
    number4 = int("%s%s%s%s" % (values, values, values, values))
    total = number1 + number2 + number3 + number4
    print(total)


def main():
    values = int(input("Enter an integer:"))
    print(digits(values))


if __name__ == "__main__":
    main()