while True:
    answer = input(
        "\nWould you like to convert the text to the maximum number of characters per line starting from 36 characters:\n\
    Yes, I would like to - 'yes/Y'\n    No, I don't want to - 'no/N'\n    enter an option: ")

    variable_yes, variable_Y = "yes", "Y"
    variable_no, variable_N = "no", "N"

    if answer == variable_no or answer == variable_N:
        print("\nWell, it's your choice! If anything, call the function yourself...")
    elif answer != variable_yes and answer != variable_Y:
        print(
            f"\nYou have introduced some kind of heresy - {answer}, read the condition carefully and make your choice!\n")
        continue
    else:
        # I don't use a chunk since the file is known to me
        with open("text.txt", 'r') as text_original:
            with open("text2.txt", 'w') as text_modified:
                data_text = text_original.read()
                text_original.seek(0)
                text_lines = text_original.readlines()
                input_user = input(
                    f"Enter the number of characters from 36 to {len(data_text)}: ")

                if input_user.isdigit() == False:
                    print(f"\nYou have entered string data - {input_user}")
                    continue

                user_values = int(input_user)
                if user_values <= 35 or user_values > len(data_text):
                    print(
                        f"\nYou have entered an invalid character value equal to: {user_values}")
                    continue
                else:
                    for text_line in text_lines:
                        while len(text_line) > user_values:
                            text_line = text_line[::-1]
                            len_st = -text_line.find(' ', -user_values, -1)
                            text_line = text_line[::-1]
                            str_worlds = text_line[0:len_st-1]
                            words_list = str_worlds.split()
                            word_symbols = 0
                            for values in words_list:
                                word_symbols += len(values)
                            space, total = divmod(
                                user_values-word_symbols, len(words_list)-1)
                            count_space = [
                                ' '*(space+1)]*total + [' ' * space]*(len(words_list)-1-total) + ['']
                            data = ''
                            for i in range(len(words_list)):
                                data += words_list[i]+count_space[i]
                                result = ''.join(data)+"\n"
                            text_modified.write(result)
                            text_line = text_line[len_st:]
                        text_modified.write(text_line)
                    print(
                        "\nYour data will be formatted and saved in a file - text2.txt\n")
    break
