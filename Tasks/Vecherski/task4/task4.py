while True:
    length = input (f"enter the maximum number of characters for one line for text formatting(min 36):\n")
    if not length.isdigit():
        print(f"only numbers,please:")
        continue
    elif int(length) <= 35:    
        print(f"minimum value = 36, try again")
        continue
    else:
        length = int(length)
        with open ('text.txt','r',encoding='utf-8') as old:
            strings = old.readlines()
            with open("new_text.txt","w+",encoding='utf-8') as new:
                for string in strings:
                    while len(string) > length:
                        string = string[::-1]
                        st = -string.find(' ', -length, -1)
                        string = string[::-1]
                        new_string = string[0:st-1]    
                        words = new_string.split()
                        lenght = 0
                        for word in words:
                            lenght += (len(word))
                        sp = length - lenght - len(words)
                        line_list = []
                        for word in words:
                            if sp != 0:
                                line_list.append(word+" ")
                                sp -= 1
                            else:
                                line_list.append(word) 
                        new.write(' '.join(line_list)+'\n')
                        string = string[st:]
                    new.write(string)
        break            
print (f'text formatted and written to file "new_text.txt", located in the same directory')
    
