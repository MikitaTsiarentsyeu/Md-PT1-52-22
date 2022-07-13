
import decimal

print('\nDeposit calculation(monthly capitalization)')
answer = input('\nWould you like to calculate the deposit: yes(Y)/no(N)? ')
positive, positive_2 = 'yes', 'Y'
negative, negative_2 = 'no', 'N'

if answer == positive or answer == positive_2:

    print('\nSelect the type of calculation: \n initial deposit amount/deposit period of year(years)/annual interest rate(%) - option 1 \
        \n initial deposit amount/deposit period of month(months)/annual interest rate(%) - option 2')
    calculation = int(input('option - '))
    variable_1 = 1
    variable_2 = 2

    if calculation == variable_1:
        present_value = decimal.Decimal(
            input('\nInitial deposit amount in BYN: '))
        year = decimal.Decimal(input('Specify for how many years(year): '))
        interest_rate = decimal.Decimal(
            input('Enter the desired annual percentage(%): '))
        result_rate = decimal.Decimal(
            interest_rate / 100)  # conversion of interest
        result_value = present_value * \
            ((1 + result_rate / 12) ** (12 * year))
        print(
            f"\nYour contribution {present_value} BYN; term {year} year/years; {interest_rate}% annual. The amount to be issued is {result_value} BYN.")
    elif calculation == variable_2:
        present_value = decimal.Decimal(
            input('\nInitial deposit amount in BYN: '))
        user_month = decimal.Decimal(
            input('Specify for how many months(month): '))
        interest_rate = decimal.Decimal(
            input('Enter the desired annual percentage(%): '))
        result_rate = decimal.Decimal(
            interest_rate / 100)  # conversion of interest
        result_value = present_value * \
            ((1 + result_rate / 12) ** user_month)
        print(
            f"\nYour contribution {present_value} BYN; term {user_month} month/months; {interest_rate}% annual. The amount to be issued is {result_value} BYN.")
    else:
        print('There is no other way!!!')

elif answer == negative or answer == negative_2:
    print('Think! Get richer! Contribute!')
else:
    print('Incorrect input')
