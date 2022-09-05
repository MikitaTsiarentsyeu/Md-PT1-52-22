def sum_list(l):

    if len(l) == 1 and isinstance(l[0],int):
        return l[0]
    elif isinstance(l[0],int):
        return l[0]+sum_list(l[1:len(l)])
    elif isinstance(l[0],list):
        if isinstance(l[0],list) and len(l) != 1:
            l[0] = sum_list(l[0])
            return sum_list(l)
        else: 
            return sum_list(l[0])
        
l = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print (f"Result of the first task = {sum_list(l)}") 
        
      
def fib(n):
    def fib_calc(n):
        if (n <= 1):
            return n
        else:
            return (fib_calc(n-1) + fib_calc(n-2))
    return ','.join([str(fib_calc(i)) for i in range(n)])
   
  
print(f"Result of the second task = fib(5) -> {fib(5)}")
print(f"Result of the second task = fib(10) -> {fib(10)}")
    


    
