# In one varible (if don't count string and dictionary):
d = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
     'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
     'fifteen':15, 'sixteen':16, 'seventeen': 17, 'eighteen': 18,  'nineteen': 19, 'twenty': 20}
s = input('Input numberes form 0 into 21 in words please:\n')
# Validation fron 0 into 21:
for i in range(len(s.split(' '))):
     if (not s.split(' ')[i].isalpha()) or (s.split(' ')[i] not in d.keys()):
          print('Incorrect')
          exit()
else:
     print('\n')
     print([d[i] for i in s.split(' ')])
     print(set([d[i] for i in s.split(' ')]))
     print(list(set([d[i] for i in s.split(' ')])))
     print(sorted(list(set([d[i] for i in s.split(' ')]))))
     print([sorted(list(set([d[i] for i in s.split(' ')])))[i]*sorted(list(set([d[i] for i in s.split(' ')])))[i+1] if i%4==0 else sorted(list(set([d[i] for i in s.split(' ')])))[i]+sorted(list(set([d[i] for i in s.split(' ')])))[i+1] for i in range(0, len(sorted(list(set([d[i] for i in s.split(' ')])))) - 1, 2)])
     print(sum([i for i in sorted(list(set([d[i] for i in s.split(' ')]))) if i%2!=0]))
