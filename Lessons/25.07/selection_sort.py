l = [3,2,5,4,6,8,9,6,5,3,3,5,89,0]


for i in range(len(l)-1):
    min, current = i, i
    for i in range(current, len(l)):
        
        if l[i] < l[min]:
            min = i
    else:
        l[current], l[min] = l[min], l[current]
        print(l)

# min, current = 1, 1
# for i in range(current, len(l)):
    
#     if l[i] < l[min]:
#         min = i
# else:
#     l[current], l[min] = l[min], l[current]

# print(l)

# min, current = 2, 2
# for i in range(current, len(l)):
    
#     if l[i] < l[min]:
#         min = i
# else:
#     l[current], l[min] = l[min], l[current]

# print(l)

# min, current = 3, 3
# for i in range(current, len(l)):
    
#     if l[i] < l[min]:
#         min = i
# else:
#     l[current], l[min] = l[min], l[current]

# print(l)

# min, current = 4, 4
# for i in range(current, len(l)):
    
#     if l[i] < l[min]:
#         min = i
# else:
#     l[current], l[min] = l[min], l[current]

# print(l)

# min, current = 5, 5
# for i in range(current, len(l)):
    
#     if l[i] < l[min]:
#         min = i
# else:
#     l[current], l[min] = l[min], l[current]

# print(l)


l = [3,2,5,4,6,8,9,6,5,3,3,5,89,0]

print(l)


for i in range(len(l)):
    for j in range(i, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
            print(l[i], l[j])
    print(l)

#more optimal version
for i in range(len(l)):
    min = i
    for j in range(i, len(l)):
        if l[min] > l[j]:
            min = j
    l[i], l[min] = l[min], l[i]
    print(l)