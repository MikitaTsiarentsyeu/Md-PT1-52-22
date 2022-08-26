def sum_lists(list):
    sum = 0
    for i in list:
        try:
           int(i)
           sum+=i
        except:
            sum+= sum_lists(i)
    return sum        


list_1 = [[1, 2], [2, 4, [[7, 8], [4, 6],[8,8]]]]
print(sum_lists(list_1))




mas = [0,1]

def fib(n):
    mas.append(mas[-1]+mas[-2])
    if len(mas)< n:   
        fib(n)
    return mas[0:n]    

print(fib(20))