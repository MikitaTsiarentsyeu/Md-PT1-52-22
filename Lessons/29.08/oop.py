class Dog:

    name = "Psina"
    breed = "shepherd"
    color = "dirty"

    def introduce_myself(self):
        print(f"Hello there my dear human, I'm a {self.color} {self.breed}, my name is {self.name}")

    def eat(self):
        print("eating!")

    def sleep(self):
        print("sleeping...")

    def walkywalky(self):
        print("I'm going!!!")


dog1 = Dog()
dog1.name = "Zephyrka"
dog1.breed = "wss"
dog1.color = "white"

dog2 = Dog()
dog2.name = "Chappi"
dog2.breed = "colly"
dog2.color = "colorless"

dog1.introduce_myself()
dog2.introduce_myself()

Dog.introduce_myself(dog1)
Dog.introduce_myself(dog2)



class Simpleton: pass

s = Simpleton()
print(s, type(s))
print(Simpleton, type(Simpleton))

s2 =  Simpleton()

s.test = "some new test value"

s2.test = "test value for s2"

s3 = Simpleton()

Simpleton.test = "default value"

print(s.test)
print(s2.test)
print(s3.test)