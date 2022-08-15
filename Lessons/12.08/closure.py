def maker(n):
    def action(x):
        print(n)
        return x ** n
    return action

square = maker(2)
cube = maker(3)
forth = maker(4)

print(square(4), cube(4), forth(4))

