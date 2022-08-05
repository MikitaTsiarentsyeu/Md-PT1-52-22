# In one varible with using comprehanson and the teacher's method [True, 0, 0]:
print('\n====*-*====')
s = 'seven one twelve nine nineteen four twenty nine nineteen fourteen'
print(f'Starting string is: {s}')
s = [{'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
'fifteen':15, 'sixteen':16, 'seventeen': 17, 'eighteen': 18,  'nineteen': 19, 'twenty': 20}[s] for s in s.split(' ')]
print(f'Only numbers: {s}')
s = set(s)
print(f'Do dublicates: {s}')
s = sorted(list(set(s)))
print(f'Sorted list: {s}')
s += [True, 0, 0]
print(f'Calculate: {[s[s[-1]]*s[s[-1]+1] if s[-1]%2!=0 else s[s[-1]]+s[s[-1]+1] for s[-1] in range(len(s) - 4)]}')
print(f'Sum: {sum([s[-2] + s[s[-1]] for s[-1] in range(len(s) - 3) if s[s[-1]] if s[s[-1]]%2!=0])}')
print('====*-*====\n')