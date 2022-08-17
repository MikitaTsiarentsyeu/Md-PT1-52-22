from random import randint


def chek_str(string):
    upper_cace = 0
    lower_cace = 0
    for i in string:
        if ord(i) in range(65, 91):
            upper_cace += 1
        elif ord(i) in range(97, 123):
            lower_cace += 1
    return f'{upper_cace} upper cace, {lower_cace} lower case'


def is_prime(num):
    for i in range(1,round(num / 2) + 1):
        if i != 1 and num % i == 0:
            return False
    return True


def get_ranges(lst):
	output = []
	j = 0
	for i in range(len(lst)):
		if i != len(lst) - 1 and lst[i + 1] == lst[i] + 1:
			j += 1
		else:
			output.append(str(lst[i])) if j == 0 else output.append(f'{lst[i - j]}-{lst[i]}')
			j = 0
	return ', '.join(output)



num_list = list(set([randint(0,randint(5,15)) for i in range(20)])) #num list generator


print(chek_str('The quick Brown Fox'))
print(is_prime(8))
print(get_ranges(num_list))
