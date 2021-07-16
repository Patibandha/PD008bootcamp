class Veggies:
    #class constructor
    def __init__(self):
        pass
    #Veggies class method with the same name overriding with Carrots class
    def tell_where(self):
        print("I am inside Veggies class ")

class Carrots(Veggies):
    # class constructor
    def __init__(self):
        pass
    #Carrots class method with the same name overriding with Veggies class
    def tell_where(self):
        print("I am inside Carrots class")

veggies_object = Veggies() #initiating Veggies class object
carrots_object = Carrots() #initiating Carrots class object

veggies_object.tell_where() #calling Veggies class tell_where()
carrots_object.tell_where() #calling Carrots class tell_where()


#Method overloading with multiple inheritance

class Root_veggitables:  # first parent class
    def tell_where(self): # overriding method
        print("I am in Root_vegitables class")
    def why_roots_r_good(self): # class specific method
        print("Because I am invisible")

class Leafy_veggitables: # second parent class
    def tell_where(self): # overriding method
        print("I am in Leafy_vegitables class")
    def why_leafies_r_good(self): # class specific method
        print("I have lots amino acids and vitamins in me")

class My_choice(Root_veggitables,Leafy_veggitables): # child class inheriting all properties from parent 1 and 2 class
    def tell_where(self): # oveerriding method
        print("I am in My_choice class")

root_veggitables_object = Root_veggitables() # creating Root_veggitables() object
leafy_veggitables_object = Leafy_veggitables() # creating Leafy_Veggietables() object
my_choice_object = My_choice() # creating My_choice() object that can also access parent 1 and 2 class methods
my_choice_object.why_leafies_r_good()
my_choice_object.why_roots_r_good()

my_choice_object.tell_where()
root_veggitables_object.tell_where()
leafy_veggitables_object.tell_where()

#which method executed will be determined by which class object we are using to invoke the method
# for example,if an object of a parent class is used to invoke the method, then parent class method will be executed,
# but if an object of the child class/subclass is used to invoke the method, then the child class method will be executed.