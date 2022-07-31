tt = open('text.txt', 'r')
t = tt.read()
tt.close()

while True:
    n = input('\nEnter the lenght of the string in the text please:\n')
    if n.isdigit() == False:
        print('Incorrect input. Please input just numbers.')
        continue
    if int(n) <= 35:
        print('Incorrect input. Please input a number greater 35.')
        continue
    break
n = int(n)
l = t.split(' ')
l1 = ''
l2 = ''
t = 0
m = n
add = ''
l4 = ''
flag = True
while t < len(l):
    for i in range(t, len(l)):
        if i <= len(l):
            if len(l1 + ''.join(l[i])) >= n:
                break
            if '\n' in l[i]:
                for j in range(len(''.join(l[i]))):
                    if '\n' in ''.join(l[i])[j]:
                        l1 += ''.join(l[i]).split('\n')[0]
                        add = ''.join(l[i]).split('\n')[1] + ' '
                flag = False                      
                t += 1  
                break
            l1 += f"{add}{''.join(l[i])} "
            add = ''
            t += 1
        else:
            break
    l2 = l1.strip(' ')
    l3 = l2.split(' ')
    if flag == True and t != len(l):
        while len(' '.join(l3)) != n:
            for i in range(len(l3) - 1):
                if len(' '.join(l3)) < n:
                    l3[i] += ' '
    # print(' '.join(l3)) # Disscomment it if you want to see the text in the console.
    l4 += f"{' '.join(l3)}\n"
    flag = True
    m += n
    l1 = ''
    
tt = open('text2.txt', 'w')
tt.write(l4.strip('\n'))
tt.close()
print('\nThe file with a formatted text has already written.\nPlease open text2.txt and make sure in it.\n')
