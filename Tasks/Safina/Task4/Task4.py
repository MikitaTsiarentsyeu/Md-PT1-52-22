while True:
    string_length = (input('Please enter the maximum number of characters per line, but no more than 35:\n'))
    if string_length.isdigit():
        string_length = int(string_length)
    else:
        print('Error: use only digits.\n')
        continue
    if string_length <= 35:
       print('Error: please use more 35 elements.\n')  
       continue
    break

with open("text.txt", 'r', encoding = 'utf-8') as file:
    with open("new.txt", 'w', encoding = 'utf-8') as n_file:
        file.seek(0)
        string = file.readlines()
        for line in string:
            last_space_index = 0
            while len(line) > string_length:
                if line[string_length] == ' ':
                    n_file.write(line[:string_length] + '\n')
                    line = line[string_length+1:]
                    last_space_index = 0
                else:
                    for i in range(last_space_index + 1, len(line)+1):
                        last = line[i]
                        if last == ' ' and line[i+1] != ' ':
                            if i == line[:string_length].rindex(' '):
                                last_space_index = 0
                                break
                            line = line[:i] + ' ' + line[i:]
                            last_space_index = i + 1
                            break
            n_file.write(line)
    print('Ready: please check the file as "new.txt"') 