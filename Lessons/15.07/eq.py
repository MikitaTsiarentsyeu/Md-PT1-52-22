eq = input("Input your eq:\n")
x = int(input("Input the x val:\n"))

eq = eq.replace(' ', '').replace('y=', '')
print(eq)

coeff = eq.split('x')
print(coeff)

res = x*int(coeff[0])+int(coeff[1])
print(res)