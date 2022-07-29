# this solution uses 2 variables
"five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
а = list(set({'five': 5, 'thirteen': 13, 'two':2, 'eleven': 11, 'seventeen':17, 'one':1, 'ten':10, 'four':4, 'eight':8, 'five':5, 'nineteen':19}.values()))
print(а)
for a in range (len(а)-1):
    print (а[a]*а[a+1], end="  ") if a%2 == 0 else print (а[a]+а[a+1], end="  ")
print()
print(f"The total sum of all odd numbers = {sum(а for а in а if а%2 !=0)}")



# this solution uses 1 variable
import math
"five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
a = list(set({'five': 5, 'thirteen': 13, 'two':2, 'eleven': 11, 'seventeen':17, 'one':1, 'ten':10, 'four':4, 'eight':8, 'five':5, 'nineteen':19}.values()))
print(a)

if len(a) == 0:
    print("The collection is empty. Please add a few items to the collection.")

elif len(a) == 1:
    print("Please add at least 2 numerals to the collection to multiply the items in the collection.")

elif len(a) == 2:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")

elif len(a) == 3:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")

elif len(a) == 4:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")

elif len(a) == 5:    
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")

elif len(a) == 6:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")

elif len(a) == 7:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")

elif len(a) == 8:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")

elif len(a) == 9:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")

elif len(a) == 10:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")
    print(f"{math.prod(a for a in a[8:10])}", end="  ")

elif len(a) == 11:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")
    print(f"{math.prod(a for a in a[8:10])}", end="  ")
    print(f"{sum(a for a in a[9:11])}", end="  ")

elif len(a) == 12:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")
    print(f"{math.prod(a for a in a[8:10])}", end="  ")
    print(f"{sum(a for a in a[9:11])}", end="  ")
    print(f"{math.prod(a for a in a[10:12])}", end="  ")

elif len(a) == 13:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")
    print(f"{math.prod(a for a in a[8:10])}", end="  ")
    print(f"{sum(a for a in a[9:11])}", end="  ")
    print(f"{math.prod(a for a in a[10:12])}", end="  ")
    print(f"{sum(a for a in a[11:13])}", end="  ")

elif len(a) == 14:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")
    print(f"{math.prod(a for a in a[8:10])}", end="  ")
    print(f"{sum(a for a in a[9:11])}", end="  ")
    print(f"{math.prod(a for a in a[10:12])}", end="  ")
    print(f"{sum(a for a in a[11:13])}", end="  ")
    print(f"{math.prod(a for a in a[12:14])}", end="  ")

elif len(a) == 15:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")
    print(f"{math.prod(a for a in a[8:10])}", end="  ")
    print(f"{sum(a for a in a[9:11])}", end="  ")
    print(f"{math.prod(a for a in a[10:12])}", end="  ")
    print(f"{sum(a for a in a[11:13])}", end="  ")
    print(f"{math.prod(a for a in a[12:14])}", end="  ")
    print(f"{sum(a for a in a[13:15])}", end="  ")

elif len(a) == 16:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")
    print(f"{math.prod(a for a in a[8:10])}", end="  ")
    print(f"{sum(a for a in a[9:11])}", end="  ")
    print(f"{math.prod(a for a in a[10:12])}", end="  ")
    print(f"{sum(a for a in a[11:13])}", end="  ")
    print(f"{math.prod(a for a in a[12:14])}", end="  ")
    print(f"{sum(a for a in a[13:15])}", end="  ")
    print(f"{math.prod(a for a in a[14:16])}", end="  ")

elif len(a) == 17:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")
    print(f"{math.prod(a for a in a[8:10])}", end="  ")
    print(f"{sum(a for a in a[9:11])}", end="  ")
    print(f"{math.prod(a for a in a[10:12])}", end="  ")
    print(f"{sum(a for a in a[11:13])}", end="  ")
    print(f"{math.prod(a for a in a[12:14])}", end="  ")
    print(f"{sum(a for a in a[13:15])}", end="  ")
    print(f"{math.prod(a for a in a[14:16])}", end="  ")
    print(f"{sum(a for a in a[15:17])}", end="  ")

elif len(a) == 18:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")
    print(f"{math.prod(a for a in a[8:10])}", end="  ")
    print(f"{sum(a for a in a[9:11])}", end="  ")
    print(f"{math.prod(a for a in a[10:12])}", end="  ")
    print(f"{sum(a for a in a[11:13])}", end="  ")
    print(f"{math.prod(a for a in a[12:14])}", end="  ")
    print(f"{sum(a for a in a[13:15])}", end="  ")
    print(f"{math.prod(a for a in a[14:16])}", end="  ")
    print(f"{sum(a for a in a[15:17])}", end="  ")
    print(f"{math.prod(a for a in a[16:18])}", end="  ")

elif len(a) == 19:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")
    print(f"{math.prod(a for a in a[8:10])}", end="  ")
    print(f"{sum(a for a in a[9:11])}", end="  ")
    print(f"{math.prod(a for a in a[10:12])}", end="  ")
    print(f"{sum(a for a in a[11:13])}", end="  ")
    print(f"{math.prod(a for a in a[12:14])}", end="  ")
    print(f"{sum(a for a in a[13:15])}", end="  ")
    print(f"{math.prod(a for a in a[14:16])}", end="  ")
    print(f"{sum(a for a in a[15:17])}", end="  ")
    print(f"{math.prod(a for a in a[16:18])}", end="  ")
    print(f"{sum(a for a in a[17:19])}", end="  ")

elif len(a) == 20:
    print(f"{math.prod(a for a in a[0:2])}", end="  ")
    print(f"{sum(a for a in a[1:3])}", end="  ")
    print(f"{math.prod(a for a in a[2:4])}", end="  ")
    print(f"{sum(a for a in a[3:5])}", end="  ")
    print(f"{math.prod(a for a in a[4:6])}", end="  ")
    print(f"{sum(a for a in a[5:7])}", end="  ")
    print(f"{math.prod(a for a in a[6:8])}", end="  ")
    print(f"{sum(a for a in a[7:9])}", end="  ")
    print(f"{math.prod(a for a in a[8:10])}", end="  ")
    print(f"{sum(a for a in a[9:11])}", end="  ")
    print(f"{math.prod(a for a in a[10:12])}", end="  ")
    print(f"{sum(a for a in a[11:13])}", end="  ")
    print(f"{math.prod(a for a in a[12:14])}", end="  ")
    print(f"{sum(a for a in a[13:15])}", end="  ")
    print(f"{math.prod(a for a in a[14:16])}", end="  ")
    print(f"{sum(a for a in a[15:17])}", end="  ")
    print(f"{math.prod(a for a in a[16:18])}", end="  ")
    print(f"{sum(a for a in a[17:19])}", end="  ")
    print(f"{math.prod(a for a in a[18:20])}", end="  ")

else:
    print('Error! All numbers must be greater than 0 and less than 21 in the collection')

print()
print(f"The total sum of all odd numbers = {sum(a for a in a if a%2 !=0)}")