while True:
    width = input("Please, еnter the maximum number of characters per line (should be >35):\n")
    if width.isdigit():
         width = int(width)
    else:
        print("Incorrect input. Only digits allowed.\n")
        continue
    if width <= 35:
        print("Incorrect input. The number should be more than 35.\n")
        continue
    break
with open("text.txt", 'r+', encoding = 'utf-8') as file:
    lines = (file.readlines())
    with open ("new_text.txt", 'a+', encoding = 'utf-8') as new_text:
        for line in lines:
            while len(line) > width:
                line = line[::-1]
                st = -line.find(' ', -width, -1)
                line = line[::-1]
                new_line = line[0:st-1]    
                words = new_line.split()
                lenght = 0
                for word in words:
                   lenght += (len(word))
                sp = width - lenght - len(words)
                line_list = []
                for word in words:
                    if sp != 0:
                        line_list.append(word+" ")
                        sp -= 1
                    else:
                        line_list.append(word) 
                new_text.write(' '.join(line_list)+'\n')
                line = line[st:]
            new_text.write(line)
print ("Changed file saved as new_text.txt\n")