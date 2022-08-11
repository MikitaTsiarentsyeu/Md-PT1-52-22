
while True:
    try:
        print('Please, enter the max number of symbols per line: ')
        max_number = int(input())
        if max_number < 35:
            raise Exception()
        break
    except Exception as e:
        print("Entered value must be greater than 35. Try again.\n")    

read_file = 'text.txt'
write_file = 'new_text.txt'
with open(read_file, 'r', encoding='utf-8') as fr, open(write_file, 'w', encoding='utf-8') as fw:
    for line in fr:
        last_space_index = 0
        while len(line) > max_number:
            if line[max_number]==' ':
                fw.write(line[:max_number] + '\n')
                line = line[max_number+1:]
                last_space_index = 0
            else:
                for i in range(last_space_index + 1, len(line)+1):
                    char = line[i]
                    if char == ' ' and line[i+1] != ' ':
                        if i == line[:max_number].rindex(' '):
                            last_space_index = 0
                            break
                        line = line[:i] + ' ' + line[i:]
                        last_space_index = i + 1
                        break
        fw.write(line)
print('Please, take a look on formatted text in "new_text.txt" file')        
fw.close()
fr.close()