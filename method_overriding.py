class Family:

    def father(self):
        print("I am father")

    def mother(self):
        print("I am a mother")


class Mother(Family):
    def mother(self):
        print("I am mother of vinay")


class Father(Family):
    def father(self):
        print("I am father of vinay")


father = Father()
mother = Mother()

father.father()
mother.mother()








