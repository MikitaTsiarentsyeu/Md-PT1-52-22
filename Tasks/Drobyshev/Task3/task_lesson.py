"five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
а = list(set({'five': 5, 'thirteen': 13, 'two':2, 'eleven': 11, 'seventeen':17, 'one':1, 'ten':10, 'four':4, 'eight':8, 'five':5, 'nineteen':19}.values()))
print(а)
for a in range (len(а)-1):
    if a%2 == 0:
        print (а[a]*а[a+1], end="  ")
    else:
        print (а[a]+а[a+1], end="  ")
print()
print(f"The total sum of all odd numbers = {sum(а for а in а if а%2 !=0)}")