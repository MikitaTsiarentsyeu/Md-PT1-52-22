def sum(line):
    num = 0
    for i in line:
        if isinstance (i,list):
             num = num + sum(i)
        else:
           num = num + i
    return num
print(f'Sum of items: {sum([2,3,[4,5,[6,7,[8,9]]]])}\n') #44

def fib_list(n,c=0,p=1,r=[]):
    if n==0:
        return r
    else:
        r.append(c+p)
        return fib_list(n-1,c+p,c,r)
print('F(10)=')
print(*fib_list(int(10)))