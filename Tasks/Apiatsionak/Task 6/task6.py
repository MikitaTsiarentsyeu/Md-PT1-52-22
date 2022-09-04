1

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


2
for i in range(1,101):
    a = ''
    if i % 3 == 0:
        a += 'Fizz'
    if i % 5 == 0:
        a += 'Buzz'
    if not a:
        a = i
    print(a)

3
print('\n'.join(map(lambda n: 'FizzBuzz' if n%15==0 else 'Fizz' if n % 3==0 else 'Buzz'if n % 5 == 0 else str(n),range(1,101))))