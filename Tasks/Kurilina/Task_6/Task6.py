word = "FizzBuzz"
for x in range (1,101):
    
    if x % 3 == 0:
        if x % 5 ==0:
            print(word)
        else:    
            print(word[:4])    
    elif x%5 ==0:
        print(word[4:])        
    else:
        print(x)    

print([word if x % 15 == 0 else word[:4] if x % 3 == 0 else word[4:] if x % 5 == 0 else x for x in range(1,101)])      