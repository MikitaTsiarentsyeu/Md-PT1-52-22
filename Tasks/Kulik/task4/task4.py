while True:
    str_length = (input('Please, enter the length of line which is more than 35 elements: '))
    if not str_length.isdigit():
        print('Error! Please, enter the digits.')
        continue
    str_length = int(str_length)
    if str_length <= 35:
        print('Error! Please, enter the length of line which is more than 35 elements.')
        continue
    break      
with open('text.txt', 'r', encoding = 'utf-8') as f:
  with open('changed_text.txt', 'w', encoding = 'utf-8') as f_new:
        text = f.read().split() 
        line = [] 
        for word in text:
            if str_length - len(''.join(line)) >= len(word): 
                line.append(word), line.append(' ') 
            else:
                line.pop() 
                while len(''.join(line).rstrip()) != str_length: 
                    for i, symbol in enumerate(line):
                        if len(''.join(line).rstrip()) == str_length: 
                            break
                        if symbol != ' ':
                            line.insert(i + 1, ' ')
                f_new.write(''.join(line) + '\n')
                line = [word, ' ']
        f_new.write(''.join(line))
print('Done! Please, check the file "changed_text.txt"')