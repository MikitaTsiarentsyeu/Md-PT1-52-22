word = "FizzBuzz"
print(*(word[(0,4,4)[x%3]:4 if x % 5 else 8] or x for x in range(1,101)))