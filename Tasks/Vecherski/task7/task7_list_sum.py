def list_sum(l):
    sum = 0
    for i in l:
        sum += list_sum(i) if isinstance(i,list) else i 
    return sum    

l = [11,2,[[30,[4,[[15],6]],[77]],8],19]

print(list_sum(l))