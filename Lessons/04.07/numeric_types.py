import decimal
import fractions

x = 3

print(type(x))

print(12//3, 2+3, 4-8, 2*7)

print(int(12/3))

print(int(2.8), int(-2.8))

print(round(2.5), round(3.5)) #banking rounding

print(type(3.5))

print(1.0+2)

print(float(3))

print(1.1+1.1+1.1)

print(0.1)

x = decimal.Decimal(0.1)
print(x)

print(x+x+x)

x = decimal.Decimal('0.1')
print(x)
print(x+x+x)

print(type(x*25))

print(fractions.Fraction(2.5))
print(fractions.Fraction(0.1))
print(fractions.Fraction('0.1'))

print(fractions.Fraction('0.1') + fractions.Fraction('0.1') + fractions.Fraction('0.1'))

print(fractions.Fraction('0.1')+fractions.Fraction('2.5'))

print(fractions.Fraction('0.1')*fractions.Fraction('0.1'))