def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 // num2


def cal(num1, num2, opr):
    # TODO: add logic to get different operation
    if opr == 1:
        answer = add(num1, num2)
        return answer
    elif opr == 2:
        answer = subtract(num1, num2)
        return answer

    elif opr == 3:
        answer = multiply(num1, num2)
        return answer

    elif opr == 4:
        answer = divide(num1, num2)
        return answer

    else:
        print("invalid")


# TODO: add main method to take input string for calculator operation
def main():
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    print("Select operation.")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Divide: ")
    opr = int(input("Select the following option:"))
    if opr in (1, 2, 3, 4):
        try:
            answer = cal(num1, num2, opr)
            print("Final answer is: ", answer)
        except ValueError:
            print("Number must be between 1-4. Try again: ")
    else:
        print("How would I end up here?")


if __name__ == '__main__':
    main()
