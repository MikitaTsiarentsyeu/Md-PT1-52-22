class Engine:

    def __init__(self, power, volume):
        self.power = power
        self.volume = volume

class SerialCar:

    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

eng = Engine(120, 5)
sc = SerialCar("VW", "Polo", eng)

sc.engine = Engine(330, 6)

class SuperCar:

    def __init__(self, make, model, power, volume):
        self.make = make
        self.model = model
        self.engine = Engine(power, volume)

    def get_power(self):
        return self.engine.power

    
