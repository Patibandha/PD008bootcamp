"""
(1) To avoid repetition of code

Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects

Object-Oriented Programming (OOP) vs Procedure Oriented Programming (POP)
The basic difference between OOP and procedural programming is-

One way to think about POP is the same way you make lemonade for example. The procedure of making lemonade involves- first taking water according to the need, then adding sugar to the water, then adding lemon juice to the mixture, and finally mixing the whole solution. And your lemonade is ready to serve. In a similar way, POP requires a certain procedure of steps. A procedural program consists of functions. This means that in the POP approach the program is divided into functions, which are specific to different tasks. These functions are arranged in a specific sequence and the control of the program flows sequentially.
Whereas an OOP program consists of objects. The object-Oriented approach divides the program into objects. And these objects are the entities that bundle up the properties and the behavior of the real-world objects.
POP is suitable for small tasks only. Because as the length of the program increases, the complexity of the code also increases. And it ends up becoming a web of functions. Also, it becomes hard to debug. OOP solves this problem with the help of a clearer and less complex structure. It allows code re-usability in the form of inheritance.
Another important thing is that in procedure-oriented programming all the functions have access to all the data, which implies a lack of security. Suppose you want to secure the credentials or any other critical information from the world. Then the procedural approach fails to provide you that security. For this OOP helps you with one of its amazing functionality known as Encapsulation, which allows us to hide data. Don’t worry I’ll cover this in detail in the latter part of this article along with other concepts of Object-Oriented Programming. For now, just understand that OOP enables security and POP does not.
Programming languages like C, Pascal and BASIC use the procedural approach whereas  Java, Python, JavaScript, PHP, Scala, and C++ are the main languages that provide the Object-oriented approach.

Class
Object
Method
Inheritance
Encapsulation
Polymorphism
Abstraction
"""


class Dog:

    def __init__(self, breed, age, name, length, weight):
        self.breed = breed
        self.age = age
        self.name = name
        self.length = length
        self.weight = weight

    # Instance Method
    def descr(self):
        return f"Dog name is {self.name}, it is {self.age} old and it's breed is {self.breed}", self
        # return "Dog name is" + " " + self.name + ", it is " + self.age + " old and it's breed is " + self.breed

    @classmethod
    def phsic(cls):
        self = cls("Golden Retriver", "3", "Tiger", 24, 30)
        return f"{self.length}", cls


################## Inheritance#########################################################
class Parent:
    def __init__(self, gp, gm):
        self.gp = gp
        self.gm = gm

    def grand_parent_name(self):
        return f"My Grandfather Name is {self.gp} & My Grandmother Name is {self.gm}"

class Child1(Parent):
    pass


class Child2(Parent):
    def __init__(self, papa, mom, gp, gm):
        super().__init__(gp, gm)
        self.papa = papa
        self.mom = mom

    def parent_name(self):
        return f"My father Name is {self.papa} & My mother Name is {self.mom}"

#############################Encapsulation######################################
class Motercycle:
    def __init__(self, brand, model, horsepower):
        self._brand = brand   #protected variable
        self.model = model
        self.__horsepower = horsepower    #private variable

    def about_motorcycle(self):
        return f"This Awesome {self._brand}'s {self.model}"

    @classmethod
    def accessing_private(cls):
        self = cls("Indian", "Chef", 1000)
        return f"This Awesome {self._brand}'s {self.model} and it has {self.__horsepower}"


#####################################Polymorphism/ Method Overloading#######################################
class Cloth:
    def __init__(self, brand, type, matrial ):
        self.brand = brand
        self.type = type
        self.matrial = matrial

    def summer(self):
        print(f"In summer I like to wear {self.brand} cloths of {self.type} with {self.matrial}")

class Cloth_winter:
    def __init__(self, brand, type, matrial):
        self.brand = brand
        self.type = type
        self.matrial = matrial

    def summer(self):
        # return \
        print(f"In summer I like to wear {self.brand} cloths of {self.type} with {self.matrial}")

    # def winter(self):
    #     return f"In summer I like to wear {self.brand} cloths of {self.type} with {self.matrial}"



def runner():
    # dog = Dog("Golden Retriver", "3", "Tiger", 24, 30)
    # ans = dog.descr()
    # print(ans)
    # ans2 = dog.phsic()
    # print(ans2)

    parent_object = Child1("Ambalal", "Rasilaben")
    print(parent_object.grand_parent_name())

    parent = Child2("Alkeshbhi", "Bhavanaben", "Ambalal", "Rasilaben")
    print(parent.grand_parent_name())
    print(parent.parent_name())

    moto = Motercycle("Indian", "Chef", 1000)

    print(moto.about_motorcycle())
    print(moto._brand)
    print(moto.model)
    print(moto._Motercycle__horsepower)
    print(moto.accessing_private())

    cloth = Cloth("old navy", "pants", "cotton")
    cloth_winter = Cloth_winter("A&F", "T-shirt", "polyester")

    for my_cloth in (cloth, cloth_winter):
        print(my_cloth.summer())

if __name__ == '__main__':
    runner()