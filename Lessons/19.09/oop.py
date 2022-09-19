class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return str(self.__x)

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return str(self.__y)

    def set_y(self, y):
        self.__y = y

    x = property(get_x, set_x)
    y = property(get_y, set_y)
        

p = Point(2, 3)
p.y = 4
print(p.x, p.y)
    