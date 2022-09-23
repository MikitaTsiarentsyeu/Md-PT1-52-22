# class Animal:

#     def SaySomething(self):
#         print("Hello, I'm an animal")

class Dog():

    def SaySomething(self):
        print("Woof")

class Cat():

    def SaySomething(self):
        print("Nyaaa")

# class Cow(Animal): pass

class Human():

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def SaySomething(self):
        print(f"Hello, I'm {self.name}")

# a = Animal()
d = Dog()
c = Cat()
# cw = Cow()
h = Human("Igor")

for elem in [ d, c, h]:
    elem.SaySomething()