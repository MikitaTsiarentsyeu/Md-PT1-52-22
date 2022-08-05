import decimal

print('Hello, to calculate income, select the following type of capitalization:')
try:
    a = int(input('Annual - 1 and Monthly - 2''\n'))
    b = decimal.Decimal(input('What amount will you deposit in BYN''\n'))
    c = int(input('How long will you sign the contract in months''\n'))
    r = decimal.Decimal(input('Enter what interest rate you will have''\n'))
    e = r / 100  # This is a part of the amount invested or already paid together with the invested#
    f = c // 12  # This is how many years in 24 months#
    z = int(c % 12)  # How many months without a year#
    # The formula for calculating the annual capitalization for years only! or 12.24.... months
    #
    d1 = (decimal.Decimal(1 + e)) ** decimal.Decimal(c / 12) * b
    # Formula for calculating annual capitalization with year and month or 25, 37 months, etc.
    #
    d2 = (b * ((decimal.Decimal(1 + e)) ** decimal.Decimal(f))) * (decimal.Decimal(1 + (e * decimal.Decimal(z / 12))))
    # Formula for Monthly Capitalization
    d3 = b * (1 + e / 12) ** c
    # When months are divisible by 12 without a remainder for annual capitalization
    if a == 1 and c % 12 == 0:
        print('Your income together with profit:')
        print(round(d1, 2))
        print(
            "You can look at the formulas and calculate the income on the site yourself on the calculator raiffeisen.ru")
        input('To recalculate, press enter')
    # Divided by 12 with remainder for annual capitalization
    elif a == 1 and c % 12 != 0:
        print('Your income together with profit:')
        print(round(d2, 2))
        print(
            "You can look at the formulas and calculate the income on the site yourself on the calculator raiffeisen.ru")
        input('To recalculate, press enter')
    elif a == 2:
        print('Your income together with profit:')
        print(round(d3, 2))
        print(
            "You can look at the formulas and calculate the income on the site yourself on the calculator raiffeisen.ru")
        input('To recalculate, press enter')
    elif a != int or b != decimal or c != int or r != decimal:
        print('Error')
        print("Please enter correct data")
        input('To recalculate, press enter')
    else:
        input('To recalculate, press enter')
    # This is necessary because the program runs quickly and we do not see the result.

except ValueError:
    print(('Error: You did not enter a correct number'))
except Exception as v:
        print('Unknown error: You did not enter a number', v)


