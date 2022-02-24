"""
Question: Define a class which has at least two methods: getString:
to get a string from console input printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints: Use init method to construct some parameters

"""
class InOutString(object):
    def __init__(self):
        self.string1 = ""


    def getString(self):
        self.string1 = raw_input()


    def printString(self):
        print self.string1.upper()

stringObject = InOutString()
stringObject.getString()
stringObject.printString()


