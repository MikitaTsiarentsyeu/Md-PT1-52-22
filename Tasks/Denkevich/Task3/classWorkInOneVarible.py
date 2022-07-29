# In one varible (if don't count string and dictionary):
s = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
d = {'five': 5, 'thirteen': 13, 'two': 2, 'eleven': 11, 'seventeen': 17,
     'one': 1, 'ten': 10, 'four': 4, 'eight': 8, 'nineteen': 19}
print('\n')
print([d[i] for i in s.split(' ')])
print(set([d[i] for i in s.split(' ')]))
print(list(set([d[i] for i in s.split(' ')])))
print(sorted(list(set([d[i] for i in s.split(' ')]))))
print([sorted(list(set([d[i] for i in s.split(' ')])))[i]*sorted(list(set([d[i] for i in s.split(' ')])))[i+1] if i%4==0 else sorted(list(set([d[i] for i in s.split(' ')])))[i]+sorted(list(set([d[i] for i in s.split(' ')])))[i+1] for i in range(0, len(sorted(list(set([d[i] for i in s.split(' ')])))) - 1, 2)])
print(sum([i for i in sorted(list(set([d[i] for i in s.split(' ')]))) if i%2!=0]))