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





def fib(n):
    while n>1:
        mas = fib(n-1)
        mas.append(1) if n==2 else mas.append(mas[-1]+ mas[-2])
        return mas
    return [0]    


print(fib(20))