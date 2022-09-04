def fizzbuzz(n):
    def fizzbuzz_solve(n):
        if n%5==0:
            if n%3 ==0:
                return "FizzBuzz"
            return "Buzz"
        if n%3==0:
            return "Fizz"

        else:
            return n
    
    return ','.join([str(fizzbuzz_solve(i)) for i in range(1,n)])
  
    
print(fizzbuzz(100))
