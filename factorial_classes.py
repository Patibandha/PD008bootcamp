class Factorial:


    def factorial_number(self, number):
        if number < 0:
            msg = "Please enter a positive number only"
            return msg
        elif number == 0 or number == 1:
            return 1
        else:
            factorial = 1
            for i in range(1, number + 1):
                factorial = factorial * i
            return factorial


factorial = Factorial()


def main():
    number = int(input("Please enter a number:"))
    print("The factorial is: ", factorial.factorial_number(number))


if __name__ == '__main__':
    main()
