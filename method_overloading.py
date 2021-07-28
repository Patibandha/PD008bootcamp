# Created a class
class Number:
    # function instance
    def any_number(welf, name=None):
        if name is not None:
            print("Hello my name is: " + name)
        else:
            print("No name is given")


# object create
ans = Number()
# empty value. it will print else statement
ans.any_number()
# name is given in this one. will print if statement
ans.any_number('vinay')
