from multipledispatch import dispatch
class Calc:

    # First add method takes two nums arguments and print their addition
    def add(self,num1,num2):
        print("two numbers addition is", num1+num2)

    # second add method takes three nums arguments and print their addition
    def add(self,num1,num2,num3):
        print("three numbers addition is", num1+num2+num3)

    # method overloading with Multiple Dispatch Decorator
    @dispatch(int, int)  # this line will execute first whenever we call following function
    def multiplication(num1, num2):
        print("multiplication of two nums is", num1 * num2)

    @dispatch(int, int, int)  # this line will execute first whenever we call following function
    def multiplication(num1, num2, num3):
        print("multiplication of three nums is", num1 * num2 * num3)

# creating Calc class object to access add() methods
calc_object = Calc()

# below line will give TypeError as Python can only use the latest defined method.
# in this case, we have add() with three arguments as out last latest define method
# so it will only consider that one
#calc_object.add(8,9)

#it will call second add() method with three arguments
calc_object.add(8,9,12)

# it will call multiplication() with three arguments
calc_object.multiplication(2,3,2)
# it will call multiplication() with two arguments
calc_object.multiplication(10,2)

# Dispatcher creates an object which stores different implementation
# and on runtime, it selects the appropriate method as the type
# and number of parameters passed.