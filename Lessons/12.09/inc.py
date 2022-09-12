
class Student:

    def __init__(self, name, year):
        self.set_name(name)
        self.__year = year

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def provide_info(self):
        print(f"I'm {self.get_name()}, a student of {self.__year} year")

s = Student("Vasya", 3)
# s.__name = "Vasya"
# s._Student__year = 3
# s.__name = "test"
# print(s.__name)
s.set_name("test")
print(s.get_name())
s.provide_info()