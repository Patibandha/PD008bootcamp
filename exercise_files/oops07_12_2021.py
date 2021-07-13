"""
(1) To avoid repetition of code
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


def runner():
    dog = Dog("Golden Retriver", "3", "Tiger", 24, 30)
    ans = dog.descr()
    print(ans)
    ans2 = dog.phsic()
    print(ans2)


if __name__ == '__main__':
    runner()