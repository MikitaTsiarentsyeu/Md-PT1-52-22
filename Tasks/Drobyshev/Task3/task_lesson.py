# this solution uses 2 variables
а = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
print(а)

а = а.split()
while а[0] not in range(1,21):
	    а.append({'one':1, 'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10, 
                  'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,
		          'eighteen':18,'nineteen':19, 'twenty':20}[а.pop(0)])
    
а = sorted(list(set(а)))
print(а)
for a in range (len(а)-1):
    print (а[a]*а[a+1], end="  ") if a%2 == 0 else print (а[a]+а[a+1], end="  ")
print()
print(f"The total sum of all odd numbers = {sum(а for а in а if а%2 !=0)}\n")



# this solution uses 1 variable

a = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
print(a)

a = a.split()
while a[0] not in range(1,21):
	    a.append({'one':1, 'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10, 
                  'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,
		          'eighteen':18,'nineteen':19, 'twenty':20}[a.pop(0)])
    
a = sorted(list(set(a)))
print(a)

if len(a) == 0:
    print("The collection is empty. Please add a few items to the collection.")

elif len(a) == 1:
    print("Please add at least 2 numerals to the collection to multiply the items in the collection.")

elif len(a) == 2:
    print(a[0]*a[1], end="  ")

elif len(a) == 3:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")

elif len(a) == 4:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")

elif len(a) == 5:    
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")

elif len(a) == 6:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")

elif len(a) == 7:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")

elif len(a) == 8:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")

elif len(a) == 9:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")

elif len(a) == 10:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")
    print(a[8]*a[9], end="  ")

elif len(a) == 11:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")
    print(a[8]*a[9], end="  ")
    print(a[9]+a[10], end="  ")

elif len(a) == 12:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")
    print(a[8]*a[9], end="  ")
    print(a[9]+a[10], end="  ")
    print(a[10]*a[11], end="  ")

elif len(a) == 13:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")
    print(a[8]*a[9], end="  ")
    print(a[9]+a[10], end="  ")
    print(a[10]*a[11], end="  ")
    print(a[11]+a[12], end="  ")

elif len(a) == 14:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")
    print(a[8]*a[9], end="  ")
    print(a[9]+a[10], end="  ")
    print(a[10]*a[11], end="  ")
    print(a[11]+a[12], end="  ")
    print(a[12]*a[13], end="  ")

elif len(a) == 15:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")
    print(a[8]*a[9], end="  ")
    print(a[9]+a[10], end="  ")
    print(a[10]*a[11], end="  ")
    print(a[11]+a[12], end="  ")
    print(a[12]*a[13], end="  ")
    print(a[13]+a[14], end="  ")

elif len(a) == 16:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")
    print(a[8]*a[9], end="  ")
    print(a[9]+a[10], end="  ")
    print(a[10]*a[11], end="  ")
    print(a[11]+a[12], end="  ")
    print(a[12]*a[13], end="  ")
    print(a[13]+a[14], end="  ")
    print(a[14]*a[15], end="  ")

elif len(a) == 17:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")
    print(a[8]*a[9], end="  ")
    print(a[9]+a[10], end="  ")
    print(a[10]*a[11], end="  ")
    print(a[11]+a[12], end="  ")
    print(a[12]*a[13], end="  ")
    print(a[13]+a[14], end="  ")
    print(a[14]*a[15], end="  ")
    print(a[15]+a[16], end="  ")

elif len(a) == 18:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")
    print(a[8]*a[9], end="  ")
    print(a[9]+a[10], end="  ")
    print(a[10]*a[11], end="  ")
    print(a[11]+a[12], end="  ")
    print(a[12]*a[13], end="  ")
    print(a[13]+a[14], end="  ")
    print(a[14]*a[15], end="  ")
    print(a[15]+a[16], end="  ")
    print(a[16]*a[17], end="  ")

elif len(a) == 19:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")
    print(a[8]*a[9], end="  ")
    print(a[9]+a[10], end="  ")
    print(a[10]*a[11], end="  ")
    print(a[11]+a[12], end="  ")
    print(a[12]*a[13], end="  ")
    print(a[13]+a[14], end="  ")
    print(a[14]*a[15], end="  ")
    print(a[15]+a[16], end="  ")
    print(a[16]*a[17], end="  ")
    print(a[17]+a[18], end="  ")

elif len(a) == 20:
    print(a[0]*a[1], end="  ")
    print(a[1]+a[2], end="  ")
    print(a[2]*a[3], end="  ")
    print(a[3]+a[4], end="  ")
    print(a[4]*a[5], end="  ")
    print(a[5]+a[6], end="  ")
    print(a[6]*a[7], end="  ")
    print(a[7]+a[8], end="  ")
    print(a[8]*a[9], end="  ")
    print(a[9]+a[10], end="  ")
    print(a[10]*a[11], end="  ")
    print(a[11]+a[12], end="  ")
    print(a[12]*a[13], end="  ")
    print(a[13]+a[14], end="  ")
    print(a[14]*a[15], end="  ")
    print(a[15]+a[16], end="  ")
    print(a[16]*a[17], end="  ")
    print(a[17]+a[18], end="  ")
    print(a[18]*a[19], end="  ")

else:
    print('Error! All numbers must be greater than 0 and less than 21 in the collection')

print()
print(f"The total sum of all odd numbers = {sum(a for a in a if a%2 !=0)}")