while True:
    x = input ('Please enter your name:\n')
    print ('Hello,', x, end = '!\n')
    start = input('Welcome to Pynote! Choose action:\n1. Start\n2. Exit\n')
    if start == '2':
        print ('Understandble. Have a nice day!')
        break
    elif start != '1' and start != '2':
        print ('Wrong input, please try again')
        continue
    elif start == '1':
        with open ("text.txt", 'r') as f:
            with open ("newtext.txt", 'w') as m:
                f.seek(0)
                strings_text = f.readlines()
                symbol = input ('You should type the maximum number of symbols per line(from 35 or more)\n')
                enter = int(symbol)
                if enter < 35:
                    print ('The enter must contain number from 35 or more symbols. Try again!')
                    continue
                elif enter >= 35:
                    for string_text in strings_text:
                       while len(string_text) > enter:
                            string_text = string_text[::-1]
                            len_string = -string_text.find(' ', -enter, -1)
                            string_text = string_text[::-1]
                            lines = string_text[0:len_string-1]
                            data_page = lines.split()
                            letter_symbols = 0
                            for values in data_page:
                               letter_symbols += len(values)
                            gap, full = divmod(enter-letter_symbols, len(data_page)-1)
                            gap_count = [' '*(gap+1)]*full + [' ' * gap]*(len(data_page)-1-full) + ['']
                            inf = ''
                            for i in range(len(data_page)):
                               inf += data_page[i]+gap_count[i]
                               finish = ''.join(inf)+"\n"
                            m.write(finish)
                            string_text = string_text[len_string:]
                    m.write(string_text)
                print('Job is done! Formatted text is already in file\n')
                break