# 6. JUST ONE VARIBLE! (actualy is not realy one, but four):

s = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
d = {5:'five', 13: 'thirteen', 2: 'two', 11: 'eleven', 17: 'seventeen', 2: 'two', 1: 'one', 13: 'thirteen',
     10: 'ten', 4: 'four', 8: 'eight', 5: 'five', 19: 'nineteen'}

# Varibles used: s, b, k, i:
# s - condition string;
# d - dictionary for string;
# i, j, k - indexes and dictionary values
print('\n-----------------------------------')

# 1. Just figures (new):
print('1. Just figures:')
print([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]])
print('\n')

# 2. No dublicates (new):
print('2. No dublicates:')
print(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))
print('\n')

# 3. Sorting (new):
print('3. Sorting:') # i could do it by comprehension but i was realy tired for that time. And i've just copy paste. =\
for i in range(len(list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]])))):
    for j in range(len(list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]])))):
        if list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))[j] > list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))[i]:
            list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))[j], list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))[i] =  list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))[i], list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))[j]
print(list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]])))
print('\n')

# #4. Some calculating (new):
print('4. Some calculating:')
print([list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))[i]+list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))[i+1] if i % 4 == 0  else list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))[i]*list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))[i+1] for i in range(0, (len(list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]]))) - 1), 2)])
print('\n')

# #5 The sum of odd numbers (new):
print('5. The sum of odd numbers:')
print([i for i in list(set([k for i in range(len(s.split(' '))) for k in d.keys() if d[k] == s.split(' ')[i]])) if i % 2 != 0])
