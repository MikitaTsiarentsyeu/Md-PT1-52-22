

while True:
    symbols = input("Please, input count of symbols in string. The digit must be greater than 35\n")
    if symbols.isdigit():
        if int(symbols) > 35:
            symbols = int(symbols)
            break 
with open("Task_4//text.txt", "r", encoding = "UTF-8") as donor:               
    with open("Task_4//format_text.txt", "w+", encoding = "UTF-8") as receiver:
        cursor = 0
        # donor.seek(0)
        # while cursor<200:
        while True:
            read_string = donor.read(symbols+1)
            if len(read_string) < symbols:
                receiver.write(read_string)
                break
            if read_string:
                if read_string.__contains__('\n'):
                    ind = read_string.find('\n')
                    format_string = read_string[:ind+1]
                    cursor += len(format_string)+1
                    donor.seek(cursor)
                    receiver.write(format_string)

                elif read_string[-1] == ' ':
                    cursor+=len(read_string)
                    receiver.write(read_string[:-1]+'\n')

                else:
                    index= -2
                    count = 2
                    while read_string[index] != ' ':
                        index -=1
                        count+=1
                    format_string = read_string[:index]
                    cursor += len(format_string)+1#readstr + index
                    donor.seek(cursor)
                    while len(format_string) != symbols:
                        mas = format_string.split()
                        account1 = ((count-1) // (len(mas)-1)) + 1
                        account2 = (count-1) % (len(mas)-1)
                        mas1 = []
                        sep = ' '*account1
                             
                        for it in range(0,len(mas)):
                            if it < account2:
                                mas1.append(mas[it] + ' ')
                            else:
                                mas1.append(mas[it])                                     
                        format_string = sep.join(mas1)
                            
                                        
                    receiver.write(format_string+'\n')
                      
                    
            else:
                break
print('Done!')
print(cursor)
