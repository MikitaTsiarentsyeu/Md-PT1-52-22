
class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make
        
    make = property(get_make, set_make)
    model = property(get_model, set_model)

    def move(self):
        print(f"I'm {self.make} {self.model} and I'm moving very fast")

class Car(Vehicle):

    def __init__(self, make, model, color='red'):
        super().__init__(make, model)
        self.color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    color = property(get_color, set_color)

    def make_doughnut(self):
        print("Vroooooom....")

    def move(self):
        super().move()
        print(f"And btw I'm {self.color}")


c = Car("volvo", "v60")
c.move()

c.make_doughnut()
