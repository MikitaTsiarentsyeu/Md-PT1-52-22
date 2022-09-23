class Food:

    def __init__(self, desc, type):
        self.desc = desc
        self.type = type

    def __str__(self):
        return self.desc

class Animal:

    def eat(self, something):
        print(f"eating {something}")
        
    def phe(self):
        print("phe...")

class Carnivore(Animal):

    def eat(self, something):
        if something.type == "meat":
            Animal.eat(self, something)
        else:
            self.phe()

class Herbivore(Animal):

    def eat(self, something):
        if something.type == "herbal":
            Animal.eat(self, something)
        else:
            self.phe()

class Omnivore(Herbivore, Carnivore):

    def eat(self, something):
        if something.type == "meat":
            Carnivore.eat(self, something)
        elif  something.type == "herbal":
            Herbivore.eat(self, something)
        else:
            self.phe()


beef = Food("beef", "meat")
grass = Food("grass", "herbal")

c = Carnivore()
h = Herbivore()
o = Omnivore()

c.eat(beef)
c.eat(grass)

h.eat(beef)
h.eat(grass)

o.eat(beef)
o.eat(grass)

print(Omnivore.mro())