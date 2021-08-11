# Question 5
# Level 1
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use init method to construct some parameters

class Capital:

    def __init__(self):
        self.name_string = ""

    def get_input(self):
        self.name_string = input("Enter a string")

    def original(self):
        print('console input is: ', self.name_string, '. The final output is: ', self.name_string.upper())


def main():
    capital = Capital()
    capital.get_input()
    capital.original()


if __name__ == "__main__":
    main()

