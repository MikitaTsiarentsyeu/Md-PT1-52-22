
while True:
    symbols = input("Please, input count of symbols in string. The digit must be greater than 35\n")
    if symbols.isdigit():
        if int(symbols) > 35:
            symbols = int(symbols)
            break 

with open("Task_4//text.txt", "r", encoding = "UTF-8") as donor:               
    with open("Task_4//format_text1.txt", "w+", encoding = "UTF-8") as receiver:
        read_text = donor.read()
        read_mas = read_text.split('\n')
        
        for i in read_mas:
            start = 0
            finish = symbols+1
            while True:
              if finish < len(i):
                operate_string = i[start:finish]
                if operate_string[-1] == ' ':
                    start+=len(operate_string)
                    finish = start + symbols+1
                    receiver.write(operate_string[:-1]+'\n')
                else:
                    index= -2
                    count = 2
                    while operate_string[index] != ' ':
                        index -=1
                        count+=1
                    format_string = operate_string[:index]
                    start += len(format_string)+1#readstr + index
                    finish= start+symbols+1
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
                receiver.write(i[start:] + '\n')
                break
        print('Done!')    