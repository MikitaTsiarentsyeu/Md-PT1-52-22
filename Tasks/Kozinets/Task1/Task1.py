from decimal import Decimal as Dec


def profit(deposit, rate, term_y, term_m, cap_period):
    """Profit calculating
     Arguments:
    - deposit:  deposit amount, currency unit;
    - rate:  interest rate, % / year
    - term_y:  deposit term, years;
    - term_m:  deposit term, months;
    - cap_period:  period of capitalisation, months."""

    if cap_period not in (1,3,6,12):
        raise ValueError ('Period of capitalisation must be 1, 3, 6 or 12 months!')

    profit = deposit

    for i in range(term_y * int(12/cap_period)):
        profit *= (1 + (rate * Dec('0.01')))**Dec(str(cap_period/12))

    if term_m // cap_period != 0:
        for j in range(term_m // cap_period):
            profit *= (1 + (rate * Dec('0.01')))**Dec(str(cap_period/12))

    return round(profit,2)


print(profit(20000,15,5,0,1))