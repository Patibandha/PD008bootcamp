#Question: Define a class which has at least two methods:
# getString: to get a string from console input printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#Hints: Use init method to construct some parameters

class InputOut_String:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())


def main():
    string_obj = InputOut_String()
    string_obj.getString()
    string_obj.printString()


if __name__ == '__main__':
    main()

