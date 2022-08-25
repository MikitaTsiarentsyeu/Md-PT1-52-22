def list_sum(l, i=0):
    if len(l) == 1:
        if type(l[i]) == list:
            sum = list_sum(l[i])   
        else:
            sum = l[i]
    elif type(l[i]) == list:
        sum = list_sum(l[i]) + list_sum(l[i+1:])   
    else:
        sum = l[i] + list_sum(l[i+1:])
    return sum    

l = [1,2,[[3,[4,[[5],6]],[7]],8],9]

print(list_sum(l))