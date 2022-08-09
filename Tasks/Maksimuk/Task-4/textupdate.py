while True:    
    element = input("Choose number of elements in line (more then 35):\n")
    if element.isdigit():
        number = int(element)
    else:
        print("Error, wrong input")
        continue
    if number <= 35:
        print("The number should be more then 35")
    else:
        with open("text.txt", "r") as f:
            with open("newtext.txt", "w") as k:
                f.seek(0)
                string = f.readlines()
                for line in string:
                    last_space_index = 0
                    while len(line) > number:
                        if line[number] == ' ':
                            k.write(line[:number] + '\n')
                            line = line[number+1:]
                            last_space_index = 0
                        else:
                            for i in range(last_space_index + 1, len(line) + 1):
                                last = line[i]
                                if last == ' ' and line[i+1] != ' ':
                                    if i == line[:number].rindex(' '):
                                        last_space_index = 0
                                        break
                                    line = line[:i] + ' ' + line[i:]
                                    last_space_index = i + 1
                                    break
                    k.write(line)
        print('Please, take a look on formatted text in "new_text.txt" file')

            

