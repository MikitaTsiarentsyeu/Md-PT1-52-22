class FreightTrain:

    cart_len = 10

    def __init__(self, cart_count) -> None:
        self.cart_count = cart_count

    def __str__(self):
        return f"I'm a train of {self.cart_count} carts, choo-choo!"

    def __int__(self):
        return self.cart_count

    def __len__(self):
        return self.cart_count * self.cart_len

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FreightTrain):
            return False

        return self.cart_count == other.cart_count

    def __add__(self, other):
        try:
            return FreightTrain(self.cart_count+other.cart_count)
        except:
            raise TypeError("connot add non-FreightTrain objects")



shorty = FreightTrain(3)
loooooong = FreightTrain(10)

print(shorty)
print(loooooong)

print(int(shorty))
print(len(loooooong))

print(shorty == loooooong)
print(FreightTrain(10) == loooooong)

print(shorty + loooooong)