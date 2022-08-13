

word = "FizzBuzz"
print(*(word[(0,4,4)[x%3]:4 if x % 5 else 8] or x for x in range(1,101)))


for i in range(1,101):
    
    final_word = ''
    if i % 3 == 0:
        final_word+=word[:4]
    if i % 5 == 0:
        final_word+=word[4:]
    if not final_word:
        print(i) 
        continue
    print(final_word)     
