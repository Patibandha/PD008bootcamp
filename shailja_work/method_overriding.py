# parent class
class Animal:

    # function breath
    def breathe(self):
        print("I breathe oxygen.")

    # function feed
    def feed(self):
        print("I eat food.")


# child class
class Herbivorous(Animal):

    # function feed
    def feed(self):
        print("I eat only plants.")



class Carnivorous(Animal):

    # function feed
    def feed(self):
        print("I eat only meat.")

herbi = Herbivorous()
carni = Carnivorous()
herbi.feed()
carni.feed()
