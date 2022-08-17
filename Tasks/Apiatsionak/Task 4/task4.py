while True:
    nummer = input("Please enter a maximum number of characters more than 35:\n")
    if not nummer.isdigit():
        print("Attention, incorrect enter. Please enter a number more than 35")
        continue

    nummer = int(nummer)

    if nummer <= 35:
        print("Attention, incorrect enter. Please enter a number more than 35")
        continue
    break

with open("text.txt", 'r', encoding = "utf-8") as r:
    with open("formatted.txt", 'w', encoding = "utf-8") as w:

        for line in r:
            l = line.split()

            while len(' '.join(l)) > nummer:
                word = [l.pop(0)]
                lenwords = len(' '.join(word))

                while lenwords < nummer:
                    nachstwortlen = len(l[0])
                    if lenwords + nachstwortlen + 1 > nummer:
                        break
                    word.append(l.pop(0))
                    lenwords += nachstwortlen + 1

                space = nummer - lenwords

                while space != 0:
                    for i in range(len(word) - 1):
                        if space == 0:
                            break
                        word[i] += ' '
                        space -= 1

                w.write(' '.join(word) + '\n')

            w.write(' '.join(l) + '\n')

print("The file is written as formatted.txt")
input('Press enter to close the program')

