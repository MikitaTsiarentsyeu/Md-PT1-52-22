while True:
    num = input("Please enter the maximum number of characters per line (more than 35):\n")
    if not num.isdigit():
        print ("Error, incorrect input. Please enter a number more than 35")
        continue

    num = int(num)

    if num <= 35:
        print ("Error, incorrect input. Please enter a number more than 35")
        continue
    break

with open("text.txt", 'r', encoding="utf-8") as r:
    with open("123.txt", 'w', encoding="utf-8") as w:

        for line in r:
            l = line.split()
        
            while len(' '.join(l)) > num:
                word = [l.pop(0)]
                len_words = len(' '.join(word))
           
                while len_words < num:
                    next_word_len = len(l[0])
                    if len_words + next_word_len + 1 > num:
                        break
                    word.append(l.pop(0))
                    len_words += next_word_len + 1

                space = num - len_words

                while space != 0:
                    for i in range(len(word) - 1):
                        if space == 0:
                            break
                        word[i] += ' '
                        space -= 1

                w.write(' '.join(word) + '\n')

            w.write(' '.join(l) + '\n')

print("The file is written as 123.txt")