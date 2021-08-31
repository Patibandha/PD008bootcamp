# Question 1: Write a program which will find all such numbers
# which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.


def div_seven():
    div_list = []
    for i in range(2000, 3201):
        if (i % 7 == 0) and (i % 5 == 0):
            div_list.append(i)
    return div_list


def main():
    final_list = div_seven()
    print(final_list)


if __name__ == '__main__':
    main()
