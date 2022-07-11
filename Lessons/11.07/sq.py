a, b, c = float(input("Enter a:\n")), float(input("Enter b:\n")), float(input("Enter c:\n"))

D = b*b - 4*a*c

if D < 0:
    print("there are no roots")
elif D == 0:
    print("there is one root:\n")
    print(-b/(2*a))
else:
    print("there are two roots:\n")
    print((-b-D**0.5)/(2*a))
    print((-b+D**0.5)/(2*a))