# 1.1)
# [print('fizz' * (not i % 3), 'buzz' * (not i % 5), str(i) * (not not i % 3) * (not not i % 5), sep = '') for i in range(1,101)]
# [print(f'{"fizz" * (not i % 3)}{"buzz" * (not i % 5)}{str(i) * (not not i % 3) * (not not i % 5)}') for i in range(1,101)]
# 1.2)
# [print('fizz' * (not i % 3), 'buzz' * (not i % 5), str(i) * (not not (i % 3 * i % 5)), sep = '') for i in range(1,101)]
# [print(f'{"fizz" * (not i % 3)}{"buzz" * (not i % 5)}{str(i) * (not not (i % 3 * i % 5))}') for i in range(1,101)]
# 1.3)
# [print('fizz' * (i % 3 == 0), 'buzz' * (i % 5 == 0), str(i) * ((i % 3 * i % 5) != 0), sep = '') for i in range(1,101)]
# [print(f'{"fizz" * (i % 3 == 0)}{"buzz" * (i % 5 == 0)}{str(i) * ((i % 3 * i % 5) != 0)}') for i in range(1,101)]
# 1.4)
# [print('fizz' * (not i % 3), 'buzz' * (not i % 5), str(i) * ((i % 3 * i % 5) != 0), sep = '') for i in range(1,101)]
# [print(f'{"fizz" * (not i % 3)}{"buzz" * (not i % 5)}{str(i) * ((i % 3 * i % 5) != 0)}') for i in range(1,101)]
# 1.5)
# [print('fizz' * (not i % 3) + 'buzz' * (not i % 5) or i) for i in range(1,101)]
# [print(f'{"fizz" * (not i % 3)}{"buzz" * (not i % 5)}' or i) for i in range(1,101)]


# 2.1)
# l = lambda x: [not x % 3,not x % 5]
# [print('fizz' * l(i)[0], 'buzz' * l(i)[1], str(i)*(not sum(l(i))), sep = '') for i in range(1,101)]
# 2.2)
# l = lambda x: [not x % 3,not x % 5]
# [print(f'{"fizz" * l(i)[0]}{"buzz" * l(i)[1]}{str(i)*(not sum(l(i)))}') for i in range(1,101)]
# 2.3)
# l = lambda x: [not x % 3,not x % 5]
# [print('fizz' * l(i)[0] + 'buzz' * l(i)[1] or i) for i in range(1,101)]


# 3)
# a = ['fizz' if i%3 == 0 else i for i in range(1,101)]
# for j in range(4,100,5):
# 	a[j] = 'fizzbuzz' if a[j] == 'fizz'  else  'buzz'
# for n in a:
# 	print(n)


# 4.1)
# for i in range(1,101):
# 	a = ''
# 	if not i % 3:
# 		a += 'fizz'
# 	if not i % 5:
# 		a += 'buzz'
# 	if a == '':
# 		a += str(i)
# 	print(a)
# 4.2)
# for i in range(0,101):
#     a = 'fizz' if not i % 3 else ''
#     a += 'buzz'if not i % 5 else ''
#     a += str(i) * (not len(a))
#     print(a)
