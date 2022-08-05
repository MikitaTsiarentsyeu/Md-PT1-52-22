with open ('text.txt', 'r+', encoding = 'utf-8') as f:
    while True:
        width = (input ('Enter the number of symbols for text alignment (more than 35): '))
        if not width.isdigit():
            print("Error. Only digits allowed")
            continue
        width = int(width)
        if width <= 35:
            print("Error. The number should be more than 35")
            continue
        break
    t = open('text2.txt', 'a+', encoding = 'utf-8')
    lines = (f.readlines())
    for line in lines:
        while len(line)>width:
            line = line[::-1]
            x =-line.find(' ', -width,-1)
            line = line[::-1]
            newLine = line[0:x-1]     
            words = newLine.split()
            lenght = 0
            for i in words:
                lenght += (len(i))
            sp, rest = divmod(width-lenght,len(words)-1)
            spWord = [' '*sp]*(len(words)-1-rest)+[' '*(sp+1)]*rest +['']
            lineList = [word+space for word,space in zip(words,spWord)]
            t.write(''.join(lineList)+'\n')
            line = line[x:]
        t.write(line)
print ('File text2.txt is ready')